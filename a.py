import   socket
target_ip="127.0.0.0"
target_port=7888
#FOR CREATING UDP SOCKET
s=(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    task=input("plz say")
    newmsg=msg.encode('ascii')
    print(newmsg)
    s.sendto(newmsg,(target_ip,target_port))
    print(s.recvfrom)
