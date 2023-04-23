from pygame import *
from random import *
from math import *
from tkinter import *                
from tkinter import filedialog

#WELCOME TO MY PAINT PROJECT, my theme is NieR:Automata Become Like God's, its a good game go check it out :)
#everything you see was made by me because I am extra, enjoy :0

#-------------------------------------------MUSIC-----------------------------------------------

pos=0 # changes the song
init() #Initialies the music
songs=["songs/NieR Automata - The Tower.mp3","songs/NieR Automata - Amusement Park.mp3",
       "songs/NieR Automata - City Ruins.mp3","songs/NieR Automata - blissful death.mp3",
       "songs/NieR Automata - Memories of Dust.mp3"] #List for all the songs
mixer.music.load(songs[pos]) # loads the song
mixer.music.play() # plays the song
volume=mixer.music.get_volume() # gets the original volume of the song
#-----------------------------------------------------------------------------------------------------


root = Tk() # Installes Tk engine
root.withdraw() # hides that window that appears after the program closes  

screen = display.set_mode((1530,900)) #canvas is displayed
display.set_caption("NieR: Automata") #When program is running, instead of "pygame window" its "NieR: Automata
#giving each tool its own square
#                            location   size
canvasRect = Rect(500,100,900,600) #make a rect for the canvas
pencilRect = Rect(1440,65,55,50) #make a rect for the pencil tool
markerRect = Rect(1440,125,55,50) #make a rect for the marker tool
eraserRect = Rect(1440,185,55,50) #make a rect for the eraser tool
lineRect = Rect(1440,245,55,50) #make a rect for the line tool
squareRect = Rect(1440,305,55,50) #make a rect for the square tool
fillsquare = Rect(1440,365,55,50) #make a rect for the fill square tool
elipseRect = Rect(1440,425 ,55,50) #make a rect for the ellipse tool
fillelipseRect = Rect(1440,485,55,50) #make a rect for the fill ellipse tool
sprayRect=Rect(1440,545,55,50) #make a rect for the spray tool

clearRect =Rect(1440,610,55,50) #make a rect for the clear tool
colorRect=Rect(930,755,423,101) #make a rect for the color tool
extraRect = Rect(930,755,423,101) #make an extra rect for the color tool

twoBRect = Rect(20,414,130,130) #make a rect for the sticker
nineSRect = Rect(165,417,130,130) #make a rect for the sticker
twoARect = Rect(310,417,130,130) #make a rect for the sticker
first_PodRect = Rect(20,560,130,180) #make a rect for the sticker
second_PodRect = Rect(170,560,130,180) #make a rect for the sticker
Emil_MaskRect = Rect(310,580,130,140) #make a rect for the sticker
ShuffleRect = Rect(184,350,75,50) #make a rect for the sticker
BackRect = Rect(115,351,64,47) #make a rect for the sticker
NextRect = Rect(265,351,64,47) #make a rect for the sticker
UnPauseRect = Rect(338,351,56,47) #make a rect for the sticker
PauseRect = Rect(49,351,56,47) #make a rect for the sticker


LoadRect=Rect(710,760,180,40) #make a rect for the load button
SaveRect=Rect(710,810,180,40) #make a rect for the save button
UndoRect=Rect(520,760,180,40) #make a rect for the unfo button
RedoRect=Rect(520,810,180,40) #make a rect for the save button


#----------------------------------------------BG--------------------------------------------------

background = image.load("images/nier-automata.png") #importing the image
screen.blit(background,(0,0)) #insert the image when running

#------------------------------------------STICKER--------------------------------------------

twoB = image.load("images/2b.png") #importing the image, will not show until 'screen.blit' is added later on
nineS = image.load("images/9s.png") #importing the image, will not show until 'screen.blit' is added later on
twoA = image.load("images/2a.png") #importing the image, will not show until 'screen.blit' is added later on
first_Pod = image.load("images/2b_pod.png") #importing the image, will not show until 'screen.blit' is added later on
second_Pod = image.load("images/9s_pod.png") #importing the image, will not show until 'screen.blit' is added later on
Emil_Mask = image.load("images/emil mask.png") #importing the image, will not show until 'screen.blit' is added later on

