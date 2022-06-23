import os

def cadastraJogador(nome, email):
    w = open('jogador.txt', 'a')
    w.write('Nome: {}, E-mail: {}\n'.format(nome, email))
    w.close()

def continuar():
    os.system("pause")

def checa_cartao(playerX, playerY, larguraPlayer, alturaPlayer, cartaoX, cartaoY, tamanhoCartao):
    if(playerX - cartaoX)<= tamanhoCartao and (cartaoX - playerX) <= larguraPlayer:
        if(playerY - cartaoY)<= tamanhoCartao and (cartaoY - playerY) <= alturaPlayer:
            return True
    return False


def dead(gameDisplay, bg_perdeu, pygame, cor, pygameDisplay, pontos):
    gameDisplay.blit(bg_perdeu, (0, 0))
    # pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    texto = fonte.render("Você Perdeu! Só recolheu "+str(pontos) +
                        " cartoes :(", True, cor)
    gameDisplay.blit(texto, (50, 100))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    textoContinue = fonteContinue.render("press enter to restart", True, cor)
    gameDisplay.blit(textoContinue, (50, 200))
    pygameDisplay.update()

def venceu(gameDisplay, bg_venceu, pygame, cor, pygameDisplay, pontos):
    gameDisplay.blit(bg_venceu, (0, 0))
    # pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    texto = fonte.render("Você Ganhou! Recolheu todos os \n 10 cartões e ajudou o prof Marcão a comprar seu Civic!", True, cor)
    gameDisplay.blit(texto, (50, 100))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    textoContinue = fonteContinue.render("press enter to restart", True, cor)
    gameDisplay.blit(textoContinue, (50, 200))
    pygameDisplay.update()

