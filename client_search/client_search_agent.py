from client_search_tool import ClientSearchTool
from client_data import dummy_clients

class ClientSearchAgent:
    def __init__(self):
        self.tool = ClientSearchTool(dummy_clients)

    def get_client_info(self, query):
        return self.tool.forward(query)

# Run test
if __name__ == "__main__":
    agent = ClientSearchAgent()
    print(agent.get_client_info({"id": "101"}))
    print(agent.get_client_info({"email": "bob@example.com"}))
    print(agent.get_client_info({"role": "CTO"}))
    print(agent.get_client_info({"id": "999"}))
    print(agent.get_client_info({}))
