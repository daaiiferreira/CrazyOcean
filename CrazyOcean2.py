import pygame
import random

pygame.init()


# Define as dimensões da janela
largura_janela = 800
altura_janela = 750
tamanho = (largura_janela, altura_janela)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Crazy Ocean")
relogio = pygame.time.Clock()
cor_tela = (0, 0, 255) 

janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Crazy Ocean")

# Define as dimensões do personagem
largura_personagem = 80
altura_personagem = 80

#criar inimigo
def criaInimigo():
    imagem = pygame.image.load(f"imagens/shark/shark1.png")

    tipos = [
        'tubarao',
        'polvo'
    ]

    velocidade = random.randint(5, 10)
    tamanho = random.randint(60, 80)
    

    return {
        "posicao": [random.randint(100, largura_janela - 100), random.randint(10, 20)],
        "velocidade": velocidade,
        "tipo": random.choice(tipos),
        "tamanho": tamanho,
        "vidas": random.randint(5, 8), 
        "direcao": pygame.Vector2(1, 1),
        "categoria": 'inimigo',
        "retangulo": pygame.Rect(0, 0, 100, 100)
    }

#criar amigos
def criaObstaculo():
    tipos = [
        'peixe',
        'aguaviva',
        'tartaruga'
    ]

    velocidade = random.randint(6, 8)
    tipo = random.choice(tipos)
    tamanho = random.randint(10, 20)
    posicao_x = random.randint(50, largura_janela)
    posicao_y = random.randint(0, 0)
   
    return {
        "posicao": [posicao_x, posicao_y],
        "velocidade": velocidade,
        "tipo": tipo,
        "tamanho": tamanho, 
        "direcao": pygame.Vector2(1, 1),
        "categoria": 'amigo',
        "ataque": random.randint(2, 4),
        "retangulo": pygame.Rect(posicao_x, posicao_y, tamanho, tamanho)
    }

#criar boss
def criaBoss():
    imagem = pygame.image.load(f"imagens/boss/1.png")

    tipos = [
        'amarelo'
    ]

    velocidade = random.randint(2, 5)
    tamanho = random.randint(200, 230)
    

    return {
        "posicao": [random.randint(100, largura_janela - 100), random.randint(10, 20)],
        "velocidade": velocidade,
        "tipo": random.choice(tipos),
        "tamanho": tamanho,
        "vidas": random.randint(12, 18), 
        "direcao": pygame.Vector2(1, 1),
        "retangulo": pygame.Rect(0, 0, 200, 200)
    }

listaImagensFundo = []
for index in range(1):
    imagem = pygame.image.load(f"imagens/fundo/fundo.jpg")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, tamanho).convert_alpha()
    listaImagensFundo.append(imagem)

