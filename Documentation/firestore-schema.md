# FireStore Schema 
This file will define the structure of the Firestore database colections 


## 'Users'

### Description
Stores information about each user of the applicaiton 

### Document Structure: 
USERS_SCHEMA = {
    "id: "auto-generated",
    "fullName": str,
    "email": str,
    "role": str,  # e.g., 'admin', 'user'
    "isActive": bool,
}

## 'Emails' 

### Description 
Stores emails received or managed through the app 

### Document Structure 
EMAILS_SCHEMA = {
    "id": "auto-generated",
    "userId": str,
    "sender": str,
    "recipient": str,
    "subject": str,
    "body": str,
    "labels": list,  # list of strings
    "isRead": bool,
} 

## AutoReply 

### Description
Stores predefined auto reply templates 

### Document Structure 

AUTO_REPLIES_SCHEMA = {
    "id": "auto-generated",
    "userId": str,
    "templateName": str,
    "message": str,
    "isActive": bool
}