text2 = image.load("images/text_2.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text3 = image.load("images/text_3.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text4 = image.load("images/text_4.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text5 = image.load("images/text_5.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text6 = image.load("images/text_6.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text7 = image.load("images/text_7.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text8 = image.load("images/text_8.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools
text9 = image.load("images/text_9.png") #importing the image, will not show until 'screen.blit' is added later on, descriptions for the tools

#----------------------------------------------------------------------------------------------------

myClock = time.Clock() #track the amount of time
color= (0,0,0) #black is the defult color
size = 1 # 1 is the defult size
mx,my = (0,0) #starting points

tool = " " #the program will not have a tool selected when it's open
drawn = False #dont loop
running =True #loop

undoList = [screen.subsurface(canvasRect).copy()] #subsurface creates a new surface for the undo, considered a child of the original
redoList = [] #will take the information from the undo when the undo button is used
while running:
    click = False #dont loop
    for e in event.get(): #get events from the queue
        if e.type == QUIT:
            running = False #dont loop
            
        if e.type == MOUSEBUTTONDOWN: #when the mouse press down 
            keys = key.get_pressed() #when the up or down button is pressed
            copy = screen.copy() #Screenshot
            sx,sy = mouse.get_pos() #Starting position
            startx,starty = e.pos
            click = True #loop
            if e.button == 1:
                click = True #loop
            
        if e.type == MOUSEBUTTONUP: #when the mouse lets go 
            ucopy = screen.subsurface(canvasRect).copy() # copies the surface of the canvas
            
            if drawn:
                drawn = False #dont loop
                redoList = [] #empty, until information from undo is added into here
                undoList.append(ucopy)

    keys = key.get_pressed() #stolen and modified from keyboard.py
    if keys[K_UP]: #when the up button is pressed, the size increases
        size += 1 #increase by 1
    if keys[K_DOWN]: #when the button is pressed, the size decreases
        size -= 1 #decrease by 1 
    if size<=1: #if the size is less or equil to 1, it will stay at 1
        size=1
    if size>20: #if the size is more or equil to 20, it will stay at 20
        size=20

    if mixer.music.get_busy()==False: #if the music doesn't play
        pos+=1 #increases the position 
        if pos>4: #see if  position is greater than 4 
            pos=1 #then it will becomes 1
        mixer.music.load(songs[pos]) #load music
        mixer.music.play() #plays it

#----------------------------------------------------------------------------------------------------

# the icons are displayed

    draw.rect(screen,(255,255,255),pencilRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),eraserRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),markerRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),lineRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),squareRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),fillsquare,2) #display the rectangle 
    draw.rect(screen,(255,255,255),clearRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),elipseRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),fillelipseRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),sprayRect,2)

    draw.rect(screen,(255,255,255),extraRect,2) #display the rectangle     
    draw.rect(screen,(255,255,255),UndoRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),RedoRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),LoadRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),SaveRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),ShuffleRect,2) #display the rectangle
    draw.rect(screen,(255,255,255),BackRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),NextRect,2) #display the rectangle
    draw.rect(screen,(255,255,255),UnPauseRect,2) #display the rectangle 
    draw.rect(screen,(255,255,255),PauseRect,2) #display the rectangle 



    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    mods = key.get_mods()

