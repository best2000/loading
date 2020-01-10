import tkinter as tk
import threading, time, socket

def soc_wait(s):
    con, addr = s.accept()
    global l 
    l = 0

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 60000        # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

t = threading.Thread(target=soc_wait, args=(s,), daemon=True)
t.start()

l = 1
while l == 1:
    print("\rLOADING | ", end="")
    time.sleep(0.1)
    print("\r          ", end="")
    time.sleep(0.1)    
    print("\rLOADING / ", end="")
    time.sleep(0.1)
    print("\r          ", end="")
    time.sleep(0.1)    
    print("\rLOADING - ", end="")
    time.sleep(0.1)  
    print("\r          ", end="")
    time.sleep(0.1)    
    print("\rLOADING \ ", end="")
    time.sleep(0.1)
    print("\r          ", end="")
    time.sleep(0.1)    





