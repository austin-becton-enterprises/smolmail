from client_search_tool import ClientSearchTool
from client_data import dummy_clients

class ClientSearchAgent:
    def __init__(self):
        self.tool = ClientSearchTool(dummy_clients)

    def get_client_info(self, query):
        result = self.tool.forward(query)
        if result["status"] =="success": 
            return result["prompt"]
        return result("message")
