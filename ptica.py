import pygame
import random

prepreka1 = pygame.image.load(r'prepreka1.png')
prepreka2 = pygame.image.load(r'prepreka2.png')
ptica0 = pygame.image.load(r'ptica.png')

try:
    fajl = open("skor.txt", 'r')
    hajskor = int(fajl.readline())
    if hajskor == "":
        hajskor = 0
    fajl.close()
except:
    hajskor = 0
brzina = 3
class Ptica:
    def __init__(self, dis):
        self.x = 100
        self.y = 350
        self.skace = False
        self.krenulo = False
        self.dis = dis
        self.skokic = 0
        self.padanje = 3.8

    def update(self):
        if not self.krenulo:
            self.dis.blit(ptica0, (self.x, self.y))
            return
        if not self.skace:
            self.y += self.padanje
            self.padanje += 0.4
        else:
            self.skokic += 1
            if self.skokic <= 10:
                self.y -= 8
            elif self.skokic <= 15:
                self.y -= 8 - self.skokic + 10
            if self.skokic == 17:
                self.skokic = 0
                self.skace = False
                self.padanje = 3.8
        self.dis.blit(ptica0, (self.x, self.y))

    def skoci(self):
        if self.skokic == 0:
            self.krenulo = True
            self.skace = True
        
        
#vel1 = 570
#vel2 = 570

class Prepreka:
    def __init__(self):
        self.x = 400
        self.broj = random.randint(365, 580)
        self.stvar = random.randint(540, 570)

    def update(self, dis):
        self.x -= brzina
        dis.blit(prepreka1, (self.x, self.broj))
        dis.blit(prepreka2, (self.x, self.broj - self.stvar))

    def iks(self):
        return self.x

pygame.init()
screen_w = 400
screen_h = 700
dis = pygame.display.set_mode((screen_w, screen_h))
pygame.display.update()
pygame.display.set_caption("Flepi bird")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#dis.blit(prepreka1, (0, 570))
#dis.blit(prepreka2, (0, 0))


while True:
    prepreke = []
    prepreke.append(Prepreka())

    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render('Skor: 1000', True, BLACK)
    text2 = font.render('Haj Skor: 1000', True, BLACK)
    skor = text.get_rect()
    skor.center = (90, 20)
    skor2 = text2.get_rect()
    skor2.center= (122, 55)

    ptica = Ptica(dis)
    clock = pygame.time.Clock()
    skorv = 0
    while True:
        clock.tick(60)
        dis.fill(WHITE)
        dis.blit(font.render('Skor: ' + str(skorv), True, BLACK), skor)
        if skorv > hajskor:
            dis.blit(font.render('Haj Skor: ' + str(skorv), True, BLACK), skor2)
        else:
            dis.blit(font.render('Haj Skor: ' + str(hajskor), True, BLACK), skor2)
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                if skorv > hajskor:
                    fajl = open("skor.txt", 'w')
                    fajl.write(str(skorv))
                    fajl.close()
                    exit()
        ptica.update()
        if ptica.krenulo:
            for b in prepreke:
                b.update(dis)   
            if prepreke[0].iks() < -170:
                prepreke.pop(0)
            if prepreke[0].iks() < -100 and len(prepreke) == 1:
                prepreke.append(Prepreka()) 
                skorv += 1
                if brzina <= 5:
                    brzina += 0.3
                if skorv % 100 == 0:
                    brzina += 1
        keys_pressed = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.MOUSEBUTTONDOWN]:
            ptica.skoci()
        if ((abs(ptica.x - prepreke[0].x) < 50) and (ptica.y > prepreke[0].broj-66 or ptica.y < prepreke[0].broj - 232 + 570 - prepreke[0].stvar)) or ptica.y >= 600 or ptica.y <= 0:
            if skorv > hajskor:
                fajl = open("skor.txt", 'w')
                fajl.write(str(skorv))
                fajl.close()
                hajskor = skorv
            break
        #if (skorv % 20 == 0):
            #if vel1 > 400:
            #    vel1-=10
            #if vel2 > 480:
            #    vel2-=10
        #if pygame.mouse.get_pressed()[0]:
        #    print(pygame.mouse.get_pos())
        #    print(prepreke[0].broj)
        #    pygame.display.update()
        #    break
        #clock.tick()
        pygame.display.update()
        
