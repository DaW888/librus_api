from py_librus_api import Librus
from settings import haslo, login

librus = Librus()

while not librus.logged_in:
    if not librus.login(login, haslo):
        print("cant login")
    else:
        print("Udało sie")
        oceny = librus.get_teachers(mode='print')
        print(oceny)