listaImagensBoss = []
for index in range(1, 360):
    imagem = pygame.image.load(f"imagens/boss/{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (400, 250)).convert_alpha()
    listaImagensBoss.append(imagem)

listaImagensPeixe = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/peixe/peixe{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (60, 60)).convert_alpha()
    listaImagensPeixe.append(imagem)

    listaImagensTartaruga = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/tartaruga/tart{index}.png")
    imagem = pygame.transform.flip(imagem, False, False)
    imagem = pygame.transform.scale(imagem, (80, 80)).convert_alpha()
    listaImagensTartaruga.append(imagem)

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

listaImagensTubaraoDano = []
for index in range(1, 3):
    imagem = pygame.image.load(f"imagens/shark/dano/sharkdano{index}.png")
    imagem = pygame.transform.flip(imagem, False, True)
    imagem = pygame.transform.scale(imagem, (100, 100)).convert_alpha()
    listaImagensTubaraoDano.append(imagem)

listaImagensPolvo = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/polvo/polvo{index}.png")
    imagem = pygame.transform.flip(imagem, True, True)
    imagem = pygame.transform.scale(imagem, (100, 100)).convert_alpha()
    listaImagensPolvo.append(imagem)

listaImagensPolvoDano = []
for index in range(1, 3):
    imagem = pygame.image.load(f"imagens/polvo/dano/dano{index}.png")
    imagem = pygame.transform.flip(imagem, True, True)
    imagem = pygame.transform.scale(imagem, (100, 100)).convert_alpha()
    listaImagensPolvoDano.append(imagem)

# Carrega as imagens do personagem
listaImagensPersonagemAndando = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/pers/andando/andando{index}.png")
    imagem = pygame.transform.flip(imagem, True, False)
    imagem = pygame.transform.scale(imagem, (largura_personagem, altura_personagem)).convert_alpha()
    listaImagensPersonagemAndando.append(imagem)

personagem_rect = listaImagensPersonagemAndando[0].get_rect()

listaImagensPersonagemDano = []
for index in range(1, 7):
    imagem = pygame.image.load(f"imagens/pers/dano/pers{index}.png")
    imagem = pygame.transform.flip(imagem, True, False)
    imagem = pygame.transform.scale(imagem, (largura_personagem, altura_personagem)).convert_alpha()
    listaImagensPersonagemDano.append(imagem)

listaImagensPersonagemVida = []
for index in range(1, 3):
    imagem = pygame.image.load(f"imagens/pers/dano/dano{index}.png")
    imagem = pygame.transform.flip(imagem, True, False)
    imagem = pygame.transform.scale(imagem, (largura_personagem, altura_personagem)).convert_alpha()
    listaImagensPersonagemVida.append(imagem)

listaImagensPersonagemMorrendo = []
for index in range(1, 9):
    imagem = pygame.image.load(f"imagens/pers/morreu/morte{index}.png")
    imagem = pygame.transform.flip(imagem, True, False)
    imagem = pygame.transform.scale(imagem, (largura_personagem, altura_personagem)).convert_alpha()
    listaImagensPersonagemMorrendo.append(imagem)

listaObstaculo = []

listaJogador = []

listaInimigo = []

listaBoss = []

pontuacao = 0
ataque = 0
vidas = 2

fonte = pygame.font.Font(None, 50)
fonteObstaculo = pygame.font.Font(None, 30)
fonteVidaJogador = pygame.font.Font(None, 35)
fonteInimigo = pygame.font.Font(None, 40)
fontePontuacao = pygame.font.Font(None, 40)
fonteAtaque = pygame.font.Font(None, 35)


obstaculoEvent = pygame.USEREVENT + 2

inimigoEvent = pygame.USEREVENT + 1

bossEvent = pygame.USEREVENT + 1

personagemEvent = pygame.USEREVENT + 1


pygame.time.set_timer(obstaculoEvent, 2000)

pygame.time.set_timer(inimigoEvent, 6000)

# Função para criar o jogador
def criaJogador():
    return {
        "posicao_x": largura_janela // 2,
        "posicao_y": altura_janela // 1.5,
        "velocidade": 20,
        "imagem_index": 0,
        "retangulo": pygame.Rect(largura_janela // 2, altura_janela // 2, largura_personagem, altura_personagem)  
    }

# Cria o jogador
personagem = criaJogador()

janela_aberta = True
clock = pygame.time.Clock()


temaSonoro = pygame.mixer.Sound("sons/tema3.wav")
musica_efeito = pygame.mixer.Sound("sons/inimigo.wav")
musica_efeito_derrota = pygame.mixer.Sound("sons/ainn-cafezinho.mp3")
#musica_efeito_vitoria = pygame.mixer.Sound("sons/bubble_01.ogg")
musica_efeito_pontuacao = pygame.mixer.Sound("sons/victory-3.wav")
musica_efeito_obstaculo = pygame.mixer.Sound("sons/bubble_01.ogg")
musica_efeito_dano = pygame.mixer.Sound("sons/ataque.wav")
musica_efeito_ataque_up = pygame.mixer.Sound("sons/colisao_ob.ogg")
musica_efeito_inimigo_morre = pygame.mixer.Sound("sons/inimigo.wav")
musica_efeito_personagem_dano = pygame.mixer.Sound("sons/vida.wav")
musica_efeito_inimigo_dano = pygame.mixer.Sound("sons/dano.mp3")

pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1) 
temaSonoro.play(-1)

print("iniciar")

jogoAcabou = False

while janela_aberta:
    clock.tick(15)
    
  # Limita a taxa de atualização da tela

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:

                jogoAcabou = False
                listaObstaculo = []
                listaInimigo = []
                pontuacao = 0
                ataque = 0
                vidas = 2         

        if evento.type == obstaculoEvent:
            listaObstaculo.append(criaObstaculo()) 
            musica_efeito_obstaculo.play()

        if evento.type == inimigoEvent:
            listaInimigo.append(criaInimigo())
            musica_efeito.play() 

        if evento.type == bossEvent:
            listaBoss.append(criaBoss())
            musica_efeito.play()   

    for i in range(len(listaImagensFundo)):
        tela.blit(listaImagensFundo[i], (0,0))

    inimigo = criaInimigo()

    boss = criaBoss()

    if vidas == 0 or ataque == -1:
             
        jogoAcabou = True     

        # Desenha a mensagem de game over
        texto = fonte.render("VOCÊ PERDEU!", True, (255, 0, 0))
        texto_rect = texto.get_rect(center=(tamanho[0] // 2, 150))
        tela.blit(texto, texto_rect)

        texto = fonte.render(f"PONTUAÇÃO: {pontuacao}", True, (255, 255, 255)) # Cria o texto
        texto_rect = texto.get_rect(center=(tamanho[0] // 2, 280)) # Cria um retangulo para o texto
        tela.blit(texto, texto_rect) # Desenha o texto na tela

        texto = fonteVidaJogador.render("Aperte ENTER para recomeçar...", True, (0, 0, 155))
        texto_rect = texto.get_rect(center=(tamanho[0] // 2, 400))
        tela.blit(texto, texto_rect)
           
        # Atualiza o índice da imagem do personagem para a animação de dano
        personagem["imagem_index"] = (personagem["imagem_index"] + 1) % len(listaImagensPersonagemMorrendo)
      # Desenha o personagem na tela com a animação de dano
        janela.blit(listaImagensPersonagemMorrendo[personagem["imagem_index"]], (tamanho[0] // 2 - 50, 300))
        pygame.time.delay(200)   

    if not jogoAcabou:             

        # Verifica as teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            personagem["posicao_y"] -= personagem["velocidade"]
        if teclas[pygame.K_DOWN]:
            personagem["posicao_y"] += personagem["velocidade"]
        if teclas[pygame.K_RIGHT]:
            personagem["posicao_x"] += personagem["velocidade"]
        if teclas[pygame.K_LEFT]:
            personagem["posicao_x"] -= personagem["velocidade"]

        # Atualiza a posição do retângulo do personagem
        personagem_rect.x = personagem["posicao_x"]
        personagem_rect.y = personagem["posicao_y"]

        #pygame.draw.rect(tela, (255, 0, 0), personagem_rect)
            
        if teclas[pygame.K_SPACE]:
        # Verifica o dano do inimigo quando a tecla de espaço é pressionada
            musica_efeito_dano.play()
            
            # Atualiza o índice da imagem do personagem para a animação de dano
            personagem["imagem_index"] = (personagem["imagem_index"] + 1) % len(listaImagensPersonagemDano)
            # Desenha o personagem na tela com a animação de dano
            janela.blit(listaImagensPersonagemDano[personagem["imagem_index"]], (personagem["posicao_x"], personagem["posicao_y"]))

            
        else:
            # Atualiza o índice da imagem do personagem para a animação de movimento normal
            personagem["imagem_index"] = (personagem["imagem_index"] + 1) % len(listaImagensPersonagemAndando)
            # Desenha o personagem na tela com a animação de movimento normal
            janela.blit(listaImagensPersonagemAndando[personagem["imagem_index"]], (personagem["posicao_x"], personagem["posicao_y"]))


        # Defina as coordenadas para o texto
        posicao_texto_vida = (400, 70)  

        # Renderize o texto
        textoVidaJogador = fonteVidaJogador.render(f"Vidas: {vidas}", True, (0, 0, 80))

        # Obtenha o retângulo do texto
        textoVidaJogadorRect = textoVidaJogador.get_rect()

        # Defina as coordenadas do retângulo do texto
        textoVidaJogadorRect.topleft = posicao_texto_vida

        # Desenhe o texto na tela
        tela.blit(textoVidaJogador, textoVidaJogadorRect)

        posicao_texto_ataque = (400, 100)  

        # Renderize o texto
        textoAtaque = fonteAtaque.render(f"Ataque: {ataque}", True, (0, 0, 80))

        # Obtenha o retângulo do texto
        textoAtaqueRect = textoAtaque.get_rect()

        # Defina as coordenadas do retângulo do texto
        textoAtaqueRect.topleft = posicao_texto_ataque

        # Desenhe o texto na tela
        tela.blit(textoAtaque, textoAtaqueRect)

        

        # Desenha a pontuação na tela
        texto = fontePontuacao.render(f"Pontuação: {pontuacao}", True, (0, 0, 80)) # Cria o texto
        centro_tela = (tamanho[0] // 1 - 150, tamanho[1] // 15) # Calcula o centro da tela
        texto_rect = texto.get_rect(center=centro_tela) # Cria um retangulo para o texto
        tela.blit(texto, texto_rect) # Desenha o texto na tela

            # Processa a lista de bolas, desenhando e movendo
        for obstaculo in listaObstaculo:
                # Desenhar a bola na tela
            circulo = pygame.Rect(
                obstaculo["posicao"][0] - obstaculo["tamanho"], 
                obstaculo["posicao"][1] - obstaculo["tamanho"], 
                obstaculo["tamanho"] * 2, 
                obstaculo["tamanho"] * 2
            )
            
            listaImagens = []
            if obstaculo["tipo"] == 'peixe': listaImagens = listaImagensPeixe
            elif obstaculo["tipo"] == 'aguaviva': listaImagens = listaImagensAviva
            elif obstaculo["tipo"] == 'tartaruga': listaImagens = listaImagensTartaruga

            imagem = listaImagens[(pygame.time.get_ticks() // 100) % len(listaImagens)]
            imagem_rect = imagem.get_rect(center=(obstaculo["posicao"][0] - 30, obstaculo["posicao"][1] - 30))

            tela.blit(imagem, imagem_rect)

            obstaculo["retangulo"].x = obstaculo["posicao"][0] - 30
            obstaculo["retangulo"].y = obstaculo["posicao"][1] - 30

            #pygame.draw.rect(tela, (255, 255, 0), obstaculo["retangulo"])

            obstaculo["posicao"][1] += 14

            textoObstaculo = fonteObstaculo.render(f"{obstaculo['ataque']}", True, (255, 255, 255))
            textoObstaculoRect = textoObstaculo.get_rect(center=obstaculo["posicao"])
            tela.blit(textoObstaculo, textoObstaculoRect)

            if personagem_rect.colliderect(obstaculo["retangulo"]):
                # verificaChoqueObstaculo()
                musica_efeito_ataque_up.play()
                ataque  += obstaculo["ataque"]
                listaObstaculo.remove(obstaculo)
                
                #som de colisão
                #pygame.mixer.Sound("bubble_01.ogg").play()

        

        for inimigo in listaInimigo:
            listaImagens = []
            

            if personagem_rect.colliderect(inimigo["retangulo"]) & teclas[pygame.K_SPACE]:
                # verificaChoqueObstaculo()
                musica_efeito_inimigo_dano.play()
                
                inimigo["vidas"] -= 1
                ataque -= 1
                if inimigo["vidas"] == 0:
                    pontuacao += 1                    
                    musica_efeito_inimigo_morre.play()
                    listaInimigo.remove(inimigo)


                if inimigo["tipo"] == 'tubarao':
                    # Atualiza o índice da imagem do personagem para a animação de dano
                    inimigo["tamanho"] = (inimigo["tamanho"] + 1) % len(listaImagensTubaraoDano)
                    # Desenha o personagem na tela com a animação de dano
                    janela.blit(listaImagensTubaraoDano[inimigo["tamanho"]], (inimigo["posicao"], inimigo["posicao"]))

                else:
                    # Atualiza o índice da imagem do personagem para a animação de dano
                    inimigo["tamanho"] = (inimigo["tamanho"] + 1) % len(listaImagensPolvoDano)
                    # Desenha o personagem na tela com a animação de dano
                    janela.blit(listaImagensPolvoDano[inimigo["tamanho"]], (inimigo["posicao"], inimigo["posicao"]))

            else: 
                if inimigo["tipo"] == 'tubarao': listaImagens = listaImagensTubarao        
                elif inimigo["tipo"] == 'polvo': listaImagens = listaImagensPolvo
                imagem = listaImagens[(pygame.time.get_ticks() // 100) % len(listaImagens)]
                imagem_rect = imagem.get_rect(center=(inimigo["posicao"][0] - 10, inimigo["posicao"][1] - 10))
                tela.blit(imagem, imagem_rect)

                inimigo["retangulo"].x = inimigo["posicao"][0] - 10
                inimigo["retangulo"].y = inimigo["posicao"][1] - 10

                # pygame.draw.rect(tela, (255, 0, 255), inimigo["retangulo"])


                inimigo["posicao"][1] += 8

                textoInimigo = fonteInimigo.render(f"{inimigo['vidas']}", True, (0, 0, 0))
                textoInimigoRect = textoInimigo.get_rect(center=inimigo["posicao"])
                tela.blit(textoInimigo, textoInimigoRect)

            if inimigo["posicao"][1] >= 800:
                vidas += (-1)
                musica_efeito_personagem_dano.play()
                listaInimigo.remove(inimigo)
                # Atualiza o índice da imagem do personagem para a animação de dano
                personagem["imagem_index"] = (personagem["imagem_index"] + 1) % len(listaImagensPersonagemVida)
            # Desenha o personagem na tela com a animação de dano
                janela.blit(listaImagensPersonagemVida[personagem["imagem_index"]], (personagem["posicao_x"], personagem["posicao_y"]))
            
        
        # Dentro do seu código onde a pontuação é atualizada
        if pontuacao == 3:
            for boss in listaBoss:
                listaImagens = []
                
                if boss["tipo"] == 'amarelo':
                    # Atualiza o índice da imagem do personagem para a animação de dano
                    boss["tamanho"] = (boss["tamanho"] + 1) % len(listaImagensBoss)
                    # Desenha o personagem na tela com a animação de dano
                    janela.blit(listaImagensBoss[boss["tamanho"]], (boss["posicao"], boss["posicao"]))
                    musica_efeito_pontuacao.play()

            
    

    # Atualiza a tela
    
    pygame.display.update()
    relogio.tick(60)

pygame.quit()
