# test_vulnerability.py
def connect_to_database():
    # CodeQL will flag this as a hardcoded credential vulnerability
    password = "SuperSecretPassword123!"
    print(f"Connecting with password: {password}")