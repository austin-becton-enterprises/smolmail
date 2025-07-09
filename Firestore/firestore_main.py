from Firestore.core.services.client_service import ClientService
from Firestore.core.services.template_service import TemplateService
from Firestore.utils.helpers import input_choice, input_non_empty, input_yes_no

def print_client_summary(client):
    print(f"ID: {client.get('client_id')}, Name: {client.get('client_name')}, Email: {client.get('client_email')}")

def print_template_summary(template):
    desc = template.get('template_desc', '')
    print(f"ID: {template.get('template_id')}, Desc: {desc[:30]}..., Client ID: {template.get('client_id')}")

def print_email_summary(email):
    print(f"Email ID: {email.get('email_id', 'N/A')}, Template ID: {email.get('template_id')}, Status: {email.get('status')}")

def manage_clients(fs_client):
    while True:
        print("\n--- Manage Clients ---")
        print("1. Register New Client")
        print("2. List Clients")
        print("3. Read Client")
        print("4. Update Client")
        print("5. Delete Client")
        print("0. Back")

        choice = input_choice("Select option", ['0','1','2','3','4','5'])
        if choice == '1':
            fs_client.register_client()
        elif choice == '2':
            clients = fs_client.list_clients()
            if not clients:
                print("No clients found.")
            else:
                for c in clients:
                    print_client_summary(c)
            input("Press Enter to continue...")
        elif choice == '3':
            cid = input_non_empty("Client ID to read: ")
            client = fs_client.read_client(cid)
            if client:
                print(client)
            else:
                print("Client not found.")
            input("Press Enter to continue...")
        elif choice == '4':
            cid = input_non_empty("Client ID to update: ")
            key = input_non_empty("Field to update: ")
            val = input_non_empty(f"New value for {key}: ")
            fs_client.update_client(cid, {key: val})
            input("Press Enter to continue...")
        elif choice == '5':
            cid = input_non_empty("Client ID to delete: ")
            if input_yes_no(f"Delete client '{cid}' and all related data? (y/n): "):
                fs_client.delete_client(cid)
            else:
                print("Delete cancelled.")
            input("Press Enter to continue...")
        else:
            break

def template_menu(fs_template):
    while True:
        print(f"\n--- Template Menu (Logged in as: {fs_template.logged_in_client_id}) ---")
        print("1. Create Template")
        print("2. List Templates")
        print("3. Read Template")
        print("4. Update Template")
        print("5. Delete Template")
        print("6. Render Template")
        print("7. Log Email")
        print("8. View Emails")
        print("0. Logout")

        choice = input_choice("Select option", [str(i) for i in range(9)])

        if choice == '1':
            fs_template.create_template()
        elif choice == '2':
            templates = fs_template.list_templates()
            if not templates:
                print("No templates found.")
            else:
                for t in templates:
                    print_template_summary(t)
        elif choice == '3':
            tid = input_non_empty("Template ID to read: ")
            tpl = fs_template.read_template(tid)
            if tpl:
                print(tpl)
            else:
                print("Template not found.")
        elif choice == '4':
            tid = input_non_empty("Template ID to update: ")
            key = input_non_empty("Field to update: ")
            val = input_non_empty("New value: ")
            fs_template.update_template(tid, {key: val})
        elif choice == '5':
            tid = input_non_empty("Template ID to delete: ")
            fs_template.delete_template(tid)
        elif choice == '6':
            tid = input_non_empty("Template ID to render: ")
            fs_template.render_template(tid)
        elif choice == '7':
            tid = input_non_empty("Template ID to log email for: ")
            opened = input_yes_no("Was email opened? (y/n): ")
            fs_template.log_email(tid, {"opened": opened})
        elif choice == '8':
            emails = fs_template.get_emails()
            if not emails:
                print("No emails found.")
            else:
                for e in emails:
                    print_email_summary(e)
        elif choice == '0':
            fs_template.logout()
            break
        input("Press Enter to continue...")

def firestoremain():
    fs_client = ClientService()
    fs_template = TemplateService()

    while True:
        print("\n=== Firestore CLI ===")
        print("1. Login as Client")
        print("2. Manage Clients")
        print("0. Exit")

        choice = input_choice("Select option", ['0','1','2'])

        if choice == '1':
            cid = input_non_empty("Client ID: ")
            if fs_template.login(cid):
                template_menu(fs_template)
            else:
                print("Login failed.")
                input("Press Enter to continue...")
        elif choice == '2':
            manage_clients(fs_client)
        elif choice == '0':
            print("Goodbye!")
            break