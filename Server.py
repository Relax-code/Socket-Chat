import socket

clients = []  # Массив где храним адреса клиентов
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5050))
sock.listen()

print('Start Server')
while 1:
    data, addres = sock.accept()
    print(addres[0], addres[1])
    if addres not in clients:
        clients.append(addres)  # Если такова клиента нету , то добавить
    for client in clients:
        if client == addres:
            continue  # Не отправлять данные клиенту который их прислал
        sock.sendto(data, client)
