# Cria primeira classe
class Conta:
    # METODO CONSTRUTOR - NAO E PARECIDO COM O METODO CONSTRUTOR JAVA
    def __init__(self, numero, titular, saldo, limite):
        # self e a referencia do objeto em Memoria
        print(f"Iniciando uma classe ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Metodo extrato - imprime na tela o saldo do titular
    def extrato(self):
        print(f"O saldo de {self.__saldo} para o titular {self.__titular}.")

    # Metodo deposita - opera um deposito na conta do titular
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar (self, valor_a_sacar):
        valor_disponivel_saque = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_saque

    # Metodo saca - opera um saque na conta
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor de saque deve ser menor que o Limite disponivel para saque")

    # Metodo transfere - opera uma transferencia da conta origem para conta destino
    # 'saca' da conta origem e 'deposita' na conta destino
    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    # Metodo que devolve o Saldo
    @property
    def saldo(self):
        return self.__saldo

    # Metodo que devolve o Titular
    def getTitular(self):
        return self.__titular

    # Metodo que devolve o Limite
    @property
    def limite(self):
        return self.__limite

    # Metodo que devolve o Saldo
    def getNumero(self):
        return self.__numero

    # Metodo set Limite - Altera o limite
    @limite.setter
    def limite(self, novo_limite):
        if self.__limite == novo_limite:
            print("O novo limite deve ser diferente do limite atual.")
        else:
            self.__limite = novo_limite
            print("Limite alterado com sucesso.")

    # Metodo Static - Nao precisa declara um objeto para ser chamado
    @staticmethod
    def codigoBanco ():
        return "001"

    @staticmethod
    def codigosBancos ():
        return {'BB':'001', 'Caixa':'104', 'Itau':'341', 'Bradesco':'237'}