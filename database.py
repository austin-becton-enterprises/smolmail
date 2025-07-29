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


#constants for dictionary keys 
PROPERTY_KEY_ID = "id"
PROPERTY_KEY_NAME = "name"
PROPERTY_KEY_EMAIL = "email"

# Simple User data model 
class User: 
    def __init__ (self, user_id:str, name:str, email:str) -> None:
        #initialize with user ID, Name, and Email
        self.id:str = user_id
        self.name:str = name
        self.email:str = email 

    def to_dict(self) -> dict:
        #return user data as a dictionary 
        return {PROPERTY_KEY_ID: self.id, PROPERTY_KEY_NAME: self.name, PROPERTY_KEY_EMAIL: self.email}

mock_db = dict[str, User] = {} 

#Create function add a new user to the database
def create_user(user_id:str, name:str , email:str ) ->str: 
    #Check if user exists 
    if user_id in mock_db: 
        return f"User with ID {user_id} already exists."
    #Create new user object and store in dictionary 
    user = User(user_id, name, email)
    mock_db[user_id]=user 
    return f"User {name} created."

#Read function retrieves user's data from their ID
def read_user(user_id:str) -> dict | str: 
    user = mock_db.get(user_id)
    return user.to_dict() if user else "User not Found."
#Update function modifies existing user's information
def update_user(user_id:str ,name: str |None=None, email:str | None=None) -> str: 
    user = mock_db.get(user_id)
    if not user: 
        return "User not found"
    if name: 
        user.name = name 
    if email: 
        user.email = email
    return f"User {user_id} updated"
#Delete function removes a user from the database using ID 
def delete_user(user_id:str) -> str: 
    if user_id in mock_db: 
        del mock_db[user_id] 
        return f"User {user_id} deleted."
    return "User not Found"