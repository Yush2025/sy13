#CODE BY Sythe
import requests
import re
import os
from bs4 import BeautifulSoup as bs
import random
import urllib3
from mahdix import *
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import threading
clear()
import os
from mahdix import *
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor
import re
import requests
import json
import random
import json
import requests
import uuid
import string
import base64
import urllib
import urllib3
import re
import os
import time
import sys
from datetime import datetime
from urllib.request import urlopen
from time import sleep as slp
import re
import requests
import json


R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
K = '\x1b[1;30m'
M = '\x1b[1;35m'
E = '\x1b[1;90m'
O = '\x1b[1;91m'
L = '\x1b[1;92m'
S = '\x1b[1;94m'
P = '\x1b[1;95m'
T = '\x1b[1;96m'
red = '\x1b[1;31m'
green = '\x1b[1;32m'
yellow = '\x1b[1;33m'
blue = '\x1b[1;34m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
black = '\x1b[1;30m'
magenta = '\x1b[1;35m'
grey = '\x1b[1;90m'
orange = '\x1b[1;91m'
lime = '\x1b[1;92m'
sky_blue = '\x1b[1;94m'
purple = '\x1b[1;95m'
turquoise = '\x1b[1;96m'
ses = requests.Session()

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([
        True,
        False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent

headers = {
    'user-agent': W_ueragnt(),
    'viewport-width': '847',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'GroupCometJoinForumMutation',
    'x-fb-lsd': 'wGh6ACr3OJ2v2rPBdXy-1o' }
headersccc = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'viewport-width': '546',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'CometProfilePlusLikeMutation',
    'x-fb-lsd': 'KA9qtqSd7hV8150DnYqqmy' }

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        return None
import sys
import time

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

# Example Usage

slow_print(" '\x1b[1;31m  This Tools Is strictly 1 device only , Purchase a full script to use Multiple Devices ", delay= 0.01)
slow_print (" \x1b[1;31m Loading PLEASE WAIT ... ", delay= 0.07)


def logo():
	print(f"""\x1b[1;31m
             {G}W E L C O M E   T O  B O O S T I N G  T O O L S
{G}


         ██████╗░░█████╗░███╗░░██╗██████╗░░█████╗░███╗░░██╗
         ██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗████╗░██║
         ██████╦╝██║░░██║██╔██╗██║██████╦╝██║░░██║██╔██╗██║
         ██╔══██╗██║░░██║██║╚████║██╔══██╗██║░░██║██║╚████║
         ██████╦╝╚█████╔╝██║░╚███║██████╦╝╚█████╔╝██║░╚███║
         ╚═════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚══╝
       
                {R} NOTE {P}: {R} NOT FOR FREE 

{B}┌─── {G}❏ {Y}❏ {O}❏ {W}❏{B}───────{T}T O O L   I N F O R M A T I O N S{B}────────────────────┐
{B}│  {G}❯ {P}Uses     : {G}Boosting            {red}  ➙{white} Lifetime access          {B}       │
{B}│  {G}❯ {P}Status   : {G} Active              {red} ➙ {white}No monthly Fee              {B}    │
{B}│  {G}❯ {P}Tools    : {G}Paided/Premium       {red} ➙{white} Fast Process             {B}       │
{B}│  {G}❯ {P}Network  : {G} All Network          {red}➙ {white}Customizable             {B}       │
{B}│                                                   {red}    version {G}2.3   {white} {B} │
{B}└───────────────────────────────────────────────────── {G}❏ {Y}❏ {O}❏ {W}❏{B}──────────┘

 {B}┌──{R}[ {S}AUTHOR/OWNER{R} ]
 {B}╰────── {G}❯{Y}❯{O}❯{W}❯ {Y} BONBON  """)


def clear():
    os.system('clear')


def get_access_token_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip().split('\n')
    except FileNotFoundError:
        print(f'''{red}  Start the tool first!''')
        return None

import requests

def convert_to_traodoisub(url):
    try:
        response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
        response.raise_for_status()
        return response.json().get('id')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_uid_from_link(post_link):
    pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
    match = re.match(pattern, post_link)
    if match:
        return match.group(1)
    print('Invalid post link.')

def store():
    clear()
    logo()
    print(f"{white}  CHOOSE AN OPTION:")
    print(f"{yellow}  [1] {blue}VIEW STORE PAGES AND ACCOUNT")
    print(f"{yellow}  [2] {blue}REMOVE SPECIFIC STORE PAGES AND ACCOUNT")
    line()    
    choice = input(f"{yellow}  Choose : {green}")
    line()
    if choice == '1':
        display_file_info()
        return
    elif choice == '2':
        choose_file_and_delete_line()
        return
    else:
        print(f"{red}  Invalid choice!")

def choose_file_and_delete_line():
    print(f"{white}  CHOOSE SPECIFIC LINE TO DELETE:")
    print(f"{yellow}  [1] {blue}VIEW YOUR LIST OF FRA")
    print(f"{yellow}  [2] {blue}VIEW YOUR LIST OF RPA")
    print(f"{yellow}  [3] {blue}VIEW YOUR LIST OF FRA PAGES")
    print(f"{yellow}  [4] {blue}VIEW YOUR LIST OF RPA PAGES")
    print(f"{red}  [0] {red}RETURN TO MAIN MENU")
    line()
    account_choose = input(f"{yellow}  Choose : {green}")
    line() 
    path_file = None
    check_path = None
    if account_choose == '1':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    elif account_choose == '2':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    elif account_choose == '3':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'
    elif account_choose == '4':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
    elif account_choose == '0':
        print('Returning...')
        return
    else:
        print("Invalid choice")
        return
    delete_line(path_file, check_path)

import os

def delete_line(path_file, check_path):
    display_file_content(check_path)
    line()
    lines_to_delete = input(f'''{yellow}  Enter numbers you want to delete {blue}[Use comma if multiple]{yellow}: {green}''')
    line_numbers = lines_to_delete.split(',') 
    if not line_numbers:
        print(f'''{red}  No valid line numbers provided.''')
        return
    sed_command_path_file = " ".join([f"-e '{line_number}d'" for line_number in line_numbers])
    sed_command_check_path = " ".join([f"-e '{line_number}d'" for line_number in line_numbers])
    os.system(f"sed -i {sed_command_path_file} {path_file}")
    os.system(f"sed -i {sed_command_check_path} {check_path}")
    print(f'''{green}  Lines {', '.join(line_numbers)} have been deleted.''')

def display_file_info():
    print(f'''{white}  CHOOSE FILE TO DISPLAY INFO:''')
    print(f'''{yellow}  [1] {blue}VIEW YOUR LIST OF FRA''')
    print(f'''{yellow}  [2] {blue}VIEW YOUR LIST OF RPA''')
    print(f'''{yellow}  [3] {blue}VIEW YOUR LIST OF FRA PAGES''')
    print(f'''{yellow}  [4] {blue}VIEW YOUR LIST OF RPA PAGES''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    while True:
        file_choose = input(f'''{yellow}  Choose : {green}''')
        line()
        if file_choose == '1' or file_choose == '01':
            file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
            display_file_content(file_path)
            break
        elif file_choose == '2' or file_choose == '02':
            file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'
            display_file_content(file_path)
            break
        elif file_choose == '3' or file_choose == '03':
            file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'
            display_file_content(file_path)
            break
        elif file_choose == '4' or file_choose == '04':
            file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
            display_file_content(file_path)
            break
        elif file_choose == '0' or file_choose == '00':
            main()
            break
        else:
            print(f'''{red}  Invalid Input!''')
            sleep(1.5)

def display_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            total_lines = len(content)
            print(f'''{yellow}  Total : {green}{total_lines}\n''')
            for index, line in enumerate(content, start=1):
                print(f'''{yellow}  [{index}] {white}- {green}''' + line.strip())
    except FileNotFoundError:
        print(f'''{red}  Please store the file first!''')

import os

def delete_files():
    clear()
    logo()
    print(f'''{white}  CHOOSE TO RESET:''')
    print(f'''{yellow}  [1] {blue}RESET YOUR LIST OF FRA''')
    print(f'''{yellow}  [2] {blue}RESET YOUR LIST OF RPA''')
    print(f'''{yellow}  [3] {blue}RESET YOUR LIST OF FRA PAGES''')
    print(f'''{yellow}  [4] {blue}RESET YOUR LIST OF RPA PAGES''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    while True:
        account_choose = input(f'''{yellow}  Choose : {green}''')
        line()
        if account_choose == '1' or account_choose == '01':
            file_paths = [
                '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
                '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt']
            all_deleted = True
            for file_path in file_paths:
                if os.path.exists(file_path):
                    os.remove(file_path)
                else:
                    all_deleted = False
            if all_deleted:
                print(f'''{green}\n  Tool Successfully Reset!''')
                break
            else:
                print(f'''{red}\n  Use the tool first!''')
                break
        elif account_choose == '2' or account_choose == '02':
            file_paths = [
                '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
                '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt']
            all_deleted = True
            for file_path in file_paths:
                if os.path.exists(file_path):
                    os.remove(file_path)
                else:
                    all_deleted = False
            if all_deleted:
                print(f'''{green}\n  Tool Successfully Reset!''')
                break
            else:
                print(f'''{red}\n  Use the tool first!''')
                break
        elif account_choose == '3' or account_choose == '03':
            file_paths = [
                '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
                '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt']
            all_deleted = True
            for file_path in file_paths:
                if os.path.exists(file_path):
                    os.remove(file_path)
                else:
                    all_deleted = False
            if all_deleted:
                print(f'''{green}\n  Tool Successfully Reset!''')
                break
            else:
                print(f'''{red}\n  Use the tool first!''')
                break
        elif account_choose == '4' or account_choose == '04':
            file_paths = [
                '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt',
                '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt']
            all_deleted = True
            for file_path in file_paths:
                if os.path.exists(file_path):
                    os.remove(file_path)
                else:
                    all_deleted = False
            if all_deleted:
                print(f'''{green}\n  Tool Successfully Reset!''')
                break
            else:
                print(f'''{red}\n  Use the tool first!''')
                break
        elif account_choose == '0' or account_choose == '00':
            main()
            break
        else:
            print(f'''{red}  Invalid Input!''')
            sleep(1.5)

def extract_and_save_facebook_pages():
    line()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    paths = {
        '1': ['/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'],
        '2': ['/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'],
        '3': ['/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'],
        '4': ['/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt']
    }
    if account_choose in paths:
        for file in paths[account_choose]:
            with open(file, 'a') as f:
                pass
        path_file, check_path = paths[account_choose]
        get_facebook_pages(path_file, check_path)  # Pass the correct paths to the function
        return None
    elif account_choose == '0':
        start_tool()
        return None
    else:
        print(f'''{red}  Invalid choice!''')
        return None

import requests

def get_facebook_pages_with_token(poo):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'''Bearer {poo}'''
    }
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    paths = {
        '1': ['/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'],
        '2': ['/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'],
        '3': ['/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'],
        '4': ['/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt']
    }
    if account_choose in paths:
        path_file, check_path = paths[account_choose]
    elif account_choose == '0':
        start_tool()
        return None
    else:
        print(f'''{red}  Invalid choice!''')
        return None
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f'''  {red}Error: {response.text}''')
        line()
        return None
    data = response.json()
    pages_data = data['data']
    total_pages = 0
    new_pages = 0
    print(f'''{yellow}  Total pages in account: {green}{len(pages_data)}''')
    line()
    try:
        with open(check_path, 'r') as file:
            existing_pages = file.readlines()
            existing_pages = {line.strip().split('|')[0]: line.strip().split('|')[1] for line in existing_pages}
    except FileNotFoundError:
        existing_pages = {}
    for page in pages_data:
        page_id = page['id']
        page_name = page['name']
        page_access_token = page['access_token']
        if page_id in existing_pages and existing_pages[page_id] == page_name:
            print(f'''{red}  Page already exists: {yellow}{page_id} | {page_name}''')
        else:
            print(f'''{white}ID: {yellow}{page_id} {white}---> {green}Successfully Extracted!''')
            new_pages += 1
            total_pages += 1
            with open(check_path, 'a') as file:
                file.write(f'''{page_id}|{page_name}\n''')
            with open(path_file, 'a') as file:
                file.write(f'''{page_access_token}\n''')
    print(f'''{yellow}  New pages extracted: {green}{new_pages}''')
    line()
    return pages_data

