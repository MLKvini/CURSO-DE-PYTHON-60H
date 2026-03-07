import pygame


pygame.init()
tamanho  =  300,200
screen = pygame.display.set_mode(tamanho)


run = True
while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         screen.fill('LightSkyBlue')
         
         pygame.draw.rect(screen,'black',(125,50,50,50) ) 
         pygame.draw.ellipse(screen, 'yellow', (150,100,100,100))
         pygame.draw.line(screen, 'green', (0,0), (300,150), 5)
         pygame.draw.circle(screen, 'blue', (50,50), 30)
         
         pygame.display.update()
         
pygame.quit()               
         
         
    
