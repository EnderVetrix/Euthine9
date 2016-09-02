#                       _____________
#______________________/  Euthine 9  \__________________________________________
import pygame,sys, random
import pyganim
from pygame.locals import *
import time
# the following line is not needed if pgu is installed
#import sys; sys.path.insert(0, "..")

#from pgu import gui

#app = gui.Desktop()
#app.connect(gui.QUIT,app.quit,None)

##The table code is entered much like HTML.
##::
#c = gui.Table()

#c.tr()
#c.td(gui.Label("Name"))
#c.td(gui.Input(value='Name',size=8),colspan=6)


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.font.init()
mainclock= pygame.time.Clock()
window=pygame.display.set_mode((360,560,),FULLSCREEN,32)
windowf=pygame.FULLSCREEN
pygame.display.set_caption('Euthine 9')
score=0
Texty = pygame.font.Font('coure.fon', 20)
Textyy = pygame.font.Font('coure.fon', 10)
text = Texty.render('Score: %d' % score, 0, (255,255,255))

#       ________________
# =====|Entity Frequency|======
#  ____________________________
# |the higher the less frequent|

astrfrqnc=1 
dbfrqc=400
player=pygame.Rect(170,380,20,20)
shield=False
#                       ___________
#______________________/  Images   \____________________________________________

#shipx=pygame.image.load('Euthine 9.png')
shiplx=pygame.image.load('Euthine 9 Left.png')
shiprx=pygame.image.load('Euthine 9 Right.png')
shipfx=pygame.image.load('Euthine 9 Forward.png')
shipbx=pygame.image.load('Euthine 9 Backward.png')
shipshield=pygame.image.load('Shield.png')
bullet=pygame.image.load('Bullet.png')
bulletE=pygame.image.load('BulletE.png')
asteroidx=pygame.image.load('Asteroid.png')
#drone1x=pygame.image.load('Mantis.png')
#drone2x=pygame.image.load('PXMK9XX.png')
drone3x=pygame.image.load('Drone.png')
drone4x=pygame.image.load('America.png')
star=pygame.image.load('Star.png')
backdrop=pygame.image.load('Backdrop.png')
backdropt=pygame.image.load('Backdroptitle.png')
# create the animation objects   ('filename of image',    duration_in_seconds)
shipx = pyganim.PygAnimation([('Sprite/Euthine 9.png', 0.1),
                                 ('Sprite/Euthine 9 1.png', 0.1),
                                 ('Sprite/Euthine 9 2.png', 0.1),
                                 ('Sprite/Euthine 9 3.png', 0.1),
                                 ('Sprite/Euthine 9 4.png', 0.1),
                                 ('Sprite/Euthine 9 5.png', 0.1),
                                 ('Sprite/Euthine 9 6.png', 0.1),
                                 ('Sprite/Euthine 9 7.png', 0.1),
                                 ('Sprite/Euthine 9 8.png', 0.1),
                                 ('Sprite/Euthine 9 9.png', 0.1),
                                 ('Sprite/Euthine 9 10.png', 0.1)])
shipx.play() # there is also a pause() and stop() method

# create the animation objects   ('filename of image',    duration_in_seconds)
drone1x = pyganim.PygAnimation([('Sprite/Mantis.png', 0.5),
                                 ('Sprite/Mantis 2.png', 0.5)])
drone1x.play() # there is also a pause() and stop() method

# create the animation objects   ('filename of image',    duration_in_seconds)
drone2x = pyganim.PygAnimation([('Sprite/PXMK9XX.png', 0.5),
                                 ('Sprite/PXMK9XX 1.png', 0.5)])
drone2x.play() # there is also a pause() and stop() method

#                       ______________
#______________________/  Variables   \_________________________________________

shadow=[]
blink=255
a=0
pb=[]
db=[]

tp=False