import requests
import random
import string

def get_facebook_pages():
    clear()
    logo()
    print(f'''{green}  METHOD 1 {white}---> {yellow}EXTRACT NORMAL ACCOUNT PAGES''')
    line()
    ids = input(f'''{yellow}  Enter Facebook ID: {green}''')
    line()
    pas = input(f'''{yellow}  Enter Facebook Password: {green}''')
    line()
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = f'''[FBAN/FB4A;FBAV/{random.randint(49, 66)}.0.0.{random.randint(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv};FBCR/CLARO BR;FBMF/Xiaomi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/density=2.75,width=1080,height=2216;FB_FW/1;FBRV/470765339;] FBBK/1'''
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pas,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        response = requests.post(url, data=data, headers=headers)
        po = response.json()
        if 'session_key' in po:
            token = po.get('access_token', '')
            cookie = po.get('session_cookies', {})
            print(f'''  {white}ID : {yellow}{uid} {white}---> {green}Successfully Extract!''')
            return get_facebook_pages_with_token(token)
        else:
            print(f'''  {red}ID : {red}{uid} {white}---> {red}Failed to Extract!''')
            return None
    except Exception as e:pass

import requests
import random
import string
import uuid

import random
import string
import requests

def get_facebook_account():
    clear()
    logo()
    print(f'''{green}  METHOD 2 {white}---> {yellow}EXTRACT SINGLE NORMAL ACCOUNT''')
    line()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    if account_choose == '1':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    elif account_choose == '2':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    elif account_choose == '3':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'
    elif account_choose == '4':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
    elif account_choose == '0':
        start_tool()
        return None
    else:
        print(f'''{red}Invalid choice!''')
        return None
    uid = input(f'''{yellow}  Enter Facebook ID: {green}''')
    line()
    pas = input(f'''{yellow}  Enter Facebook Password: {green}''')
    line()
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    ua_bgraph = f'''[FBAN/FB4A;FBAV/{random.randint(49, 66)}.0.0.{random.randint(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv};FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBCA/arm64-v8a:;FBOP/1]'''
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pas,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://graph.facebook.com/auth/login'
    try:
        response = requests.post(url, data=data, headers=headers)
        po = response.json()
        if 'session_key' in po:
            cookie = '; '.join([f"{i['name']}={i['value']}" for i in po.get('session_cookies', [])])
            token = po.get('access_token', '')
            open('/sdcard/.EXTRACT-COOKIE-ACCOUNT-NAME-ID.txt', 'a').write(f'{cookie}\n')
            print(f'''  {white}ID : {yellow}{uid} {white}---> {green}Successfully Extracted!''')
            open(check_path, 'a').write(f'{uid}\n')
            open(path_file, 'a').write(f'{token}\n')
        else:
            print(f'''  {red}ID : {red}{uid} {white}---> {red}Failed to Extract!''')
    except Exception as e:pass

ok = []
checkpoint = []
loop = 0
import uuid
import requests
import random
import sys
from concurrent.futures import ThreadPoolExecutor as thread

import os
import threading
from concurrent.futures import ThreadPoolExecutor

def bgraph_bulk_account():
    clear()
    logo()
    print(f'''{green}  METHOD 3 {white}---> {yellow}EXTRACT BULK NORMAL ACCOUNTS M1''')
    print(f'''{red}  File Format : {green}uid|password''')
    line()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    if account_choose == '1':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    elif account_choose == '2':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    elif account_choose == '3':
        path_file = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'
    elif account_choose == '4':
        path_file = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt'
    elif account_choose == '0':
        start_tool()
        return None
    else:
        print(f'''{red}Invalid choice!''')
        return None
    filee = input(f'''{yellow}  Input File Path : {green}''')
    line()
    try:
        with open(filee, 'r') as file:
            fo = file.read().splitlines()
    except FileNotFoundError:
        print(f'''{red}  File Not Found''')
        slp(5)
        main()
        return None
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in fo:
                uid, pw = i.split('|')
                executor.submit(graph, uid, pw, path_file, check_path)

import random
import requests

def graph(uid, pw, path_file, check_path):
    global loop
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    simm3 = random.choice(['GLOBE', 'SMART'])
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    try:
        po = requests.post(url, headers=headers, data=data).json()
        if 'session_key' in po:
            cookies = po.get('session_cookies', [])
            cookie_str = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            access_token = po.get('access_token', '')
            with open(check_path, 'r') as check_file:
                if uid in check_file.read():
                    print(f'''{red}  Account Already Exist in Tool {yellow}---> {red}{uid}''')
                    line()
                    return
            print(f'''  {white}ID : {yellow}{uid} {white}---> {green}account Successfully Extract !''')
            line()
            with open(check_path, 'a') as check_file:
                check_file.write(uid + '\n')
            with open(path_file, 'a') as path_file_obj:
                path_file_obj.write(f'{access_token}\n')
            ok.append(uid)
        else:
            print(f'''  {red}ID : {red}{uid} {white}---> {red}account Failed to Extract! {yellow} [ Account Failed ] ''')
            line()
    except Exception as e:pass
    loop += 1

import requests

