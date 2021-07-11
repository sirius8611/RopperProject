import os
from pwn import *
import json
from pathlib import Path
end = 5 
passwordFile = open(Path.cwd() / "passwords.txt",'w')
passwordFile.write("")
passwordFile.close()
for i in range(end):
    passwordFile = open(Path.cwd() / "passwords.txt")
    passwordlist = passwordFile.readlines()
    passwordFile.close()
    
    passwordFile = open(Path.cwd() / "passwords.txt", 'a')
    config = open(Path.cwd() / f'bandit{i+1}.cfg')
    configdata = json.loads(config.readline())
    data = configdata["info"]
    command = configdata["command"]
    if(i ==0):
        Password = data["password"]
    else:
        Password = passwordlist[i-1][3:].strip()
    Username = data["username"]
    address = data["address"]
    Port = data["port"]
    session = ssh(Username,host= address,port = Port,password = Password)  
    io = session.process('/bin/sh')
    cnt = command["numberofcommand"]
    for j in range(cnt):
        io.sendline(command[f'{j+1}'])
    X = io.recvline().decode('utf-8')
    n = len(x)
    x = x[n-33:n]
    inp = f'{i+1}. {x}'
    passwordFile.write(inp)
    passwordFile.close()


