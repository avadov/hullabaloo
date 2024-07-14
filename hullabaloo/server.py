class Server:
    def __init__(self, blockchain, connection_pool, p2p_protocol):
        pass
    
    async def get_external_ip(self):
        # Finds our "external" IP so that we can advertize it
        # to our peers
        pass
    
    async def handle_connection(self, reader: StreamReader, 
                                writer: StreamWriter):
        # This function is called when we receive a new connection 
        # The 'writer' object represents the connecting peer 
        while True:
            try:
                # We handle and/or reply to the incoming data
                pass
            except (asyncio.exceptions.IncompleteReadError,
                    ConnectionError):
                # An error happened, break out of the wait loop
                break
            
    async def listen(self, hostname="0.0.0.0", port=8888):
        #This is the listen method which spawns our server
        server = await asyncio.start_server(self.handle_connection,
                                            hostname, port)
        logger.info(f"Server listening on {hostname}:{port}")
        async with server:
            await server.serve_forever()
                
