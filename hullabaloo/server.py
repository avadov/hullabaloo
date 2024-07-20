import asyncio
from asyncio import StreamReader, StreamWriter

import structlog
from marshmallow.exceptions import MarshmallowError

from hullabaloo.messages import BaseSchema
from hullabaloo.utils import get_external_ip

logger = structlog.getLogger()


class Server:
    def __init__(self, blockchain, connection_pool, 
                 p2p_protocol):
        self.blockchain = blockchain
        self.connection_pool = connection_pool
        self.p2p_protocol = p2p_protocol
        self.external_ip = None
        self.external_port = None
        
        if not (blockchain and connection_pool and
                p2p_protocol):
            logger.error("'blockchain', 'connection_pool', and"
                +" 'p2p_protocol' must all be instantiated")
            raise Exception("Could not start")
        
    async def get_external_ip(self):
        self.external_ip = await get_external_ip()
        
    async def handle_connection(self, reader: StreamReader,
                                writer: StreamWriter)
    while True:
        try:
            # Wait forever on new data to arrive
            data = await reader.readuntil(b"\n")
            
            decoded_data = data.decode("utf-8").strip()
            
            try:
                message = BaseSchema().loads(decoded_data)
            except MarshmallowError:
                logger.info("Received unreadable message",
                            peer=writer)
                break
            
            # Extract the address from the message, add it to 
            # the writer object
            writer.address = message["meta"]["address"]
            
            # Adding the peer to our connection pool 
            self.connection_pool.add_peer(writer)
            
            # Handle the message
            await self.p2p_protocol.handle_message(message, writer)
            
            await writer.drain()
            if writer.is_closing():
                break
            
        except (asyncio.exceptions.IncompleteReadError,
                ConnectionError):
            # Break out of the wait loop
            break
        
    # The connection has closed. Cleaning up
    writer.close()
    await writer.wait_closed()
    self.connection_pool.remove_peer(writer)
    
async def listen(self, hostname="0.0.0.0", port=8888):
    server = await asyncio.start_server(self.handle_connection,
                                        hostname, port)
    logger.info(f"Server listening on {hostname}:{port}")
    
    self.external_ip = await self.get_external_ip()
    self.external_port = 8888
    
    async with server:
        await server.serve_forever()