def get_facebook_pages_with_token3(uid, poo, path_file, check_path):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {poo}'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'''  {red}ACCOUNT : {red}{uid} {white}---> {red}Failed! Error: {e}''')
        line()
        return None
    try:
        data = response.json()
        pages_data = data.get('data', [])
    except ValueError:
        print(f'''  {red}ACCOUNT : {red}{uid} {white}---> {red}Failed! Invalid JSON Response.''')
        line()
        return None
    total_accounts = 0
    new_accounts = 0
    print(f'''  {white}ACCOUNT : {yellow}{uid}{white} ---> Total pages extracted: ''', end=' ')
    try:
        with open(check_path, 'r') as file:
            existing_pages = file.readlines()
        existing_page_ids = {line.strip().split('|')[0] for line in existing_pages}
    except FileNotFoundError:
        existing_page_ids = set()
    for page in pages_data:
        pages_access_token = page.get('access_token', '')
        pages_name = page.get('name', 'Unknown')
        pages_id = page.get('id', '')
        if not pages_id:
            continue
        if pages_id in existing_page_ids:
            print(f'''\n{red}  Page Already Exists in Tool {yellow}---> {red}{pages_id} | {pages_name}''')
            continue
        new_accounts += 1
        total_accounts += 1
        try:
            with open(check_path, 'a') as file:
                file.write(f'{pages_id}|{pages_name}\n')
        except Exception as e:
            print(f'''{red}  Error writing to check_path: {e}''')
        try:
            with open(path_file, 'a') as file:
                file.write(f'{pages_access_token}\n')
        except Exception as e:
            print(f'''{red}  Error writing to path_file: {e}''')
    print(f'''{green}[{total_accounts}]''')
    line()
    return pages_data

import os
import time
import concurrent.futures

def bgraph_bulk_pages():
    clear()
    logo()
    print(f'''{green}  METHOD 5 {white}---> {yellow}EXTRACT BULK ACCOUNTS PAGES''')
    print(f'''{red}  File Format : {green}uid|password''')
    line()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    paths = {
        '1': ('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt'),
        '2': ('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt'),
        '3': ('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt'),
        '4': ('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', '/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt')
    }
    if account_choose == '0':
        start_tool()
        return
    if account_choose not in paths:
        print(f"{red} Invalid choice!")
        return
    path_file, check_path = paths[account_choose]
    try:
        open(path_file, 'a').close()
        open(check_path, 'a').close()
    except Exception as e:
        print(f"{red} Error initializing files: {e}")
        return
    filee = input(f'''{yellow}  Input File Path : {green}''')
    line()
    if not os.path.exists(filee):
        print(f'''{red}  File Not Found''')
        time.sleep(5)
        main()
        return
    try:
        with open(filee, 'r') as file:
            fo = file.read().splitlines()
    except Exception as e:
        print(f"{red} Error reading input file: {e}")
        return
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for line in fo:
                uid, pw = line.split('|')
                executor.submit(graph2, uid, pw, path_file, check_path)

def graph2(uid, pw, path_file, check_path):
    global loop
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    simm3 = random.choice(['GLOBE', 'SMART'])
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    try:
        po = requests.post(url, headers=headers, data=data).json()
        if 'session_key' in po:
            cookies = po.get('session_cookies', [])
            cookie_str = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            access_token = po.get('access_token', '')
            with open(check_path, 'r') as check_file:
                if uid in check_file.read():
                    print(f'''{red}  Account Already Exist in Tool {yellow}---> {red}{uid}''')
                    line()
                    return
            print(f'''  {white}ID : {yellow}{uid} {white}---> {green}Successfully Extract!''')
            line()
            with open(check_path, 'a') as check_file:
                check_file.write(uid + '\n')
            with open(path_file, 'a') as path_file_obj:
                path_file_obj.write(f'{access_token}\n')
            ok.append(uid)
        print(f'''  {red}ID : {red}{uid} {white}---> {red}Failed to Extract!''')
        line()
    except Exception as e:pass
    loop += 1

ids = []
OK = []
CP = []
loop = 0

def get_ua():
    return f'''Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/{random.randrange(100, 9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(1, 9)}; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B'''

import threading
from concurrent.futures import ThreadPoolExecutor

def datr():
    global loop
    ids.clear()
    OK.clear()
    CP.clear()
    loop = 0
    clear()
    logo()
    print(f'''{green}  METHOD 4 {white}---> {yellow}EXTRACT BULK NORMAL ACCOUNTS M2''')
    line()
    file_name = input(f'''{yellow}  Put file path : {green}''')
    line()
    try:
        with open(file_name, 'r') as file:
            ids.extend(file.read().splitlines())
    except Exception as e:
        print(f"Error reading file: {e}")
        sleep(0.8)
        main()
        return
    with ThreadPoolExecutor(max_workers=30) as checker:
        for id in ids:
            checker.submit(_Cookies, id)
    exit()

import requests
import re

def getCookies(uid, password):
    session = requests.Session()
    _ua = get_ua()
    _fb = session.get('https://m.facebook.com').text
    _data = {
        'lsd': re.search('name="lsd" value="(.*?)"', _fb).group(1),
        'jazoest': re.search('name="jazoest" value="(.*?)"', _fb).group(1),
        'm_ts': re.search('name="m_ts" value="(.*?)"', _fb).group(1),
        'li': re.search('name="li" value="(.*?)"', _fb).group(1),
        'try_number': '0',
        'unrecognized_tries': '0',
        'email': uid,
        'pass': password,
        'login': 'Log In'
    }
    _header = {
        'authority': 'm.facebook.com',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-PK,en-GB,en-US;q=0.9,en;q=0.8,en;q=0.7',
        'dnt': '1',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br',
        'cache-control': 'max-age=0',
        'user-agent': _ua
    }
    _res = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=_data, headers=_header).text
    cookies_dict = session.cookies.get_dict()
    cookies = "; ".join([f"{key}={value}" for key, value in cookies_dict.items()])
    return cookies

def _Cookies(id):
    global loop
    uid, psw = id.split('|')
    _cookies = getCookies(uid, psw)
    if 'c_user' in _cookies:
        print(f'''  {white}ID : {yellow}{uid} {white}---> {green}Successfully Extract!''')
        line()
        with open('/sdcard/.EXTRACT-COOKIE-ACCOUNT.txt', 'a') as f:
            f.write(_cookies + '\n')
    elif 'checkpoint' in _cookies:
        print(f'''  {red}ID : {red}{uid} {white}---> {red}Failed!''')
        line()
    loop += 1
    return None

import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs
import os

def p_like():
    clear()
    logo()
    ses = requests.Session()
    cokix = input(f'''{yellow}  Cookie : {green}''')
    line()
    ids_coki = input(f'''{yellow}  Input File Path :{green} ''')
    page_id = []
    try:
        with open(ids_coki, 'r') as file:
            page_id = file.read().splitlines()
    except FileNotFoundError:
        print("  File not found")
        sleep(3)
        return
    page_ids = input(f'''{yellow}  Input Target Page ID : {green}''')
    line()
    limitx = int(input(f'''{yellow}  Quantity : {green}'''))
    headersccc['user-agent'] = W_ueragnt()
    mbasic_url = 'https://mbasic.facebook.com/' + page_ids
    reqx = bs(ses.get(mbasic_url, headers=headersccc, cookies={'cookie': cokix}).content, 'html.parser')
    reqxx = reqx.find_all('a', string='Message')
    d_pa_id = str(reqxx).split('href="/messages/thread/')[1].split('/')[0]
    clear()
    logo()
    print(f'''{yellow}  Total Page : {green}{len(page_id)}''')
    print(f'''{yellow}  Target     : {green}{page_ids}''')
    line()
    for i in range(min(len(page_id), limitx)):
        pageid = page_id[i]
        page_uidz = 'i_user=' + pageid
        cookies_page = {'cookie': cokix + page_uidz}
        mylove = ThreadPoolExecutor(max_workers=30)
        mylove.submit(likepage, cookies_page, pageid, page_ids, d_pa_id)
        line()
        line()
        print(f'{red}  FAILED')
        print(cokix)
        print(linex())
        with open('failed.txt', 'a', encoding='utf8') as f:
            f.write(f'''{cokix}\n''')
        return
    return None

import requests
import re
from bs4 import BeautifulSoup as bs

def likepage(cookies_page, pageid, page_ids, d_pa_id, ses, headers):
    headers['user-agent'] = W_ueragnt()
    web_url = f'https://www.facebook.com/profile.php?id={page_ids}'
    try:
        req = bs(ses.get(web_url, headers=headers, cookies=cookies_page).content, 'html.parser')
        uidx = re.search('__user=(.*?)&', str(req))
        if uidx:
            uidx = uidx.group(1)
        else:
            print(f"{red}Failed to find user ID for page {pageid}")
            return None
        dpr = re.search('"pr":(.*?),', str(req))
        fb_dtsg = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req))
        jazoest = re.search('&jazoest=(.*?)"', str(req))
        lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req))
        if not all([dpr, fb_dtsg, jazoest, lsd]):
            print(f"{red}Missing necessary data for page {pageid}")
            return None
        data_post = {
            'av': uidx,
            'dpr': dpr.group(1),
            'fb_dtsg': fb_dtsg.group(1),
            'jazoest': jazoest.group(1),
            'lsd': lsd.group(1),
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
            'variables': f'''{{"input":{{"is_tracking_encrypted":false,"page_id":{d_pa_id!s},"source":null,"tracking":null,"actor_id":{uidx!s},"client_mutation_id":"1"}},"scale":1}}''',
            'server_timestamps': 'true',
            'doc_id': '6716077648448761'
        }
        response = ses.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data_post)
        if response.status_code == 200:
            data = response.json()
            subscribe_status = data['data']['page_like']['page']['subscribe_status']
            done.append(pageid)
            print(f'''{white}  [{len(done)}] {green}Page Like and Follow Done :{white} {pageid} ''')
        else:
            print(f"{red}  Failed to like page {pageid} with status code {response.status_code}")
    except Exception as e:
        print(f"{red}An error occurred while processing page {pageid}: {str(e)}")
    return None

done = []

import requests
import re
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs

def g_join():
    clear()
    logo()
    cokix = input(f'''{yellow}  Cookie : {green}''')
    line()
    try:
        ids_coki = input(f'''{yellow}  Input File Path : {green} ''')
        page_id = open(ids_coki).read().splitlines()
    except FileNotFoundError:
        print('  File not found')
        sleep(3)
        return
    line()
    group_ids = input(f'''{yellow}  Input Group ID : {green}''')
    line()
    limitx = int(input(f'''{yellow}  Quantity : {green}'''))
    clear()
    logo()
    print(f'''{yellow}  Total Pages: {green}{len(page_id)}''')
    print(f'''{green}  Target Group: {green}{group_ids}''')
    line()
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(min(len(page_id), limitx)):
            pageid = page_id[i]
            page_uidz = f'i_user={pageid}'
            cookies_page = {
                'cookie': cokix + page_uidz
            }
            executor.submit(g_joining, cookies_page, pageid, group_ids)
    print(f"Joining process completed for {len(done)} pages.")
    return None

def g_joining(cookies_page, pageid, group_ids):
    secx = requests.Session()
    use_link = f'https://www.facebook.com/groups/{group_ids}'
    headers = {'user-agent': W_ueragnt()}
    req = bs(secx.get(use_link, headers=headers, cookies=cookies_page).content, 'html.parser')
    try:
        av = re.search('__user=(.*?)&', str(req)).group(1)
        dpr = re.search('"pr":(.*?),', str(req)).group(1)
        fb_dtsg = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req)).group(1)
        jazoest = re.search('&jazoest=(.*?)"', str(req)).group(1)
        lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1)
    except AttributeError:
        print(f"{red}Error extracting necessary data for page {pageid}")
        return None        
    data = {
        'av': av,
        'dpr': dpr,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': lsd,
        'qpl_active_flow_ids': '431626709',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
        'variables': f'''{{"feedType":"DISCUSSION","groupID":{group_ids!s},"imageMediaType":"image/x-auto","input":{{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1697077069058,802502,2361831622,","group_id":{group_ids!s},"group_share_tracking_params":{{"app_id":"2220391788200892","exp_id":"null","is_from_share":false}},"actor_id":{av!s},"client_mutation_id":"1"}},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":true,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":true}}''',
        'server_timestamps': 'true',
        'doc_id': '24830959139836152',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]'
    }
    response = secx.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data)
    if response.status_code == 200:
        done.append(pageid)
        print(f'''{white}  [{len(done)}] {green}Group Joining Done: {white}{pageid}''')
    else:
        print(f"{red}Error: Failed to join group {pageid}")
    return None

done = []

import requests
import re
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs

def g_join():
    clear()
    logo()
    cokix = input(f'''{yellow}  Cookies : {green}''')
    line()
    try:
        ids_coki = input(f'''{yellow}  Input File Path : {green} ''')
        with open(ids_coki, 'r') as file:
            page_id = file.read().splitlines()
    except FileNotFoundError:
        print('  File not found')
        sleep(2)
        return
    line()
    group_ids = input(f'''{yellow}  Input Group ID : {green}''')
    line()
    limitx = int(input(f'''{yellow}  Quantity : {green}'''))
    clear()
    logo()
    print(f'''{green}  Total Pages: {yellow}{len(page_id)}''')
    print(f'''{green}  Target Group: {yellow}{group_ids}''')
    line()
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(min(len(page_id), limitx)):
            pageid = page_id[i]
            page_uidz = f'i_user={pageid}'
            cookies_page = {'cookie': cokix + page_uidz}
            executor.submit(g_joining, cookies_page, pageid, group_ids)
    print(f"Joining process completed for {len(done)} pages.")
    return None

def g_joining(cookies_page, pageid, group_ids):
    secx = requests.Session()
    use_link = f'https://www.facebook.com/groups/{group_ids}'    
    headers = {'user-agent': W_ueragnt()}
    req = bs(secx.get(use_link, headers=headers, cookies=cookies_page).content, 'html.parser')
    try:
        av = re.search('__user=(.*?)&', str(req)).group(1)
        dpr = re.search('"pr":(.*?),', str(req)).group(1)
        fb_dtsg = re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req)).group(1)
        jazoest = re.search('&jazoest=(.*?)"', str(req)).group(1)
        lsd = re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1)
    except AttributeError:
        print(f"{red}Error extracting necessary data for page {pageid}")
        return None
    data = {
        'av': av,
        'dpr': dpr,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'lsd': lsd,
        'qpl_active_flow_ids': '431626709',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
        'variables': f'''{{"feedType":"DISCUSSION","groupID":{group_ids!s},"imageMediaType":"image/x-auto","input":{{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1697077069058,802502,2361831622,","group_id":{group_ids!s},"group_share_tracking_params":{{"app_id":"2220391788200892","exp_id":"null","is_from_share":false}},"actor_id":{av!s},"client_mutation_id":"1"}},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":true,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":true}}''',
        'server_timestamps': 'true',
        'doc_id': '24830959139836152',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]'
    }
    response = secx.post('https://www.facebook.com/api/graphql/', cookies=cookies_page, headers=headers, data=data)
    if response.status_code == 200:
        done.append(pageid)
        print(f'''{white}  [{len(done)}] {green}Group Joining Done: {white}{pageid}''')
    else:
        print(f"{red}Error: Failed to join group {pageid}")
    return None

