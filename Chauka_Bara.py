import pygame
from pygame.locals import*
import random
pygame.init()
windowsize=(1128,790)
gamewindow=(183,200,476,476)#(x,y,width,height)width and height of one box is 70
screen = pygame.display.set_mode(windowsize,HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Anoop\'s Game')
bg = pygame.image.load("data\\Chaukabara.png")
FONT = pygame.font.SysFont('gabriola', 40)
quitt_box=pygame.Rect(940,20,168,50)
COLOR_ACTIVE=(50,50,255)
COLOR_INACTIVE=(255,255,255)
red=pygame.image.load("data\\red1.png")
green=pygame.image.load("data\\green1.png")
blue=pygame.image.load("data\\blue1.png")
yellow=pygame.image.load("data\\yellow1.png")
screen1=pygame.image.load('data\\Chaukabara.png')
turn_indicator=[0,pygame.image.load('data\\blueturn.png'),pygame.image.load('data\\yellowturn.png'),pygame.image.load('data\\greenturn.png'),pygame.image.load('data\\redturn.png')]
back=pygame.image.load('data\\Back button.png')
note=pygame.image.load('data\\Note.png')
howtoplay=pygame.image.load('data\\Howtoplay.png')
howtoplaybtn=pygame.image.load('data\\Htpbtn.png')
notebtn=pygame.image.load('data\\Disclaimer.png')
Nokillyetsound=pygame.mixer.Sound('data\\NoKillYet.wav')
xJodixsound=pygame.mixer.Sound('data\\xJodix.wav')
oneplayerwinsound=pygame.mixer.Sound('data\\OnePlayerWins.wav')
Ohhosound=pygame.mixer.Sound('data\\Ohho.wav')
Killsound=pygame.mixer.Sound('data\\Kill.wav')
Tokengoesinsound=pygame.mixer.Sound('data\\TokenGoesIn.wav')
Innerloopentersound=pygame.mixer.Sound('data\\Innerloopenter.wav')
print()
kill=False
run =True
start=True
isjump=False
MoreThanNeeded=False
turn=1

plyr1=''
plyr2=''
plyr3=''
plyr4=''

safe=[1,7,13,19,25,29,33,37,49,0]
token_left=[0,4,4,4,4]
winorder=[0,0,0,0,0]
turntoken=[0,1,1,1,1]
pos=[(0,0),(390,612),(460,612),(528,612),(597,612),(597,544),(597,476),(597,406),(597,338),(597,269),(597,200),(528,200),(460,200),(390,200),(322,200),(253,200),(184,200),(184,269),(184,338),(184,406),(184,476),(184,544),(184,612),(253,612),(322,612),(253,544),(253,476),(253,406),(253,338),(253,269),(322,269),(390,269),(460,269),(528,269),(528,338),(528,406),(528,476),(528,544),(460,544),(390,544),(322,544),(322,476),(322,406),(322,338),(390,338),(460,338),(460,406),(460,476),(390,476),(390,406)]
path=[[0],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,0,0,0,0,0,0]
		,[0,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,37,38,39,40,25,26,27,28,29,30,31,32,33,34,35,36,47,48,41,42,43,44,45,46,49,0,0,0,0,0,0]
		,[0,13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12,33,34,35,36,37,38,39,40,25,26,27,28,29,30,31,32,45,46,47,48,41,42,43,44,49,0,0,0,0,0,0]
		,[0,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,29,30,31,32,33,34,35,36,37,38,39,40,25,26,27,28,43,44,45,46,47,48,41,42,49,0,0,0,0,0,0]]

colorpos =  [[0],
			[0,1,1,1,1,'s','s','s','s',0,25,blue,1],# 1st element is 0th so turn cannot access it tokens 1,2,3,4 and  
			[0,7,7,7,7,'s','s','s','s',0,37,yellow,7],#next 4they being in either safe or unsafe position and 
			[0,13,13,13,13,'s','s','s','s',0,33,green,13],#index 9th one is no. of kills and
			[0,19,19,19,19,'s','s','s','s',0,29,red,19]]#index 10th one is if in this pos he has to check if he has kiiled anyone or not. from this pos only he enters the inner sides

