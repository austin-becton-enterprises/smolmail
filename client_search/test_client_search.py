from client_search_tool import ClientSearchTool
from client_data import dummy_clients

def test_valid_id(): 
    tool = ClientSearchTool(dummy_clients)
    result = tool.forward({"id": "101"})
    print("test_valid_id result:", result)

    assert result["status"] == "success"

def test_invalid_id():
    tool = ClientSearchTool(dummy_clients)
    result = tool.forward({"id": "999"})  # ID not in dummy_clients
    print("test_invalid_id result:", result)
    assert result["status"] == "error"

def test_valid_email():
    tool = ClientSearchTool(dummy_clients)
    result = tool.forward({"email": "charlie@sunny.com"})
    print("test_valid_email result:", result)
    assert result["status"] == "success"

def test_empty_query():
    tool = ClientSearchTool(dummy_clients)
    result = tool.forward({})
    print("test_empty_query result:", result)

    assert result["status"] == "error"

if __name__ == "__main__":
    test_valid_id()
    test_invalid_id()
    test_valid_email()
    test_empty_query()
    print("All tests passed.")