import requests
import re
import time

def react():
    ses = requests.Session()

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_path = None
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    if file_path is None:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        react()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    post_link = input(f'''{yellow}  Enter post link: {green}''')
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f'''{red}  UID extraction failed. Please provide a valid post link. Copy link on Facebook Lite!''')
        return None
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{red}  [1] {blue}LIKE''')
    print(f'''{red}  [2] {blue}LOVE''')
    print(f'''{red}  [3] {blue}HAHA''')
    print(f'''{red}  [4] {blue}WOW''')
    print(f'''{red}  [5] {blue}ANGRY''')
    print(f'''{red}  [6] {blue}SAD''')
    line()
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f"{red}  Failed to convert the link.")
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{target_uid}_{converted_link}'''
        auto_react = f'''https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {'user-agent': W_ueragnt()}  # Assuming W_ueragnt() is defined
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            print(f'''{green}  REACTOR {i + 1} ---> Successfully Reacted! ''')
            success_count += 1
        else:
            print(f'''{red}  REACTOR {i + 1} ---> Failed to React!''')
            failure_count += 1
    line()
    print(f'''{yellow}  TOTAL : ''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')

import requests
import re
import time

def react_to_story():
    ses = requests.Session()

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_path = None
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    if file_path is None:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        react_cover()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    line() 
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        target_uid = '100023826018132'
        uid_url = '959545101516348'
        auto_react = f'''https://graph.facebook.com/100023826018132_959545101516348/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {'user-agent': W_ueragnt()}
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            print(f'''{green}  REACTOR {i + 1} ---> Successfully Reacted! ''')
            success_count += 1
        else:
            print(f'''{red}  REACTOR {i + 1} ---> Failed to React!''')
            failure_count += 1
    line()
    print(f'''{yellow}  TOTAL : ''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')

import requests
import re
import time

def react_dp_cover():
    ses = requests.Session()

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_path = None
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return

    if file_path is None:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        react_cover()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    substory_index = input(f'''{yellow}  Input DP/Cover FB ID: {green}''')
    line()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    line()
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        auto_react = f'''https://graph.facebook.com/v18.0/{substory_index}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {'user-agent': W_ueragnt()}
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            print(f'''{green}  REACTOR {i + 1} ---> Successfully Reacted! ''')
            success_count += 1
        else:
            print(f'''{red}  REACTOR {i + 1} ---> Failed to React!''')
            failure_count += 1
    line()
    print(f'''{yellow}  TOTAL : ''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')

headers_fb_lite = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/380.0.0.14.112;]',
    'viewport-width': '707' }

import requests
from concurrent.futures import ThreadPoolExecutor
import time

def react_with_care():
    clear()
    logo()
    coki_file_name = '/sdcard/.EXTRACT-COOKIE-ACCOUNT.txt'
    try:
        with open(coki_file_name, 'r', encoding='utf-8') as file:
            coki_file = file.read().splitlines()
    except FileNotFoundError:
        print(f'''{red}  Start the tool first!''')
        return None
    inpt_link = input(f'''{yellow}  Post Link : {green}''')
    uid = convert_to_traodoisub(inpt_link)
    if not uid:
        print(f'''{red}  Unable to extract UID from the provided link.''')
        return None 
    post_link = f'''https://mbasic.facebook.com/reactions/picker/?ft_id={uid}&origin_uri='''
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}CARE''')
    print(f'''{yellow}  [4] {blue}HAHA''')
    print(f'''{yellow}  [5] {blue}WOW''')
    print(f'''{yellow}  [6] {blue}ANGRY''')
    print(f'''{yellow}  [7] {blue}SAD''')
    line()
    inx = input(f'''{yellow}  Choose : {green}''')
    reaction_ids = {
        '1': '1635855486666999',
        '2': '1678524932434102',
        '3': '613557422527858',
        '4': '115940658764963',
        '5': '478547315650144',
        '6': '444813342392137',
        '7': '908563459236466'
    }
    if inx not in reaction_ids:
        print(f'''{red} Invalid option selected.''')
        return None    
    r_id = reaction_ids[inx]
    line()
    try:
        limite = int(input(f'''{yellow}  Input limit less than {green}{len(coki_file)} {yellow}: {green}'''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limite > len(coki_file):
        print(f'''{red}  Error: The specified limit exceeds the number of available cookies.''')
        return None
    clear()
    logo()
    print(f'''{yellow}  Target    : {green}{uid}''')
    print(f'''{yellow}  Limit     : {green}{limite}''')
    line()
    executor = ThreadPoolExecutor(max_workers=30)
    for i in range(min(len(coki_file), limite)):
        coki = coki_file[i]
        executor.submit(sending, coki, post_link, r_id)

def sending(coki, post_link, r_id):
    headers_fb_lite = {
    'user-agent': W_ueragnt(),
    'cookie': coki
    }
    try:
        getdata = html_req(post_link, headers=headers_fb_lite, cookies={'cookie': coki})
        all_links = getdata.find_all('a')
        for link in all_links:
            url = 'https://mbasic.facebook.com' + link['href']
            if r_id in url:
                response = requests.get(url, headers=headers_fb_lite, cookies={'cookie': coki})
                pageid = str(coki).split('c_user=')[1].split(';')[0]
                if pageid in response.text:
                    print(f'''{yellow}  Successfully Reacted! {white}---> {green}{pageid}''')
    except Exception as e:
        print(f'''{red}  An error occurred: {e}''')

import requests
import time

def react_comment():
    ses = requests.Session()

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f'''{red}  Start the tool first!''')
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    comment_uid = input(f'''{yellow}  Enter Comment UID: {green}''')
    line()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    line()
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : {green}'''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{comment_uid}'''
        auto_react = f'''https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            success_count += 1
            print(f'''{green}  REACTOR {i + 1} ---> Successfully Reacted!''')
        else:
            failure_count += 1
            print(f'''{red}  REACTOR {i + 1} ---> Failed to React!''')
    line()
    print(f'''{yellow}  TOTAL : \n''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')

import requests
import time

def get_access_token_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip().split('\n')
    except FileNotFoundError:
        print(f'''{red}  Start the tool first!''')
        return None

def react_reels():
    ses = requests.Session()
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    comment_uid = input(f'''{yellow}  Enter Reels Video UID: {green}''')
    line()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    line()
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{comment_uid}'''
        auto_react = f'''https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers = {
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_react, headers=headers)
        if response.ok:
            success_count += 1
            print(f'''{green}  REACTOR {i + 1} ---> Successfully Reacted!''')
        else:
            failure_count += 1
            print(f'''{red}  REACTOR {i + 1} ---> Failed to React!''')
    line()
    print(f'''{yellow}  TOTAL : \n''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')

def follow():
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO FOLLOW:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    user_id = input(f'''{yellow}  Enter target UID: {green}''')
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of follows, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available followers.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        auto_follow_url = f'''https://graph.facebook.com/v19.0/{user_id}/subscribers'''
        time.sleep(1)
        headers = {
            'Authorization': f'''Bearer {access_token}''',
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_follow_url, headers=headers)
        if response.ok:
            success_count += 1
            print(f'''{green}  FOLLOWER {i + 1} ---> Successfully Followed!''')
        else:
            failure_count += 1
            print(f'''{red}  FOLLOWER {i + 1} ---> Failed to Follow!''')
    line()
    print(f'''{yellow}  TOTAL : \n''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')

import requests
import time
import re

def auto_comment():
    
    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f'''{red}  An error occurred: {e}''')
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f'''{red}  Invalid post link.''')
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f'''{red}  Start the tool first!''')
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO COMMENT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }
    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        auto_comment()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    post_link = input(f'''{yellow}  Enter post link: {green}''')
    line()
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f'''{red}  UID extraction failed. Please provide a valid post link. Copy link on Facebook Lite!''')
        return None 
    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f'''{red}  Failed to convert post link.''')
        return None
    input_comment = input(f'''{yellow}  Enter Comment : {green}''')
    comments = input_comment.split('|')
    num_comments = len(comments)
    line()
    try:
        limit = int(input(f'''{yellow}  Enter number of comments, total available is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available commentors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]
        auto_comment_url = f'''https://graph.facebook.com/{converted_link}/comments'''
        params = {'message': comment, 'access_token': access_token}
        time.sleep(1)
        headers = {'user-agent': W_ueragnt()}
        response = requests.post(auto_comment_url, params=params, headers=headers)
        if response.ok:
            print(f'''{green}  COMMENTOR {i + 1} ---> Successfully Comment!''')
            success_count += 1
        else:
            print(f'''{red}  COMMENTOR {i + 1} ---> Failed to Comment!''')
            failure_count += 1
        line()
        print(f'''{yellow}  TOTAL : \n''')
        print(f'''{green}  Completed : {white}{success_count}''')
        print(f'''{red}  Failed : {white}{failure_count}''')
    return None

import requests
import time
import re

def auto_comment_to_dp():
    
    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f'''{red}  An error occurred: {e}''')
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f'''{red}  Invalid post link.''')
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f'''{red}  Start the tool first!''')
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO COMMENT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }
    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        auto_comment_to_dp()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    converted_link = input(f'''{yellow}  Enter post FB ID: {green}''')
    line()
    input_comment = input(f'''{yellow}  Enter Comment : {green}''')
    comments = input_comment.split('|')
    num_comments = len(comments)
    line()
    try:
        limit = int(input(f'''{yellow}  Enter number of comments, total available is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available commentors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]
        auto_comment_url = f'''https://graph.facebook.com/{converted_link}/comments'''
        params = {'message': comment, 'access_token': access_token}
        time.sleep(1)
        headers = {'user-agent': W_ueragnt()}
        response = requests.post(auto_comment_url, params=params, headers=headers)
        if response.ok:
            print(f'''{green}  COMMENTOR {i + 1} ---> Successfully Comment!''')
            success_count += 1
        else:
            print(f'''{red}  COMMENTOR {i + 1} ---> Failed to Comment!''')
            failure_count += 1
        line()
        print(f'''{yellow}  TOTAL : \n''')
        print(f'''{green}  Completed : {white}{success_count}''')
        print(f'''{red}  Failed : {white}{failure_count}''')
    return None

import requests
import time
import re

def reply_to_comment():
    
    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f'''{red}  An error occurred: {e}''')
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f'''{red}  Invalid post link.''')
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f'''{red}  Start the tool first!''')
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REPLY:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }
    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        reply_to_comment()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    converted_link = input(f'''{yellow}  Enter comment FB ID: {green}''')
    line()
    input_comment = input(f'''{yellow}  Enter Comment : {green}''')
    comments = input_comment.split('|')
    num_comments = len(comments)
    line()
    try:
        limit = int(input(f'''{yellow}  Enter number of comments, total available is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available commentors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]
        auto_comment_url = f'''https://graph.facebook.com/{converted_link}/comments'''
        params = {'message': comment, 'access_token': access_token}
        time.sleep(1)
        headers = {'user-agent': W_ueragnt()}
        response = requests.post(auto_comment_url, params=params, headers=headers)
        if response.ok:
            print(f'''{green}  COMMENTOR {i + 1} ---> Successfully Comment!''')
            success_count += 1
        else:
            print(f'''{red}  COMMENTOR {i + 1} ---> Failed to Comment!''')
            failure_count += 1
        line()
        print(f'''{yellow}  TOTAL : \n''')
        print(f'''{green}  Completed : {white}{success_count}''')
        print(f'''{red}  Failed : {white}{failure_count}''')
    return None

import requests
import time
import re

def auto_comment_to_reels():
    
    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f'''{red}  An error occurred: {e}''')
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f'''{red}  Invalid post link.''')
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f'''{red}  Start the tool first!''')
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO COMMENT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{yellow}  Choose : {green}''')
    line()
    file_paths = {
        '1': '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt',
        '2': '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt',
        '3': '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt',
        '4': '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    }
    file_path = file_paths.get(account_choose)
    if not file_path:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        auto_comment_to_reels()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None  
    converted_link = input(f'''{yellow}  Enter Reels Video UID: {green}''')
    line()
    input_comment = input(f'''{yellow}  Enter Comment : {green}''')
    comments = input_comment.split('|')
    num_comments = len(comments)
    line()
    try:
        limit = int(input(f'''{yellow}  Enter number of comments, total available is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available commentors.''')
        return None 
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        comment_index = i % num_comments
        comment = comments[comment_index]
        auto_comment_url = f'''https://graph.facebook.com/{converted_link}/comments'''
        params = {'message': comment, 'access_token': access_token}
        time.sleep(1)
        headers = {'user-agent': W_ueragnt()}
        response = requests.post(auto_comment_url, params=params, headers=headers)
        if response.ok:
            print(f'''{green}  COMMENTOR {i + 1} ---> Successfully Comment!''')
            success_count += 1
        else:
            print(f'''{red}  COMMENTOR {i + 1} ---> Failed to Comment!''')
            failure_count += 1
        line()
        print(f'''{yellow}  TOTAL : \n''')
        print(f'''{green}  Completed : {white}{success_count}''')
        print(f'''{red}  Failed : {white}{failure_count}''')
    return None