#----------------------------------------------------------------------------------------------------

    if mb[0]==1 and colorRect.collidepoint(mx,my):
        color = screen.get_at((mx,my))#the color choice is limited to one spesific area so when you draw it wont change the color
        
    elif mb[0] == 1 and pencilRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),pencilRect,2)  #the color of the square/rectangle will change
        tool = "pencil"
        screen.blit(text2,(33,754))
        
    elif mb[0] == 1 and eraserRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),eraserRect,2)  #the color of the square/rectangle will change
        tool = "eraser"
        screen.blit(text4,(33,754))

        
    elif mb[0] == 1 and markerRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),markerRect,2)  #the color of the square/rectangle will change
        tool = "marker"
        screen.blit(text3,(33,754))

    elif mb[0] == 1 and lineRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),lineRect,2)  #the color of the square/rectangle will change
        tool = "line"
        screen.blit(text5,(33,754))

    elif mb[0] == 1 and squareRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),squareRect,2)  #the color of the square/rectangle will change
        tool = "square"
        screen.blit(text6,(33,754))
        
    elif mb[0] == 1 and fillsquare.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),fillsquare,2)  #the color of the square/rectangle will change
        tool = "fillsquare"
        screen.blit(text6,(33,754))
        
    elif mb[0] == 1 and clearRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),clearRect,2)  #the color of the square/rectangle will change
        tool = "clearRect"
        screen.blit(text9,(33,754))

    elif mb[0] == 1 and elipseRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),elipseRect,2)  #the color of the square/rectangle will change
        tool = "elipseRect"
        screen.blit(text7,(33,754))

    elif mb[0] == 1 and fillelipseRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),fillelipseRect,2)  #the color of the square/rectangle will change
        tool = "fillelipseRect"
        screen.blit(text7,(33,754))

    elif mb[0] == 1 and sprayRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),sprayRect,2)  #the color of the square/rectangle will change
        tool = "sprayRect"
        screen.blit(text8,(33,754))
        
    elif mb[0] == 1 and twoBRect.collidepoint(mx,my): #instead of tools, its the stamps. 
        tool = "twoB" #first sticker 

    elif mb[0] == 1 and nineSRect.collidepoint(mx,my): #when the mouse presses the sticker it changes to that tool
        tool = "nineS" #second sticker
        
    elif mb[0] == 1 and twoARect.collidepoint(mx,my): #when the mouse presses the sticker it changes to that tool
        tool = "twoA" #third sticker

    elif mb[0] == 1 and first_PodRect.collidepoint(mx,my): #when the mouse presses the sticker it changes to that tool
        tool = "first_Pod" #fourth sticker

    elif mb[0] == 1 and second_PodRect.collidepoint(mx,my): #when the mouse presses the sticker it changes to that tool
        tool = "second_Pod" #fifth sticker
        
    elif mb[0] == 1 and Emil_MaskRect.collidepoint(mx,my): #when the mouse presses the sticker it changes to that tool
        tool = "Emil_Mask" #sisxth sticker

    elif mb[0] == 1 and click and NextRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),NextRect,2)  #the color of the square/rectangle will change
        tool = "Next"
        pos+=1 #changes the song, plays the next
        if pos>4: 
            pos=1
        mixer.music.load(songs[pos]) # loads the song 
        mixer.music.play() #plays the song

    elif mb[0] == 1 and click and BackRect.collidepoint(mx,my): 
        draw.rect(screen,(220,200,221),BackRect,2)  
        tool = "Back"
        pos-=1 #changes the song and plays the previous song
        if pos<1:
            pos=4
        mixer.music.load(songs[pos]) 
        mixer.music.play() 

    elif mb[0] == 1 and click and UnPauseRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),UnPauseRect,2)  #the color of the square/rectangle will change
        tool = "UnPause"
        mixer.music.unpause() #unpause the song

    elif mb[0] == 1 and click and PauseRect.collidepoint(mx,my): #when the mouse is pressed to a sepsific area it will change to the tool selected for that area
        draw.rect(screen,(220,200,221),PauseRect,2)  #the color of the square/rectangle will change
        tool = "Pause"
        mixer.music.pause() #pause the song

    elif mb[0] == 1 and click and ShuffleRect.collidepoint(mx,my):
        draw.rect(screen,(220,200,221),ShuffleRect,2)  #the color of the square/rectangle will change
        tool="Shuffle"
        shuffle(songs) #plays a random song
        mixer.music.load(songs[pos]) # loads the song
        mixer.music.play() #plays the song
#----------------------------------------------------------------------------------------------------

    elif click and UndoRect.collidepoint(mx,my): #checking if the mouse clicks the undo 
        if len(undoList) > 1: #checking that the length of the undo list is greater than 1
            c = undoList.pop() #Removed the last action made on the canvas
            screen.blit(undoList[(-1)], canvasRect)
            redoList.append(c) #information is given to the redo list
                
    elif click and RedoRect.collidepoint(mx,my):#checking if the mouse clicks the redo
        if len(redoList) > 0: 
            c = redoList.pop() #the redo takes information from the undo and uses that to bring back instead of removing
            screen.blit(c, canvasRect)
            undoList.append(c)#information is given to the undo list
        
    elif click and LoadRect.collidepoint(mx,my): #checking if the mouse clicks the save
        try:
            screen.set_clip(canvasRect) #whatever is loaded stays in the canvas only
            result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])#a window appears to load your file
            file=image.load(result)#sets the file variable to be the image you want to load
            file=transform.scale(file,(600,300))
            screen.blit(file,(765,300))#displays the loaded file onto the canvas
        except:
            pass;

    elif click and SaveRect.collidepoint(mx,my): #checking if the mouse clicks the save
        try:
            result = filedialog.asksaveasfilename(filetypes = [("Picture files", "*.png;*.jpg;*.BMP")])#a window appears to save your file, include file type
            sav = screen.subsurface(canvasRect) #saves the canvas only
            if result != " ": #if the result isnt blank 
                image.save(sav,result)#save the image done on canvas
        except:
            pass;
            