token_box = [
			[pygame.Rect(0,0,2,2)],
			[0,[pygame.Rect(pos[colorpos[1][1]][0],pos[colorpos[1][1]][1],67,68)],[pygame.Rect(pos[colorpos[1][2]][0],pos[colorpos[1][2]][1],67,68)],[pygame.Rect(pos[colorpos[1][3]][0],pos[colorpos[1][3]][1],67,68)],[pygame.Rect(pos[colorpos[1][4]][0],pos[colorpos[1][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[2][1]][0],pos[colorpos[2][1]][1],67,68)],[pygame.Rect(pos[colorpos[2][2]][0],pos[colorpos[2][2]][1],67,68)],[pygame.Rect(pos[colorpos[2][3]][0],pos[colorpos[2][3]][1],67,68)],[pygame.Rect(pos[colorpos[2][4]][0],pos[colorpos[2][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[3][1]][0],pos[colorpos[3][1]][1],67,68)],[pygame.Rect(pos[colorpos[3][2]][0],pos[colorpos[3][2]][1],67,68)],[pygame.Rect(pos[colorpos[3][3]][0],pos[colorpos[3][3]][1],67,68)],[pygame.Rect(pos[colorpos[3][4]][0],pos[colorpos[3][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[4][1]][0],pos[colorpos[4][1]][1],67,68)],[pygame.Rect(pos[colorpos[4][2]][0],pos[colorpos[4][2]][1],67,68)],[pygame.Rect(pos[colorpos[4][3]][0],pos[colorpos[4][3]][1],67,68)],[pygame.Rect(pos[colorpos[4][4]][0],pos[colorpos[4][4]][1],67,68)]]
			]


def game_init():
	global kill,run,start,isjump,turn,plyr1,pos,plyr2,plyr3,plyr4,safe,token_left,winorder,turntoken,colorpos,token_box
	kill=False
	run =True
	start=True
	isjump=False
	turn=1
	plyr1=''
	plyr2=''
	plyr3=''
	plyr4=''
	safe=[1,7,13,19,25,29,33,37,49,0]
	token_left=[0,4,4,4,4]
	winorder=[0,0,0,0,0]
	turntoken=[0,1,1,1,1]
	colorpos =  [[0],
			[0,1,1,1,1,'s','s','s','s',0,25,blue,1],# 1st element is 0th so turn cannot access it tokens 1,2,3,4 and  
			[0,7,7,7,7,'s','s','s','s',0,37,yellow,7],#next 4they being in either safe or unsafe position and 
			[0,13,13,13,13,'s','s','s','s',0,33,green,13],#index 9th one is no. of kills and
			[0,19,19,19,19,'s','s','s','s',0,29,red,19]]#index 10th one is if in this pos he has to check if he has kiiled anyone or not. from this pos only he enters the inner sides

	token_box = [
				[pygame.Rect(0,0,2,2)],
				[0,[pygame.Rect(pos[colorpos[1][1]][0],pos[colorpos[1][1]][1],67,68)],[pygame.Rect(pos[colorpos[1][2]][0],pos[colorpos[1][2]][1],67,68)],[pygame.Rect(pos[colorpos[1][3]][0],pos[colorpos[1][3]][1],67,68)],[pygame.Rect(pos[colorpos[1][4]][0],pos[colorpos[1][4]][1],67,68)]],
				[0,[pygame.Rect(pos[colorpos[2][1]][0],pos[colorpos[2][1]][1],67,68)],[pygame.Rect(pos[colorpos[2][2]][0],pos[colorpos[2][2]][1],67,68)],[pygame.Rect(pos[colorpos[2][3]][0],pos[colorpos[2][3]][1],67,68)],[pygame.Rect(pos[colorpos[2][4]][0],pos[colorpos[2][4]][1],67,68)]],
				[0,[pygame.Rect(pos[colorpos[3][1]][0],pos[colorpos[3][1]][1],67,68)],[pygame.Rect(pos[colorpos[3][2]][0],pos[colorpos[3][2]][1],67,68)],[pygame.Rect(pos[colorpos[3][3]][0],pos[colorpos[3][3]][1],67,68)],[pygame.Rect(pos[colorpos[3][4]][0],pos[colorpos[3][4]][1],67,68)]],
				[0,[pygame.Rect(pos[colorpos[4][1]][0],pos[colorpos[4][1]][1],67,68)],[pygame.Rect(pos[colorpos[4][2]][0],pos[colorpos[4][2]][1],67,68)],[pygame.Rect(pos[colorpos[4][3]][0],pos[colorpos[4][3]][1],67,68)],[pygame.Rect(pos[colorpos[4][4]][0],pos[colorpos[4][4]][1],67,68)]]
				]
	#token_box[turn] gives us all the 4token's positions as (x,y,w,h) which we can directly use to see whether he clicked on a box with his token or not

class plyrbox:

    def __init__(self, x, y, w, h, text=''):
    	self.done = False
    	self.rect = pygame.Rect(x, y, w, h)
    	self.color = COLOR_INACTIVE
    	self.text = text
    	self.txt_surface = FONT.render(text, True, self.color)
    	self.active = False

    def handle_event(self, event,plyrid):
        global plyr1,plyr2,plyr3,plyr4
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    #self.text = ''
                    self.done = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        screen.blit(pygame.image.load('data\\welcome.png'),(0,0))
        screen.blit(notebtn,(25,738))
        screen.blit(howtoplaybtn,(123,738))
		#print(plyr3)
        self.txt_surface = FONT.render(self.text, True, (50,50,250))
        if plyrid == 1:
           	plyr1 = self.text
        elif plyrid == 2:
           	plyr2 = self.text
        elif plyrid == 3:
          	plyr3 = self.text
        elif plyrid == 4:
           	plyr4 = self.text
        
    def update(self):
        width = max(320, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
    	screen.blit(self.txt_surface, (self.rect.x+15, self.rect.y+15))
    	pygame.draw.rect(screen, self.color, self.rect, 4)


def gamepage1():
	start_box=pygame.Rect(370,570,375,110)
	global run,screen1,screen
	backpress=False
	screen.blit(pygame.image.load('data\\welcome.png'),(0,0))
	plyr1_box = plyrbox(102,306,320,59)
	plyr2_box = plyrbox(712,306,320,57)
	plyr3_box = plyrbox(100,477,320,57)
	plyr4_box = plyrbox(712,474,320,57)
	plyr_boxes = [ plyr1_box, plyr2_box, plyr3_box, plyr4_box]
	startbtn=False
	screen.blit(notebtn,(25,738))
	screen.blit(howtoplaybtn,(123,738))
	pygame.display.update()
	while run and not startbtn:
		plyrid=0
		screen.blit(notebtn,(25,738))
		screen.blit(howtoplaybtn,(123,738))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run = False
			if event.type==pygame.MOUSEBUTTONDOWN and pygame.Rect(25,738,100,30).collidepoint(event.pos):
				screen.blit(note,(0,0))
				screen.blit(back,(958,20))
				pygame.display.update()
				backpress=False
				while not backpress:
					for event in pygame.event.get():
						if event.type==pygame.QUIT:
							run =False
							backpress=True
							break
						if event.type==pygame.MOUSEBUTTONDOWN and pygame.Rect(958,20,150,50).collidepoint(event.pos) or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
							screen.blit(pygame.image.load('data\\welcome.png'),(0,0))
							pygame.display.update()
							backpress=True
							break
			if event.type==pygame.MOUSEBUTTONDOWN and pygame.Rect(125,738,180,30).collidepoint(event.pos):
				screen.blit(howtoplay,(0,0))
				screen.blit(back,(958,20))
				pygame.display.update()
				backpress=False
				while not backpress:
					for event in pygame.event.get():
						if event.type==pygame.QUIT:
							run =False
							backpress=True
							break
						if event.type==pygame.MOUSEBUTTONDOWN and pygame.Rect(958,20,150,50).collidepoint(event.pos) or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
							screen.blit(pygame.image.load('data\\welcome.png'),(0,0))
							pygame.display.update()
							backpress=True
							break
			if event.type == pygame.MOUSEBUTTONDOWN and start_box.collidepoint(event.pos) or event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
				startbtn=True
				screen.blit(pygame.image.load('data\\Start.png'),(374,564))
				pygame.display.update()
				pygame.time.delay(200)
				screen.blit(pygame.image.load('data\\Start2.png'),(374,564))
				pygame.display.update()
				pygame.time.delay(500)
			for box in plyr_boxes:
				plyrid+=1
				box.handle_event(event,plyrid)
		
		for box in plyr_boxes:
			box.update()

		for box in plyr_boxes:
			box.draw(screen)

		pygame.display.flip()
		pygame.time.delay(20)




def allthebest():
	global run,colorpos
	fontsize=10
	n=[0,[0,0],[0,25],[25,0],[25,25]]
	screen.fill((255,255,255))
	while fontsize<60 and run == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		fontsize+=1
		font = pygame.font.SysFont('comicsansms', fontsize)
		text = font.render('...All The Best...', True, (0,0,0))#,(150,170,250))
		textrect=text.get_rect()
		textrect.center=(windowsize[0]//2,windowsize[1]//2+fontsize)
		screen.blit(text,textrect)
		pygame.display.update()
		pygame.time.delay(3)
		screen.fill((255,255,255))
	pygame.time.delay(500)
	screen.blit(bg,(0,0))
	colorpos =  [[0],
			[0,1,1,1,1,'s','s','s','s',0,25,blue,1],# 1st element is 0th so turn cannot access it tokens 1,2,3,4 and  
			[0,7,7,7,7,'s','s','s','s',0,37,yellow,7],#next 4they being in either safe or unsafe position and 
			[0,13,13,13,13,'s','s','s','s',0,33,green,13],#index 9th one is no. of kills and
			[0,19,19,19,19,'s','s','s','s',0,29,red,19]]#index 10th one is if in this pos he has to check if he has kiiled anyone or not. from this pos only he enters the inner sides
	token_box = [
			[pygame.Rect(0,0,2,2)],
			[0,[pygame.Rect(pos[colorpos[1][1]][0],pos[colorpos[1][1]][1],67,68)],[pygame.Rect(pos[colorpos[1][2]][0],pos[colorpos[1][2]][1],67,68)],[pygame.Rect(pos[colorpos[1][3]][0],pos[colorpos[1][3]][1],67,68)],[pygame.Rect(pos[colorpos[1][4]][0],pos[colorpos[1][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[2][1]][0],pos[colorpos[2][1]][1],67,68)],[pygame.Rect(pos[colorpos[2][2]][0],pos[colorpos[2][2]][1],67,68)],[pygame.Rect(pos[colorpos[2][3]][0],pos[colorpos[2][3]][1],67,68)],[pygame.Rect(pos[colorpos[2][4]][0],pos[colorpos[2][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[3][1]][0],pos[colorpos[3][1]][1],67,68)],[pygame.Rect(pos[colorpos[3][2]][0],pos[colorpos[3][2]][1],67,68)],[pygame.Rect(pos[colorpos[3][3]][0],pos[colorpos[3][3]][1],67,68)],[pygame.Rect(pos[colorpos[3][4]][0],pos[colorpos[3][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[4][1]][0],pos[colorpos[4][1]][1],67,68)],[pygame.Rect(pos[colorpos[4][2]][0],pos[colorpos[4][2]][1],67,68)],[pygame.Rect(pos[colorpos[4][3]][0],pos[colorpos[4][3]][1],67,68)],[pygame.Rect(pos[colorpos[4][4]][0],pos[colorpos[4][4]][1],67,68)]]
			]
	for j in range(1,5):
		for i in range(1,5):
			screen.blit(colorpos[i][11],(pos[colorpos[i][j]][0]+10+n[j][0],pos[colorpos[i][j]][1]+10+n[j][1]))
			pygame.display.update()
		pygame.time.delay(200)


def DispPlayerName():
	#center 400,135 green  1
	#center 400,740 blue   4
	#top    790,200 yellow 2 bottom 790,660 middle 790,430
	#top    55, 200 red    3 bootom 55, 660 middle 55, 430
	global turn,turn_indicator,token_box
	font=pygame.font.SysFont('constantia', 35)
	text = font.render(plyr1, True, (0,0,0))#,(150,170,250))
	textrect=text.get_rect()
	textrect.center=(400,740)
	screen.blit(text,textrect)
	pygame.display.update()
	pygame.time.delay(200)

	plyrgap = -30*len(plyr2)//2+1
	for i in plyr2:
		text = font.render(i, True, (0,0,0))#,(150,170,250)
		textrect=text.get_rect()
		textrect.center=(790,430+plyrgap)
		screen.blit(text,textrect)
		plyrgap+=30
	pygame.display.update()
	pygame.time.delay(200)
		
	text = font.render(plyr3, True, (0,0,0))#,(150,170,250))
	textrect=text.get_rect()
	textrect.center=(400,135)
	screen.blit(text,textrect)
	pygame.display.update()
	pygame.time.delay(200)

	plyrgap = -30*len(plyr4)//2+1
	for i in plyr4:
		text = font.render(i, True, (0,0,0))#,(150,170,250)
		textrect=text.get_rect()
		textrect.center=(55,430+plyrgap)
		screen.blit(text,textrect)
		plyrgap+=30
	pygame.display.update()
	pygame.time.delay(200)

	screen.blit(turn_indicator[turn],(972,109))
	pygame.display.update()
	

	FONt = pygame.font.SysFont('comicsansms', 35)
	for k in range(1,5):
		text=FONt.render(str(colorpos[k][9]),True,(0,0,0))
		textrect=text.get_rect()
		textrect.center=(910,252+(k-1)*48-k)
		screen.blit(text,textrect)
		pygame.display.update()
	

def animate_text(msg,x1,y1,w1,h1):
	global screen1
	fontsz=25
	sub=screen1.subsurface(pygame.Rect(x1,y1,w1,h1))
	while fontsz<=35:
		FOnt=pygame.font.SysFont('comicsansms', fontsz)
		text=FOnt.render(msg,True,(50,50,50))
		textrect=text.get_rect()
		textrect.center=(x1+w1//2,y1+h1//2)
		screen.blit(text,textrect)
		pygame.display.update()
		pygame.time.delay(30)
		screen.blit(sub,(x1,y1))
		pygame.display.update()
		fontsz+=1
	screen.blit(text,textrect)
	pygame.display.update()
	pygame.time.delay(900)
	screen.blit(sub,(x1,y1))
	pygame.display.update()


def adjustbox(mane,screen2):
	global pos,colorpos,token_left,screen1
	sadasya_count=0
	s1=1
	sadasya=[0,[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	for colour in range(1,5):
		for j in range(1,5):
			if colorpos[colour][j]==mane:
				sadasya_count+=1
				sadasya[s1][0]=colour
				sadasya[s1][1]=j
				s1+=1
	s1=1
	#print("Sadsya count is "+str(sadasya_count))
	if mane!=49:
		if sadasya_count>0:
			if sadasya_count==1:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+23,pos[mane][1]+23))
			elif sadasya_count==2:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+10,pos[mane][1]+25))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+35,pos[mane][1]+25))
			elif sadasya_count==3:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+23,pos[mane][1]+15))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+10,pos[mane][1]+35))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+33,pos[mane][1]+35))
			elif sadasya_count==4:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+10,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+35,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+10,pos[mane][1]+35))
				screen2.blit(colorpos[sadasya[s1+3][0]][11],(pos[mane][0]+35,pos[mane][1]+35))
			elif sadasya_count==5:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+5,pos[mane][1]+5))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+40,pos[mane][1]+5))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+5,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+3][0]][11],(pos[mane][0]+40,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+4][0]][11],(pos[mane][0]+23,pos[mane][1]+23))
			elif sadasya_count==6:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+1,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+23,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+45,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+3][0]][11],(pos[mane][0]+1,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+4][0]][11],(pos[mane][0]+23,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+5][0]][11],(pos[mane][0]+45,pos[mane][1]+40))
			elif sadasya_count==7:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+1,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+23,pos[mane][1]+5))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+45,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+3][0]][11],(pos[mane][0]+1,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+4][0]][11],(pos[mane][0]+23,pos[mane][1]+45))
				screen2.blit(colorpos[sadasya[s1+5][0]][11],(pos[mane][0]+45,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+6][0]][11],(pos[mane][0]+23,pos[mane][1]+25))
			elif sadasya_count==8:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+1,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+21,pos[mane][1]+3))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+41,pos[mane][1]+10))
				screen2.blit(colorpos[sadasya[s1+3][0]][11],(pos[mane][0]+1,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+4][0]][11],(pos[mane][0]+21,pos[mane][1]+48))
				screen2.blit(colorpos[sadasya[s1+5][0]][11],(pos[mane][0]+41,pos[mane][1]+40))
				screen2.blit(colorpos[sadasya[s1+6][0]][11],(pos[mane][0]+31,pos[mane][1]+25))
				screen2.blit(colorpos[sadasya[s1+7][0]][11],(pos[mane][0]+11,pos[mane][1]+25))
			elif sadasya_count==9:
				screen2.blit(colorpos[sadasya[s1][0]][11],(pos[mane][0]+1,pos[mane][1]+2))
				screen2.blit(colorpos[sadasya[s1+1][0]][11],(pos[mane][0]+21,pos[mane][1]+2))
				screen2.blit(colorpos[sadasya[s1+2][0]][11],(pos[mane][0]+41,pos[mane][1]+2))
				screen2.blit(colorpos[sadasya[s1+3][0]][11],(pos[mane][0]+1,pos[mane][1]+25))
				screen2.blit(colorpos[sadasya[s1+4][0]][11],(pos[mane][0]+21,pos[mane][1]+25))
				screen2.blit(colorpos[sadasya[s1+5][0]][11],(pos[mane][0]+41,pos[mane][1]+25))
				screen2.blit(colorpos[sadasya[s1+6][0]][11],(pos[mane][0]+1,pos[mane][1]+48))
				screen2.blit(colorpos[sadasya[s1+7][0]][11],(pos[mane][0]+21,pos[mane][1]+48))
				screen2.blit(colorpos[sadasya[s1+8][0]][11],(pos[mane][0]+41,pos[mane][1]+48))
		else:
			sub11=screen1.subsurface(pygame.Rect(pos[49][0],pos[49][1],67,68))
			screen.blit(sub11,pos[49])

		pygame.display.update()