import requests
import base64
import uuid
import time
import json
import re
import threading

# Define missing colors for print output
green = "\033[92m"
red = "\033[91m"
yellow = "\033[93m"
blue = "\033[94m"
white = "\033[97m"

# Global counter and lock for thread safety
successful_reactions = 0
counter_lock = threading.Lock()

def linex():
    print("=" * 0)

def Reaction(actor_id: str, post_id: str, react: str, token: str) -> bool:
    """ Function to send a reaction request """
    rui = requests.Session()
    
    feedback_id = base64.b64encode(f'feedback:{post_id}'.encode('utf-8')).decode('utf-8')
    
    var = {
        "input": {
            "feedback_referrer": "native_newsfeed",
            "tracking": None,
            "feedback_id": feedback_id,
            "client_mutation_id": str(uuid.uuid4()),
            "nectar_module": "newsfeed_ufi",
            "feedback_source": "native_newsfeed",
            "feedback_reaction_id": react,
            "actor_id": actor_id,
            "action_timestamp": str(int(time.time()))  # Convert to int to remove decimal
        }
    }
    
    data = {
        'access_token': token,
        'method': 'post',
        'pretty': False,
        'format': 'json',
        'server_timestamps': True,
        'locale': 'id_ID',
        'fb_api_req_friendly_name': 'ViewerReactionsMutation',
        'fb_api_caller_class': 'graphservice',
        'client_doc_id': '2857784093518205785115255697',
        'variables': json.dumps(var),
        'fb_api_analytics_tags': ["GraphServices"],
        'client_trace_id': str(uuid.uuid4())
    }

    try:
        pos = rui.post('https://graph.facebook.com/graphql', data=data).json()

        if react == '0':
            print(f"{green}SUCCESS REMOVED REACTION FROM {actor_id} ON {post_id}")
            return True
        elif react in str(pos):
            print(f"{green}SUCCESS REACTED WITH {actor_id} TO {post_id}")
            return True
        else:
            print(f"{red}FAILED TO REACT WITH {actor_id} TO {post_id}")
            return False
    except Exception as e:
        print(f"{red}REACTION FAILED DUE TO AN ERROR: {e}")
        return False

def process_reaction(actor_id, token, post_id, react):
    """ Function to process reactions safely with threading """
    global successful_reactions
    if Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token):
        with counter_lock:
            successful_reactions += 1

def extract_uid_from_link(post_link):
    """ Extracts the UID from Facebook post links """
    patterns = [
        r"https://www\.facebook\.com/([^/?&]+)",
        r"https://m\.facebook\.com/([^/?&]+)",
        r"https://web\.facebook\.com/([^/?&]+)",
        r"https://facebook\.com/([^/?&]+)",
        r"fbid=(\d+)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, post_link)
        if match:
            return match.group(1)
    
    print(f"{red}Invalid post link.")
    return None

def get_access_token_from_file(file_path):
    """ Reads access tokens from a file """
    try:
        with open(file_path, 'r') as file:
            return file.read().strip().split('\n')
    except FileNotFoundError:
        print(f"{red}No token file found!")
        return []

def choose_reactions():
    """ Function to let user select a reaction """
    linex()
    print("[1] LIKE 👍🏼")
    print("[2] LOVE ❤️")
    print("[3] HAHA 🤣")
    print("[4] WOW 😯")
    print("[5] CARE 🤗")
    print("[6] SAD 😣")
    print("[7] ANGRY 😡")
    print("[8] REMOVE REACTION")
    linex()
    
    rec = input("\033[1;32mCHOOSE: ")
    
    reaction_ids = {
        '1': '1635855486666999',
        '2': '1678524932434102',
        '3': '115940658764963',
        '4': '478547315650144',
        '5': '613557422527858',
        '6': '908563459236466',
        '7': '444813342392137',
        '8': '0'
    }

    return [reaction_ids[r.strip()] for r in rec if r.strip() in reaction_ids]

def convert_to_traodoisub(url):
    """ Converts a URL using traodoisub API """
    try:
        response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
        if response.status_code == 200:
            return response.json().get('id')
    except Exception as e:
        print(f"{red}An error occurred: {e}")
    return None

def react_to_story():
    """ Function to handle reactions from a list of accounts """
    file_path = "/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt"
    
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None

    post_link = input(f"{yellow}Enter post link: {green}")
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f"{red}UID extraction failed. Please provide a valid post link.")
        return None

    reaction_type = choose_reactions()
    if not reaction_type:
        print(f"{red}Invalid reaction choice.")
        return None

    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f"{red}Failed to convert the link.")
        return None

    try:
        limit = int(input(f"{yellow}Input quantity of reactions (max {len(access_tokens)}): "))
    except ValueError:
        print(f"{red}Error: Please enter a valid number.")
        return None

    if limit > len(access_tokens):
        print(f"{red}Error: Specified limit exceeds available accounts.")
        return None

    success_count, failure_count = 0, 0

    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f"{target_uid}_{converted_link}"
        auto_react = f"https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}"
        time.sleep(1)

        response = requests.post(auto_react)
        if response.ok:
            print(f"{green}Reactor {i + 1} ---> Successfully Reacted!")
            success_count += 1
        else:
            print(f"{red}Reactor {i + 1} ---> Failed to React!")
            failure_count += 1

    print(f"{yellow}TOTAL: {green}Completed: {white}{success_count} {red}Failed: {white}{failure_count}")
import requests
import random
import string
import time
import sys
import re
import json

import requests
import threading
import time
from datetime import timedelta
import time as t

