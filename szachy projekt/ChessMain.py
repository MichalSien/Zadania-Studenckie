import ChessEngine #załadowane pakiety
import pygame as p
import math
import random
import sys  

import mysql.connector
from mysql.connector import errorcode
import time




WIDTH = HEIGHT = 512 #określa długość i szerokość okna
dim = 8 #określa ilość kwadratów na planszy (dim*dim)
sqsize = HEIGHT // dim #określa wielkość jednego kwadrata
images = {} 

def loadImages():
    pieces = ["wP","wR","wN","wB","wQ","wK","bP","bR","bN","bB","bQ","bK"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece +".png"),(sqsize,sqsize))
#(sqsize,sqsize) określa jakiej wielkości ma być grafika
#p.transform.scale - pozwala na zmiane rozmiaru do nowej rozdzielczości
        
def main():
    p.init() #inicjalizuje/wczytanie modułu pygame
    screen = p.display.set_mode((WIDTH,HEIGHT))
    gs = ChessEngine.GameState() #wczytujemy klase GameState, która jest odpowiedzialna za logike programu
    validMoves = gs.get_valid_moves()
    moveMade = False #sprawdzenie czy został wykonany ruch
    loadImages()
    running = True
    uuu=[] #tablica odczytywana w bazie
    yyy=0
    sqSelected = () #resetuje wszystkie wcześniejsze ruchy gracza
    playerClicks = []
    while running: #1. reaguje na naciśnięcie, 2. odświerza grafike w zależności od ruchu, 3. sprawdza stan gry, czy jest remis, szach mat - i tak w pętli
        for e in p.event.get():
            if e.type == p.QUIT: #kiedy naciśniemy x, program się wyłączy
                print("Koniec gry")
                running = False
                
            elif e.type == p.MOUSEBUTTONDOWN: #jeśli naciśniemy myszke
                location = p.mouse.get_pos() #pozycja na ekranie która została naciśnięta przez myszke
                col = location[0]//sqsize #dzieli oś na 8 części, dzięki temu program wie, który kwadrat został naciśnięty
                row = location[1]//sqsize
                if sqSelected == (row,col): #jeśli drugi raz, naciśniemy na to same miejsce na planszy, naciśnięcie się resetuje
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row,col) #jeśli naciśniemy na jakąś figure to zostanie ona zapamiętana
                    playerClicks.append(sqSelected)
                    
                if len(playerClicks) == 2: #jeśli gracz kliknie drugi raz
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1], gs.board)
                    for i in range(len(validMoves)):
                        if move == validMoves[i]: #jeśli ruch jest możliwy do wykonania
                            gs.makeMove(validMoves[i])
                            moveMade = True #dzięki temu można przejść do "if moveMade", w którym wyświetla ruchy w konsoli
                            sqSelected = () #po wykonaniu ruchu te tablice się resetuje
                            playerClicks = []
                    if not moveMade: #jeśli ruch nie zostaje wykonany to figura jest nadal zaznaczona
                        playerClicks = [sqSelected]
                
    
        drawGameState(screen, gs) #rysuje grafike
        p.display.flip() #komenda odpowiedzialna za aktualizacje ekranu gry
                    
        if moveMade: #kiedy dochodzi do ruchu
            
            print(move.get_chess_not()) #wyświetla ruch w szachach (np. a2a4, g8f6)
            yyy=yyy+1
            kkk = [((yyy), move.get_chess_not())] #tworzy tablice, którą będzie odczytywać nasza baza
            uuu=uuu+kkk
            main.abc=uuu
            
            validMoves = gs.get_valid_moves()
            moveMade = False
            move_made = False
        if gs.check_mate:
            print("Czarni wygrywają") if gs.white_to_move else print("Biali wygrywają")
            running = False #nie można się już ruszać
        
        if gs.stale_mate: #w sytuacji gdy będzie mat, pojawia się napis remis
            print("Remis")
            running = False #nie można się już ruszać
            