astroid=[]
drone=[]
drone2=[]
drone3=[]
drone4=[]
power=0
p=-250
W=(255,255,255)
B=(0,0,0)
R=(100,0,100)
BL=(0,200,255)
P=(130,245,107)
Ast=(160,160,160)
shieldS=[]
ms=4
bs=10
bulln=0
ha=0
ba=0
son=0 #Required for drones
son2=0 #Required for drones
son3=0 #Required for drones
son4=0 #Required for drones
bonus=0
highscore=0
Nameinput=0
TeP=[]
Try=0
Loaded=False

Laser=False

bugfix1=False
bugfix2=False
bugfix3=False
bugfix4=False

Boss=20 #Boss Health
Bossd=0
shoot=False
test=False
menu=True
game=False
option=0
counter=0
r=True
r2=True
r3=True
r4=True
dronetop=0
dronetop2=0
dronetop3=0
dronetop4=0
Combo=False
die=False
moveleft=False
moveright=False
moveup=False
movedown=False
windowSurface = pygame.display.set_mode((360,560,),FULLSCREEN,32)

    

#                       ____________
#______________________/   Music    \___________________________________________
try:
    b3living=pygame.mixer.Sound('Buzz3.wav')
    b2living=pygame.mixer.Sound('Buzz2.wav')
    b1living=pygame.mixer.Sound('Buzz1.wav')
    lvlup=pygame.mixer.Sound('LevelAdvance.wav')
    Pdead=pygame.mixer.Sound('Laser3.wav')


    shielderror=pygame.mixer.Sound('Rumble3.wav')
    shieldp=pygame.mixer.Sound('Fizzle.wav')
    shootp=pygame.mixer.Sound('Laser1.wav')
    shoote=pygame.mixer.Sound('Laser2.wav')
    hitb=pygame.mixer.Sound('Rumble3.wav')
    death=pygame.mixer.Sound('Explosion.wav')
    deathb=pygame.mixer.Sound('LargeExplosion.wav')
    hit=pygame.mixer.Sound('Pop2.wav')
    #Level1=pygame.mixer.Sound('Level1.mid')
    #titlescreen=pygame.mixer.Sound('Title.mid')
    pygame.mixer.music.load('MusicLoop.wav')
except:
    raise UserWarning, "could not load or play soundfiles."
pygame.mixer.music.set_volume(.4)
pygame.mixer.music.play(-1)
makesound=False


back=[pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5),pygame.Rect(random.randint(0,350),random.randint(0,500),5,5)]
backspd=1
if die==True:
    
    die=False
while True:


#                       ________________
#______________________/  Title Screen  \___________________________________________



    while game==False:
      
        moveleft=False
        moveright=False
        moveup=False
        movedown=False
        counter=0
        Bossd=0
        bonus=0
        astroid=[]
        drone=[]
        drone2=[]
        drone3=[]
        drone4=[]
        db=[]
        pb=[]
        tp=False
        Combo=False
        p=-250
        player=pygame.Rect(170,380,12,20)
        window.blit(backdropt,(-225,0))
        
        #titlescreen.play(-1)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN:
                if event.key== K_DOWN and option==0:
                    option=option+1
                if event.key==K_UP and option==1:
                    option=option-1
                if event.key==K_EQUALS and option==1:
                    pygame.quit()
                    sys.exit()
                if event.key==K_RIGHT and option==0:
                    
                    Nameinput=1   
                    #app.run(c)
                    moveup=False
                    movedown=False
                    moveright=False
                    moveleft=False
                    
        #for event in pygame.event.get():
            #if event.type== KEYDOWN:
                #if event.key==K_e and Nameinput==1:
                    #gui.QUIT()
                    game=True
                    Loaded=True
                    if Loaded==True:
                        Try=Try+1
                        print Try,"Tries"
                        Loaded=False
                        score=0
                        moveright=True


            
        if option==0:
            player.top=380
        if option==1:
            player.top=440
        for booz in back:
            window.blit(star,(booz))
            booz.top+=backspd
            if booz.top>=500:
                booz.left=random.randint(0,300)
                booz.top=-5
    

#                       ______________
#______________________/  Highscore   \_________________________________________
            
        f = open('highscore.txt','r')
        highscore = int(f.read() )
        f.close()
        if score>=highscore:
            highscore=int(round(score,0))
            f = open('highscore.txt','w')
            f.write(str(highscore))
            f.close()
            
        
        
        
          
            
        
                 
        
