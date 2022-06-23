from funcoes import cadastraJogador, continuar
import pygame
import re
import random

print("")
nomeJogador = input("Digite seu nome: ");
emailJogador= input("Digite seu e-mail: ");

while not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", emailJogador):
    print("E-mail Inválido!")
    emailJogador= input("Digite seu e-mail: ");
    continuar();

while len(nomeJogador) < 3:
    print("Nome Inválido!");
    nomeJogador = input("Digite seu nome: ");
    continuar();

cadastraJogador(nomeJogador, emailJogador);


pygame.init()
altura = 500
largura = 900
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("")
bg = pygame.image.load("assets/fundo.png")
bg_perdeu = pygame.image.load("assets/ganhou.png")
gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()
pink = (237, 141, 172);
black = (0, 0, 0);
white = (255,255,255);


def dead(pontos):
    gameDisplay.blit(bg_perdeu, (0, 0))
    pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(explosaoSound)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                        " pontos!", True, black)
    gameDisplay.blit(texto, (50, 100))
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    # textoContinue = fonteContinue.render("press enter to restart", True, white)
    # gameDisplay.blit(textoContinue, (50, 200))
    pygameDisplay.update()

def jogo():
    jogando = True
    movimentoXvovozinha = 0
    movimentoYvovozinha = random.randrange(0, altura)
    movimentoXbanqueiro = 0
    movimentoYbanqueiro = random.randrange(0, altura)
    velocidade = 1
    direcao = True
    posicaoXPlayer = 450
    posicaoYPlayer = 100
    movimentoXPlayer = 0
    movimentoYPlayer = 0
    pontos = 0
    vovozinha = pygame.image.load("assets/senhora.png")
    vovozinha = pygame.transform.flip(vovozinha, True, False)
    banqueiro = pygame.image.load("assets/cearensebanqueiro.png")
    banqueiro = pygame.transform.flip(banqueiro, True, False)
    #missile = pygame.transform.scale(missile, (300, 30))
    player = pygame.image.load("assets/cabecaPedro.png")
    # pygame.mixer.music.load("assets/trilha.mp3")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.1)
    # pygame.mixer.Sound.play(missileSound)
    larguraPlayer = 60
    alturaPlayer = 60
    larguraVovozinha = 60
    alturaVovozinha = 60
    largurabanqueiro = 60
    alturabanqueiro = 60
    velocidadePlayer = 10
    limiar = 28

    while True:
       
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoXPlayer = -velocidadePlayer
                elif event.key == pygame.K_RIGHT:
                    movimentoXPlayer = velocidadePlayer
                elif event.key == pygame.K_UP:
                    movimentoYPlayer = -velocidadePlayer
                elif event.key == pygame.K_DOWN:
                    movimentoYPlayer = velocidadePlayer
                elif event.key == pygame.K_RETURN:
                    jogo()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXPlayer = 0
                    movimentoYPlayer = 0
        if jogando == True:
          
            posicaoXPlayer = posicaoXPlayer + movimentoXPlayer
            if posicaoXPlayer < 0:
                posicaoXPlayer = 0
            elif posicaoXPlayer > largura - larguraPlayer:
                posicaoXPlayer = largura - larguraPlayer
            posicaoYPlayer = posicaoYPlayer + movimentoYPlayer
            if posicaoYPlayer < 0:
                posicaoYPlayer = 0
            elif posicaoYPlayer > altura - alturaPlayer:
                posicaoYPlayer = altura - alturaPlayer
            gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(player, (posicaoXPlayer, posicaoYPlayer))
            gameDisplay.blit(vovozinha, (movimentoXvovozinha, movimentoYvovozinha))
            gameDisplay.blit(banqueiro, (movimentoXbanqueiro, movimentoXbanqueiro))
            
            if direcao == True:
                if movimentoXvovozinha <= 900 - 150 and movimentoXbanqueiro <= 900 - 150:
                    movimentoXvovozinha = movimentoXvovozinha + velocidade
                    movimentoXbanqueiro = movimentoXbanqueiro + velocidade
                else:
                    # pygame.mixer.Sound.play(missileSound)
                    direcao = False
                    pontos = pontos + 1
                    movimentoYvovozinha = random.randrange(0, altura)
                    movimentoYbanqueiro = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    vovozinha = pygame.transform.flip(vovozinha, True, False)
                    banqueiro = pygame.transform.flip(banqueiro, True, False)
            else:
                if movimentoXvovozinha  >= 0 and movimentoYbanqueiro >= 0:
                    movimentoXvovozinha = movimentoXvovozinha + velocidade
                    movimentoXbanqueiro = movimentoXbanqueiro + velocidade
                else:
                    # pygame.mixer.Sound.play(missileSound)
                    direcao = True
                    pontos += 1
                    movimentoYvovozinha = random.randrange(0, altura)
                    movimentoYbanqueiro = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    vovozinha = pygame.transform.flip(vovozinha, True, False)
                    banqueiro = pygame.transform.flip(banqueiro, True, False)
            
            
            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 280))
            
            pixelYVovozinha = list(range(movimentoYvovozinha, movimentoYvovozinha+alturaVovozinha + 1))
            pixelXVovozinha = list(range(movimentoXvovozinha, movimentoXvovozinha+larguraVovozinha + 1))
            pixelYbanqueiro = list(range(movimentoYbanqueiro, movimentoYbanqueiro+alturabanqueiro + 1))
            pixelXbanqueiro= list(range(movimentoXbanqueiro, movimentoXbanqueiro+largurabanqueiro + 1))
            pixelYPlayer = list(range(posicaoYPlayer, posicaoYPlayer + alturaPlayer +1 ))
            pixelXPlayer = list(range(posicaoXPlayer, posicaoXPlayer + larguraPlayer +1 ))
            colisaoY = list( set(pixelYVovozinha) & set(pixelYbanqueiro) & set(pixelYPlayer)  )
            colisaoX = list( set(pixelXVovozinha) & set(pixelXbanqueiro)  & set(pixelXPlayer)  )
            if len(colisaoY) > limiar:
                if len(colisaoX) > limiar:
                    jogando =  False
                    dead(pontos)
        
        pygameDisplay.update()
        clock.tick(60)
jogo()