def share():
    clear()
    logo()    
    access_token = input('ENTER THE TOKEN: ').strip()
    linex()
    share_url = input('ENTER THE FACEBOOK POST LINK: ').strip()
    linex()
    try:
        share_count = int(input('HOW MANY SHARES WILL THE TOOL STOP: ').strip())
    except ValueError:
        print('{red}INVALID INPUT PLEASE ENTER A NUMBER FOR SHARE COUNT.')
        return
    linex()
    time_interval = 0.01
    delete_after = 3600
    shared_count = 0
    lock = threading.Lock()
    start_time = t.time()
    success_list = []
    headers = {
        'authority': 'b-graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def share_post():
        nonlocal shared_count
        try:
            response = requests.post(
                f'https://b-graph.facebook.com/me/feed?access_token={access_token}&fields=id&limit=1&published=0',
                json={
                    'link': share_url,
                    'privacy': {'value': 'SELF'},
                    'no_story': True,
                },
                headers=headers
            )
            if response.status_code == 200:
                with lock:
                    shared_count += 1
                    success_list.append(response.json().get('id'))
                print(f'{green} SUCCESSFULLY {red}SHARED {shared_count} {orange} ⪼ {white} {share_count}')
                if shared_count == share_count:
                    print('{green}FINISHED SHARING POSTS.')
                    if success_list:
                        threading.Timer(delete_after, delete_post, args=(success_list[-1],)).start()
            else:
                print(f'{red}FAILED TO SHARE POST: {response.json()}')
        except requests.exceptions.RequestException as error:
            print(f'{red}ERROR: {str(error)}')
    while shared_count < share_count:
        share_post()
        #time.sleep(time_interval)
    elapsed_time = t.time() - start_time
    avg_time_per_share = elapsed_time / share_count if share_count > 0 else 0
    total_time = timedelta(seconds=int(elapsed_time))
    avg_time = timedelta(seconds=int(avg_time_per_share))
    print(f"🚀 TARGET: {share_url}")
    print(f"✅ SUCCESSFULLY SHARED: {shared_count}/{share_count}")
    print(f"⏳ TOTAL TIME: {total_time}")
    print(f"⏱️ AVERAGE TIME PER SHARE: {avg_time}")
    linex()
    def delete_post(post_id):
        try:
            response = requests.delete(f'https://b-graph.facebook.com/{post_id}?access_token={access_token}')
            if response.status_code == 200:
                print(f'{green}POST DELETED: {post_id}')
            else:
                print(f'{red}FAILED TO DELETE POST: {response.json()}')
        except requests.exceptions.RequestException as error:
            print(f'{red}FAILED TO DELETE POST: {str(error)}')
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(share_count):
            executor.submit(share_post)
    print(f'{green}SHARING PROCESS COMPLETED.')

    def extract_fb_pages(token):
        url = 'https://graph.facebook.com/v18.0/me/accounts'
        headers = {
            'Authorization': f'Bearer {token}' }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: {response.text}")
            return None
        data = response.json()
        pages_data = [{"accessToken": page['access_token']} for page in data['data']]
        return pages_data

    def convert_to_traodoisub(post_link):
        response = requests.post('https://id.traodoisub.com/api.php', data={'link': post_link})
        if response.status_code == 200:
            return response.json().get('id')
        return None

    def auto_share_post(post_link, token, cookie):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'authority': 'graph.facebook.com' }
        post = ses.post(f'https://graph.facebook.com/v13.0/me/feed?link={post_link}&published=0&access_token={token}', headers=headers, cookies=cookie).text
        try:
            data = json.loads(post)
            if 'id' in data:
                print(f'Post shared successfully: {data["id"]}')
            else:
                print('Error in sharing post')
        except Exception as e:
            print(f"An error occurred: {e}")    
    line()
    post_link = input(f'''{yellow}  Enter post link: {green}''')
    pages_data = extract_fb_pages(token)
    if not pages_data:
        print(f'''{red}  Error fetching Facebook.''')
        return None
    converted_link = convert_to_traodoisub(post_link)
    line()
    limit = int(input(f'''{yellow}  Enter limit of shares : {green}'''))
    line()
    n = 0
    for page in pages_data:
        auto_share_post(post_link, token, cookie)
        n += 1
        if n >= limit:
            break
    print(f'''{green}  Sharing Completed!''' )
    
import requests
import re

def Video_Extractid(url):
    match = re.search(r'/(videos|photos)/(\d+)', url)
    return match.group(2) if match else None

def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"{red}FAILED TO LOAD DATA: {e}")
        return []

def validate_access_token(access_token):
    validation_url = f"https://graph.facebook.com/debug_token?input_token={access_token}&access_token={access_token}"
    response = requests.get(validation_url)
    if response.status_code == 200:
        data = response.json().get("data", {})
        if data.get("is_valid"):
            return True
        else:
            print(f"{red}ACCESS TOKEN IS INVALID: {data}")
            return False
    else:
        print(f"{red}FAILED TO VALIDATE ACCESS TOKEN RESPONSE: {response.json()}")
        return False

def perform_comment(media_id, comment_text, access_token):
    try:
        url = f'https://graph.facebook.com/v18.0/{media_id}/comments'
        params = {'access_token': access_token, 'message': comment_text}
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print(f"{green}SUCCESS COMMENTED: '{comment_text}' ON MEDIA ID '{media_id}'.")
            return True
        else:
            error_data = response.json()
            if error_data['error']['code'] == 190 and error_data['error'].get('error_subcode') == 490:
                print(f"{red}CHECKPOINT REQUIRED FOR THIS ACCOUNT TOKEN: {access_token[:10]}... SKIPPING THIS TOKEN.")
                return False
            else:
                print(f"{red}FAILED TO POST COMMENT ON MEDIA ID '{media_id}'. RESPONSE: {error_data}")
                return False
    except requests.exceptions.RequestException as error:
        print(f"{red}AN ERROR OCCURRED DURING THE REQUEST: {error}")
        return False

def post_same_comment(url, comment_text, num_comments):
    media_id = Video_Extractid(url)
    if not media_id:
        print("{red}INVALID URL OR UNABLE TO EXTRACT MEDIA ID.")
        return
    access_tokens = load_data('/sdcard/ERROR-BOOSTING/tokp.txt')
    comment_count = 0
    while comment_count < num_comments:
        for access_token in access_tokens:
            if validate_access_token(access_token):
                if perform_comment(media_id, comment_text, access_token):
                    comment_count += 1
                if comment_count >= num_comments:
                    print(f"REACHED THE LIMIT OF {num_comments} COMMENTS.")
                    return
            else:
                print(f"SKIPPING INVALID ACCESS TOKEN: {access_token[:10]}...")
    print(f"{green}TOTAL COMMENTS POSTED: {comment_count}")

def post_different_comments(url, num_comments):
    media_id = Video_Extractid(url)
    if not media_id:
        print("{red}INVALID URL OR UNABLE TO EXTRACT MEDIA ID.")
        return
    access_tokens = load_data('/sdcard/ERROR-BOOSTING/tokp.txt')
    comments = []
    for i in range(num_comments):
        comment = input(f"ENTER COMMENT {i+1}: ")
        comments.append(comment)
    comment_count = 0
    while comment_count < num_comments:
        for access_token in access_tokens:
            if validate_access_token(access_token):
                comment_text = comments[comment_count]
                if perform_comment(media_id, comment_text, access_token):
                    comment_count += 1
                if comment_count >= num_comments:
                    print(f"REACHED THE LIMIT OF {num_comments} COMMENTS.")
                    return
            else:
                print(f"SKIPPING INVALID ACCESS TOKEN: {access_token[:10]}...")
    print(f"{green}TOTAL DIFFERENT COMMENTS POSTED: {comment_count}")

def comments_vids():
    clear()
    logo()
    print(f"[1] POST THE SAME COMMENTS")
    print(f"[2] POST DIFFERENT COMMENTS")
    print(f"[3] EXIT")
    linex()
    choice = input('\x1b[1;32mCHOOSE : ')
    linex()
    url = input("ENTER THE MEDIA URL: ")
    linex()
    if choice == '1':
        comment_text = input("ENTER THE COMMENT TEXT: ")
        linex()
        num_comments = int(input("ENTER THE NUMBER OF COMMENTS TO POST: "))
        linex()
        post_same_comment(url, comment_text, num_comments)
    elif choice == '2':
        num_comments = int(input("ENTER THE NUMBER OF COMMENTS TO POST: "))
        linex()
        post_different_comments(url, num_comments)
    elif choice == '3':
        exit()
    else:
        print(f"{red}INVALID OPTION.")
        comments_vids()

import requests
from datetime import datetime

