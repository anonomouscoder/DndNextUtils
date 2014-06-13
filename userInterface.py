import characterGenerator,pygame,drawUtils,time
from drawUtils import *


#bascially anything that the user may click on and have an effect
class Clickable():
   def __init__(self,text,boundaries=(0,0,0,0)):
      self.text = text
      self.boundaries = boundaries
      self.focused = False
   def isWithinBoundaries(self,x,y):
      (boundaryx,boundaryy,lenx,leny) = self.boundaries
      if x > boundaryx and x < boundaryx + lenx and y > boundaryy and y < boundaryy + leny:
         return True
      return False
   def display(self):
      (x,y,l,h) = self.boundaries
      if self.focused:
         color = WHITE
      else:
         color = GREY
      pygame.draw.rect(MAINWINDOW, color,  self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))
class Label(Clickable):
   def display(self):
      (x,y,l,h) = self.boundaries
      pygame.draw.rect(MAINWINDOW, WHITE,  self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))
class TextBox(Clickable):
   def __init__(self,text="",boundaries=(0,0,0,0)):
      Clickable.__init__(text,boundaries)
#Add a bunch of clickables to a Tab
class Tab():
   def __init__(self):
      self.header = ""
      self.listOfClickables = []
      self.focused = False
   def display(self):
      for i in self.listOfClickables:
         i.display()
      
class creationWindow():
   def __init__(self):
      self.buffer = ""
      self.listOfTabs = []    
   def menuKeyboardDown(self,char):
      for tab in self.listOfTabs:
         if tab.header.focused == True:
            for clickable in tab.listOfClickables:
               if isinstance(clickable, TextBox):
                  clickable.text = clickable.text + char
   def menuMouseClickedLogic(self,mousex,mousey):
      for tab in self.listOfTabs:
         if tab.header.isWithinBoundaries(mousex,mousey):
            for otherTabs in self.listOfTabs:
               otherTabs.header.focused = False
            tab.header.focused = True
         if tab.header.focused == True:
            for clickable in tab.listOfClickables:
               if clickable.isWithinBoundaries(mousex,mousey):
                  clickable.focused = True
               else:
                  clickable.focused = False
            self.refreshMenu() 
   def menuHoverLogic(self,mousex,mousey):
      for tab in self.listOfTabs:
         if tab.header.focused == True:
            for clickable in tab.listOfClickables:
               if isinstance(clickable, TextBox):
                  if clickable.isWithinBoundaries(mousex,mousey):
                     pygame.mouse.set_cursor(textCursor)
   def refreshMenu(self):
      MAINWINDOW.fill(BGCOLOR)
      for tab in self.listOfTabs:
         tab.header.display()
         if tab.header.focused == True:
            tab.display()
      pygame.display.update()
   def displayMenu(self):
      self.setupNameTab()
      self.setupAbilityScoresTab()
      self.setupRaceTab()
      self.setupClassTab()
      self.setupBackgroundTab()
      self.setupSkillsTab()
      self.setupCharacterSheetTab()
      
      headerList = []
      for tab in self.listOfTabs:
         headerList.append(tab.header)
      
      self.setSpacing(headerList,(0,0))
      for i,tab in enumerate(self.listOfTabs):
         tab.header = headerList[i]
      
      self.refreshMenu()
   def setSpacing(self,listToSpace,startingCoordinate,columnWidth=105,rowHeight=15,verticalBuffer=20):
      x,y = startingCoordinate
      for i in listToSpace:
         i.boundaries = (x,y,columnWidth,rowHeight)
         y = y + verticalBuffer
   def setupNameTab(self):
      t = Tab()
      listOfClickables = [Clickable("Player"),Clickable("Character")]
      self.setSpacing(listOfClickables,(110,0))
      t.listOfClickables = listOfClickables
      t.header = Clickable("Names")
      self.listOfTabs.append(t)
   def setupAbilityScoresTab(self):
      t = Tab()
      listOfClickables = [Clickable("Roll"),Clickable("Point buy")]
      self.setSpacing(listOfClickables,(110,20))
      t.listOfClickables = listOfClickables
      t.header = Clickable("Ability Scores")
      self.listOfTabs.append(t)
   def setupRaceTab(self):
      t = Tab()
      listOfClickables = [Clickable("Race"),Clickable("Subrace")]
      self.setSpacing(listOfClickables,(110,40))
      t.listOfClickables = listOfClickables
      t.header = Clickable("Race")
      self.listOfTabs.append(t)
   def setupClassTab(self):
      t = Tab()
      listOfClickables = [Clickable("Class name"),Clickable("Level")]
      self.setSpacing(listOfClickables,(110,60))
      t.listOfClickables = listOfClickables
      t.header = Clickable("Classes")
      self.listOfTabs.append(t)
   def setupBackgroundTab(self):
      t = Tab()
      t.header = Clickable("Background")
      self.listOfTabs.append(t)
   def setupSkillsTab(self):
      t = Tab()
      t.header = Clickable("Skills")
      self.listOfTabs.append(t)
   def setupCharacterSheetTab(self):
      t = Tab()
      t.header = Clickable("Character Sheet")
      self.listOfTabs.append(t)
   def creationLoop(self):
      self.displayMenu()
      self.hostnameString = ""
      UserHasNotQuit = True
      while UserHasNotQuit:
         mouseClicked = False
         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
            elif event.type == MOUSEMOTION:
               mousex, mousey = event.pos
               self.menuHoverLogic(mousex,mousey)
            elif event.type == MOUSEBUTTONUP:
               mousex, mousey = event.pos
               mouseClicked = True
            if event.type == KEYDOWN:
               char = event.unicode
               self.menuKeyboardDown(char)
            if mouseClicked == True:
               self.menuMouseClickedLogic(mousex,mousey)
      pygame.quit()
      sys.exit()
      
window = creationWindow()   
window.creationLoop()
time.sleep(4)