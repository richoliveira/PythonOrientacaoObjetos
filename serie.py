from programa import Programa

class Serie(Programa):
    def __init__(self, nomeSerie, anoSerie, temporadasSerie):
        super().__init__(nomeSerie, anoPrograma=anoSerie)
        self.temporadasSerie = temporadasSerie

    def imprime(self):
        print(f'Nome da Serie: {self.nomePrograma} - {self.temporadasSerie} temporadas - Ano: {self.anoPrograma} - {self.likes} Likes')

    def __str__(self):
        return f'Nome da Serie: {self.nomePrograma} - {self.temporadasSerie} temporadas - Ano: {self.anoPrograma} - {self.likes} Likes'