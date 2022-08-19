class Programa:
    def __init__(self, nomePrograma, anoPrograma):
        self._nomePrograma = nomePrograma.title()
        self.anoPrograma = anoPrograma
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nomePrograma(self):
        return self._nomePrograma.title()

    @nomePrograma.setter
    def nomePrograma(self, novo_programa):
        self._nomePrograma = novo_programa

    def imprime(self):
        print(f'Nome: {self.nomePrograma} - {self.likes} Likes')

    def __str__(self):
        return f'Nome: {self.nomePrograma} - {self.likes} Likes'