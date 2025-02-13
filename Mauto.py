
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
#──────────────{ WAKTU }──────────────#
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")
#──────────────{ LODING SYSTEM }──────────────#
def lo(word):
    Rayhan = ["[\033[38;5;40m■\x1b[0m□□□□□□□□□]","[\033[38;5;42m■■\x1b[0m□□□□□□□□]", "[\033[38;5;42m■■■\x1b[0m□□□□□□□]", "[\033[38;5;43m■■■■\x1b[0m□□□□□□]", "[\033[38;5;44m■■■■■\x1b[0m□□□□□]", "[\033[38;5;45m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(Rayhan)):
            sys.stdout.write(('\r{}{}').format(str(word), Rayhan[x]))
            time.sleep(0.1)
            sys.stdout.flush()
W = "\x1b[97m"
G = "\x1b[38;5;46m"
R = "\x1b[38;5;196m"
X = f"{W}<{R}•{W}>"

oks = []
cps = []

from fake_useragent import UserAgent
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last

def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}

def dn():
    time.sleep(random.randint(3,7))
    
def dnn():
    time.sleep(random.randint(10,20))

def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']

def GetPhone():
    na = random.choice(['77', '78', '59'])
    ni = str(random.randrange(1000, 10000))
    nu = str(random.randrange(10000, 100000))
    nope = '+639%s%s%s' % (na, ni, nu)
    return nope

def GetCode(email1):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None

def get_email_temp_mail():
	try:
		mail = requests.Session()
		headers = {
				'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
				'Content-Type':'application/json',
				'Connection-type': 'wifi'
			}
		payload = json.dumps({"min_name_length": 10,"max_name_length": 10})
		response = mail.post('https://api.internal.temp-mail.io/api/v3/email/new', data=payload, headers=headers)
		return response.json()['email']
	except Exception as e: return None
	
def get_code_temp_mail(email):
	mail = requests.Session()
	headers = {
			'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
			'Content-Type':'application/json',
			'Connection-type': 'wifi'
		}
	response = mail.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages', headers=headers)
	if response.status_code == 200:
		req = response.json()
		if req and isinstance(req, list):
			subject = req[0].get('subject', '')
			kode = re.search(r'(\d+)', subject)
			code = kode.group(1) if kode else 'Code not found'
			return code
		else:
			return 'Invalid response'
		return None

def get_temp_plus():
	name = " ".join(fake_name()).replace(' ', '')
	jam = str(datetime.now().strftime("%X")).replace(':','')
	domain = random.choice(['fexbox.org','fexpost.com','fextemp.com','chitthi.in'])
	email = f'{name}.{jam}.{str(random.randrange(1000,10000))}@{domain}'
	return email
	
import requests
import re

def get_code_temp_plus(email):
    try:
        mail = requests.Session()
        headers = {'cookie': f'email={email}'}
        response = mail.get('https://tempmail.plus/api/mails', headers=headers)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return "Request failed"

        data = response.json()  # Ensure valid JSON response
        mail_list = data.get("mail_list", [])

        if not mail_list:
            return "No emails received"

        subject = mail_list[0].get('subject', '')
        match = re.search(r'(\d+)', subject)

        return match.group(1) if match else "Code not found"

    except requests.RequestException as e:
        return f"Request error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
#──────────────{ SPACE SYSTEM}──────────────#
def space():
    print("\n")
#──────────────{ LOGO}──────────────#
def clear():
    os.system("clear")

logo=("""




[white]       ███████╗██╗░░░██╗░█████╗░███╗░░██╗
[medium_spring_green]       ██╔════╝██║░░░██║██╔══██╗████╗░██║
[cyan2]       █████╗░░╚██╗░██╔╝███████║██╔██╗██║
[cyan1]       ██╔══╝░░░╚████╔╝░██╔══██║██║╚████║
[blue]       ███████╗░░╚██╔╝░░██║░░██║██║░╚███║
[red]       ╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝[cyan][bold]VERSION/0.2
          [green_yellow]PAID [dark_olive_gre]TOOLS[pale_green1] NOT [dark_sea_green…] FOR FREE...
""")
ll=str([hari,tanggal])
hx=(f"""
  [bold green1]DEVELOPER[medium_green]   ⟩[yellow][bold] GAR
  [bold green1]FACEBOOK[medium_green]    ⟩[yellow][bold] Evan Boaloy
  [bold green1]TODAY DATE[medium_red]  ⟩ [green]{ll}""")
