# importa funcionario
from funcionario import Alura, Caelum, Hipster

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass