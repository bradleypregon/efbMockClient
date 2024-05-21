import socket
import time
import struct

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 49002)

# alternate between coordinates

#41.13, -92.74
#41.98, -97.30
#41.44, -115.27

def createGDLMsg(msgType, data):
  header = struct.pack("B", msgType)
  payload = struct.pack('27s', data.encode('utf-8'))

  gdlMsg = header + payload
  return gdlMsg

# while True:
#   sock.sendto(createGDLMsg(0xA, "Remaining 27 byte message here"), addr)
#   time.sleep(0.25)

# long, lat, 
while True:
  sock.sendto(b'XGPSMSFS,-92.74,41.13,123567.1234,270.456,350.0', addr)
  time.sleep(0.1)
  sock.sendto(b'XGPSMSFS,-97.30,41.98,1342.1234,265.456,350.0', addr)
  time.sleep(0.1)
  sock.sendto(b'XGPSMSFS,-115.27,41.44,123.1234,275.456,350.0', addr)
  time.sleep(0.1)
  sock.sendto(b'XGPSMSFS,-115.27,41.44,132.1234,90.456,350.0', addr)
  time.sleep(0.1)
  sock.sendto(b'XGPSMSFS,-97.30,41.98,13453.12340,95.456,350.0', addr)
  time.sleep(0.1)
  sock.sendto(b'XGPSMSFS,-92.74,41.13,145.1234,85.456,350.0', addr)
  time.sleep(0.1)
