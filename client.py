import pwn
r = pwn.remote('213.159.213.15', 42137)
r.recvline()
r.sendline('base64')
r.recvline()
r.sendline('rot13')
r.recvline()
r.sendline('md5')
print(r.recvline())