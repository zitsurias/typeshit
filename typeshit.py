import os
import socket
import hashlib
import random
import string
import requests
import base64
import json
import platform
import time
from rich.console import Console
from rich.panel import Panel
import pyfiglet

console = Console()
TOKEN = "dc1d1cfca29b9f"

# -------- CLEAR --------
def clear():
    os.system("clear")

# -------- BANNER --------
def banner():
    ascii_banner = pyfiglet.figlet_format("R6SXAK PRO", font="slant")
    console.print(f"[bold red]{ascii_banner}")
    console.print("[bold white]MULTITOOL v2[/]\n")

# -------- 1 IP LOOKUP --------
def ip_lookup():
    ip = input("Enter IP: ")
    url = f"https://api.ipinfo.io/lite/{ip}?token={TOKEN}"
    try:
        r = requests.get(url)
        data = r.json()
        result = "\n".join(f"{k}: {v}" for k, v in data.items())
        console.print(Panel(result, title="IP RESULT"))
    except:
        console.print("[red]Error retrieving IP data")

# -------- 2 DNS --------
def dns_lookup():
    domain = input("Enter domain: ")
    try:
        ip = socket.gethostbyname(domain)
        console.print(Panel(f"{domain} -> {ip}", title="DNS RESULT"))
    except:
        console.print("[red]DNS lookup failed")

# -------- 3 HASH --------
def hash_tool():
    text = input("Enter text: ")
    result = f"""
MD5: {hashlib.md5(text.encode()).hexdigest()}
SHA1: {hashlib.sha1(text.encode()).hexdigest()}
SHA256: {hashlib.sha256(text.encode()).hexdigest()}
"""
    console.print(Panel(result, title="HASH RESULT"))

# -------- 4 PASSWORD --------
def password_generator():
    length = int(input("Length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(length))
    console.print(Panel(password, title="PASSWORD"))

# -------- 5 WEBSITE --------
def website_info():
    site = input("Enter website (example.com): ")
    try:
        r = requests.get(f"http://{site}")
        headers = "\n".join(f"{k}: {v}" for k, v in r.headers.items())
        console.print(Panel(f"Status: {r.status_code}\n\n{headers}", title="WEBSITE INFO"))
    except:
        console.print("[red]Failed to fetch site")

# -------- 6 PORT SCANNER --------
def port_scanner():
    target = input("Target IP: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    open_ports = []

    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            open_ports.append(port)
        sock.close()

    console.print(Panel(str(open_ports), title="OPEN PORTS"))

# -------- 7 SUBDOMAIN CHECK --------
def subdomain_checker():
    domain = input("Enter domain: ")
    subs = ["www", "mail", "ftp", "api", "dev", "test"]
    found = []

    for sub in subs:
        try:
            socket.gethostbyname(f"{sub}.{domain}")
            found.append(f"{sub}.{domain}")
        except:
            pass

    console.print(Panel("\n".join(found) if found else "None found", title="SUBDOMAINS"))

# -------- 8 BASE64 --------
def base64_tool():
    choice = input("1 Encode | 2 Decode: ")
    text = input("Enter text: ")

    if choice == "1":
        encoded = base64.b64encode(text.encode()).decode()
        console.print(Panel(encoded, title="ENCODED"))
    else:
        try:
            decoded = base64.b64decode(text).decode()
            console.print(Panel(decoded, title="DECODED"))
        except:
            console.print("[red]Invalid Base64")

# -------- 9 JWT DECODER --------
def jwt_decoder():
    token = input("Enter JWT: ")
    try:
        header, payload, signature = token.split(".")
        header_decoded = json.loads(base64.urlsafe_b64decode(header + "=="))
        payload_decoded = json.loads(base64.urlsafe_b64decode(payload + "=="))

        result = f"HEADER:\n{json.dumps(header_decoded, indent=2)}\n\nPAYLOAD:\n{json.dumps(payload_decoded, indent=2)}"
        console.print(Panel(result, title="JWT DECODE"))
    except:
        console.print("[red]Invalid JWT")

# -------- 10 SYSTEM INFO --------
def system_info():
    info = f"""
System: {platform.system()}
Node: {platform.node()}
Release: {platform.release()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}
"""
    console.print(Panel(info, title="SYSTEM INFO"))

# -------- MENU --------
def menu():
    console.print("""
[bold cyan]
1 IP Lookup
2 DNS Lookup
3 Hash Tool
4 Password Generator
5 Website Info
6 Port Scanner
7 Subdomain Checker
8 Base64 Tool
9 JWT Decoder
10 System Info
0 Exit
""")
    choice = input("Select: ")

    if choice == "1": ip_lookup()
    elif choice == "2": dns_lookup()
    elif choice == "3": hash_tool()
    elif choice == "4": password_generator()
    elif choice == "5": website_info()
    elif choice == "6": port_scanner()
    elif choice == "7": subdomain_checker()
    elif choice == "8": base64_tool()
    elif choice == "9": jwt_decoder()
    elif choice == "10": system_info()
    else:
        console.print("[red]Exiting")
        return

    input("\nPress Enter to continue...")
    clear()
    banner()
    menu()

# -------- MAIN --------
def main():
    clear()
    banner()
    menu()

if __name__ == "__main__":
    main()