def jump(i,frompos,topos):
	global isjump,turn,colorpos,pos,path
	vel=6
	neg=1
	x=frompos[0]
	y=frompos[1]
	if frompos[0]<topos[0] and frompos[1]<topos[1]:#down right
		a=4
		b=7
		vel=abs(vel)
	elif frompos[0]<topos[0] and frompos[1]>topos[1]:#up right
		a=7
		b=4
		vel=abs(vel)
	elif frompos[0]>topos[0] and frompos[1]<topos[1]:#down left
		a=4
		b=7
		vel=-vel
	elif frompos[0]>topos[0] and frompos[1]>topos[1]:#up left
		a=7
		b=4
		vel=-vel
	elif frompos[0]==topos[0] and frompos[1]<topos[1]:#down only
		a=4
		b=7
		vel=0
	elif frompos[0]==topos[0] and frompos[1]>topos[1]:#up only
		a=7
		b=4
		vel=0
	elif frompos[0]<topos[0] and frompos[1]==topos[1]:#right only
		a=5
		b=5
		vel=abs(vel)
	elif frompos[0]>topos[0] and frompos[1]==topos[1]:#left only
		a=5
		b=5
		vel=-vel
	jmpcount=a
	if vel!=0 and a!=b:
		Innerloopentersound.play()
	screen1=pygame.image.load('data\\Chaukabara.png')
	for j in range(1,5):
		if j!=turn:
			if colorpos[j][1+4]=='u':
				screen1.blit(colorpos[j][11],(pos[colorpos[j][1]][0]+10+15,pos[colorpos[j][1]][1]+10+15))
			if colorpos[j][2+4]=='u':
				screen1.blit(colorpos[j][11],(pos[colorpos[j][2]][0]+10+30-15,pos[colorpos[j][2]][1]+10+15))
			if colorpos[j][3+4]=='u':	
				screen1.blit(colorpos[j][11],(pos[colorpos[j][3]][0]+10+15,pos[colorpos[j][3]][1]+10+30-15))
			if colorpos[j][4+4]=='u':
				screen1.blit(colorpos[j][11],(pos[colorpos[j][4]][0]+10+30-15,pos[colorpos[j][4]][1]+10+30-15))
			if colorpos[j][1+4]=='s':
				adjustbox(colorpos[j][1],screen1)
			if colorpos[j][2+4]=='s':
				adjustbox(colorpos[j][2],screen1)
			if colorpos[j][3+4]=='s':
				adjustbox(colorpos[j][3],screen1)
			if colorpos[j][4+4]=='s':
				adjustbox(colorpos[j][4],screen1)
				
	sub=screen1.subsurface(pygame.Rect(178,194,487,486))
	screen.blit(sub,(178,194))

	while isjump:
		if jmpcount>=-b:
			neg=1
			if jmpcount<0:
				neg=-1
			y-=(jmpcount**2)*0.6*neg
			x+=vel
			jmpcount-=1
		else:
			isjump=False
			jmpcount=a
		for k in range(1,5):
			if k!=i:
				if colorpos[turn][k+4]=='s':
					adjustbox(colorpos[turn][k],screen)
				else:
					if colorpos[turn][k]!=49:
						screen.blit(colorpos[turn][11],(pos[colorpos[turn][k]][0]+25,pos[colorpos[turn][k]][1]+25)) 						
		win=screen1.subsurface(pygame.Rect(x-vel,y+(((jmpcount+1)**2)*0.6*neg),20,20))
		screen.blit(win,(x-vel,y+(((jmpcount+1)**2)*0.6*neg)))
		screen.blit(colorpos[turn][11],(x,y))
		pygame.display.update()
		pygame.time.delay(20)



