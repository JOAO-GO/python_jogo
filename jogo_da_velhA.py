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
personagem_y = fonte_quadrinhos.render('o', True, 'red')
cor_fundo = 1

while running:
    # controle de evento do jogo
    for event in pygame.event.get():
    # pygame.QUIT significa que quando usuario clicar x a tela fechará
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            cor_fundo = cor_fundo + 1
            if(cor_fundo > 3):
                cor_fundo = 1
 # desenha tabuleiro
    pygame.draw.line(screen, 'white',(200, 0,), (200, 600), 10)
    pygame.draw.line(screen, 'white',(400, 0,), (400, 600), 10)
    pygame.draw.line(screen, 'white',(0, 200,), (600, 200), 10)
    pygame.draw.line(screen, 'white',(0, 400,), (600, 400), 10)

    screen.blit(personagem_x,(60,30)) #primeiro
    screen.blit(personagem_y,(260,30)) #segundo
    screen.blit(personagem_y,(460,30)) #segundo
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()