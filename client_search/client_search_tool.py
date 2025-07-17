class ClientSearchTool:
    def __init__(self, database):
        self.database = database
    
    def forward(self, query: dict):
        if not query or len(query) != 1: 
            return {"status": "error", "message": "Search value cannot be empty."}
        
        key, value = list(query.items())[0]
        
        if not value:
            return {"status": "error", "message": "Search value cannot be empty."}

        for client in self.database: 
            if client.get(key) == value:
                return {"status": "success", "data": client}
            
        return {"status": "error", "message": "Client not found"}
