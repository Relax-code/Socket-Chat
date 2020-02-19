import socket
import threading
from info import check_username, del_username
import sys


def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = '127.0.0.1', 5050  # Данные сервера
alias = check_username()
Joined = True

sor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sor.bind(('', 0))  # Задаем сокет как клиент
sor.sendto((alias+' Connect to server').encode('utf-8'),
           server)  # Уведомляем сервер о подключении

potok = threading.Thread(target=read_sok)
potok.start()


def func():
    global Joined
    try:
        mensahe = input()
        #print ("\033[A                             \033[A")
        if mensahe == 'quit' and input('Вы уверены, что хотите покинуть чат?(N) ') == 'Y':
            del_username(alias)
            sor.sendto(("{} left the chat ".format(
                alias)).encode('utf-8'), server)
            Joined = False
        else:
            return sor.sendto(('['+alias+'] '+mensahe).encode('utf-8'), server)
    except:
        del_username(alias)
        sor.sendto(("{} left the chat ".format(alias)).encode('utf-8'), server)
        Joined = False


while Joined is not False:
    func()

potok.join()
sor.close()
