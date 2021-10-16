import pwn
import base64
import hashlib

flag = 'SamaraCTF{7CP_3NCrYP73D_D474_9223}'

#r = pwn.remote('127.0.0.1', 42137)
try:
    for i in range (3):
        r.sendline(str(i))
        x = r.recvline().decode().strip()
        if x == "base64":
            flag = base64.b64encode(flag.encode()).decode()
        elif x == 'rot13':
            target_array = [ord(i) for i in flag]
            encrypted_target_array = [i+1 for i in target_array]
            flag = ''.join(map(lambda x: chr(x),encrypted_target_array))
        elif x == 'md5':
            flag = str(hashlib.md5(flag.encode()).digest())
    r.sendline(flag)
finally:
    r.close()



