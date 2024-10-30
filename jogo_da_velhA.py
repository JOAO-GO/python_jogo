# Ecoordenada_xample file showing a basic pygame "game loop"
import pygame


# pygame setup
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Velha') #nome da janela
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100) #importar 
running = True #variavel de controle do status do jogo

personagem_x = fonte_quadrinhos.render('x', True, 'red')
personagem_o = fonte_quadrinhos.render('o', True, 'green')

jogador_atual = personagem_x # inicializa com x

rodadas = 0
tabuleiro_desenhado = False
coordenada_x = 0
coordenada_y = 0

def desenha_tabuleiro(espessura, cor):
    print ('desenha')
# desenha tabuleiro                   origem      destino   
#                                    ( x , y )  ( x , y )
    pygame.draw.line(screen, cor,(200, 0,), (200, 600), espessura)
    pygame.draw.line(screen, cor,(400, 0,), (400, 600), espessura)
    pygame.draw.line(screen, cor,(0, 200,), (600, 200), espessura)
    pygame.draw.line(screen, cor,(0, 400,), (600, 400), espessura)

def faz_jogada():

    #primeira linha
    #
    #                             
    # 
    # coordenada_x  coordenada_y
    if coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:
        screen.blit(jogador_atual,(70,20)) #primeiro

    elif coordenada_x >=  200 and coordenada_x < 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(270,20)) #segundo

    elif coordenada_x >= 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(470,20)) #terceiro   

    elif coordenada_x < 200 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(70,220)) #quarto

    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(270,220)) #quinto

    elif coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(470,220)) #sexto

    elif coordenada_x < 200 and coordenada_y >= 400:
        screen.blit(jogador_atual,(70,420)) #setimo

    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(270,420)) #oitavo

    elif coordenada_x >= 400 and coordenada_y >= 400:
        screen.blit(jogador_atual,(470,420)) #nono

while running:
    # controle de evento do jogo
    for event in pygame.event.get():
   
    # pygame.QUIT significa que quando usuario clicar coordenada_x a tela fechará
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            click_pos = pygame.mouse.get_pos() # a posicao do mouse quando houve o evento de click 
            print('coordenada_x:', click_pos[0])
            print('coordenada_y:', click_pos[1])     
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]
            rodadas = rodadas + 1
            if(rodadas >= 10):
                screen.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0
                tabuleiro_desenhado = False
            
            if rodadas != 1:
                if jogador_atual == personagem_x:
                    jogador_atual = personagem_o
                else:
                    jogador_atual = personagem_x
            else:  
                jogador_atual = personagem_x
            
            faz_jogada()#acrescentar
 
    if tabuleiro_desenhado == False:   
        desenha_tabuleiro(20,'white')
        tabuleiro_desenhado = True


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()