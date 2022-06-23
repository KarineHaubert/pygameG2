from funcoes import cadastraJogador, continuar, checa_cartao, dead, venceu
import pygame
import re
import random


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
bg = pygame.image.load("assets/fundo.jpeg")
bg_perdeu = pygame.image.load("assets/perdeu.png")
bg_ganhou = pygame.image.load("assets/ganhou.png")
gameDisplay = pygame.display.set_mode(tamanho)
gameEvents = pygame.event
clock = pygame.time.Clock()
pink = (237, 141, 172);
black = (0, 0, 0);
white = (255,255,255);



def jogo():
    jogando = True

    vovozinha = pygame.image.load("assets/senhora.png")
    banqueiro = pygame.image.load("assets/cearensebanqueiro.png")
    player = pygame.image.load("assets/cabecaPedro.png")
    cartao = pygame.image.load("assets/cartao.png")
    velocidade = 5
   
    movimentoXvovozinha, movimentoXbanqueiro = 0, 0
    movimentoYvovozinha, movimentoYbanqueiro = random.randrange(0, altura), random.randrange(0, altura)
    cartaoX, cartaoY = 0, random.randrange(0.2*largura, 0.8*altura, velocidade)

    posicaoXPlayer = 450
    posicaoYPlayer = 100
    movimentoXPlayer = 0
    movimentoYPlayer = 0
    
  
    larguraPlayer = 109
    alturaPlayer = 149
    larguraVovozinha = 119
    alturaVovozinha = 130
    largurabanqueiro = 117
    alturabanqueiro = 130
    velocidadePlayer = 10
    larguraCartao = 133
    limiar = 40
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

            gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))
            gameDisplay.blit(player, (posicaoXPlayer, posicaoYPlayer))
            gameDisplay.blit(vovozinha, (movimentoXvovozinha, movimentoYvovozinha))
            gameDisplay.blit(banqueiro, (movimentoXbanqueiro, movimentoYbanqueiro))
            gameDisplay.blit(cartao, (cartaoX, cartaoY));
            
            cartaoX += velocidade
            movimentoXvovozinha += velocidade
            movimentoXbanqueiro += velocidade

            if (checa_cartao(movimentoXPlayer, movimentoYPlayer, larguraPlayer, alturaPlayer, cartaoX, cartaoY, larguraCartao)):
                cartaoX, cartaoY = 0, random.randrange(0, altura) 
                pontos +=1
                print(pontos)
             
            if cartaoX >= largura:
                cartaoX, cartaoY = 0, random.randrange(0, altura)   
            if movimentoXvovozinha >= largura:
                movimentoXvovozinha, movimentoYvovozinha = 0, random.randrange(0, altura)   
            if movimentoXbanqueiro >= largura:
                movimentoXbanqueiro, movimentoYbanqueiro = 0, random.randrange(0, altura)  


            
            fonte = pygame.font.Font('freesansbold.ttf', 20)
            texto = fonte.render("cartões: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 280))
            
            pixelYVovozinha = list(range(movimentoYvovozinha, movimentoYvovozinha+alturaVovozinha + 1))
            pixelXVovozinha = list(range(movimentoXvovozinha, movimentoXvovozinha+larguraVovozinha + 1))
            pixelYbanqueiro = list(range(movimentoYbanqueiro, movimentoYbanqueiro+alturabanqueiro + 1))
            pixelXbanqueiro= list(range(movimentoXbanqueiro, movimentoXbanqueiro+largurabanqueiro + 1))
            pixelYPlayer = list(range(posicaoYPlayer, posicaoYPlayer + alturaPlayer +1 ))
            pixelXPlayer = list(range(posicaoXPlayer, posicaoXPlayer + larguraPlayer +1 ))
            colisaoYPerde = list( set(pixelYVovozinha) & set(pixelYbanqueiro) & set(pixelYPlayer)  )
            colisaoXPerde = list( set(pixelXVovozinha) & set(pixelXbanqueiro)  & set(pixelXPlayer)  )
            if len(colisaoYPerde) > limiar:
                if len(colisaoXPerde) > limiar:
                    jogando =  False
                    dead(gameDisplay, bg_perdeu, pygame, black, pygameDisplay, pontos)
            elif pontos == 10:
                jogando = False
                venceu(gameDisplay, bg_ganhou, pygame, black, pygameDisplay, pontos)
        pygameDisplay.update()
        clock.tick(60)
jogo()