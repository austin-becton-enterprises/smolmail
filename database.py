#Simple User data model 
class User: 
    def __init__ (self, user_id, name, email):
        #initialize with user ID, Name, and Email
        self.id = user_id
        self.name = name
        self.email = email 

    def to_dict(self):
        #return user data as a dictionary 
        return {"id": self.id, "name": self.name, "email": self.email}

mock_db = {} 

#Create function add a new user to the database
def create_user(user_id,name, email): 
    #Check if user exists 
    if user_id in mock_db: 
        return f"User with ID {user_id} already exists."
    #Create new user object and store in dictionary 
    user = User(user_id, name, email)
    mock_db[user_id]=user 
    return f"User {name} created."

#Read function retrieves user's data from their ID
def read_user(user_id): 
    user = mock_db.get(user_id)
    return user.to_dict() if user else "User not Found."
#Update function modifies existing user's information
def update_user(user_id,name=None,email=None): 
    user = mock_db.get(user_id)
    if not user: 
        return "User not found"
    if name: 
        user.name = name 
    if email: 
        user.email = email
    return f"User {user_id} updated"
#Delete function removes a user from the database using ID 
def delete_user(user_id): 
    if user_id in mock_db: 
        del mock_db[user_id] 
        return f"User {user_id} deleted."
    return "User not Found"


#TESTING 
if __name__ == "__main__": 
    print(create_user(1,"Liana", "liana@gmail.com"))
    print(read_user(1))
    print(update_user(1, email="newliana@example.com"))
    print(read_user(1))
    print(read_user(2))
    print(delete_user(1))
    print(read_user(1))
