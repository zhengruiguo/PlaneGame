import time
import random
import pygame
from pygame.locals import *

class HeroPlane(object):
    def __init__(self,screen):
        self.x = 230
        self.y = 600
        self.screen = screen
        #self.image_name = 'plane.gif'
        self.image = pygame.image.load('plane.gif').convert()
        self.bullet_list = []
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        need_del_list=[]
        for item in self.bullet_list:
            if item.judge():
                need_del_list.append(item)
        for del_item in need_del_list:
            self.bullet_list.remove(del_item)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def launch_bullet(self):
        new_bullet = Bullet(self.x,self.y,self.screen)
        self.bullet_list.append(new_bullet)

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10
        
class EnemyPlane(object):
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.screen=screen
        self.image_name='timg.gif'
        self.image=pygame.image.load(self.image_name).convert()
        self.bullet_list=[]
        self.direction = 'right'

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        need_del_list=[]
        for i in self.bullet_list:
            if i.judge():
                need_del_list.append(i)
        for i in need_del_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self):
        if self.direction == 'right':
            self.x += 2
        elif self.direction == 'left':
            self.x -= 2
        if self.x > 480 - 50 :
            self.direction = 'left'
        elif self.x < 0 :
            self.direction = 'right'
        time.sleep(0.01)

    def launch_bullet(self):
        number = random.randint(1,100)
        if number == 88:
            new_bullet = EnemyBullet(self.x,self.y,self.screen)
            self.bullet_list.append(new_bullet)
        
        
        
class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load('BD14866_.gif').convert()
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 2

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x=x+30
        self.y=y+30
        self.screen=screen
        self.image = pygame.image.load('BD14868_.GIF').convert()

    def move(self):
        self.y+=2

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def judge(self):
        if self.y>890:
            return True
        else:
            return False


    
def start():
    screen = pygame.display.set_mode((480,890),0,32)
    background = pygame.image.load(r'./Desert.png').convert()
    hero_plane = HeroPlane(screen)
    enemy_plane = EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        hero_plane.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()
        for event in pygame.event.get():
            if event.type == QUIT:
                print('exit')
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    hero_plane.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    hero_plane.move_right()
                elif event.key == K_SPACE:
                    print('space')
                    hero_plane.launch_bullet()
        pygame.display.update()

        
if __name__=='__main__':
    start()
