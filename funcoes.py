import os

def cadastraJogador(nome, email):
    w = open('jogador.txt', 'a')
    w.write('Nome: {}, E-mail: {}\n'.format(nome, email))
    w.close()

def continuar():
   return os.system("pause")


def inicio():
    print("Bem-vinde ao:")
    print("""
_________________                                             ________                _____                                
____  _/______  /______ ______________ _________   _____      ___  __/____  _____________(_)______ ______________ _________
 __  /  _  __  / _  __ \__  ___/_  __ `/__  ___/   _  _ \     __  /_  _  / / /__  ___/__  / _  __ \__  ___/_  __ `/__  ___/
__/ /   / /_/ /  / /_/ /_(__  ) / /_/ / _(__  )    /  __/     _  __/  / /_/ / _  /    _  /  / /_/ /_(__  ) / /_/ / _(__  ) 
/___/   \__,_/   \____/ /____/  \__,_/  /____/     \___/      /_/     \__,_/  /_/     /_/   \____/ /____/  \__,_/  /____/  """)
    print("Ajude Pedrinho a clonar 10 cartões para o Professor Marcão comprar seu tão sonhado CIVIC VTEC EG6 1995 TURBO, enquanto precisa fugir de uma aposentada furiosa.")
    continuar()



def colisaoXCartao(cartaoX, larguraCartao, pixelXPlayer):
    pixelXCartao = list(range(cartaoX, cartaoX + larguraCartao +1 ))
    colisaoXCartao = list( set(pixelXCartao) & set(pixelXPlayer))
    return colisaoXCartao

def colisaoYCartao(cartaoY, alturaCartao, pixelYPlayer):
    pixelYCartao = list(range(cartaoY, cartaoY + alturaCartao +1 ))
    colisaoYCartao = list( set(pixelYCartao) & set(pixelYPlayer))
    return colisaoYCartao


def colisaoXVovozinha(movimentoXvovozinha, larguraVovozinha, pixelXPlayer):
    pixelXVovozinha = list(range(movimentoXvovozinha, movimentoXvovozinha+larguraVovozinha +1))
    colisaoXVovo = list( set(pixelXVovozinha) & set(pixelXPlayer))
    return colisaoXVovo

def colisaoYVovozinha(movimentoYvovozinha, alturaVovozinha, pixelYPlayer):
    pixelYVovozinha = list(range(movimentoYvovozinha, movimentoYvovozinha+alturaVovozinha +1))
    colisaoYVovo = list( set(pixelYVovozinha) & set(pixelYPlayer))
    return colisaoYVovo



def dead(gameDisplay, bg_perdeu, pygame, cor, pygameDisplay, pontos):
    somPerdeu = pygame.mixer.Sound("assets/somPerdeu.wav")
    somPerdeu.set_volume(0.5)

    gameDisplay.blit(bg_perdeu, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(somPerdeu)
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    texto = fonte.render("Opss! O seu total de cartões clonados foi de: "+str(pontos) +
                        " cartões :(", True, cor)
    gameDisplay.blit(texto, (50, 250))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 15)
    textoContinue = fonteContinue.render("Pressione ENTER para jogar novamente", True, cor)
    gameDisplay.blit(textoContinue, (50, 280))
    pygameDisplay.update()

def venceu(gameDisplay, bg_venceu, pygame, cor, pygameDisplay):
    somGanhou = pygame.mixer.Sound("assets/somGanhou.wav")
    somGanhou.set_volume(0.5)

    gameDisplay.blit(bg_venceu, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(somGanhou)
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    texto1 = fonte.render("Você Ganhou! \o/", True, cor)
    texto2 =fonte.render("Recolheu todos os 10 cartões e ajudou o prof Marcão a comprar seu Civic!", True, cor)
    gameDisplay.blit(texto1, (50, 240))
    gameDisplay.blit(texto2, (50, 265))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 15)
    textoContinue = fonteContinue.render("Pressione ENTER para jogar novamente", True, cor)
    gameDisplay.blit(textoContinue, (50, 300))
    pygameDisplay.update()