#----------------------------------------------------------------------------------------------------

    draw.rect(screen, color, (1445,800,50,50) ) #display the current color in use

    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)#all the action below will only be limited to the canvas, nothing can get out
        drawn = True #the code considers clicking false and drawing true
        
        if tool == 'pencil': #if you press the tool 'pencil'
            disk = hypot(mx-omx,my-omy)#connects the first circle to the next one, by filling up the space
            disk= max(1,disk)
            for i in range(int(disk+1)):
                sx= int(i*(mx-omx)/disk)
                sy=int(i*(my-omy)/disk)
                draw.line(screen,(color),(omx,omy),(mx,my),size)

                
        elif tool == 'marker': #if you press the tool 'marker'
            disk = hypot(mx-omx,my-omy)#connects the first circle to the next one, by filling up the space
            disk= max(1,disk)
            for i in range(int(disk+1)):
                sx= int(i*(mx-omx)/disk)
                sy=int(i*(my-omy)/disk)
                draw.circle(screen,(color),(omx+sx,omy+sy),size)

        elif tool == 'eraser': #if you press the tool 'eraser'
            disk = hypot(mx-omx,my-omy) #connects the first circle to the next one, by filling up the space
            disk= max(1,disk)
            for i in range(int(disk+1)):
                sx= int(i*(mx-omx)/disk)
                sy=int(i*(my-omy)/disk)
                draw.circle(screen,(255,255,255),(omx+sx,omy+sy),size)
                
        elif tool == 'line': #if you press the tool 'line'
            screen.blit(copy,(0,0)) #displays the line
            draw.line(screen,(color),(startx,starty),(mx,my),size) #the line takes information from where you first click, startx and starty, to where you will let go 
            
        elif tool == 'square': #if you press the tool 'square'
            screen.blit(copy,(0,0)) #displays the square
            rect = Rect(startx,starty,mx-startx,my-starty)
            rect.normalize()
            draw.rect(screen,(color),rect,size)#when a size is given, the tool will not be filled
            
        elif tool == 'fillsquare': #if you press the tool 'fill square'
            screen.blit(copy,(0,0)) #displays the full square
            rect = Rect(startx,starty,mx-startx,my-starty)
            rect.normalize()
            draw.rect(screen,(color),rect)#when a size isnt spesified, the tool will be filles
            
        elif tool == 'clearRect': #if you press the tool 'clear rect'
            draw.rect(screen,(255,255,255),(500,100,900,600)) #clears the canvas by adding white

        elif tool == 'elipseRect': #if you press the tool 'ellipse'
            try:
                if mb[0]==1:
                    screen.blit(copy,(0,0)) #displays the ellipse
                    rect = Rect(startx,starty,mx-startx,my-starty)
                    rect.normalize()
                    if rect.width > 40 and rect.height> 40:
                        sirc = Surface((rect.width,rect.height),SRCALPHA) #SRCALPHA is the pixel format, includes per-pixel alpha
                        draw.ellipse(sirc,(color),(0,0,rect.width,rect.height),size)
                        screen.blit(sirc,(rect.x,rect.y))
            except: #if it doesnt work
                pass #then don't work it, let it pass so the program wont crash

        elif tool == 'fillelipseRect': #if you press the tool 'filled ellipse'
            screen.blit(copy,(0,0))  #displays the full ellipse
            rect = Rect(startx,starty,mx-startx,my-starty)
            rect.normalize()
            draw.ellipse(screen,(color),rect) #draw ellipse
            

        elif tool == 'sprayRect': #if you press the tool 'spray'
          for x in range(10): #This fills the area that you press
              randX=randint(mx-30,mx+20) #randint randomizes the circles
              randY=randint(my-30,my+20)
              dx=abs(sqrt((randX-mx)**2+(randY-my)**2))
              if dx<20: #see if the dots are drawn within the radius
                  draw.line(screen,color,(randX,randY),(randX,randY),1)

        elif tool == 'twoB': #if you press the first sticker
            if mb[0]==1:
                screen.blit(twoB,(mx-95,my-100)) #display sticker, and fix mouse location 
                
        elif tool == 'nineS': #if you press the second sticker
            if mb[0]==1:
                screen.blit(nineS,(mx-95,my-100)) #display sticker, and fix mouse location 
                
        elif tool == 'twoA': #if you press the third sticker
            if mb[0]==1:
                screen.blit(twoA,(mx-95,my-100)) #display sticker, and fix mouse location 

        elif tool == 'first_Pod':  #if you press the fourth sticker
            if mb[0]==1:
                screen.blit(first_Pod,(mx-80,my-100)) #display sticker, and fix mouse location 

        elif tool == 'second_Pod':  #if you press the fifth sticker
            if mb[0]==1:
                screen.blit(second_Pod,(mx-80,my-100)) #display sticker, and fix mouse location 
                
        elif tool == 'Emil_Mask':  #if you press the sixth sticker
            if mb[0]==1:
                screen.blit(Emil_Mask,(mx-80,my-80)) #display sticker, and fix mouse location 
                
        screen.set_clip(None)
    omx,omy= mx,my
#----------------------------------------------------------------------------------------------------

    display.flip()
    myClock.tick(60) #the program will never run at more than 60 FPS.

quit()
