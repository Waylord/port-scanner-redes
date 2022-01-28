import socket
from threading import Thread
from time import sleep

# status
ABERTA = "Aberta"
FECHADA = "Fechada"
FILTRADA = "Filtrada"
DESCONHECIDA = "Desconhecida"


class PortScanner:

    def map_status(self, status):
        if status == 0:
            return ABERTA
        elif status in [11, 110, 10013, 10035, 10060, 10049]:
            return FILTRADA
        elif status in [111, 10061]:
            return FECHADA
        else:
            return DESCONHECIDA

    def port_scanner(self, host, ports):

        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            status = client.connect_ex((host, port))
            client.close()
            type_status = self.map_status(status)
            print("Port = " + str(port) + " " + "Status = " + str(type_status))
            sleep(1)

    def __init__(self):
        ports1 = [20, 21, 22, 23, 25, 80 , 115, 443]
        ports2 = [990, 992, 993, 995, 1433, 1521, 2049]
        ports3 = [2081, 2083, 3306, 8081, 8090, 5432, 5500]
        ports4 = [514, 530, 547, 587, 636, 873]
        ip_host = socket.gethostbyname('www.google.com')
        th1 = Thread(target=self.port_scanner, args=(ip_host, ports1,)).start()
        th2 = Thread(target=self.port_scanner, args=(ip_host, ports2,))
        th2.start()
        th2.join()
        th3 = Thread(target=self.port_scanner, args=(ip_host, ports3,)).start()
        th4 = Thread(target=self.port_scanner, args=(ip_host, ports4,)).start()

/Users/millenacosta/PycharmProjects/pythonProject/main.py

PortScanner()




