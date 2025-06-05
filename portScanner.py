import socket

def scanPort(ip, ports):
    openPort = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            openPort.append(port)
            print(f"port {port} is opened.")
        except:
            print(f"port {port} is not opened.")
        finally:
            sock.close()
    return openPort


ip = input("Please enter the ip: ")
port = input("please insert your wanted port or set a range of ports with (-) : ")
if "-" in port:
    port = [int(x) for x in port.split("-")]
    port = list(range(port[0], port[1]+1))
    print("opend port :", scanPort(ip, port))
else:
    port = [int(x) for x in port.split()]
    print("opend port :", scanPort(ip, port))