def get_ids_tokens(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def linktradio(post_link):
    try:
        if 'photo.php?fbid=' in post_link:
            post_id = post_link.split('fbid=')[1].split('&')[0]
        elif '/posts/' in post_link:
            post_id = post_link.split('/posts/')[1].split('/')[0]
        elif '/videos/' in post_link:
            post_id = post_link.split('/videos/')[1].split('/')[0].split('?')[0]
        elif '/reel/' in post_link:
            post_id = post_link.split('/reel/')[1].split('/')[0].split('?')[0]
        else:
            print(f"{red}INVALID POST, VIDEO, OR REEL LINK.")
            return None
        return post_id
    except IndexError:
        print(f"{red}COULD NOT EXTRACT POST, VIDEO, OR REEL ID.")
        return None
import requests
import re

def get_ids_tokens(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def extract_reel_id(reels_link):
    match = re.search(r'reel/(\d+)', reels_link)
    if match:
        return match.group(1)
    else:
        print(f"{red}INVALID REEL LINK FORMAT!")
        return None

def auto_comment_on_reels(reels_link, comments, num_comments, tokens):
    reel_id = extract_reel_id(reels_link)
    if not reel_id:
        return
    url = f'https://graph.facebook.com/v13.0/{reel_id}/comments'
    total_successful_comments = 0
    total_failed_comments = 0
    token_index = 0
    comment_index = 0
    available_tokens = len(tokens)
    if num_comments > available_tokens * len(comments):
        print(f"{white}REQUESTED {num_comments} COMMENTS, BUT ONLY {available_tokens * len(comments)} COMMENTS ARE POSSIBLE WITH AVAILABLE TOKENS.")
        num_comments = available_tokens * len(comments)  
    while total_successful_comments < num_comments:
        for _ in range(available_tokens):  
            if total_successful_comments >= num_comments:
                break
            current_token = tokens[token_index % available_tokens]
            current_comment = comments[comment_index % len(comments)]
            if current_token.startswith("EA") or current_token.startswith("EAA"):
                params = {'access_token': current_token, 'message': current_comment}
                try:
                    response = requests.post(url, params=params)
                    if response.status_code == 200:
                        total_successful_comments += 1
                        print(f"{green}COMMENT: '{current_comment}' THEN SUCCESSFUL TOKEN {current_token[:10]}... ({total_successful_comments}/{num_comments})")
                        comment_index += 1
                    else:
                        total_failed_comments += 1
                        error_message = response.json().get("error", {}).get("message", "Unknown error")
                        print(f"{red}FAILED COMMENT: '{current_comment}' WITH TOKEN {current_token[:10]}... STATUS CODE: {response.status_code} - ERROR: {error_message}")
                except requests.exceptions.RequestException as e:
                    print(f"{red}REQUEST FAILED WITH TOKEN {current_token[:10]}... Error: {e}")
                    total_failed_comments += 1
            else:
                print(f"{red}INVALID TOKEN FORMAT: {current_token[:10]}...")
            token_index += 1
        if token_index >= available_tokens:
            token_index = 0
    print(f'{green}TOTAL SUCCESSFUL COMMENTS: {total_successful_comments}')

def comments_reels():
    clear()
    logo()
    print(f"[1] AUTO COMMENT WITH THE SAME COMMENT")
    print(f"[2] AUTO COMMENT WITH DIFFERENT COMMENTS")
    print(f"[3] EXIT")
    linex()
    choice = input('\x1b[1;32mCHOOSE : ')
    linex()
    if choice == '1':
        reels_link = input("ENTER THE REEL LINK: ")
        linex()
        comment = input("ENTER THE COMMENT: ")
        linex()
        num_comments = int(input("ENTER THE NUMBER OF COMMENTS TO SEND: "))
        linex()
        tokens = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokp.txt')
        if len(tokens) == 0:
            print(f"{red}NO TOKENS FOUND PLEASE ADD TOKENS TO THE FILE.")
            return
        auto_comment_on_reels(reels_link, [comment], num_comments, tokens)
    elif choice == '2':
        reels_link = input("ENTER THE REEL LINK: ")
        linex()
        num_comments = int(input("ENTER THE NUMBER OF COMMENTS TO SEND: "))
        linex()
        comments = []
        for i in range(num_comments):
            comment = input(f"ENTER COMMENT {i+1}: ")
            comments.append(comment)
        linex()
        tokens = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokp.txt')
        if len(tokens) == 0:
            print(f"{red}NO TOKENS FOUND PLEASE ADD TOKENS TO THE FILE.")
            return
        auto_comment_on_reels(reels_link, comments, num_comments, tokens)
    elif choice == '3':
        exit()
    else:
        print(f"{red}INVALID OPTION.")
        comments_reels()
def update():
    clear()
    logo()
    main_repo_path = '.'
    boosting_repo_path = './BOOSTING'
    try:
        print(f"{green}UPDATING THE MAIN REPOSITORY...")
        subprocess.run(['git', 'pull'], cwd=main_repo_path, check=True)
        print(f"{white}MAIN REPOSITORY UPDATED SUCCESSFULLY.")
    except subprocess.CalledProcessError as e:
        print(f"{red}ERROR OCCURRED WHILE UPDATING THE MAIN REPOSITORY: {e}")
    if not os.path.exists(boosting_repo_path):
        print(f"{red}BOOSTING REPOSITORY NOT FOUND LOCALLY. PLEASE CLONE IT FIRST.")
        return
    try:
        print(f"{green}PULLING THE LATEST CHANGES FROM THE BOOSTING REPOSITORY...")
        subprocess.run(['git', 'pull'], cwd=boosting_repo_path, check=True)
        print(f"{green}BOOSTING REPOSITORY UPDATED SUCCESSFULLY.")
    except subprocess.CalledProcessError as e:
        print(f"{red}ERROR OCCURRED WHILE UPDATING THE BOOSTING REPOSITORY: {e}")

def deletefiles():
	clear()
	logo()
	print(f"[01] RESET")
	linex()
	choice = input('\x1b[1;32mCHOOSE : ')
	if choice == '1':
		reset()
	else:
		print(f"{red}INVALID OPTION.")
		deletefiles()
	
def AutoReact():
    def Reaction(actor_id: str, post_id: str, react: str, token: str) -> bool:
        rui = requests.Session()
        user_agent = generate_user_agent()
        rui.headers.update({"User-Agent": user_agent})        
        feedback_id = str(base64.b64encode(f'feedback:{post_id}'.encode('utf-8')).decode('utf-8'))
        var = {
            "input": {
                "feedback_referrer": "native_newsfeed",
                "tracking": [None],
                "feedback_id": feedback_id,
                "client_mutation_id": str(uuid.uuid4()),
                "nectar_module": "newsfeed_ufi",
                "feedback_source": "native_newsfeed",
                "feedback_reaction_id": react,
                "actor_id": actor_id,
                "action_timestamp": str(time.time())[:10]
            }
        }
        data = {
            'access_token': token,
            'method': 'post',
            'pretty': False,
            'format': 'json',
            'server_timestamps': True,
            'locale': 'id_ID',
            'fb_api_req_friendly_name': 'ViewerReactionsMutation',
            'fb_api_caller_class': 'graphservice',
            'client_doc_id': '2857784093518205785115255697',
            'variables': json.dumps(var),
            'fb_api_analytics_tags': ["GraphServices"],
            'client_trace_id': str(uuid.uuid4())
        }
        pos = rui.post('https://graph.facebook.com/graphql', data=data).json()
        try:
            if react == '0':
                print(f"{green}SUCCESSFULLY REMOVED REACTION FROM {actor_id} ON {post_id}")
                return True
            elif react in str(pos):
                print(f"{green}SUCCESSFULLY REACTED WITH {actor_id} TO {post_id}")
                return True
            else:
                print(f"{red}FAILED REACTED WITH {actor_id} TO {post_id}")
                return False
        except Exception:
            print(f"{red}REACTION FAILED DUE TO AN ERROR.")
            return False

    def process_reaction(actor_id, token, post_id, react):
        global successful_reactions
        if Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token):
            with counter_lock:
                if successful_reactions < react_count:
                    successful_reactions += 1

    def choose_reaction():
        linex()
        print(f"[1] LIKE")
        print(f"[2] LOVE")
        print(f"[3] HAHA")
        print(f"[4] WOW")
        print(f"[5] CARE")
        print(f"[6] SAD")
        print(f"[7] ANGRY")
        print(f"[8] REMOVE REACTION")
        linex()
        rec = input('\x1b[1;32mCHOOSE : ')
        reaction_ids = {
            '1': '1635855486666999',
            '2': '1678524932434102',
            '3': '115940658764963',
            '4': '478547315650144',
            '5': '613557422527858',
            '6': '908563459236466',
            '7': '444813342392137',
            '8': '0'
        }
        return reaction_ids.get(rec)

    def linktradio(post_link: str) -> str:
        patterns = [
            r'/posts/(\w+)',
            r'/videos/(\w+)',
            r'/groups/(\d+)/permalink/(\d+)',
            r'/reels/(\w+)',
            r'/live/(\w+)',
            r'/photos/(\w+)',
            r'/permalink/(\w+)',
            r'story_fbid=(\w+)',
            r'fbid=(\d+)'
        ]        
        for pattern in patterns:
            match = re.search(pattern, post_link)
            if match:
                if pattern == r'/groups/(\d+)/permalink/(\d+)':
                    return match.group(2)
                return match.group(1)
        
        print(f"{red}INVALID POST LINK OR FORMAT")
        return None

    def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def choose_type():
        clear()
        logo()
        print("[1] A REGULAR POST")
        print("[2] A GROUP POST")
        print("[3] A VIDEO POST")
        print("[4] A PHOTO POST")
        linex()
        choice = input('\x1b[1;32mCHOOSE : ')
        return choice
    actor_ids = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokpid.txt')
    tokens = get_ids_tokens('/sdcard/ERROR-BOOSTING/tokp.txt')    
    choice = choose_type()    
    if choice == '1':
        linex()
        post_link = input('ENTER THE FACEBOOK POST LINK: ')
        post_id = linktradio(post_link)
    elif choice == '2':
        linex()
        post_link = input('ENTER THE FACEBOOK GROUP POST LINK: ')
        post_id = linktradio(post_link)
    elif choice == '3':
        linex()
        post_link = input('ENTER THE FACEBOOK VIDEO POST LINK: ')
        post_id = linktradio(post_link)
    elif choice == '4':
        linex()
        post_link = input('ENTER THE FACEBOOK PHOTO POST LINK: ')
        post_id = linktradio(post_link)
    else:
        print(f'''{red}INVALID CHOICE.''')
        return
    if not post_id:
        return
    react = choose_reaction()
    linex()
    if react:
        global react_count
        react_count = int(input("HOW MANY REACTIONS DO YOU WANT TO SEND? "))
        linex()
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(process_reaction, actor_id, token, post_id, react)
                for actor_id, token in zip(actor_ids, tokens)
            ][:react_count]
                
        print(f"{green}{successful_reactions} SUCCESSFUL REACTIONS SENT! YOU'RE AWESOME!{white}")
    else:
        print(f'{red}INVALID REACTION OPTION.{white}')
def Initialize():
    clear()
    logo()
    print(f"[1] MANUAL THROUGH INPUT   - [UID AND PASSWORD]")
    print(f"[2] MANUAL THROUGH FILE    - [THRU TXT FILE]")
    print(f"[3] AUTOMATIC THROUGH FILE - [THRU TXT FILE]")
    linex()
    choice = input('\x1b[1;32mCHOOSE : ')
    linex()
    if choice == '1':
        Manual()
    elif choice == '2':
        ManFile()
    elif choice == '3':
        Auto()
    else:
        print(f"{red}INVALID OPTION.")
        Initialize()