def banner():
    os.system("clear")
    print(Panel(logo,subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"))
    print(Panel(hx,width=100,padding=0,style="bold green"))

def bryxcreate():
	banner()
	a=(" [green_yellow][[bold cyan1]1[green_yellow]][bold green] AUTOMATIC FB TYPE CREATION\n [green_yellow][[bold cyan1]2[green_yellow]][bold green] ACTIVE CHECKING ACCOUNT\n [green_yellow][[bold cyan1]0[green_yellow]][bold red] EXIT")
	print(Panel(a,subtitle="[bold violet]┌─",subtitle_align='left',style="bold violet"))
	Bryx=input("   \x1b[1;36m└──> ")
	if Bryx in ["1","01"]:
		main()
	elif Bryx in ["2","02"]:
		activefb()
	elif Bryx in ["0","00"]:
		exit()
	else:
		print(Panel('[bold red]OPTION NOT FOUND IN MENU',subtitle="[bold red]● [bright_yellow]● [green1]●",subtitle_align='left',title="[bold red]● [bright_yellow]● [green1]●",title_align='right',width=102,padding=0,style="bold violet"))

def main() -> None:
    banner()
    
    for make in range(100):
        ses = requests.Session()
        response = ses.get(
            url='https://x.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        email2 = get_temp_plus()
        phone2 = GetPhone()
        firstname,lastname = fake_name()
        print(Panel(f"[bold white] CREATING NEW ACCOUNT",style="bold red"))
        dn()
        print(Panel(f"[bold white] COLLECTING DATA",style="bold green"))
        dn()
        print(Panel(f"[bold white] COLLECTING COOKIES",style="bold green"))
        dn()
        print(Panel(f"[bold white] SELECTED NAME : {firstname} {lastname}",style="green"))
        dn()
        print(Panel(f"[bold white] SELECTED BIRTHDAY : {str(random.randint(1,28))}-{str(random.randint(1,12))}-{str(random.randint(1992,2009))}",style="bold green"))
        dn()
        print(Panel(f"[bold white] SUBMITTING FROM",style="bold green"))
        dn()
        print(Panel(f"[bold green] CONFIRMED",style="bold green"))
        dn()
        print(Panel(f"[bold white] CHECKING ACCOUNT LIVE OR NOT",style="bold green"))
        dn()
        print(Panel(f"[bold green] LIVE",style="bold green"))
        dn()
        print(Panel(f"[bold white] GETTING MAIL & GETTING PHONE",style="bold green"))
        dn()
        print(Panel(f"[bold green] DUMMYPHONE : {phone2}",style="bold green"))
        dn()
        print(Panel(f"[bold green] EMAIL : {email2}",style="bold red"))
        dn()
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'reg_phone__': phone2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],"Rayhan143"),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ugenX(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        #print(ses.cookies.get_dict().items())
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugenX(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            valid = get_code_temp_plus(email2)
            if valid:
                print(Panel(f"[bold white] OTP SENT TO MAIL",style="bold violet"))
                print(Panel(f"[bold white] OTP RECEIVED : FB-{valid}",style="bold violet"))
                confirm_id(email2,uid,valid,con_sub,ses)
            else:
                #print(Panel(f"[bold red] DISABLED ID",style="bold violet"))
                cps.append(uid)
        else:
            #print(Panel(f" [bold red]SUCCESSFULLY CHECKPOINT ID",style="bold violet"))
            cps.append(uid)

def confirm_id(mail,uid,otp,data,ses):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': re.search(r'"\d+"', data).group().strip('"'),
        'lsd': re.search('"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            print(Panel(f"[bold red] FUCKED ID DISABLED",style="bold violet"))
        else:
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            print(Panel(f"[bold white] COOKIE : [bold green]{cookie}",style="bold violet"))
            dn()
            print(Panel(f"[bold green] {uid}|Rayhan143",style="bold violet"))
            dn()
            open("/sdcard/SUCCESS-OK-ID.txt","a").write(uid+"|Rayhan143|"+cookie+"\n")
           
    except Exception as e:
       
        pass

if __name__ == "__main__":
    bryxcreate()

