import pygame
import random
import os

pygame.init()
pygame.mixer.music.load("sons/tema3.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 
   

#criar personagem principal
def criaJogador():
    imagem = pygame.image.load(f"imagens/pers/andando/andando1.png")

    tipos = [
        'sereia'
    ]
    vidas = 6
    posicao_jogador_x = 250
    posicao_jogador_y = 800
    largura_jogador = 50
    altura_jogador = 50
    velocidade_jogador = 5

    return{
        "velocidade": velocidade_jogador,
        "tipo": random.choice(tipos),
        "tamanho": (largura_jogador, altura_jogador),
        "vidas": vidas, 
        "retangulo": imagem.get_rect(midbottom=(posicao_jogador_x, posicao_jogador_y))
       
    }  


#criar inimigo
def criaInimigo():
    imagem = pygame.image.load(f"imagens/shark/shark1.png")

    tipos = [
        'tubarao',
        'polvo'
    ]

    velocidade = random.randint(10, 16)
    tamanho = random.randint(30, 50)
    

    return {
        "posicao": [random.randint(50, 350), random.randint(10, 20)],
        "velocidade": velocidade,
        "tipo": random.choice(tipos),
        "tamanho": tamanho,
        "vidas": 3, 
        "direcao": pygame.Vector2(1, 1),
        "categoria": 'inimigo',
    }

#criar amigos
def criaObstaculo():
    tipos = [
        'peixe',
        'aguaviva'
    ]

    velocidade = random.randint(6, 10)
    tipo = random.choice(tipos)
    tamanho = random.randint(10, 20)
   
    return {
        "posicao": [random.randint(50, 350), random.randint(10, 20)],
        "velocidade": velocidade,
        "tipo": tipo,
        "tamanho": tamanho, 
        "direcao": pygame.Vector2(1, 1),
        "categoria": 'amigo',
        "vidas": 3
    }

personagem = criaJogador()

velocidade_jogador = 5


def verificaCliqueObstaculo(listaObstaculo):
    global pontuacao 

listaObstaculo = []

listaJogador = []

listaInimigo = []

#amigo_jogado = []

obstaculoEvent = pygame.USEREVENT + 2

inimigoEvent = pygame.USEREVENT + 1

personagemEvent = pygame.USEREVENT + 1


#criar tela azul 
pygame.init()
largura = 400
altura = 750
tamanho = (largura, altura)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Crazy Ocean")
relogio = pygame.time.Clock()
cor_tela = (0, 0, 255) 

fonte = pygame.font.Font(None, 200)
fonteObstaculo = pygame.font.Font(None, 15)
fonteVidaJogador = pygame.font.Font(None, 30)

pygame.time.set_timer(obstaculoEvent, 1000)

pygame.time.set_timer(inimigoEvent, 5000)


listaImagensFundo = []
for index in range(1):
    imagem = pygame.image.load(f"imagens/fundo/fundo.jpg")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
    listaImagensFundo.append(imagem)


listaImagensPeixe = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/peixe/peixe{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (60, 60)).convert_alpha()
    listaImagensPeixe.append(imagem)

listaImagensAviva = []
for index in range(1, 5):
    imagem = pygame.image.load(f"imagens/aguaviva/aviva{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (80, 80)).convert_alpha()
    listaImagensAviva.append(imagem)

listaImagensTubarao = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/shark/shark{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (100, 100)).convert_alpha()
    listaImagensTubarao.append(imagem)

listaImagensPersonagemAndando = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/pers/andando/andando{index}.png")
    imagem = pygame.transform.flip(imagem, True, False)
    imagem = pygame.transform.scale(imagem, (80, 80)).convert_alpha()
    listaImagensPersonagemAndando.append(imagem)

posicao_jogador_x = 250
posicao_jogador_y = 800
largura_jogador = 50
altura_jogador = 50
velocidade_jogador = 5

posicao_elemento_x = 0
posicao_elemento_y = 0
largura_elemento = 50
altura_elemento = 50
velocidade_elemento = 3


#lógica: mapa corre na vertical, de baixo pra cima. Personagem principal pega peixinhos para alimentar os tubarões para conseguir se defender. Caso não tenha peixinhos, precisa matar o tubarão para avançar.

while True:  

    for evento in pygame.event.get():
        
        # se o evento for de fechar a tela
        if evento.type == pygame.QUIT:
            pygame.quit() #fecha o pygame
            exit() #fecha o programa

        


        if evento.type == obstaculoEvent:
            listaObstaculo.append(criaObstaculo())  

        if evento.type == inimigoEvent:
            listaInimigo.append(criaInimigo())  
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                #jogoAcabou = False
                listaImagensJogador = []
                listaImagensJogador.append(criaJogador())
                #pontuacao = 0

        

        
            
            # elif evento.key == pygame.K_SPACE:
            #     if personagem.amigo_jogado is None:
            #         personagem.amigo_jogado = amigo_jogado
    # Atualização do estado do jogador
    

   
    # Desenho na tela
    


    

    tela.fill(cor_tela)

    for i in range(len(listaImagensFundo)):
        tela.blit(listaImagensFundo[i], (0,0))


    # DESENHO DO PERSONAGEM
    listaImagensJogador = []
    keys = pygame.key.get_pressed()           
    if keys[pygame.K_UP]:
                posicao_jogador_y -= velocidade_jogador
    if keys[pygame.K_RIGHT]:
                largura += velocidade_jogador
    if personagem["tipo"] == 'sereia' : listaImagensJogador = listaImagensPersonagemAndando
                    
    imagem = listaImagensJogador[(pygame.time.get_ticks() // 100) % len(listaImagensJogador)]
    tela.blit(imagem, personagem["retangulo"])   

    

    
    for obstaculo in listaObstaculo:
        
        listaImagens = []
        if obstaculo["tipo"] == 'peixe': listaImagens = listaImagensPeixe
        elif obstaculo["tipo"] == 'aguaviva': listaImagens = listaImagensAviva
        #elif obstaculo["tipo"] == 'polvo': listaImagens = listaImagensPolvo

        imagem = listaImagens[(pygame.time.get_ticks() // 100) % len(listaImagens)]
        imagem_rect = imagem.get_rect(center=(obstaculo["posicao"][0] - 30, obstaculo["posicao"][1] - 30))

        tela.blit(imagem, imagem_rect)

        obstaculo["posicao"][1] += 5

        textoObstaculo = fonteObstaculo.render(f"{obstaculo['vidas']}", True, (255, 255, 255))
        textoBolinhaRect = textoObstaculo.get_rect(center=obstaculo["posicao"])
        tela.blit(textoObstaculo, textoBolinhaRect)

        

    for inimigo in listaInimigo:
        listaImagens = []
        if inimigo["tipo"] == 'tubarao': listaImagens = listaImagensTubarao        
        elif inimigo["tipo"] == 'polvo': listaImagens = listaImagensTubarao

        imagem = listaImagens[(pygame.time.get_ticks() // 100) % len(listaImagens)]
        imagem_rect = imagem.get_rect(center=(inimigo["posicao"][0] - 30, inimigo["posicao"][1] - 30))

        tela.blit(imagem, imagem_rect)

        inimigo["posicao"][1] += 1

    

          
        
    #tela.fill((cor_tela))
    pygame.display.update()

    # Controla a quantidade de FPS
    relogio.tick(60)

#criar a lógica