from universal_crud import create, read, update, delete

#Simple Contact data model 
class Contact: 
    def __init__ (self, contact_id, name, email):
        #initialize with user ID, Name, and Email
        self.id = contact_id
        self.name = name
        self.email = email 

    def to_dict(self):
        #return user data as a dictionary 
        return {"id": self.id, "name": self.name, "email": self.email}

contact_dict = {} 

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

    
