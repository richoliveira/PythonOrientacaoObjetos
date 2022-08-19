from serie import Serie
from filme import Filme
from playlist import Playlist

apostolo = Filme('o apostolo Paulo', 2017, 120)
vingadores = Filme('Os Vingadores - Era de Ultron', 2016, 180)
homem_aranha = Filme('Homem Aranha - Sem Volta', 2020, 150)

stranger = Serie('Stranger Things', 2019, 5)
suits = Serie('Suits', 2016, 9)

apostolo.dar_like()
apostolo.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()
stranger.dar_like()
stranger.dar_like()
stranger.dar_like()
stranger.dar_like()
suits.dar_like()

print(f'Filme: {apostolo.nomePrograma}, Ano: {apostolo.anoPrograma}, Duração: {apostolo.duracaoFilme}, Likes: {apostolo.likes}')
print(f'Serie: {stranger.nomePrograma}, Ano: {stranger.anoPrograma}, Temporadas: {stranger.temporadasSerie}, Likes: {stranger.likes}')

# Cria uma lista de objetos
filmes_e_series = [apostolo, stranger, vingadores, suits]

# Itera sobre a lista
print('\nfor com if\n')
for prog in filmes_e_series:
    detalhes = f'{prog.duracaoFilme} min' if hasattr(prog, 'duracaoFilme') else f'{prog.temporadasSerie} temporadas'
    print(f'Programa: {prog.nomePrograma} - Ano: {prog.anoPrograma} - {detalhes} - Likes: {prog.likes}')

print('\nfor com imprime()\n')
for prog in filmes_e_series:
    prog.imprime()

print('\nfor com str\n')
for prog in filmes_e_series:
    print(prog)

print('\nfor com Playlist\n')
lista_prog = [apostolo, stranger, vingadores, suits]
# Declara o objeto Playlist
play = Playlist('Maratona Final de Semana', lista_prog)

for prog in play.listagem:
    print(prog)

print(f'Tamanho da Playlist {len(play.listagem)}')
print(f'Tamanho da Playlist {play.tamanho}')

print('\nfor com Playlist como Iterable\n')
lista_prog = [apostolo, stranger, vingadores, suits]
# Declara o objeto Playlist
play = Playlist('Maratona Final de Semana', lista_prog)

# Itera sobre o objeto play - a classe Playlist possui o metodo __item__ que deixa a classe com comportamento Iterable
for prog in play:
    print(prog)

print(f'Tamanho da Playlist {len(play)}')
print(f'Tamanho da Playlist {play}')