def react_new():
    ses = requests.Session()

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None
    clear()
    logo()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {green}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {green}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {green}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {green}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {green}RETURN TO MAIN MENU''')
    line()
    account_choose = input(f'''{blue}  Choose : {green}''')
    line()
    file_path = None
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    if file_path is None:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        react()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    post_link = input(f'''{yellow}  Enter post link: {green}''')
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f'''{red}  UID extraction failed. Please provide a valid post link. Copy link on Facebook Lite!''')
        return None
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{red}  [1] {blue}LIKE''')
    print(f'''{red}  [2] {blue}LOVE''')
    print(f'''{red}  [3] {blue}HAHA''')
    print(f'''{red}  [4] {blue}WOW''')
    print(f'''{red}  [5] {blue}ANGRY''')
    print(f'''{red}  [6] {blue}SAD''')
    line()
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE👍🏼',
        '2': 'LOVE💜',
        '3': 'HAHA🤣',
        '4': 'WOW😯',
        '5': 'ANGRY😡',
        '6': 'SAD😭'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f"{red}  Failed to convert the link.")
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{target_uid}_{converted_link}'''
        auto_react = f'''https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {'user-agent': W_ueragnt()}  # Assuming W_ueragnt() is defined
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            print(f'''{green}   Reaction Count »  {i + 1} ━━━━━━》 Successfully Reacted! ''')
            print(f''' {P} Reaction Version 2 {G} Control I.D {uid_url} ''')
            success_count += 1
        else:
            print(f'''{red}  Reaction Count {i + 1} ---> Unsuccessful Reaction !!!''')
            print(f''' {P} Reaction Version 2 {G} Control I.D {uid_url} ''')
            failure_count += 1
    line()
    print(f'''{yellow}  TOTAL : ''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')
    
def count_lines_in_files(*file_paths):
    for i, file_path in enumerate(file_paths, start=1):
        try:
            with open(file_path, 'r') as file:
                total_lines = sum(1 for line in file)
            if i == 1:
                print(f'\t\t{white}     FRA ACCOUNT {red}: {green}{total_lines}')
            elif i == 2:
                print(f'\t\t{white}     RPA ACCOUNT {red}: {green}{total_lines}')
            elif i == 3:
                print(f'\t\t{white}     FRA PAGES   {red}: {green}{total_lines}')
            elif i == 4:
                print(f'\t\t{white}     RPA PAGES   {red}: {green}{total_lines}')
        except FileNotFoundError:
            print(f'\t\t{red}   NOT FOUND!')

path_file1 = '/sdcard/ERROR-BOOSTING/tokpid.txt'
path_file2 = '/sdcard/ERROR-BOOSTING/tokp.txt'
path_file3 = '/sdcard/ERROR-BOOSTING/toka.txt'
path_file4 = '/sdcard/ERROR-BOOSTING/tokaid.txt'

import requests, json, time, uuid, base64, re, threading

successful_reactions = 0
counter_lock = threading.Lock()

headers_global = {
    'user-agent': W_ueragnt(),
    'viewport-width': '576' }
ser = requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/cnt/main/MY_SELL_PROJECT/smm.txt').text
speed = 100
allcookie = []
s_react = []
s_comment = []
s_flw = []
logos = logo

def enc(txt):
    encoded_bytes = base64.b64encode(txt.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def start_tool():
    clear()
    logo()
    print(f'''{yellow}  [1] {cyan}EXTRACT NORMAL ACCOUNT PAGES     {yellow}-  {green}[UID and Password]''')
    print(f'''{yellow}  [2] {cyan}EXTRACT SINGLE NORMAL ACCOUNT    {yellow}-  {green}[No Duplicate Checker]''')
    print(f'''{yellow}  [3] {cyan}EXTRACT BULK NORMAL ACCOUNTS M1  {yellow}-  {green}[Thru TXT File]''')
    print(f'''{yellow}  [4] {cyan}EXTRACT BULK NORMAL ACCOUNTS M2  {yellow}-  {green}[Thru TXT File]''')
    print(f'''{yellow}  [5] {cyan}EXTRACT BULK ACCOUNTS PAGES      {yellow}-  {green}[Thru TXT File]''')
    print(f'''{yellow}  [0] {red}RETURN TO MAIN MENU''')
    line()
    choice = input(f'''{yellow}  Choose : {green}''')    
    if choice == '1':
        get_facebook_pages()
    elif choice == '2':
        get_facebook_account()
    elif choice == '3':
        bgraph_bulk_account()
    elif choice == '4':
        datr()
    elif choice == '5':
        bgraph_bulk_pages()
    elif choice == '0':
        main()
    else:
        print(f'''{red}  Invalid choice. Please pick a number from 1 to 5 or 0 to return to the main menu.''')
        return start_tool()

def count_lines_in_files(*file_paths):
    for i, file_path in enumerate(file_paths, start=1):
        try:
            with open(file_path, 'r') as file:
                total_lines = sum(1 for line in file)
            if i == 1: 
                print(f'''\t\t{B}        │ {G} FRA ACCOUNT {R}: {green}{total_lines} {B} │''')
            elif i == 2:
                print(f'''\t\t{B}        │ {G} RPA ACCOUNT {R}: {green}{total_lines} {B} │''')
            elif i == 3:
                print(f'''\t\t{B}        │ {G} FRA PAGES   {R}: {green}{total_lines}  {B}│''')
            elif i == 4:
                print(f'''\t\t{B}        │{G}  RPA PAGES   {R}: {green}{total_lines}  {B}│''')
            elif i == 5:
            	print(f'''\t\t{B} ━━━━━━━━━━━━━━━ ''')
                	
        except FileNotFoundError:
            print(f'''\t\t{red}   {file_path} Not Found!''')
            continue

path_file1 = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
path_file2 = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
path_file3 = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
path_file4 = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'

def main():
    clear()
    logo()
    open('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT-NAME-ID.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT-NAME-ID.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-FRA-PAGES-NAME-ID.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt', 'a').write('')
    open('/sdcard/.EXTRACT-TOKEN-RP-PAGES-NAME-ID.txt', 'a').write('')
    print(f'''\t\t{B}    ┌────────────────────────────┐ ''')
    print(f'''\t\t{B}    ┃  {G}     TOOL OVERVIEW    {B}    ┃''')
    print(f''''\t\t{B}    └────────────────────────────┘''')
    count_lines_in_files(path_file1, path_file2, path_file3, path_file4)
   
    linex()
    print(f'''{B} ┌─────────────────────{T}T O O L   S E R V I C E S{B}────────────────────────┐''')
    print(f'''{B} │{G}  [01] {P}ACCOUNTS                     {white}➠  {P}[ {R}Log in account{P} ]       {B}      │''')
    print(f''' {B}│{G}  [02] {P}AUTO REACT W/O {W}CARE          {white}➠  {P}[ {W}Page & Normal Account{P} ]   {B}   │ ''')
    print(f'''{B} │{G}  [03] {P}AUTO REACT WITH{W} CARE         {white}➠  {P}[ {W}Normal Account Only{P} ]     {B}   │''')
    print(f'''{B} │{G}  [04] {P}AUTO REACT TO {W}COMMENT        {white}➠  {P}[ {W}Page & Normal Account{P} ]   {B}   │''')
    print(f'''{B} │{G}  [05] {P}AUTO REACT TO {W}DP & COVER     {white}➠  {P}[ {W}Page & Normal Account{P} ]  {B}    │''')
    print(f'''{B} │{G}  [06] {P}AUTO REACT TO {W}REELS          {white}➠  {P}[ {W}Page & Normal Account{P} ]    {B}  │''')
    print(f''' {B}│{G}  [07] {P}AUTO{W} FOLLOW                  {white}➠  {P}[ {W}Page & Normal Account{P} ]  {B}    │''')
    print(f'''{B} │{G}  [08] {P}AUTO COMMENT TO{W} POST         {white}➠  {P}[ {W}Page & Normal Account{P} ]  {B}    │''')
    print(f''' {B}│{G}  [09] {P}AUTO COMMENT TO{W} REELS        {white}➠  {P}[ {W}Page & Normal Account{P} ]  {B}    │''')
    print(f'''{B} │{G}  [10] {P}AUTO COMMENT TO{W} DP           {white}➠  {P}[ {W}Page & Normal Account{P} ]    {B}  │''')
    print(f'''{B} │{G}  [11] {P}REPLY TO {W}COMMENT             {white}➠  {P}[ {W}Page & Normal Account{P} ]   {B}   │''')
    print(f''' {B}│{G}  [12] {P}AUTO SHARE {W}V2                {white}➠  {P}[ {W}Normal Account Only{P} ]    {B}    │''')
    print(f'''{B} │{G}  [13] {P}AUTO GROUP {W}JOIN              {white}➠  {P}[ {W}Facebook Page Only{P} ]  {B}       │''')
    print(f'''{B} │{G}  [14] {P}LIKE & FOLLOW{W} PAGE           {white}➠  {P}[ {W}Facebook Page Only{P} ]    {B}     │''')
    print(f''' {B}│{G}  [15] {P}STORED{W} PAGES AND ACCOUNT     {white}➠  {P}[ {W}Page & Normal Account{P} ]  {B}    │''')
    print(f''' {B}│{G}  [16] {P}RESET {W}TOOL                   {white}➠  {P}[ {W}Restarting {P} ]        {B}        │''')
    print(f''' {B}│{G}  [17] {P}AUTO REACTS {W}LIVE           {white}  ➠  {P}[ {W}Ongoing {R}Live {P} ] {B}             │ ''')
    print(f''' {B}│{G}  [18] {P}AUTO COMMENTS FOR{W} VIDEOS     {white}➠  {P}[ {W} Restarting {P} ]  {B}             │ ''')
    print(f''' {B}│{G}  [19] {P}AUTO COMMENTS FOR {W}REELS V2   {white}➠ {P} [ {W}PAGE & NORMAL ACCOUNT {P}] {B}     │ ''')
    print(f''' {B}│{G}  [20] {P}AUTO REACTION {W}V2.2           {white}➠  {P}[ {W}Page & Normal Account{P} ] {B}     │ ''') 
    print(f''' {B}│{G}  [21] {P}UPDATE   TOOLS               {white}➠ {P} [ {W}Updating {P}]{B}                   │ ''')
    print(f''' {B}│{G}  [22] {P}DELETE FILES                 {white}➠ {P} [ {W}DELETE ALL ACCOUNG{P} ] {B}        │ ''')
    print(f''' {B}│{G}  [23] {P}INITIALIZE                   {white}➠ {P} [ {W}CHEKING{P} ] {B}                   │ ''')
    print(f''' {B}│ {G} [24] {P}REACTION V3                  {white}➠  {P}[ {W}Page & Normal Account{P} ] {B}     │ ''')
    print(f'''{B} │{G}  [00] {P} EXIT                        {white}➠ {P} [ {R}Exit{P} ]               {B}        │''')
    print(f'''{B} └──────────────────────────────────────────────────────────────────────┘''')
    linex()
    choice = input(f'''{yellow}  Choose : {green}''').upper()
    if choice == '1' or choice == '01':
        start_tool()
    elif choice == '2' or choice == '02':
        react()
    elif choice == '3' or choice == '03':
        react_with_care()
    elif choice == '4' or choice == '04':
        react_comment()
    elif choice == '5' or choice == '05':
        react_dp_cover()
    elif choice == '6' or choice == '06':
        react_reels()
    elif choice == '7' or choice == '07':
        follow()
    elif choice == '8' or choice == '08':
        auto_comment()
    elif choice == '9' or choice == '09':
        auto_comment_to_reels()
    elif choice == '10':
        auto_comment_to_dp()
    elif choice == '11':
        reply_to_comment()
    elif choice == '12':
        share()
    elif choice == '13':
        g_join()
    elif choice == '14':
        p_like()
    elif choice == '15':
        store()
    elif choice == '16':
        delete_files()
    elif choice == '17':
        react_live()
    elif choice =='18':
    	comments_vids()
    elif choice == '19':
    	comments_reels()
    elif choice == '20':
    	react_new()
    elif choice == '21':
    	update()
    elif choice == '22':
    	delete()
    elif choice == '23':
    	Initialize()
    elif choice =='24':   	
         AutoReact()
    elif choice =='24':
        print(f'''\n{red}  Byeeeeers!''')
        return
    else:
        print(f'''{red}  Invalid choice.''')

if __name__ == '__main__':
    main()
    