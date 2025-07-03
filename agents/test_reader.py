from Tools.read_email import EmailReader

reader = EmailReader()

# testing mode = all
print("--- All Emails ---")
print(reader.forward(mode="all"))

# testing mode = latest
print("--- Latest Email ---")
print(reader.forward(mode="latest"))

# testing mode = specific
print("--- Specific Email ---")
print(reader.forward(mode="specific", index=1))

# testing mode = 'specific' and index = invalid
print("\n=== Invalid Index ===")
print(reader.forward(mode="specific", index=100))

# testing mode = invalid 
print("\n=== Invalid Mode ===")
print(reader.forward(mode="nonsense"))
