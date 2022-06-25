
from funcoes import cadastraJogador, continuar, dead, inicio, venceu, colisaoXVovozinha, colisaoYVovozinha, colisaoXCartao, colisaoYCartao
import pygame
import re
import random


inicio()
nomeJogador = input("Digite seu nome: ").lower();
emailJogador= input("Digite seu e-mail: ").lower();

while not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", emailJogador):
        print("E-mail Inválido!")
        emailJogador= input("Digite seu e-mail: ");

while len(nomeJogador) < 3:
        print("Nome Inválido! Precia conter mais de 3 caracteres");
        nomeJogador = input("Digite seu nome: ");
     

cadastraJogador(nomeJogador, emailJogador);
continuar();

pygame.init()
altura = 500
largura = 900
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Idosas e Furiosas")
bg = pygame.image.load("assets/fundo.jpeg")
bg_perdeu = pygame.image.load("assets/perdeu.png")
bg_ganhou = pygame.image.load("assets/ganhou.png")
gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()
black = (0, 0, 0);
white = (255,255,255);

somCartao = pygame.mixer.Sound("assets/somCartao.wav")
somCartao.set_volume(0.1)

def jogo():
    jogando = True

    vovozinha = pygame.image.load("assets/senhora.png")
    vovozinha = pygame.transform.flip(vovozinha, True, False)
    player = pygame.image.load("assets/cabecaPedro.png")
    cartao = pygame.image.load("assets/cartao.png")
    velocidade = 1
    direcao = True
    vovozinhaX = 0
    vovozinhaY = random.randrange(0, altura)
    cartaoX = 0
    cartaoY = random.randrange(0.2*largura, 0.8*altura, velocidade)
    posicaoXPlayer = 450
    posicaoYPlayer = 100
    movimentoXPlayer = 0
    movimentoYPlayer = 0
    
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    gameIcon = pygame.image.load("assets/iconCivic.png")
    pygameDisplay.set_icon(gameIcon)

    larguraPlayer = 109
    alturaPlayer = 149
    larguraVovozinha = 105
    alturaVovozinha = 105
    velocidadePlayer = 10
    larguraCartao = 133
    alturaCartao = 84
    limiar = 21
    pontos = 0

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

            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(player, (posicaoXPlayer, posicaoYPlayer))
            gameDisplay.blit(vovozinha, (vovozinhaX, vovozinhaY))
            gameDisplay.blit(cartao, (cartaoX, cartaoY));
            
            cartaoX += velocidade + 1

            if cartaoX >= largura:
                cartaoX, cartaoY = 0, random.randrange(0, altura)

            if direcao == True:
                if vovozinhaX <= 900 - 150:
                    vovozinhaX += velocidade
                else:
                    direcao = False
                    vovozinhaY = random.randrange(0, altura)
                    vovozinha = pygame.transform.flip(vovozinha, True, False)
            else:
                if vovozinhaX >= 0:
                    vovozinhaX -= velocidade
                else:
                    direcao = True
                    vovozinhaY = random.randrange(0, altura)
                    vovozinha = pygame.transform.flip(vovozinha, True, False)

            
            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("cartões: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 450))
            
            

            pixelYPlayer = list(range(posicaoYPlayer, posicaoYPlayer + alturaPlayer +1 ))
            pixelXPlayer = list(range(posicaoXPlayer, posicaoXPlayer + larguraPlayer +1 ))
            colisaoXCard = colisaoXCartao(cartaoX,larguraCartao,pixelXPlayer)
            colisaoYCard = colisaoYCartao(cartaoY,alturaCartao,pixelYPlayer)
            colisaoXVovo = colisaoXVovozinha(vovozinhaX,larguraVovozinha,pixelXPlayer)
            colisaoYVovo = colisaoYVovozinha(vovozinhaY,alturaVovozinha,pixelYPlayer)


            if len(colisaoXVovo) > limiar:
                if len(colisaoYVovo) > limiar:
                    jogando =  False
                    dead(gameDisplay, bg_perdeu, pygame, black, pygameDisplay, pontos)

            elif len(colisaoXCard) > 14:
                 if len(colisaoYCard) > limiar:
                    cartaoX, cartaoY = 0, random.randrange(0, altura) 
                    pontos +=1
                    pygame.mixer.Sound.play(somCartao)
                    velocidade += 1 
                    vovozinhaX += 1
                    if pontos == 10:
                        jogando = False
                        venceu(gameDisplay, bg_ganhou, pygame, white, pygameDisplay)
           
        pygameDisplay.update()
        clock.tick(60)

jogo();


