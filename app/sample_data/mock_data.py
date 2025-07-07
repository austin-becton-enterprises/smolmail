def get_dummy_contacts() -> list[dict]:
    return [
        {
            "contact_id": 1,
            "name": "Alice Smith",
            "email": "alice@example.com",
            "phone": "555-1234"
        },
        {
            "contact_id": 2,
            "name": "Bob Johnson",
            "email": "bob@example.com",
            "phone": "555-5678"
        },
        {
            "contact_id": 3,
            "name": "Cathy Lee",
            "email": "cathy@example.com",
            "phone": "555-9012"
        },
        {
            "contact_id": 4,
            "name": "David Kim",
            "email": "david.kim@example.com",
            "phone": None
        }
    ]

def get_dummy_templates() -> list[dict]:
    return [
        {
            "template_id": 101,
            "title": "Welcome",
            "subject": "Welcome to Our Service",
            "body": "Hi {name}, welcome to our service!"
        },
        {
            "template_id": 102,
            "title": "Follow Up",
            "subject": "Just Checking In",
            "body": "Hey {name}, just following up on our last conversation."
        },
        {
            "template_id": 103,
            "title": "Reminder",
            "subject": "Don't Miss Out",
            "body": "Hi {name}, don't forget about your upcoming appointment!"
        },
        {
            "template_id": 104,
            "title": "Thank You",
            "subject": "Thanks for Reaching Out",
            "body": "Hello {name}, thanks for getting in touch with us!"
        }
    ]
