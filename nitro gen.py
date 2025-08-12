import random
import string
import requests
import time
import os
from pyfiglet import Figlet
from colorama import Fore, Style, init
import itertools
import sys

init(autoreset=True)

def generate_nitro_gift_link():
    chars = string.ascii_letters + string.digits
    code = ''.join(random.choice(chars) for _ in range(16))
    return f"https://discord.com/gifts/{code}"

def send_to_discord(webhook_url, message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(Fore.RED + f"[OK] Message envoyé : {message}")
    else:
        print(Fore.RED + f"[ERREUR] {response.status_code} - {response.text}")

def animated_title(text):
    colors = [Fore.LIGHTRED_EX, Fore.RED]
    for color in itertools.cycle(colors):
        os.system("cls" if os.name == "nt" else "clear")
        fig = Figlet(font="slant")
        print(color + fig.renderText(text))
        sys.stdout.flush()
        time.sleep(0.3)
        yield 

def main():
    title_animation = animated_title("Nitro Generator")
    for _ in range(5):  
        next(title_animation)

    print(Fore.RED + "Created by Uruma".center(80))

    webhook_url = input(Fore.LIGHTRED_EX + "\n[?] Entrez le lien du webhook Discord : ").strip()

    while True:
        link = generate_nitro_gift_link()
        send_to_discord(webhook_url, link)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
