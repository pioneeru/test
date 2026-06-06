import os
import subprocess

# 1. Hardcoded Secret (Triggers a Secret Scanning / CodeQL Alert)
ATTACKER_C2_SERVER = "192.168.1.100"
EXFIL_TOKEN = "ghp_MaliciousTokenSimulation1234567890ABC" # Mimics a GitHub token

def malicious_backdoor():
    # 2. Remote Command Injection Vector (High Risk Alert)
    # Taking untrusted inputs directly into a system shell
    user_command = input("Enter command to execute: ")
    
    # CodeQL flags this as an unvalidated command execution vulnerability
    subprocess.Popen(user_command, shell=True) 

if __name__ == "__main__":
    print(f"Connecting to C2: {ATTACKER_C2_SERVER}")
    malicious_backdoor()