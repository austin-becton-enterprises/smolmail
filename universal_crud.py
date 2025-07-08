#Create method adds a new item to the dictionary 
def create(dict, item):
    if item.id in dict: 
        return False, f"Item with ID {item.id} already exists"
    dict[item.id] = item
    return True, item


#Read function retrieves item's data from their ID
def read(dict, item_id): 
    item = dict.get(item_id)
    if not item: 
        return False, f"Item with ID {item_id} not found"
    return True, item 

#Update function modifies existing item's data 
def update(dict, item_id, **updates):
    item = dict.get(item_id) 
    if not item:
        return False, f"Item with ID {item_id} not found."
    for key, value in updates.items(): 
        if hasattr(item, key):
            setattr(item, key, value)
        else:
            return False, f"Attribute {key} not found on item."
    return True, item
#Delete function removes an item from the dictionary using ID 
def delete(dict, item_id):
    if item_id in dict: 
        del dict[item_id]
        return True, f"Item with ID {item_id} deleted."
    return False, f"Item with ID {item_id} not found." 
