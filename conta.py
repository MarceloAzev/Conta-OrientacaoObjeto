class Conta:
    #Self é a referencia do objeto
    # __init__ função de inicialização
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto ... {}".format(self))
        # __privado o atributo
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titutlar {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def saque(self, valor):
        if(valor <= (self.__pode_sacar)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    
    def transferencia(self, valor,destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo
    @property
    def conta(self):
        return self.__titular
    

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    #código estatico, faz sentido quando todos os metedos tem algo em comum
    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}