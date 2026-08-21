import re

def fmt_08(p):
    p = re.sub(r'\D', '', str(p))
    if p.startswith('0'):
        return p
    if p.startswith('62'):
        return '0' + p[2:]
    if p.startswith('8'):
        return '0' + p
    return p

def fmt_nocode(p):
    p = re.sub(r'\D', '', str(p))
    if p.startswith('0'):
        return p[1:]
    if p.startswith('62'):
        return p[2:]
    return p

def fmt_plus(p):
    p = re.sub(r'\D', '', str(p))
    if p.startswith('0'):
        return '+62' + p[1:]
    if p.startswith('62'):
        return '+' + p
    if p.startswith('8'):
        return '+62' + p
    return p

def fmt_phone_only(p):
    return re.sub(r'\D', '', str(p))
