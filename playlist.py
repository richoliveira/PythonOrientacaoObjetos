# Constroe a classe Playlist - Heranca da classe Builtin list
class Playlist():
    def __init__(self, nome_playlist, programas):
        # Usa o metodo contrutor da classe Pai para dizer que programas e uma lista
        #super().__init__(programas)
        self.nome_playlist = nome_playlist
        self._programas = programas

    # Metodo para retornar a Playlist, no caso os objetos
    @property
    def listagem(self):
        return self._programas

    # Metodo para retornar o tamanho da lista
    @property
    def tamanho(self):
        return len(self._programas)

    # METOD QUE TRANSFORMA A CLASSE EM UM ITERABLE
    def __getitem__(self, item):
        return self._programas[item]

    # Metodo da o Comportamento de Sized
    def __len__(self):
        return len(self._programas)