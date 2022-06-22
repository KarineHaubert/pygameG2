
def cadastraJogador(nome, email):
    w = open('jogador.txt', 'a')
    w.write('Nome: {}, E-mail: {}\n'.format(nome, email))
    w.close()

def jogo():
    jogando = True
    movimentoX = 0
    movimentoY = random.randrange(0, altura)
    velocidade = 1
    direcao = True
    posicaoXPlayer = 
    posicaoYPlayer = 
    movimentoXPlayer = 0
    movimentoYPlayer = 0
    pontos = 0
    vovozinha = pygame.image.load("assets/idosa.png")
    vovozinha = pygame.transform.flip(vovozinha, True, False)
    banqueiro = pygame.image.load("assets/banqueiro.png")
    banqueiro = pygame.transform.flip(banqueiro, True, False)
    #missile = pygame.transform.scale(missile, (300, 30))
    player = pygame.image.load("assets/pedrinho.png")
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.Sound.play(missileSound)
    larguraPlayer = 
    alturaPlayer = 
    larguraVovozinha = 
    alturaVovozinha = 
    limiar = 
    velocidadePlayer = 
    
