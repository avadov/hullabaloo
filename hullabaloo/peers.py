

class P2PError(Exception):
    pass


class P2PProtocol:
    def __init__(self, server):
        pass
    
    @staticmethod
    async def send_message(writer, message):
        # Sends a message to a particular peer (the writer object)
        pass
    
    async def handle_message(self, message, writer):
        # Handles an incoming message passed by the server
        # Hands this message off to a more specific method:
        # handle_<method_name>()
        pass
    
    async def handle_ping(self, message, writer):
        # Handles an incoming "ping" message
        pass
    
    async def handle_block(self, message, writer):
        # Handles an incoming "block" message
        pass
    
    async def handle_transaction(self, message, writer):
        # Handles an incoming "transaction" message
        pass
    
    async def handle_peers(self, message, writer):
        # Handles an incoming "peers" message
        pass
    
    
