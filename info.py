import redis
import time

r = redis.Redis(host='127.0.0.1', port=6379)

def check_username():
    username = input('Введите ник: ')
    if r.get(username) is None:
        r.set(username,time.ctime())
        return username
    else:
        print('Такой ник уже занят!')
        return check_username()

def del_username(name):
    return r.delete(name)

