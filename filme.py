from programa import Programa

class Filme(Programa):
    def __init__(self, nomeFilme, AnoFilme, duracaoFilme):
        super().__init__(nomeFilme, anoPrograma=AnoFilme)
        self.duracaoFilme = duracaoFilme

    def imprime(self):
        print(f'Nome do Filme: {self.nomePrograma} - Duração: {self.duracaoFilme} min - Ano: {self.anoPrograma} - {self.likes} Likes')

    def __str__(self):
        return f'Nome do Filme: {self.nomePrograma} - Duração: {self.duracaoFilme} min - Ano: {self.anoPrograma} - {self.likes} Likes'