def win(turn,i):
	global winorder,token_left,turntoken,colorpos
	large=0
	win_pos=[0,[765,723],[765,115],[30,115],[30,723]]
	crownpos=[0,[743,660],[743,50],[10,50],[10,660]]
	if token_left[turn]==3:
		Tokengoesinsound.play()
		screen.blit(colorpos[turn][11],(win_pos[turn][0],win_pos[turn][1]))
	elif token_left[turn]==2:
		Tokengoesinsound.play()
		screen.blit(colorpos[turn][11],(win_pos[turn][0],win_pos[turn][1]+20))
	elif token_left[turn]==1:
		Tokengoesinsound.play()
		screen.blit(colorpos[turn][11],(win_pos[turn][0]+25,win_pos[turn][1]))
	else:
		oneplayerwinsound.play()
		screen.blit(colorpos[turn][11],(win_pos[turn][0]+25,win_pos[turn][1]+20))
		#the token that wins should not be played with dice throws 
		turntoken[turn]=0
		large=0
		for i in range(1,5):
			if winorder[i]>=large:
				large=winorder[i]
		if large==0:
			winorder[turn]=1
			screen.blit(pygame.image.load('data\\crown.png'),(crownpos[turn][0],crownpos[turn][1]))
		elif large==1:
			winorder[turn]=2
		elif large==2:
			winorder[turn]=3

