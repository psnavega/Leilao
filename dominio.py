import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.lance_maximo = sys.float_info.min
        self.lance_minimo = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        self.__lances.append(lance)
        if lance.valor > self.lance_maximo:
            self.lance_maximo = lance.valor
        if lance.valor < self.lance_minimo:
            self.lance_minimo = lance.valor




