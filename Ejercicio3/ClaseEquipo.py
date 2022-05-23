

from mailbox import NoSuchMailboxError


class Equipo:
    __nombre = ''
    __ciudad = ''

    def __init__(self, nombre, ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad
