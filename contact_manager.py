from universal_crud import create, read, update, delete

#Constants for property keys 
PROPERTY_KEY_ID = "id"
PROPERTY_KEY_NAME = "name"
PROPERTY_KEY_EMAIL = "email" 

#Simple Contact data model 
class Contact: 
    def __init__ (self, contact_id: int, name: str, email:str) -> None:
        #initialize with user ID, Name, and Email
        self.id: int = contact_id
        self.name: str = name
        self.email:str = email 

    def to_dict(self) -> dict:
        #return user data as a dictionary 
        return {PROPERTY_KEY_ID: self.id, PROPERTY_KEY_NAME: self.name, PROPERTY_KEY_EMAIL: self.email}

contact_dict: dict[int, Contact]={}

def create_contact (contact): 
    success, result = create(contact_dict, contact)
    if success: 
        return True, f"Contacts created: {result.to_dict()}"
    else:
        return False, f"Failed to create contact: {result}"
    
def read_contact(contact_id): 
    success, result = read(contact_dict, contact_id)
    if success and result:
        return True, f"Contact found: {result.to_dict()}"
    else: 
        return False, f"Contact with ID {contact_id} not found."

def update_contact(contact_id, **kwargs):
    success, result = update(contact_dict, contact_id, **kwargs)
    if success: 
        return True, f"Contact updated: {result.to_dict()}"
    else: 
        return False, f"Update failed: {result}"
def delete_contact(contact_id): 
    success, result = delete(contact_dict, contact_id)
    if success: 
        return True, f"Contact deleted: {result}"
    else: 
        return False, f"Delete Failed: {result}"


###TESTING

if __name__ == "__main__": 
    create_contact(Contact(1, "Liana", "liana@gmail.com"))
    print(read_contact(1))
    print(update_contact(1, name ="liana Sarkissian",email="lianasarkissian@gmail.com"))
    print(delete_contact(1))
    print(read_contact(1))

    
