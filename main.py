"""
Youssef Auth - Python Example
https://youssefauth.wuaze.com
"""

import sys
from youssefauth import api

# Replace with your app credentials from your Youssef Auth Dashboard
auth = api(
    name="YourAppName",
    ownerid="YourOwnerId",
    secret="YourAppSecret",
    version="1.0"
)

def main():
    print("=" * 50)
    print("           YOUSSEF AUTH â€¢ PYTHON CLIENT           ")
    print("=" * 50)
    
    print("\n[+] Initializing security session...")
    if not auth.init():
        print("[-] Failed to initialize. Check your credentials.")
        sys.exit(1)
        
    print("[+] Session connected successfully!\n")
    print("1. Login with Username & Password")
    print("2. Register new Account with License Key")
    print("3. Activate / Login with License Key Only")
    print("4. Exit")
    
    choice = input("\nSelect an option [1-4]: ").strip()
    
    if choice == "1":
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()
        res = auth.login(user, pwd)
        if res.get("success"):
            print(f"\n[+] Welcome back, {user}!")
            print(f"[+] Subscriptions: {res.get('info', {}).get('subscriptions', 'Default')}")
            auth.log(f"User {user} logged in via Python SDK")
        else:
            print(f"\n[-] Login failed: {res.get('message')}")
            
    elif choice == "2":
        user = input("Choose Username: ").strip()
        pwd = input("Choose Password: ").strip()
        key = input("License Key: ").strip()
        res = auth.register(user, pwd, key)
        if res.get("success"):
            print(f"\n[+] Account registered successfully! You can now log in.")
        else:
            print(f"\n[-] Registration failed: {res.get('message')}")
            
    elif choice == "3":
        key = input("License Key: ").strip()
        res = auth.license(key)
        if res.get("success"):
            print(f"\n[+] License activated successfully!")
            print(f"[+] Expiry: {res.get('info', {}).get('subscriptions', [{}])[0].get('expiry', 'N/A')}")
        else:
            print(f"\n[-] Activation failed: {res.get('message')}")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()