#                       _________
#______________________/  Text   \______________________________________________        

                
        text = Texty.render('Score: %d' % score, 0, (255,255,255))
        text2 = Texty.render('Highscore: %d' % highscore, 0, (255,255,255))
        text3=  Textyy.render('Music By Timdeuces. ', 0, (10,100,200))
        text4=  Textyy.render('Code Made In Python 2.7. ', 0, (10,100,200))
        text5=  Texty.render('Dev. Build: 4.7  Beta', 0, (255,100,0))
        text6=  Texty.render('Begin', 0, (255,0,0))
        text7=  Texty.render('Exit ', 0, (255,0,0))
        
        window.blit(text, (140,330))
        window.blit(text2, (0,0))
        
        window.blit(text3, (5,510))
        window.blit(text4, (5,530))
        
        window.blit(text5, (5,490))
        window.blit(text6, (220,375))
        window.blit(text7, (220,435))

        
            
        #pygame.draw.rect(window,R,player)
        shipx.blit(window,(player.left-2,player.top))
        mainclock.tick(30)
        pygame.display.update()


#                       ____________
#______________________/  Level 1   \___________________________________________
        
    while game :
        Boss=20
        
        if p>-250:
            p=p-1
        powerbar=pygame.Rect(330,560,20,p)
        counter=counter+1
        if p>=-1:
            shield=False
            Laser=False
        window.blit(backdrop,(0,0))
        #Level1.play(-1)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN:
                if event.key== K_DOWN:
                    movedown=True
                    moveup=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key==K_UP:
                    moveup=True
                    movedown=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key==K_RIGHT:
                    moveright=True
                    moveleft=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key==K_LEFT:
                    moveright=False
                    moveleft=True
                    shipx.blit(window,(player.left-2,player.top))
                if event.key== ord('f'):
                    shoot=True

                if event.key== ord('n'):
                    Combo=True    
                    
                if event.key== ord('s') and p<=-5:
                    shield=True
                    shieldp.play()
                    makesound=True
                    
                if event.key== ord('s') and p>-5:
                    shielderror.play()
                    makesound=True

                if event.key== ord('y') and p<=-5:
                    Laser=True
                if event.key== ord('y') and p>-5:
                    Laser=False
                if event.key== ord('u') and p<=-10:
                    tp=True
                if event.key== ord('u') and p>-10:
                    tp=False
              
            if event.type==KEYUP:
                if event.key== K_DOWN:
                    movedown=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key==K_UP:
                    moveup=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key==K_RIGHT:
                    moveright=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key==K_LEFT:
                    moveleft=False
                    shipx.blit(window,(player.left-2,player.top))
                if event.key== ord('s'):
                    blink=255
                    shield=False
                    a=225
                    shadow=[]
                if event.key== ord('y'):
                    Laser=False
                if event.key== ord('u'):
                    tp=False
                if event.key== ord('n'):
                    Combo=False
              
        
            
        i=random.randint(0,100)
        son=random.randint(0,70)
        son2=random.randint(0,70)
        son3=random.randint(0,70)
        son4=random.randint(0,70)
        shieldS=[]
        if shield==True:
            
            p=p+5
            
            ms=6
            shieldS.append(pygame.Rect(player.left-8,player.top-2,24,24))
            window.blit(shipshield,(player.left-8,player.top-2))
        else :
            ms=4
        
        if Laser==True and bulln<=5:
            
            p=p+10
            
            ms=6
            
            pb.append(pygame.Rect(player.left+2,player.top,6,16))
            window.blit(bullet,(player.left+5,player.top))
            bulln=bulln+1
        else :
            ms=4
            bulln=0
        if Laser==True and bulln>=5:
            shootp.play()
            makesound=True
        
        if tp==True:
            
                p=p+10
            
                ms=6
                shieldp.play()
        else :
            ms=4

       
        if i>99:
            test=True
        if shoot:
            pb.append(pygame.Rect(player.left+2,player.top,6,16))
            window.blit(bullet,(player.left+5,player.top))
            shootp.play()
            makesound=True
            shoot=False

        if Combo:
            pb.append(pygame.Rect(player.left+2,player.top,6,16))
            window.blit(bullet,(player.left+5,player.top))
            shootp.play()
            makesound=True
            Combo = False
      
            
        
        for x in pb:
            x.top-=bs
            
            window.blit(bullet,(x))
            for z in drone:
                if z.colliderect(x):
                    #pygame.mixer.music.play(0,0.0)
                    death.play()
                    makesound=True
                    drone.remove(z)
                    pb.remove(x)
                    bugfix1=True
                    drone.append(pygame.Rect(random.randint(0,340),-40,20,20))
                    bonus=bonus+500
            for z in drone2:
                if z.colliderect(x):
                    #pygame.mixer.music.play(0,0.0)
                    death.play()
                    makesound=True
                    drone2.remove(z)
                    if bugfix1==False:
                        pb.remove(x)
                        bugfix2=True
                    drone2.append(pygame.Rect(random.randint(0,340),-40,20,20))
                    bonus=bonus+1000
            for z in drone3:
                if z.colliderect(x):
                    Boss=Boss-1
                    hitb.play()
                    makesound=True
                if Boss<=0:
                    #pygame.mixer.music.play(0,0.0)
                    deathb.play()
                    makesound=True
                    drone3.remove(z)
                    Bossd=1
                    Boss=20
                    
                if Bossd==1 :
                    print "Boss Defeated!"
                    if bugfix1==False and bugfix2==False and Bossd==0:
                        pb.remove(x)
                        bugfix3=True
                    drone3.append(pygame.Rect(random.randint(0,340),-40,20,20))
                    bonus=bonus+95000
            for z in drone4:
                if z.colliderect(x):
                    #pygame.mixer.music.play(0,0.0)
                    death.play()
                    makesound=True
                    drone4.remove(z)
                    if bugfix1==False and bugfix2==False and bugfix3==False:
                        pb.remove(x)
                        bugfix4=True
                    drone4.append(pygame.Rect(random.randint(0,340),-40,20,20))
                    bonus=bonus+36000
            for z in astroid:
                if z.colliderect(x):
                    score=score+100
                    astroid.remove(z)
                    death.play()
                    if bugfix1==False and bugfix2==False and bugfix3==False and bugfix4==False:
                        pb.remove(x)
                    bonus=bonus+250
        
            if x.top<-80:
                pb.remove(x)
        if makesound:
            
            makesound=False
        bugfix1=False
        bugfix2=False
        bugfix3=False
        bugfix4=False
        score=counter/10 +bonus
        if test:
            astroid.append(pygame.Rect(random.randint(0,320),0,35,35))
            test=False
        for booz in back:
            #pygame.draw.rect(window,W,booz)
            window.blit(star,(booz))
            booz.top+=backspd
            if booz.top>=500:
                booz.left=random.randint(0,355)
                booz.top=-5
        for x in astroid:
            x.top+=5
            window.blit(asteroidx,(x))
            if x.colliderect(player)and shield==False:
                die=True
                Pdead.play()
                game=False
                Bossd=0
            if x.top >600:
                astroid.remove(x)
            TeP=[]
            if tp==True:
                astroid.remove(x)
                tp=False

          #---Drone Level---
                
        if counter==1020 :
            drone.append(pygame.Rect(0,0,20,20))
            lvlup.play()
            makesound=True
            print "Level Clear!"
        if counter==3400 :
            drone2.append(pygame.Rect(0,0,20,20))
            lvlup.play()
            makesound=True
            print "Level Clear!"
        if counter==6040 and Bossd==0 :
            drone3.append(pygame.Rect(0,0,24,40))
            lvlup.play()
            makesound=True
            print "Level Clear!"
        if counter==8060 :
            drone4.append(pygame.Rect(0,0,24,40))
            lvlup.play()
            makesound=True
            print "Level Clear!"
        
        
            
        for x in drone :
            drone1x.blit(window,(x))
            x.top+=dronetop
            if r:
                x.left+=1
            if x.left>=340:
                r=False
                dronetop=random.randint(-1,1)
                
            if r==False:
                x.left-=1
            if x.left<=0:
                r=True
                dronetop=random.randint(-1,1)
            if x.top<-10:
                dronetop=1
            if x.top >200:
                dronetop=-1
            if son<=0.05+counter/dbfrqc and tp==False:
                db.append(pygame.Rect(x.left,x.top,5,10))
                
      
        for w in drone2 :
            drone2x.blit(window,(w))
            w.top+=dronetop2
            if r2:
                w.left+=2
            if w.left>=340:
                r2=False
                dronetop2=random.randint(-1,1)
                
            if r2==False:
                w.left-=2
            if w.left<=0:
                r2=True
                dronetop2=random.randint(-1,1)
            if w.top<-10:
                dronetop2=1
            if w.top >220:
                dronetop2=-1
            
            if son2<=0.5+counter/dbfrqc and tp==False:
                db.append(pygame.Rect(w.left,w.top,5,10))
        
        for l in drone3 :
            window.blit(drone3x,(l))
            l.top+=dronetop3
            if r3:
                l.left+=2
            if l.left>=340:
                r3=False
                dronetop3=random.randint(-1,1)
                
            if r3==False:
                l.left-=2
            if l.left<=0:
                r3=True
                dronetop3=random.randint(-1,1)
            if l.top<-10:
                dronetop3=1
            if l.top >220:
                dronetop3=-1
            
            if son3<=10+counter/dbfrqc and tp==False:
                db.append(pygame.Rect(l.left,l.top,5,10))
        

        for m in drone4 :
            window.blit(drone4x,(m))
            m.top+=dronetop4
            if r4:
                m.left+=1
            if m.left>=340:
                r4=False
                dronetop4=random.randint(-1,1)
                m.top-100
            if r4==False:
                m.left-=1
            if m.left<=0:
                r4=True
                dronetop4=random.randint(-1,1)
                m.top-100
            if m.top<0:
                dronetop4=1
            if m.top >540:
                dronetop4=-1
            if m.left==player.left:
                dronetop4=1
                m.top-1000
            if m.top<=player.top :
                m.left-10
            if m.colliderect(player)and shield==False:
                
                die=True
                Pdead.play()
                game=False
                Bossd=0

                
            
            
            if son4<=0.002+counter/dbfrqc and tp==False:
                db.append(pygame.Rect(m.left,m.top,16,16))
            
            
            
            
        for x in db:

            x.top+=random.randint(3,5)
            if x.colliderect(player)and shield==False:
                
                die=True
                Pdead.play()
                game=False
                Bossd=0
                
                
            window.blit(bulletE,(x))
            if x.top>=580:
                db.remove(x)
                
        
            
            
            TeP=[]
            if tp==True:
            
            
            
                db.remove(x)
                tp=False
                
            
            
                
                
        
        if moveup and player.top>0:
            player.top-=ms
            shipx.blit(window,(player.left-2,player.top))
        if movedown and player.top<540:
            player.top+=ms
            shipx.blit(window,(player.left-2,player.top))
        if moveleft and player.left>0:
            player.left-=ms
            shipx.blit(window,(player.left-2,player.top))
        if moveright and player.left<340:
            player.left+=ms
            shipx.blit(window,(player.left-2,player.top))
        else:
            shipx.blit(window,(player.left-2,player.top))
        text = Texty.render('score: %d' % score, 0, (255,255,255))   
        window.blit(text, (5,0))
        
        #pygame.draw.rect(window,(255, 0, 0, 122),player)
        
        if shield==False:
            blink=255
        if shield==True:
            blink=blink-20
            if blink <=40:
                blink=255
            shipx.set_alpha(blink)
            a=a+25
            if a==250:
                shadow=[]
                shadow.append(pygame.Rect(player.left,player.top,20,20))
                a=0
        shipx.set_alpha(blink)
            #for i in shadow:
               # pygame.draw.rect(window,pygame.Color(255-a,0,0),i)
        
        
        mainclock.tick(80)
        pygame.display.update()

