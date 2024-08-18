import asyncio

from hullabaloo.blockchain import Blockchain
from hullabaloo.connections import ConnectionPool
from hullabaloo.peers import P2PProtocol
from hullabaloo.server import Server

blockchain = Blockchain()
# Our pool for peers
connection_pool = ConnectionPool()

# Instantiate the server
server = Server(blockchain, connection_pool, P2PProtocol)

async def main():
    # Start the server
    await server.listen()
    
asyncio.run(main())