def main2():
    p.init() #inicjalizuje/wczytanie modułu pygame
    screen = p.display.set_mode((WIDTH,HEIGHT))
    gs = ChessEngine.GameState2()
    validMoves = gs.get_valid_moves()
    moveMade = False
    loadImages()
    running = True
    
    sqSelected = ()
    playerClicks = []
    while running: #1. reaguje na naciśnięcie, 2. odświerza grafike w zależności od ruchu, 3. sprawdza stan gry, czy jest remis, szach mat - i tak w pętli
        for e in p.event.get():
            if e.type == p.QUIT: #kiedy naciśniemy x, program się wyłączy
                print("Koniec gry")
                running = False
                
            elif e.type == p.MOUSEBUTTONDOWN: #jeśli naciśniemy myszke
                location = p.mouse.get_pos() #pozycja na ekranie która została naciśnięta przez myszke
                col = location[0]//sqsize #dzieli oś na 8 części, dzięki temu program wie, który kwadrat został naciśnięty
                row = location[1]//sqsize
                if sqSelected == (row,col): #jeśli drugi raz, naciśniemy na to same miejsce na planszy, naciśnięcie się resetuje
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                    
                if len(playerClicks) == 2: #jeśli gracz kliknie drugi raz
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1], gs.board)
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(validMoves[i])
                            moveMade = True
                            sqSelected = ()
                            playerClicks = []
                    if not moveMade:
                        playerClicks = [sqSelected]
                
    
        drawGameState(screen, gs) #rysuje grafike
        p.display.flip() #komenda odpowiedzialna za aktualizacje ekranu gry
                    
        if moveMade: #kiedy dochodzi do ruchu
            print(move.get_chess_not()) #wyświetla ruch w szachach (np. a2a4, g8f6)
            validMoves = gs.get_valid_moves()
            moveMade = False
            move_made = False
        if gs.check_mate:
            print("Czarni wygrywają") if gs.white_to_move else print("Biali wygrywają")
            running = False #nie można się już ruszać
        
        if gs.stale_mate: #w sytuacji gdy będzie mat, pojawia się napis remis
            print("Remis")
            running = False #nie można się już ruszać
  

def main3():
    p.init() #inicjalizuje/wczytanie modułu pygame
    screen = p.display.set_mode((WIDTH,HEIGHT))
    gs = ChessEngine.GameState3()
    validMoves = gs.get_valid_moves()
    moveMade = False
    loadImages()
    running = True
    
    sqSelected = ()
    playerClicks = []
    while running: #1. reaguje na naciśnięcie, 2. odświerza grafike w zależności od ruchu, 3. sprawdza stan gry, czy jest remis, szach mat - i tak w pętli
        for e in p.event.get():
            if e.type == p.QUIT: #kiedy naciśniemy x, program się wyłączy
                print("Koniec gry")
                running = False
                
            elif e.type == p.MOUSEBUTTONDOWN: #jeśli naciśniemy myszke
                location = p.mouse.get_pos() #pozycja na ekranie która została naciśnięta przez myszke
                col = location[0]//sqsize #dzieli oś na 8 części, dzięki temu program wie, który kwadrat został naciśnięty
                row = location[1]//sqsize
                if sqSelected == (row,col): #jeśli drugi raz, naciśniemy na to same miejsce na planszy, naciśnięcie się resetuje
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                    
                if len(playerClicks) == 2: #jeśli gracz kliknie drugi raz
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1], gs.board)
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(validMoves[i])
                            moveMade = True
                            sqSelected = ()
                            playerClicks = []
                    if not moveMade:
                        playerClicks = [sqSelected]
                
    
        drawGameState(screen, gs) #rysuje grafike
        p.display.flip() #komenda odpowiedzialna za aktualizacje ekranu gry
                    
        if moveMade: #kiedy dochodzi do ruchu
            print(move.get_chess_not()) #wyświetla ruch w szachach (np. a2a4, g8f6)
            validMoves = gs.get_valid_moves()
            moveMade = False
            move_made = False
        if gs.check_mate:
            print("Czarni wygrywają") if gs.white_to_move else print("Biali wygrywają")
            running = False #nie można się już ruszać
        
        if gs.stale_mate: #w sytuacji gdy będzie mat, pojawia się napis remis
            print("Remis")
            running = False #nie można się już ruszać  

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)
    

