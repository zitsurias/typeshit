import os
import time
import random
import requests
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import pyfiglet

console = Console()

TOKEN = "dc1d1cfca29b9f"   # <- tady máš svůj token
PASSWORD = "r6sxak"

# -------- CLEAR --------
def clear():
    os.system("clear")

# -------- MATRIX INTRO --------
def matrix():
    chars = "01"
    for _ in range(20):
        line = "".join(random.choice(chars) for _ in range(90))
        console.print(f"[green]{line}")
        time.sleep(0.03)

# -------- FAKE HACK --------
def fake_hack():
    steps = [
        "Injecting packets...",
        "Bypassing firewall...",
        "Decrypting metadata...",
        "Accessing IP registry...",
        "Finalizing trace..."
    ]
    for step in steps:
        console.print(f"[red]{step}")
        time.sleep(0.6)

# -------- BANNER --------
def banner():
    ascii_banner = pyfiglet.figlet_format("R6SXAK", font="slant")
    console.print(f"[bold red]{ascii_banner}")
    console.print(Align.center("[white bold]OWNED BY R6SXAK[/]\n"))

# -------- LOGIN --------
def login():
    console.print("[bold red]SECURE LOGIN REQUIRED\n")
    pwd = input("Enter password: ")
    if pwd != PASSWORD:
        console.print("[red]ACCESS DENIED")
        exit()
    console.print("[green]ACCESS GRANTED")
    time.sleep(1)

# -------- AUTO IP --------
def auto_ip():
    try:
        r = requests.get("https://api.ipify.org?format=json")
        return r.json()["ip"]
    except:
        return "Unknown"

# -------- IP LOOKUP --------
def ip_lookup():
    ip = input("\n[?] Enter IP (leave empty for your IP): ")
    if ip == "":
        ip = auto_ip()

    fake_hack()

    url = f"https://api.ipinfo.io/lite/{ip}?token={TOKEN}"
    try:
        r = requests.get(url)
        data = r.json()

        result = f"""
IP: {data.get("ip")}
City: {data.get("city")}
Region: {data.get("region")}
Country: {data.get("country")}
Location: {data.get("loc")}
"""

        console.print(Panel(result, title="[bold red]IP TRACE RESULT[/]"))

        with open("result.txt", "w") as f:
            f.write(result)

        console.print("[green]Saved to result.txt")
    except:
        console.print("[red]ERROR retrieving data")

# -------- MENU --------
def menu():
    console.print("\n[bold cyan]╔══════════════════════╗")
    console.print("[bold cyan]║  [1] IP LOOKUP       ║")
    console.print("[bold cyan]║  [0] EXIT            ║")
    console.print("[bold cyan]╚══════════════════════╝")

    choice = input("\n[>] Select option: ")

    if choice == "1":
        ip_lookup()
    else:
        console.print("[red]Exiting...")

# -------- MAIN --------
def main():
    clear()
    matrix()
    banner()
    login()
    menu()

if __name__ == "__main__":
    main()
