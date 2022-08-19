from nivelcargo import Junior, Pleno

print('\nExec 01 - Sem Contrutor\n')

# jose = Junior()
# jose.busca_perguntas_sem_resposta()
#
# luan = Pleno()
# luan.busca_perguntas_sem_resposta()
# luan.busca_cursos_do_mes()
#
# luan.mostrar_tarefas()

print('\nExec 02 - Com Contrutor\n')

jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)