def drawBoard(screen): #narysowanie planszy
    colours = [p.Color("white"),p.Color("pink")] #określam jakie mają być kolory (colours[0]- biały, colours[1]-różowy)
    for r in range(dim):
        for c in range(dim):
            colour = colours[((r + c) % 2)] #dodaje do siebie wartości na osi, i dziele przez 2, co daje mi reszte którą jest albo 0 (biały), albo 1 (różowy)
            p.draw.rect(screen, colour, p.Rect(c*sqsize, r*sqsize, sqsize, sqsize))
            
            

def drawPieces(screen,board): #narysowanie pionków
    for r in range(dim):
        for c in range(dim):
            piece = board[r][c] #r i c to są osie na planszy
            if piece != "--": #rysuje pionka kiedy pole nie jest oznaczone jako "--", co oznacza puste pole na środku szachownicy
                screen.blit(images[piece], p.Rect(c*sqsize, r*sqsize, sqsize, sqsize))


def baza(main):
   import mysql.connector
   mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
   mycursor=mydb.cursor()
   mycursor.execute("create database baza")

   mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="baza")
   mycursor=mydb.cursor()
   mycursor.execute("create table szachy(numer varchar(250),ruch varchar(250))") #tworzy tabele

   sqlformula = "Insert into szachy(numer,ruch) values(%s,%s)"#dodaje kolumny do tabeli
   szachy = main.abc #main.abc to wartości, które będą w tabeli
   mycursor.executemany(sqlformula, szachy)#przekazuje dane
   mydb.commit()#instrukcja SQL używana do zapisania zmian


def generuj_pdf(main):
    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    dane=str(main.abc) #wczytuje dane, które zapiszemy w pliu pdf

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillColorRGB(1, 0, 0) #wybieramy kolor
    can.setFont("Times-Roman", 14) #wybieramy czcionke i rozmiar czcionki
    can.drawString(72, 655, dane)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    existing_pdf = PdfFileReader(open('/Python/Python38-32/szachy projekt/pdf/file.pdf', "rb")) #wczytuje plik pdf
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    outputStream = open('/Python/Python38-32/szachy projekt/pdf/file.pdf', 'wb') #zapisuje zmiany w tym pliku
    output.write(outputStream)
    outputStream.close()
    print("dane zostały zapisane w pliku pdf")   

#-----------------------------------------------------------------------------------------------------------


#inicjalizuje/wczytanie modułu pygame  
p.init()  
  
#określa rozdzielczość ekranu
res = (512,512)  
  
#wyświetlanie okna gry
screen = p.display.set_mode(res)  
  
#definiuje kolory 
color = (255,255,255)  
color_light = (170,170,170)   
color_dark = (100,100,100)  
  
#skracam definicje wysokości i szerokości, będziemy tego używać żeby określić miejsce w którym będą przyciski
width = screen.get_width()
height = screen.get_height()  
  
#definiujemy czcionke
font = p.font.SysFont('Corbel',35)
smallfont = p.font.SysFont('Corbel',30)
verysmallfont = p.font.SysFont('Corbel',27)
  
#definiuje tekst, który będzie na przyciskach
text  = font.render('wyjście' , True , color)
text1 = font.render('nowa gra' , True , color) 
text2 = smallfont.render('losowa gra' , True , color)
text3 = verysmallfont.render('baza danych' , True , color)
text4 = verysmallfont.render('generuj pdf' , True , color)
text5 = verysmallfont.render('krótki ruch' , True , color)

