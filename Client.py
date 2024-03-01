import socket
import time

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 49002)

# alternate between coordinates

#41.13, -92.74
#41.98, -97.30
#41.44, -115.27

# long,lat,elevation,headingspeed
while True:
  sock.sendto(b'XGPSMSFS,-92.74,41.13,100.0,270,350.0', addr)
  time.sleep(0.25)
  sock.sendto(b'XGPSMSFS,-97.30,41.98,100.0,265,350.0', addr)
  time.sleep(0.25)
  sock.sendto(b'XGPSMSFS,-115.27,41.44,100.0,275,350.0', addr)
  time.sleep(0.25)
  sock.sendto(b'XGPSMSFS,-115.27,41.44,100.0,90,350.0', addr)
  time.sleep(0.25)
  sock.sendto(b'XGPSMSFS,-97.30,41.98,100.0,95,350.0', addr)
  time.sleep(0.25)
  sock.sendto(b'XGPSMSFS,-92.74,41.13,100.0,85,350.0', addr)
  time.sleep(0.25)
