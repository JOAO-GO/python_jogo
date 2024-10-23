# Example file showing a basic pygame "game loop"
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
personagem_y = fonte_quadrinhos.render('o', True, 'green')
apresenta_personagem = 0
x = 0
y = 0

while running:
    # controle de evento do jogo
    for event in pygame.event.get():
    # pygame.QUIT significa que quando usuario clicar x a tela fechará
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            click_pos = pygame.mouse.get_pos() # a posicao do mouse quando houve o evento de click 
            print('eixo x:', click_pos[0])
            print('eixo y:', click_pos[1])     
            x = click_pos[0]
            y = click_pos[1]
            apresenta_personagem = apresenta_personagem + 1
            if(apresenta_personagem > 10):
                screen.fill('black')
                apresenta_personagem = 0

 # desenha tabuleiro

    pygame.draw.line(screen, 'white',(200, 0,), (200, 600), 10)
    pygame.draw.line(screen, 'white',(400, 0,), (400, 600), 10)
    pygame.draw.line(screen, 'white',(0, 200,), (600, 200), 10)
    pygame.draw.line(screen, 'white',(0, 400,), (600, 400), 10)

    #primeira linha
    #
    #                              x  y
    if x > 0 and x < 200 and y < 200:
        screen.blit(personagem_x,(70,20)) #primeiro

    elif x >=  200 and x < 400 and y < 200:
        screen.blit(personagem_y,(270,20)) #segundo

    elif x >= 400 and y < 200:
        screen.blit(personagem_y,(470,20)) #terceiro   

    elif x < 200 and y >= 200 and y < 400:
        screen.blit(personagem_x,(70,220)) #quarto

    elif x >= 200 and x < 400 and y >= 200 and y < 400:
        screen.blit(personagem_y,(270,220)) #quinto

    elif x >= 400 and y >= 200 and y < 400:
        screen.blit(personagem_y,(470,220)) #sexto

    elif x < 200 and y >= 400:
        screen.blit(personagem_x,(70,420)) #setimo

    elif x >= 200 and x < 400 and y >= 400:
        screen.blit(personagem_y,(270,420)) #oitavo

    elif x >= 400 and y >= 400:
        screen.blit(personagem_y,(470,420)) #nono
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()