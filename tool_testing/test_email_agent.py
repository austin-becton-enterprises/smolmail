import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from smolmail.agents.email_agent import EmailAgent

def test_email_agent():
    agent = EmailAgent()

    print("\n--- Test 1: Prompt with explicit email ---")
    prompt1 = "Please send a meeting update to jane.doe@example.com"
    result1 = agent.run(prompt1)
    print("Result:", result1)

    print("\n--- Test 2: Prompt with client name, no email ---")
    prompt2 = "Send project status update to Alice"
    result2 = agent.run(prompt2)
    print("Result:", result2)

    print("\n--- Test 3: Prompt with no recipient info ---")
    prompt3 = "Send a thank you note"
    result3 = agent.run(prompt3)
    print("Result:", result3)

def test_email_reading():
    agent = EmailAgent()

    print("\n--- Test 4: Read latest email ---")
    latest = agent.read_emails(mode="latest")
    print("Latest email:\n", latest)

    print("\n--- Test 5: Read specific email index 2 ---")
    specific = agent.read_emails(mode="specific", index=2)
    print("Specific email:\n", specific)

    print("\n--- Test 6: Read all emails (limited to 10) ---")
    all_emails = agent.read_emails(mode="all")
    print("All emails:\n", all_emails)

if __name__ == "__main__":
    test_email_agent()
    test_email_reading()
