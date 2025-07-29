# -----------------------------------------------------------------------------
# Copyright (c) 2025 SmolMail Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This project is open-source and maintained by the community.
# Contributions are welcome—please see the CONTRIBUTING.md file for guidelines.
#
# "SmolMail" and the SmolMail logo are trademarks of SmolMail, Inc.
# Use of these trademarks is subject to SmolMail's trademark policy.
#
# Created by Austin Becton
# -----------------------------------------------------------------------------


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