while True:  
    for ev in p.event.get():  
        if ev.type == p.QUIT:  
            p.quit()  
              
        #sprawdza czy kliknięto myszą
        if ev.type == p.MOUSEBUTTONDOWN:  
              
            #jeśli ten przycisk zostanie naciśnięty baza zostanie stworzona
            if width/2-70 <= mouse[0] <= width/2+70 and height/1.65 <= mouse[1] <= height/1.65+40:  
                baza(main)
            #jeśli ten przycisk zostanie naciśnięty, załuduje się nowa gra (gra losowa)
            if width/2-70 <= mouse[0] <= width/2+70 and height/3 <= mouse[1] <= height/3+40:  
                main2()
                
            if width/2-70 <= mouse[0] <= width/2+70 and height/1.38 <= mouse[1] <= height/1.38+40:
                generuj_pdf(main)
            #jeśli ten przycisk zostanie naciśnięty gra zostanie wyłączona
            if width/2-70 <= mouse[0] <= width/2+70 and height/1.18 <= mouse[1] <= height/1.18+40:               
                p.quit()
            #jeśli ten przycisk zostanie naciśnięty, załuduje się nowa gra (gra klasyczna)
            if width/2-70 <= mouse[0] <= width/2+70 and height/5.5 <= mouse[1] <= height/5.5+40:                
                main()

            if width/2-70 <= mouse[0] <= width/2+70 and height/2.15 <= mouse[1] <= height/2.15+40:                
                main3()                
                 
    # wypełnia ekran kolorem
    screen.fill((60,25,60))  
      
    # przechowuje współrzędne (x, y) do zmiennej jako krotkę
    mouse = p.mouse.get_pos()  
    
    # jeśli mysz będzie nad przyciskiem, to przycisk zmieni kolor na jaśniejszy
    if width/2-70 <= mouse[0] <= width/2+70 and height/1.65 <= mouse[1] <= height/1.65+40:  
        p.draw.rect(screen,color_light,[width/2-70,height/1.65,140,40])  
          
    else:  
        p.draw.rect(screen,color_dark,[width/2-70,height/1.65,140,40])


    if width/2-70 <= mouse[0] <= width/2+70 and height/3 <= mouse[1] <= height/3+40:  
        p.draw.rect(screen,color_light,[width/2-70,height/3,140,40])  
          
    else:  
        p.draw.rect(screen,color_dark,[width/2-70,height/3,140,40])

    if width/2-70 <= mouse[0] <= width/2+70 and height/1.38 <= mouse[1] <= height/1.38+40:  
        p.draw.rect(screen,color_light,[width/2-70,height/1.38,140,40])  
          
    else:  
        p.draw.rect(screen,color_dark,[width/2-70,height/1.38,140,40])

    if width/2-70 <= mouse[0] <= width/2+70 and height/1.18 <= mouse[1] <= height/1.18+40:  
        p.draw.rect(screen,color_light,[width/2-70,height/1.18,140,40])  
          
    else:  
        p.draw.rect(screen,color_dark,[width/2-70,height/1.18,140,40]) 
        
    if width/2-70 <= mouse[0] <= width/2+70 and height/5.5 <= mouse[1] <= height/5.5+40:  
        p.draw.rect(screen,color_light,[width/2-70,height/5.5,140,40])  
          
    else:  
        p.draw.rect(screen,color_dark,[width/2-70,height/5.5,140,40])

    if width/2-70 <= mouse[0] <= width/2+70 and height/2.15 <= mouse[1] <= height/2.15+40:  
        p.draw.rect(screen,color_light,[width/2-70,height/2.15,140,40])  
          
    else:  
        p.draw.rect(screen,color_dark,[width/2-70,height/2.15,140,40])
      
    # nałożenie tekstu na przycisk
    screen.blit(text1 , (width/2-62,height/5.5))
    screen.blit(text2 , (width/2-60,height/3+4)) 
    screen.blit(text3 , (width/2-66,height/1.65+6))      
    screen.blit(text4, (width/2-62,height/1.38+5)) 
    screen.blit(text , (width/2-48,height/1.18))
    screen.blit(text5 , (width/2-57,height/2.15+6))
    
    # uaktualnia klatki gry
    p.display.update()  


#dzięki temu kodowi program normalnie się zamyka:
from sys import exit
while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                exit()
