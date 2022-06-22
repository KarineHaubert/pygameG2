
def cadastraJogador(nome, email):
    w = open('jogador.txt', 'a')
    w.write('Nome: {}, E-mail: {}\n'.format(nome, email))
    w.close()
    