def move(i,res): 
	global turn,pos,isjump,colorpos,kill,safe,screen1,path,token_box,token_left#make kill true if killed
	vel=5
	m=[[0,0],[0,0],[0,0],[0,0]]
	currentposindex=path[turn].index(colorpos[turn][i])
	nextposindex=currentposindex+1
	count=res-1
	a=8
	b=8
	
	while count>=0:
		isjump=True
		jump(i,(pos[path[turn][currentposindex]][0]+25,pos[path[turn][currentposindex]][1]+25),(pos[path[turn][nextposindex]][0]+25,pos[path[turn][nextposindex]][1]+25))
		colorpos[turn][i]=path[turn][nextposindex]
		token_box = [
			[pygame.Rect(0,0,2,2)],
			[0,[pygame.Rect(pos[colorpos[1][1]][0],pos[colorpos[1][1]][1],67,68)],[pygame.Rect(pos[colorpos[1][2]][0],pos[colorpos[1][2]][1],67,68)],[pygame.Rect(pos[colorpos[1][3]][0],pos[colorpos[1][3]][1],67,68)],[pygame.Rect(pos[colorpos[1][4]][0],pos[colorpos[1][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[2][1]][0],pos[colorpos[2][1]][1],67,68)],[pygame.Rect(pos[colorpos[2][2]][0],pos[colorpos[2][2]][1],67,68)],[pygame.Rect(pos[colorpos[2][3]][0],pos[colorpos[2][3]][1],67,68)],[pygame.Rect(pos[colorpos[2][4]][0],pos[colorpos[2][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[3][1]][0],pos[colorpos[3][1]][1],67,68)],[pygame.Rect(pos[colorpos[3][2]][0],pos[colorpos[3][2]][1],67,68)],[pygame.Rect(pos[colorpos[3][3]][0],pos[colorpos[3][3]][1],67,68)],[pygame.Rect(pos[colorpos[3][4]][0],pos[colorpos[3][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[4][1]][0],pos[colorpos[4][1]][1],67,68)],[pygame.Rect(pos[colorpos[4][2]][0],pos[colorpos[4][2]][1],67,68)],[pygame.Rect(pos[colorpos[4][3]][0],pos[colorpos[4][3]][1],67,68)],[pygame.Rect(pos[colorpos[4][4]][0],pos[colorpos[4][4]][1],67,68)]]
			]
		currentposindex+=1
		nextposindex+=1
		count-=1
		
	if colorpos[turn][i]==49:
		token_left[turn]-=1
		print("tokenleft"+str(token_left))
		sub=screen1.subsurface(token_box[turn][i][0])
		screen.blit(sub,(pos[colorpos[turn][i]][0],pos[colorpos[turn][i]][1]))
		pygame.display.update()
		win(turn,i)#have to make colopos[turn][i]=0 and get that token near that players box

	for j in range(1,5):
		for s in safe:
			if colorpos[j][i]!=s:
				colorpos[j][i+4]='u'
			else:
				colorpos[j][i+4]='s'
				break

	#move agide eega ee mane safe manena? safe mane agidre aa maneli esht jana idare, ashtakke sariyagi display madu
	for j in range(1,5):
		for k in range(1,5):
			if j!=turn and colorpos[turn][i]==colorpos[j][k] and colorpos[turn][i+4]=='u':
				kill=True
				Killsound.play()
				colorpos[j][k]=colorpos[j][12]
				#print("Killed")
				colorpos[j][k+4]='s'
				#he killed now he goes back to his home
				#see how many members are there in his home now and display accordingly
				colorpos[turn][9]+=1
				#update kill count box
	sub11=screen1.subsurface(pygame.Rect(178,194,487,486))
	screen.blit(sub11,(178,194))#('dallali.png')(178,194))
	sub11=screen1.subsurface(pygame.Rect(868,177,216,290))
	screen.blit(sub11,(868,177))
	for j in range(1,5):
			if colorpos[j][1+4]=='u'and colorpos[j][1]!=49:
				screen.blit(colorpos[j][11],(pos[colorpos[j][1]][0]+25,pos[colorpos[j][1]][1]+25))
			if colorpos[j][2+4]=='u'and colorpos[j][2]!=49:
				screen.blit(colorpos[j][11],(pos[colorpos[j][2]][0]+25,pos[colorpos[j][2]][1]+25))
			if colorpos[j][3+4]=='u'and colorpos[j][3]!=49:
				screen.blit(colorpos[j][11],(pos[colorpos[j][3]][0]+25,pos[colorpos[j][3]][1]+25))
			if colorpos[j][4+4]=='u'and colorpos[j][4]!=49:
				screen.blit(colorpos[j][11],(pos[colorpos[j][4]][0]+25,pos[colorpos[j][4]][1]+25))
			if colorpos[j][1+4]=='s'and colorpos[j][1]!=49:
				adjustbox(colorpos[j][1],screen)
			if colorpos[j][2+4]=='s'and colorpos[j][2]!=49:
				adjustbox(colorpos[j][2],screen)
			if colorpos[j][3+4]=='s'and colorpos[j][3]!=49:
				adjustbox(colorpos[j][3],screen)
			if colorpos[j][4+4]=='s'and colorpos[j][4]!=49:
				adjustbox(colorpos[j][4],screen)
	pygame.display.update()
		#kill count box display update
	FONt = pygame.font.SysFont('comicsansms', 35)
	for h in range(1,5):
			text=FONt.render(str(colorpos[h][9]),True,(0,0,0))
			textrect=text.get_rect()
			textrect.center=(910,252+(h-1)*48-h)
			screen.blit(text,textrect)
			pygame.display.update()
	screen.blit(turn_indicator[turn],(972,109))
	pygame.display.update()

	for s in safe:
		adjustbox(s,screen)

	if kill:
		animate_text('Killed',845,500,260,75)
		token_box = [
			[pygame.Rect(0,0,2,2)],
			[0,[pygame.Rect(pos[colorpos[1][1]][0],pos[colorpos[1][1]][1],67,68)],[pygame.Rect(pos[colorpos[1][2]][0],pos[colorpos[1][2]][1],67,68)],[pygame.Rect(pos[colorpos[1][3]][0],pos[colorpos[1][3]][1],67,68)],[pygame.Rect(pos[colorpos[1][4]][0],pos[colorpos[1][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[2][1]][0],pos[colorpos[2][1]][1],67,68)],[pygame.Rect(pos[colorpos[2][2]][0],pos[colorpos[2][2]][1],67,68)],[pygame.Rect(pos[colorpos[2][3]][0],pos[colorpos[2][3]][1],67,68)],[pygame.Rect(pos[colorpos[2][4]][0],pos[colorpos[2][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[3][1]][0],pos[colorpos[3][1]][1],67,68)],[pygame.Rect(pos[colorpos[3][2]][0],pos[colorpos[3][2]][1],67,68)],[pygame.Rect(pos[colorpos[3][3]][0],pos[colorpos[3][3]][1],67,68)],[pygame.Rect(pos[colorpos[3][4]][0],pos[colorpos[3][4]][1],67,68)]],
			[0,[pygame.Rect(pos[colorpos[4][1]][0],pos[colorpos[4][1]][1],67,68)],[pygame.Rect(pos[colorpos[4][2]][0],pos[colorpos[4][2]][1],67,68)],[pygame.Rect(pos[colorpos[4][3]][0],pos[colorpos[4][3]][1],67,68)],[pygame.Rect(pos[colorpos[4][4]][0],pos[colorpos[4][4]][1],67,68)]]
			]



def movetoken(res):
	global run,turn,token_left,MoreThanNeeded,colorpos,pos,path,token_box,quitt_box,start	
	ismoved=False
	MoreThanNeeded=False
	once=False
	cantmove=0
	allinone=True
	tokenwin=[0,0,0,0,0]
	dontmove=False
	for k in range(2,5):
		if colorpos[turn][1]!=colorpos[turn][k] and colorpos[turn][k]!=49:
			allinone=False

	if token_left[turn]==1 or allinone:
		for j in range(1,5):
			if colorpos[turn][j]<49:
				i=j
				break

		if path[turn][path[turn].index(colorpos[turn][i])+res] >= colorpos[turn][10] and colorpos[turn][9]==0:#not kill and pos to get inside
			Nokillyetsound.play()
			animate_text('No Kill Yet',845,500,260,75)
			cantmove+=1
		#see if his dice results more than his required no to win
		elif path[turn][path[turn].index(colorpos[turn][i])+res]==0:
			print("tokenleft if"+str(token_left))
			print(colorpos[turn])
			print(path[turn].index(colorpos[turn][i]))
			Ohhosound.play()
			animate_text('Needed Less !',845,500,260,75)
			cantmove+=1
			morethanneeded=True
			if token_left[turn]==1:
				ismoved = True# his chance goes by
			else:
				for k in range(1,5):
					if path[turn][path[turn].index(colorpos[turn][k])+res]==0:
						ismoved=True
					else:
						ismoved=False
						break

		#see if when moved res positions it does not have another token of the same color and not a safezone
		else:
			for j in range(1,5):
				if i!=j:
					if path[turn][path[turn].index(colorpos[turn][i])+res]==colorpos[turn][j] and colorpos[turn][j+4]=='u':
						dontmove=True
						if not once:
							xJodixsound.play()
							animate_text('No Overlapping',845,500,260,75)
							once=True		
						cantmove+=1	
						break
				
			if not dontmove:
				move(i,res)#i represents which among 4 is to be moved
				ismoved=True

			if cantmove==token_left[turn]:
				ismoved=True

	else:
		while not ismoved and not start:
			tokenwin=[0,0,0,0,0]
			dontmove=False
			i=0
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run=False
					ismoved=True
				elif event.type==pygame.MOUSEBUTTONDOWN:
					if event.type==pygame.MOUSEBUTTONDOWN :
						if quitt_box.collidepoint(event.pos):
							start=True
							turn=1
							break
					for h in range(1,5):
						if colorpos[turn][h]==0:
							tokenwin[h]==1
					for i in range(1,5):
						if tokenwin[i]==0:
							for token in token_box[turn][i]:
								if token.collidepoint(event.pos):							#see if he is in pos to enter inside 
									if path[turn][path[turn].index(colorpos[turn][i])+res] >= colorpos[turn][10] and colorpos[turn][9]==0:#not kill and pos to get inside
										Nokillyetsound.play()
										animate_text('No Kill Yet',845,500,260,75)
										cantmove+=1
									#see if his dice results more than his required no to win
									elif path[turn][path[turn].index(colorpos[turn][i])+res]==0:
										#print(colorpos[turn][i])
										#print(path[turn])
										Ohhosound.play()
										animate_text('Needed Less !',845,500,260,75)
										print(colorpos[turn])
										print(path[turn].index(colorpos[turn][i]))
										cantmove+=1
										morethanneeded=True
										if token_left[turn]==1:
											ismoved = True# his chance goes by
										else:
											for k in range(1,5):
												if path[turn][path[turn].index(colorpos[turn][k])+res]==0:
													ismoved=True
												else:
													ismoved=False
													break

									#see if when moved res positions it does not have another token of the same color and not a safezone
									else:
										for j in range(1,5):
											if i!=j:
												if path[turn][path[turn].index(colorpos[turn][i])+res]==colorpos[turn][j] and colorpos[turn][j+4]=='u':
													dontmove=True	
													if not once:
														xJodixsound.play()
														animate_text('No Overlapping',845,500,260,75)		
														once=True
													cantmove+=1	
													break
										if not dontmove:
											move(i,res)#i represents which among 4 is to be moved
											ismoved=True
											break
									if cantmove==token_left[turn]:
										ismoved=True
										break
								
							if ismoved==True:
								break# if once mousebutton press results in any pos of that colour 
						#print(path[turn].index(colorpos[turn][i])+1)
					#print(colorpos[turn][i])

def rolldice(b):
	global run,start,quitt_box
	global turn,token_box
	while b>0 and run == True and not start :#no. of times dice should roll
		a=0
		while a<=95 and run == True and not start:
			for event in pygame.event.get():
				if event.type ==pygame.MOUSEBUTTONDOWN:
					if quitt_box.collidepoint(event.pos):
						start=True
						turn=1
						break
				if event.type == pygame.QUIT:
					run = False
			a+=1
			die=pygame.image.load('data\\'+str(a)+'.png')
			screen.blit(die,(936,650))
			pygame.display.update()
			pygame.time.delay(8)
		b-=1
	screen.blit(pygame.image.load('data\\res.png'),(936,650))
	res=random.randint(1,6)
	font = pygame.font.SysFont('comicsansms', 50)
	text = font.render(str(res), False, (20,60,90))#,(150,170,250))
	textrect=text.get_rect()
	textrect.center=(977,691)
	screen.blit(text,textrect)
	pygame.display.update()
	movetoken(res)#in this move the red/green/yellow/blue pan to respective positions
	screen.blit(pygame.image.load('data\\res.png'),(936,650))
	pygame.display.update()
	return res


def PlayGame():
	global run,start,turn,winorder,MoreThanNeeded,turn_indicator,kill,quitt_box,turntoken
	dice_box=pygame.Rect(913,636,124,111)
	again=False
	while run and winorder[turn]!=3:
		if turntoken[turn]!=0:
			for event in pygame.event.get():
				roll=False
				if event.type == pygame.QUIT:
					run=False
				elif event.type == pygame.MOUSEBUTTONDOWN and dice_box.collidepoint(event.pos):
						roll=True
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
						roll=True
				if roll:
						screen.blit(turn_indicator[turn],(972,109))
						dicedigit=rolldice(1)
						roll=False
						while (kill==True or dicedigit==6) and run : #should be given another turn if 6 or kills someone
							again=True
							if MoreThanNeeded==True and kill==False:
								pass
							else:
								for event2 in pygame.event.get():
									roll=False
									if event2.type == pygame.QUIT:
										run =False
									if event2.type == pygame.MOUSEBUTTONDOWN and dice_box.collidepoint(event2.pos):
										roll=True
									elif  event2.type == pygame.KEYDOWN and event2.key == pygame.K_RETURN:
										roll=True
									if roll:
										kill=False
										dicedigit=rolldice(1)
										roll=False
						if not kill or dicedigit!=6:
						    again=False
						if not again:
							if winorder[turn]==3:
								start=True
								turn=1
							else:
								turn+=1
								if turn==5:
									turn=1#blue1,yellow2,green3,red4
				elif event.type ==pygame.MOUSEBUTTONDOWN:
					if quitt_box.collidepoint(event.pos):
						start=True
						turn=1
						#run=False
					break

				screen.blit(turn_indicator[turn],(972,109))
			pygame.display.update()
			pygame.time.delay(20)
			if start:
				break
		else:
			turn+=1
			if turn==5:
				turn=1

while run:
	if start:
		game_init()	
		start=False
		gamepage1()
		if run:
			allthebest()
		if run:
			DispPlayerName()
			PlayGame()
	pygame.time.delay(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		else:

			PlayGame()
	pygame.display.update()
pygame.quit()