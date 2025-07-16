class ClientSearchTool:
    def __init__(self, database):
        self.database = database
    
    def forward(self, query: dict):
        if not query or len(query) != 1: 
            return {"Error": "Please provide one search field"}
        
        key, value = list(query.items())[0]

        for client in self.database: 
            if client.get(key) == value:
                return {"Status": "Success", "data": client}
            
        return {"status": "error", "message": "Client not found"}
