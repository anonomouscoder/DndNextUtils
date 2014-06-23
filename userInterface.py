import characterGenerator,pygame,drawUtils,time,string
from drawUtils import *
from characterGenerator import *
#bascially anything that the user may click on and have an effect
class Clickable():
   def __init__(self,text,boundaries=(0,0,0,0)):
      self.link = ""
      self.text = text
      self.boundaries = boundaries
      self.focused = False
      self.function = ""
      self.functionArgs = [[""]]
      self.updateDisplayFunction = ""
      self.updateDisplayFunctionArgs = [[""]]
   def isWithinBoundaries(self,x,y):
      (boundaryx,boundaryy,lenx,leny) = self.boundaries
      if x > boundaryx and x < boundaryx + lenx and y > boundaryy and y < boundaryy + leny:
         return True
      return False
   def display(self):
      self.updateDisplay()
      (x,y,l,h) = self.boundaries
      if self.focused:
         color = WHITE
      else:
         color = GREY
      pygame.draw.rect(MAINWINDOW, color,  self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))
   def focusFunction(self,bool):
      self.focused = bool
   def runFunctions(self):
      if self.function != "":
         for i,f in enumerate(self.function):
            if self.functionArgs[i] == []:
               output = f()
            else:
               output = f(self.functionArgs[i])
      else:
         print "function is not set!"
   def updateDisplay(self):
      if self.updateDisplayFunction != "":
         for i,f in enumerate(self.updateDisplayFunction):
            if self.updateDisplayFunctionArgs[i] == []:
               self.text = f()
            else:
               self.text = f(self.updateDisplayFunctionArgs[i])
      
#You can click it, but all it does is be displayed
class Label(Clickable):
   def display(self):
      self.updateDisplay()
      (x,y,l,h) = self.boundaries
      pygame.draw.rect(MAINWINDOW, WHITE,  self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))

#Same as label, but the text of the label is updated dynamically
class VariableLabel(Label):
   def __init__(self,var,boundaries=(0,0,0,0)):
      self.variable = var
      Clickable.__init__(self,var)
   def display(self):
      if self.variable == []:
         self.text = self.variable
      elif len(self.variable) == 1 or self.variable[1] == "":
         self.text = str(self.variable[0])
      else:
         self.text = str(self.variable[0]) + ", " + str(self.variable[1])
      Label.display(self)

#Hidden
class Hidden(Clickable):
   def display(self):
      return 

#Clicking it applies focus, focused TextBox receives characters
class TextBox(Clickable):
   def __init__(self,text="default"):
      Clickable.__init__(self,text)
      self.maxLength = 13
      self.variable = "" #where to write this value
   def display(self):
      self.updateDisplay()
      (x,y,l,h) = self.boundaries
      if self.focused:
         color = WHITE
      elif self.text == "":
         color = GREY
      else:
         color = WHITE
      pygame.draw.rect(MAINWINDOW, color, self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))

#Clicking it toggles selection
class RadioButton(Clickable):
   def __init__(self):
      Clickable.__init__(self,"")
      self.selected = False
   def display(self):
      self.updateDisplay()
      (x,y,l,h) = self.boundaries
      if self.selected:
         color = WHITE
      else:
         color = GREY
      pygame.draw.rect(MAINWINDOW, color, self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))
   def focusFunction(self,bool):
      if bool == True:
         if self.selected:
            self.selected = False
         else:
            self.selected = True
      self.focused = bool

#Pair of Clickables that when a Receiver is focused, it takes the value from the first Sender in the list
class Sender(Clickable):
   def __init__(self,text,boundaries=(0,0,0,0)):
      self.selected = False
      Clickable.__init__(self,text)
   def isWithinBoundaries(self,x,y):
      if Clickable.isWithinBoundaries(self,x,y):
         if self.selected:
            self.selected = False
         else:
            self.selected = True
         return True
      return False
   def display(self):
      if self.selected:
         self.focused = True
      else:
         self.focused = False
      Clickable.display(self)
   def runFunctions(self):
      needToDeselect = False
      if self.function != "":
         for i,f in enumerate(self.function):
            if self.functionArgs[i] == []:
               needToDeselect = f()
            else:
               needToDeselect = f(self.functionArgs[i])
            if needToDeselect:
               self.selected = False
class Receiver(Clickable):
   def __init__(self,text,boundaries=(0,0,0,0)):
      self.selected = False
      self.hasValue = False
      Clickable.__init__(self,text)
   def isWithinBoundaries(self,x,y):
      if Clickable.isWithinBoundaries(self,x,y):
         if self.selected:
            self.selected = False
         else:
            self.selected = True
         return True
      return False
   def display(self):
      if self.selected:
         self.focused = True
      else:
         self.focused = False
      if self.hasValue:
         self.focused = True
      Clickable.display(self)
   def runFunctions(self):
      needToDeselect = False
      if self.function != "":
         for i,f in enumerate(self.function):
            if self.functionArgs[i] == []:
               needToDeselect = f()
            else:
               needToDeselect = f(self.functionArgs[i])
            if needToDeselect:
               self.selected = False
               
#Pages hold sets of clickables
class Page(Clickable):
   def __init__(self):
      self.text = ""
      self.boundaries = (0,0,0,0)
      self.backgroundColor = DARKGREY
      self.listOfClickables = []
      self.visible = True
   def display(self):
      (x,y,l,h) = self.boundaries
      pygame.draw.rect(MAINWINDOW, self.backgroundColor,  self.boundaries) 
      displayLast = []
      for click in self.listOfClickables:
         if click.focused:
            displayLast.append(click)
         else:
            click.display()
      for click in displayLast:
         click.display()
   def applyFocusToClickable(self,mousex,mousey):
      hasFocus = False
      for clickable in self.listOfClickables:
         clickable.focusFunction(False)
         if isinstance(clickable,Dropdown) and clickable.isWithinBoundaries(mousex,mousey) and hasFocus == False:
            clickable.focusFunction(True)
            hasFocus = True
      
      if hasFocus == False:
         print "no has Focus"
      return hasFocus

#Add a header clickable, extra clickables for choices, and a page of clickables
class Tab():
   def __init__(self):
      self.header = ""
      self.listOfClickables = []
      self.listOfPages = []
      self.focused = False
   def display(self):
      displayLast = []
      if self.header.focused:
         for i in self.listOfClickables:
            i.display()
         for i in self.listOfPages:
            if i.visible == True:
               i.display()
               
      self.header.display()
      
class creationWindow():
   def __init__(self):
      self.buffer = ""
      self.listOfTabs = []
      self.character = Character()
      self.temporaryRolls = [0,0,0,0,0,0]
   def menuKeyboardDown(self,char):
      for tab in self.listOfTabs:
         if tab.header.focused == True:
            for clickable in tab.listOfClickables:
               if isinstance(clickable, TextBox):
                  if char == "-1":
                     clickable.text = clickable.text[0:len(clickable.text)-1]
                  elif clickable.text < clickable.maxLength:
                     clickable.text = clickable.text + char
            for page in tab.listOfPages:
               for clickable in page.listOfClickables:
                  if isinstance(clickable, TextBox) and clickable.focused == True:
                     if char == "-1":
                        if len(clickable.text) > 0:
                           clickable.text = clickable.text[0:len(clickable.text)-1]
                     elif len(clickable.text)-1 < clickable.maxLength:
                        clickable.text = clickable.text + char
      self.refreshMenu()
   def menuMouseClickedLogic(self,mousex,mousey):
      for tab in self.listOfTabs:
         #is the header clicked on?
         if tab.header.isWithinBoundaries(mousex,mousey):
            tab.header.runFunctions()
            for otherTabs in self.listOfTabs:
               otherTabs.header.focusFunction(False)
            tab.header.focusFunction(True)
            break
         #while the header is the last one clicked, parse the tab
         if tab.header.focused == True:
            #parse the extra clickables for choices
            for clickable in tab.listOfClickables:
               if clickable.isWithinBoundaries(mousex,mousey):
                  clickable.focusFunction(True)
                  clickable.runFunctions()
               else:
                  clickable.focusFunction(False)
            #parse each page
            for page in tab.listOfPages:
               if page.visible == True:
                  for clickable in page.listOfClickables:
                     if clickable.isWithinBoundaries(mousex,mousey):
                        clickable.focusFunction(True)
                        clickable.runFunctions()
                     else:
                        clickable.focusFunction(False)
               else:
                  print "page " + page.text + " is not visible"
            #for page in tab.listOfPages:
            #   for click in page.listOfClickables:
            #      if click.focused == True:
            #         print "Page: " + page.text + " , clickable: " + click.text + " has focus" 
                  
      self.refreshMenu() 
   def menuHoverLogic(self,mousex,mousey):
      for tab in self.listOfTabs:
         if tab.header.focused == True:
            for clickable in tab.listOfClickables:
               if isinstance(clickable, TextBox):
                  if clickable.isWithinBoundaries(mousex,mousey):
                     pygame.mouse.set_cursor(textCursor)
   def updatePage(self,tab,page):
      found = False
      for p in tab.listOfPages:
         if p.text == page.text:
            found = True
            p = page
            break
      if not found:
         tab.listOfPages.append(page)
   def updateTab(self,tab):
      found = False
      for t in self.listOfTabs:
         if t.header.text == tab.header.text:
            t.listOfPages = []
            for page in tab.listOfPages:
               t.listOfPages.append(page)
            found = True
            break
      if not found:
         self.listOfTabs.append(tab)
   def refreshMenu(self):
      print "refreshing menu"
      MAINWINDOW.fill(BGCOLOR)
      for tab in self.listOfTabs:
         tab.display()
      pygame.display.update()
   def displayMenu(self):
      self.setupAbilityScoresTab()
      self.setupRaceTab()
      self.setupClassTab()
      self.setupBackgroundTab()
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
   def setupAbilityScoresTab(self):
      nameWidth = 105
      numberWidth = 20
      xPageStart = 110
      yPageStart = 0
      t = Tab()
      t.header = Clickable("Ability Scores")
      listOfClickables = [Clickable("Roll"),Clickable("Point buy")]
      listOfClickables[0].function = [self.rollAbilities,self.pageShow]
      listOfClickables[0].functionArgs = [[""],["roll"]]
      listOfClickables[1].function = [self.resetAbilities,self.pageShow]
      listOfClickables[1].functionArgs = [[""],["pointbuy"]]
      self.setSpacing(listOfClickables,(110,0))
      t.listOfClickables = listOfClickables
      
                         
      
      # /Ability Scores / /Roll     / |##|   STR |  |##| INT |  |##|
      # |Race           | |Point buy| |##|   CON |  |##| WIS |  |##|
      # |Classes        |             |##|   DEX |  |##| CHA |  |##|       
      # |Background     |             |##| 
      # |Character Sheet|             |##|    
      #                               |##|
      rollPage = Page()
      rollPage.visible = True
      rollPage.text = "roll"
      rollPage.boundaries = (xPageStart+(nameWidth+5),yPageStart,(nameWidth+5)*3+(numberWidth+5)*8+5,85)
      rollPage.backgroundColor = BLACK
      rollColumns = [[Sender(""),   Sender(""),   Sender(""),   Sender(""), Sender(""), Sender("")],
                     [Label("STR"), Label("CON"), Label("DEX"), Hidden(""), Hidden(""), Hidden("")],
                     [Receiver(""), Receiver(""), Receiver(""), Hidden(""), Hidden(""), Hidden("")],
                     [Label(""),    Label(""),    Label(""),    Hidden(""), Hidden(""), Hidden("")],
                     [Label("INT"), Label("WIS"), Label("CHA"), Hidden(""), Hidden(""), Hidden("")],
                     [Receiver(""), Receiver(""), Receiver(""), Hidden(""), Hidden(""), Hidden("")],
                     [Label(""),    Label(""),    Label(""),    Hidden(""), Hidden(""), Hidden("")]]
      for i,row in enumerate(rollColumns[0]):
         row.updateDisplayFunction = [self.displayTemporaryRolls]
         row.updateDisplayFunctionArgs = [[i]]
      for column in rollColumns:
         for click in column:
            print "is click: " + str(click) + " a Swapper? " + str(isinstance(click,Sender) or isinstance(click,Receiver))
            if isinstance(click,Sender) or isinstance(click,Receiver):
               print "setting swapper function"
               click.function = [self.swapValues]
               click.functionArgs = [[rollColumns]]
      columnWidthList = [numberWidth,numberWidth,numberWidth,numberWidth,numberWidth,numberWidth,numberWidth]
      self.setHorizontalSpacing(rollPage,rollColumns,(xPageStart+(nameWidth+5),yPageStart),columnWidthList)
      
      # /Ability Scores / |Roll     | Points spent |##|
      # |Race           | /Point buy/ STR          |-| ##|##|+| INT |-|##|##|+|
      # |Classes        |             CON          |-| ##|##|+| WIS |-|##|##|+|
      # |Background     |             DEX          |-| ##|##|+| CHA |-|##|##|+|
      # |Character Sheet|             
      #       
      pointBuyPage = Page()
      pointBuyPage.visible = False
      pointBuyPage.text = "pointbuy"
      pointBuyPage.boundaries = (xPageStart+(nameWidth+5),yPageStart,(nameWidth+5)*3+(numberWidth+5)*8+5,85)
      pointBuyPage.backgroundColor = BLACK
      pointBuyColumns = [[Label("Points Spent"), Label("STR"),           Label("CON"), Label("DEX")],
                         [Label(""),             Label("-"),             Label("-"),   Label("-")],
                         [Hidden(""),            Label(""),              Label(""),    Label("")],
                         [Hidden(""),            Label(""),              Label(""),    Label("")],
                         [Hidden(""),            Label("+"),             Label("+"),   Label("+")],
                         [Hidden(""),            Label("INT"),           Label("WIS"), Label("CHA")],
                         [Hidden(""),            Label("-"),             Label("-"),   Label("-")],
                         [Hidden(""),            Label(""),              Label(""),    Label("")],
                         [Hidden(""),            Label(""),              Label(""),    Label("")],
                         [Hidden(""),            Label("+"),             Label("+"),   Label("+")]]

      (pointBuyColumns[1])[0].updateDisplayFunction = [self.printPointsSpent]
      decrementAbilityFunction = [self.decrementAbility]
      incrementAbilityFunction = [self.incrementAbility]
      for i,click in enumerate(pointBuyColumns[1]):
         if i != 0:
            click.function = decrementAbilityFunction
            click.functionArgs = [[((pointBuyColumns[0])[i].text).lower()]]
      for i,click in enumerate(pointBuyColumns[4]):
         if i != 0:
            click.function = incrementAbilityFunction
            click.functionArgs = [[((pointBuyColumns[0])[i].text).lower()]]
      for i,click in enumerate(pointBuyColumns[6]):
         if i != 0:
            click.function = decrementAbilityFunction
            click.functionArgs = [[((pointBuyColumns[5])[i].text).lower()]]
      for i,click in enumerate(pointBuyColumns[9]):
         if i != 0:
            click.function = incrementAbilityFunction
            click.functionArgs = [[((pointBuyColumns[5])[i].text).lower()]]
         
      for i,click in enumerate(pointBuyColumns[2]):
         if i != 0:
            click.updateDisplayFunction = [self.printAbility]
            click.updateDisplayFunctionArgs = [[((pointBuyColumns[0])[i].text).lower()]]
      for i,click in enumerate(pointBuyColumns[3]):
         if i != 0:
            click.updateDisplayFunction = [self.printAbilityMod]
            click.updateDisplayFunctionArgs = [[((pointBuyColumns[0])[i].text).lower()]]
      for i,click in enumerate(pointBuyColumns[7]):
         if i != 0:
            click.updateDisplayFunction = [self.printAbility]
            click.updateDisplayFunctionArgs = [[((pointBuyColumns[5])[i].text).lower()]]
      for i,click in enumerate(pointBuyColumns[8]):
         if i != 0:
            click.updateDisplayFunction = [self.printAbilityMod]
            click.updateDisplayFunctionArgs = [[((pointBuyColumns[5])[i].text).lower()]]
         
      columnWidthList = [nameWidth,nameWidth,numberWidth,numberWidth,numberWidth,numberWidth,nameWidth,numberWidth,numberWidth,numberWidth,numberWidth]
      self.setHorizontalSpacing(pointBuyPage,pointBuyColumns,(xPageStart+(nameWidth+5),yPageStart),columnWidthList)
      
      t.listOfPages.append(rollPage)
      t.listOfPages.append(pointBuyPage)
      self.listOfTabs.append(t)
      
   def setupRaceTab(self):
      t = Tab()
      t.header = Clickable("Race")
      t.header.function = [self.setFocus,self.setFocus]
      t.header.functionArgs = ["race","subrace"]
      listOfClickables = [Clickable("Dwarf"), Clickable("Elf"), Clickable("Halfling"), Clickable("Human"), Clickable("Dragonborn"), Clickable("Drow"), Clickable("Gnome"), Clickable("Halfelf"), Clickable("Halforc"), Clickable("Kender"), Clickable("Tiefling"), Clickable("Warforged")]
      nameWidth = 105
      self.setSpacing(listOfClickables,(nameWidth+5,0))
      xPageStart = (nameWidth+5)*2
      yPageStart = 0
      
      #Dwarven subraces
      sectionDwarfSubRace = Page()
      sectionDwarfSubRace.visible = True
      sectionDwarfSubRace.backgroundColor = BLACK
      sectionDwarfSubRace.text = "dwarf"
      sectionDwarfSubRace.boundaries = (xPageStart,yPageStart,(nameWidth+5)+5,45)
      subraceColumns = [[Clickable("Hill Dwarf"), Clickable("Mountain Dwarf")]]
      columnWidthList = [nameWidth]
      self.setHorizontalSpacing(sectionDwarfSubRace,subraceColumns,(xPageStart,yPageStart),columnWidthList)
      (subraceColumns[0])[0].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[0].functionArgs = [["Hill Dwarf"],["Dwarf"]]
      (subraceColumns[0])[1].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[1].functionArgs = [["Mountain Dwarf"],["Dwarf"]]
      
      #Elven subraces
      sectionElfSubRace = Page()
      sectionElfSubRace.visible = False
      sectionElfSubRace.backgroundColor = BLACK
      sectionElfSubRace.text = "elf"
      sectionElfSubRace.boundaries = (xPageStart-5,yPageStart-5,(nameWidth+5)+5,45)
      subraceColumns = [[Clickable("High Elf"), Clickable("Wood Elf")]]
      columnWidthList = [nameWidth]
      self.setHorizontalSpacing(sectionElfSubRace,subraceColumns,(xPageStart,yPageStart),columnWidthList)
      (subraceColumns[0])[0].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[0].functionArgs = [["High Elf"],["Elf"]]
      (subraceColumns[0])[1].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[1].functionArgs = [["Wood Elf"],["Elf"]]
      
      #Halfling subraces
      sectionHalflingSubRace = Page()
      sectionHalflingSubRace.visible = False
      sectionHalflingSubRace.backgroundColor = BLACK
      sectionHalflingSubRace.text = "halfling"
      sectionHalflingSubRace.boundaries = (xPageStart-5,yPageStart-5,(nameWidth+5)+5,45)
      subraceColumns = [[Clickable("Lightfoot"), Clickable("Stout")]]
      columnWidthList = [nameWidth]
      self.setHorizontalSpacing(sectionHalflingSubRace,subraceColumns,(xPageStart,yPageStart),columnWidthList)
      (subraceColumns[0])[0].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[0].functionArgs = [["Lightfoot"],["Halfling"]]
      (subraceColumns[0])[1].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[1].functionArgs = [["Stout"],["Halfling"]]
      
      #Gnomish subraces
      sectionGnomeSubRace = Page()
      sectionGnomeSubRace.visible = False
      sectionGnomeSubRace.backgroundColor = BLACK
      sectionGnomeSubRace.text = "gnome"
      sectionGnomeSubRace.boundaries = (xPageStart-5,yPageStart-5,(nameWidth+5)+5,45)
      subraceColumns = [[Clickable("Forest Gnome"), Clickable("Rock Gnome")]]
      columnWidthList = [nameWidth]
      self.setHorizontalSpacing(sectionGnomeSubRace,subraceColumns,(xPageStart,yPageStart),columnWidthList)
      (subraceColumns[0])[0].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[0].functionArgs = [["Forest Gnome"],["Gnome"]]
      (subraceColumns[0])[1].function = [self.defineSubRace,self.setFocus]
      (subraceColumns[0])[1].functionArgs = [["Rock Gnome"],["Gnome"]]
      
      #defining function for the race clickable
      for click in listOfClickables:
         click.function =     [self.pageShow,self.defineRace]
         if click.text == "Dwarf":
            click.functionArgs = [[sectionDwarfSubRace.text],[click.text]]
         elif click.text == "Elf":
            click.functionArgs = [[sectionElfSubRace.text],[click.text]]
         elif click.text == "Halfling":
            click.functionArgs = [[sectionHalflingSubRace.text],[click.text]]
         elif click.text == "Gnome":
            click.functionArgs = [[sectionGnomeSubRace.text],[click.text]]
         else:
            click.functionArgs = [[""],[click.text]]
            click.function = [self.allPagesHide,self.defineRace]

      t.listOfClickables = listOfClickables
      
      t.listOfPages.append(sectionGnomeSubRace)
      t.listOfPages.append(sectionHalflingSubRace)
      t.listOfPages.append(sectionElfSubRace)
      t.listOfPages.append(sectionDwarfSubRace)
      self.listOfTabs.append(t)
   def setupClassTab(self):
      nameWidth = 105
      numberWidth = 20
      xPageStart = 110
      yPageStart = 0
      t = Tab()
      t.header = Clickable("Classes")
      
      classColumns = [[Label("Barbarian"), Label("Bard"), Label("Cleric"), Label("Druid"), Label("Fighter"), Label("Mage"), Label("Monk"), Label("Paladin"), Label("Ranger"), Label("Rogue")],
                      [Label("-"), Label("-"), Label("-"), Label("-"), Label("-"), Label("-"), Label("-"), Label("-"), Label("-"), Label("-")],
                      [Label(""), Label(""), Label(""), Label(""), Label(""), Label(""), Label(""), Label(""), Label(""), Label("")],
                      [Label("+"), Label("+"), Label("+"), Label("+"), Label("+"), Label("+"), Label("+"), Label("+"), Label("+"), Label("+")]]
      decrementLevelFunction = [self.decrementLevel]
      for i,click in enumerate(classColumns[1]):
         click.function = decrementLevelFunction
         click.functionArgs = [[(classColumns[0])[i].text]]
         
      levelFunction = [self.findLevelOfClass]
      levelFunctionArgs = [[]]
      for i,click in enumerate(classColumns[2]):
         click.updateDisplayFunction = levelFunction
         click.updateDisplayFunctionArgs = [[(classColumns[0])[i].text]]
         
      incrementLevelFunction = [self.incrementLevel]
      for i,click in enumerate(classColumns[3]):
         click.function = incrementLevelFunction
         click.functionArgs = [[(classColumns[0])[i].text]]
         
      columnWidthList = [nameWidth,numberWidth,numberWidth,numberWidth]
      self.setHorizontalSpacing(t,classColumns,(xPageStart,yPageStart),columnWidthList)
      self.listOfTabs.append(t)
   def setupBackgroundTab(self):
      t = Tab()
      t.header = Clickable("Background")
      self.listOfTabs.append(t)
   def setupCharacterSheetTab(self):
      t = Tab()
      t.header = Clickable("Character Sheet")
      t.header.function = [self.setupCharacterSheetTab,self.refreshMenu]
      t.header.functionArgs = [[],[]]
      xPageStart = 215
      yPageStart = 5
      nameWidth = 105
      longNameWidth = 155
      numberWidth = 20
      longNumberWidth = 55
      descriptionWidth = 800
      #-----Default Section-----------------------------------------------------------------
      # Player Name     ______________             Race           ______________           |
      # Character Name  ______________             Subrace        ______________           |
      # Vision          ______________             Alignment      ______________           |
      #-------------------------------------------------------------------------------------
      sectionBasics = Page()
      sectionBasics.text = "basics"
      sectionBasics.boundaries = (xPageStart-5,yPageStart-5,(nameWidth+5)*3+(longNameWidth+5)+5,65)
      raceLabel =  VariableLabel([self.character.race])
      subRaceLabel = VariableLabel([self.character.race.subraceString])
      levelLabel = VariableLabel([self.character.totalLevel])
      basicColumns = [[Label("Player Name"), Label("Character Name"), Label("Vision")],
                      [TextBox(""), TextBox(""), Label("")],
                      [Label("Race"), Label("Subrace"), Label("Alignment")],
                      [raceLabel, subRaceLabel, Label("")]]
      columnWidthList = [nameWidth,nameWidth,nameWidth,longNameWidth]
      self.setHorizontalSpacing(sectionBasics,basicColumns,(xPageStart,yPageStart),columnWidthList)
      
      #-------------------------------------------------------------------------------------
      # Strength     _______ _______           Intelligence   _______ _______              |
      # Constitution _______ _______           Wisdom         _______ _______              |
      # Dexterity    _______ _______           Charisma       _______ _______              |
      #-------------------------------------------------------------------------------------
      sectionAttibutes = Page()
      sectionAttibutes.text = "attributes"
      sectionAttibutes.boundaries = (xPageStart-5+(nameWidth+5)*3+(longNameWidth+5)+5,yPageStart-5,(nameWidth+5)*2+(numberWidth+5)*4+5 ,65)
      strModLabel = VariableLabel([self.character.strMod])
      conModLabel = VariableLabel([self.character.conMod])
      dexModLabel = VariableLabel([self.character.dexMod])
      intModLabel = VariableLabel([self.character.intMod])
      wisModLabel = VariableLabel([self.character.wisMod])
      chaModLabel = VariableLabel([self.character.chaMod])
      attributeColumns = [[Label("Strength"), Label("Constitution"), Label("Dexterity")],
                          [VariableLabel([self.character.str]), VariableLabel([self.character.con]), VariableLabel([self.character.dex])],
                          [strModLabel, conModLabel, dexModLabel],
                          [Label("Intelligence"), Label("Wisdom"), Label("Charisma")],
                          [VariableLabel([self.character.int]), VariableLabel([self.character.wis]), VariableLabel([self.character.cha])],
                          [intModLabel, wisModLabel, chaModLabel]]
      columnWidthList = [nameWidth,numberWidth,numberWidth,nameWidth,numberWidth,numberWidth]
      self.setHorizontalSpacing(sectionAttibutes,attributeColumns,(xPageStart+(nameWidth+5)*3+(longNameWidth+5)+5,yPageStart),columnWidthList)    
      numberOfRows = 3
      yPageStart = yPageStart + numberOfRows*20 + 5
      
      #-------------------------------------------------------------------------------------
      # Class ______________ Level _______                                                 |
      #-------------------------------------------------------------------------------------
      sectionClasses = Page()
      sectionClasses.text = "classes"
      classesColumns = [[],
                        []]
      numberOfRows = 0
      for c in self.character.classLevels:
         if numberOfRows == 0:
            classesColumns[0].append(Label("Class"))
            classesColumns[1].append(Label("Level"))
            numberOfRows = numberOfRows + 1
         classLabel = VariableLabel([c])
         levelLabel = VariableLabel([c.level])
         classesColumns[0].append(classLabel)
         classesColumns[1].append(levelLabel)
         numberOfRows = numberOfRows + 1
      if numberOfRows > 2:
         classesColumns[0].append(Label("Total"))
         classesColumns[1].append(VariableLabel([self.character.totalLevel]))
         numberOfRows = numberOfRows + 1
         
      columnWidthList = [longNameWidth,nameWidth]
      self.setHorizontalSpacing(sectionClasses,classesColumns,(xPageStart,yPageStart),columnWidthList) 
      
      sectionClasses.boundaries = (xPageStart-5,yPageStart-5,(nameWidth+5)+(longNameWidth+5)+5, numberOfRows*20+5)
      
      
      yPageStart = yPageStart + numberOfRows*20 + 5
      
      #-------------------------------------------------------------------------------------
      # Experience (Next) _______ _______ | Hp        _______ _______ | Initiative _______ |
      # AC (no armor)     _______ _______ | Hit dice  _______ _______ | Speed      _______ |
      #-------------------------------------------------------------------------------------
      sectionVarious = Page()
      sectionVarious.text = "various"
      sectionVarious.boundaries = (xPageStart-5,yPageStart-5, (nameWidth+5)*3+(numberWidth+5)*3+(longNumberWidth+5)*2+5 ,45)
      variousColumns = [[Label("Exp, Next"), Label("AC, no Armor")],
                        [TextBox(""), Label("")],
                        [TextBox(""), Label("")],
                        [Label("HP"), Label("Hit Dice")],
                        [TextBox(""), Label("")],
                        [Label(""), Label("")],
                        [Label("Initiative"), Label("Speed")],
                        [Label(""), Label("")]]
      columnWidthList = [nameWidth, longNumberWidth, longNumberWidth, nameWidth, numberWidth, numberWidth, nameWidth, numberWidth]
      self.setHorizontalSpacing(sectionVarious,variousColumns,(xPageStart,yPageStart),columnWidthList) 
      #-------------------------------------------------------------------------------------
      # Languages      ______________ ______________ ______________ ______________         |
      # ______________ ______________ ______________ ______________ ______________         |
      #-------------------------------------------------------------------------------------
      sectionLanguages = Page()
      sectionLanguages.text = "languages"
      sectionLanguages.boundaries = (xPageStart-5+(nameWidth+5)*3+(longNumberWidth+5)*2+(numberWidth+5)*3+5,yPageStart-5,(nameWidth+5)*4+5,45)
      languageColumns = [[Label("Languages"), TextBox("")],
                         [TextBox(""), TextBox("")],
                         [TextBox(""), TextBox("")],
                         [TextBox(""), TextBox("")]]
      columnWidthList = [nameWidth, nameWidth, nameWidth, nameWidth]
      self.setHorizontalSpacing(sectionLanguages,languageColumns,(xPageStart+(nameWidth+5)*3+(longNumberWidth+5)*2+(numberWidth+5)*3+5,yPageStart),columnWidthList)
      numberOfRows = 2
      yPageStart = yPageStart + numberOfRows*20 + 5
      #-------------------------------------------------------------------------------------
      # Proficiency bonus _______                                                          |
      # Saving Throws   ______________ ______________                                      |
      # Tools           ______________ ______________                                      |
      # Armor           ______________ ______________                                      |
      # Weapon          ______________ ______________                                      |
      #-------------------------------------------------------------------------------------
      sectionProficiencies = Page()
      sectionProficiencies.text = "proficiencies"
      sectionProficiencies.boundaries = (xPageStart-5,yPageStart-5,longNameWidth+nameWidth*2+5*4,125)
      proficiencyColumns = [[Label("Proficiency bonus"), Label("Saving Throws"), Label("Tools"), Label("Armor"), Label("Weapon")],
                            [Label(""), Label(""), Label(""), Label(""), Label("")],
                            [Label(""), Label(""), Label(""), Label(""), Label("")]]
      columnWidthList = [longNameWidth, nameWidth, nameWidth]
      self.setHorizontalSpacing(sectionProficiencies,proficiencyColumns,(xPageStart,yPageStart),columnWidthList)
      #-------------------------------------------------------------------------------------
      # _______ Acrobatics(DEX)     _______ Insight(WIS)      _______ Persuasion(CHA)      |
      # _______ Animal Handling(WIS)_______ Intimidation(CHA) _______ Religion(INT)        |
      # _______ Arcana(INT)         _______ Medicine(WIS)     _______ Search(INT)          |
      # _______ Athletics(STR)      _______ Nature(INT)       _______ Sleight of Hand(DEX) |
      # _______ Deception(CHA)      _______ Perception(WIS)   _______ Stealth(DEX)         |
      # _______ History(INT)        _______ Performance(CHA)  _______ Survival(WIS)        |
      #------------------------------------------------------------------------------------|
      sectionSkills = Page()
      sectionSkills.text = "skills"
      sectionSkills.boundaries = (xPageStart-5+longNameWidth+nameWidth*2+5*4,yPageStart-5,(numberWidth+5)*3+(longNameWidth+5)*3+5,125)
      skillsColumns = [[RadioButton(), RadioButton(), RadioButton(), RadioButton(), RadioButton(), RadioButton()],
                       [Label("Acrobatics(DEX)"), Label("Animal Handling(WIS)"), Label("Arcana(INT)"), Label("Athletics(STR)"), Label("Deception(CHA)"), Label("History(INT)")],
                       [RadioButton(), RadioButton(), RadioButton(), RadioButton(), RadioButton(), RadioButton()],
                       [Label("Insight(WIS)"), Label("Intimidation(CHA)"), Label("Medicine(WIS)"), Label("Nature(INT)"), Label("Perception(WIS)"), Label("Performance(CHA)")],
                       [RadioButton(), RadioButton(), RadioButton(), RadioButton(), RadioButton(), RadioButton()],
                       [Label("Persuasion(CHA)"), Label("Religion(INT)"), Label("Search(INT)"), Label("Sleight of Hand(DEX)"), Label("Stealth(DEX)"), Label("Survival(WIS)")]]
      columnWidthList = [numberWidth, longNameWidth, numberWidth, longNameWidth, numberWidth, longNameWidth]
      self.setHorizontalSpacing(sectionSkills,skillsColumns,(xPageStart+longNameWidth+nameWidth*2+5*4,yPageStart),columnWidthList)
      numberOfRows = 6
      yPageStart = yPageStart + numberOfRows*20 + 5
      
      #-------------------------------------------------------------------------------------
      # Class Features Descriptions                                                        |
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      #-------------------------------------------------------------------------------------
      sectionClassFeatures = Page()
      sectionClassFeatures.text = "classfeatures"
      sectionClassFeatures.boundaries = (xPageStart-5,yPageStart-5,nameWidth+5+descriptionWidth+5+5,105)
      featureColumns = [[Label("Class Features"), Label(""), Label(""), Label(""), Label("")],
                        [Label("Descriptions"), Label(""), Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth, descriptionWidth]
      self.setHorizontalSpacing(sectionClassFeatures,featureColumns,(xPageStart,yPageStart),columnWidthList)
      numberOfRows = 5
      yPageStart = yPageStart + numberOfRows*20 + 5
      #-------------------------------------------------------------------------------------
      # Racial Traits  Description                                                         |
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      #-------------------------------------------------------------------------------------
      sectionRacialTraits = Page()
      sectionRacialTraits.text = "racial traits"
      sectionRacialTraits.boundaries = (xPageStart-5,yPageStart-5,nameWidth+5+descriptionWidth+5+5,105)
      traitColumns = [[Label("Racial Traits"), Label(""), Label(""), Label(""), Label("")],
                      [Label("Descriptions"), Label(""), Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth, descriptionWidth]
      self.setHorizontalSpacing(sectionRacialTraits,traitColumns,(xPageStart,yPageStart),columnWidthList)
      numberOfRows = 5
      yPageStart = yPageStart + numberOfRows*20 + 5
      
      #append them to the list in the order in which they should be drawn
      self.updatePage(t,sectionRacialTraits)
      self.updatePage(t,sectionClassFeatures)
      self.updatePage(t,sectionSkills)
      self.updatePage(t,sectionProficiencies)
      self.updatePage(t,sectionLanguages)
      self.updatePage(t,sectionVarious)
      #print "checking for classes"
      self.updatePage(t,sectionClasses)
      self.updatePage(t,sectionAttibutes)
      self.updatePage(t,sectionBasics)
      
      self.updateTab(t)
   def setHorizontalSpacing(self,pageToAddTo,listToSpace,startingCoordinate,columnWidthList,rowHeight=15,verticalBuffer=20):
      x,y = startingCoordinate
      previousWidth = 0
      for index,column in enumerate(listToSpace):
         width = columnWidthList[index]
         self.setSpacing(column, (x+previousWidth,y),width)
         previousWidth = previousWidth + width + 5
         for i in column:
            pageToAddTo.listOfClickables.append(i)
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
               if pygame.key.name(event.key) == "backspace":
                  self.menuKeyboardDown("-1")
               else:
                  self.menuKeyboardDown(event.unicode)
            if mouseClicked == True:
               self.menuMouseClickedLogic(mousex,mousey)
      pygame.quit()
      sys.exit()
   #Here are functions that various Clickables can can do
   # Show this page, hide other pages
   def pageShow(self,args):
      textOfPageToShow = args[0]
      print "showing page " + str(textOfPageToShow)
      for tab in self.listOfTabs:
         if tab.header.focused:
            for page in tab.listOfPages:
               if page.text == textOfPageToShow:
                  page.visible = True
               else:
                  page.visible = False
   # Hide all of the pages
   def allPagesHide(self,args):
      for tab in self.listOfTabs:
         if tab.header.text == "Race":
            for page in tab.listOfPages:
                page.visible = False
   def defineRace(self,args):
      race = characterGenerator.race.getClassFromString(args[0])
      self.character.addRace(race)
   def defineSubRace(self,args):
      self.character.addSubRace(args[0]) 
   def defineClassLevel(self,args):
      print args
      className = args[0]
      classLevel = args[1]
      c = classes.getClassFromString(className)
      for level in range(classLevel-1):
         c.levelUp()
      self.character.addClassLevel(c)
   def setFocus(self,args):
      if args == "race":
         textToSearchFor = self.character.raceString
      elif args == "subrace":
         textToSearchFor = self.character.race.subraceString
      elif args == "class":
         textToSearchFor = str(self.character.classLevels[args[1]])
      else:
         textToSearchFor = args
      for tab in self.listOfTabs:
         for click in tab.listOfClickables:
            if click.text == textToSearchFor:
               click.focused = True
         for page in tab.listOfPages:
            for click in page.listOfClickables:
               if click.text == textToSearchFor:
                  click.focused = True
   def decrementLevel(self,args):
      return
   def incrementLevel(self,args):
      print "incrementing level: " + str(args[0])
      c = classes.getClassFromString(args[0])
      self.character.addClassLevel(c)
   def findLevelOfClass(self,args):
      if self.character.findClassLevel(args[0]) == -1:
         return "0"
      else:
         return str(self.character.classLevels[self.character.findClassLevel(args[0])].level)
   def resetAbilities(self,args):
      print "Abilities reset!"
      self.character.setAbility("str",8)
      self.character.setAbility("con",8)
      self.character.setAbility("dex",8)
      self.character.setAbility("int",8)
      self.character.setAbility("wis",8)
      self.character.setAbility("cha",8)
   def incrementAbility(self,args):
      value = 8
      if args[0] == "str":
         value = self.character.str + 1
      elif args[0] == "con":
         value = self.character.con + 1
      elif args[0] == "dex":
         value = self.character.dex + 1
      elif args[0] == "int":
         value = self.character.int + 1
      elif args[0] == "wis":
         value = self.character.wis + 1
      elif args[0] == "cha":
         value = self.character.cha + 1
      self.character.setAbility(args[0],value)
   def decrementAbility(self,args):
      value = 8
      if args[0] == "str":
         value = self.character.str - 1
      elif args[0] == "con":
         value = self.character.con - 1
      elif args[0] == "dex":
         value = self.character.dex - 1
      elif args[0] == "int":
         value = self.character.int - 1
      elif args[0] == "wis":
         value = self.character.wis - 1
      elif args[0] == "cha":
         value = self.character.cha - 1
      self.character.setAbility(args[0],value)
   def rollAbilities(self,args):
      value = 0
      for i in range(6):
         least = 6
         value = 0
         for j in range(4):
            r = self.character.rollDie(6)
            if r < least:
               value = value + least
               least = r
            else:
               value = value + r
         value = value - 6 #subtract the inital least value
         self.temporaryRolls[i] = value
      self.temporaryRolls.sort(reverse=True)
      print str(self.temporaryRolls)
   def displayTemporaryRolls(self,args):
      return str(self.temporaryRolls[args[0]])
   def swapValues(self,args):
      listOfClickables = args[0]
      swapValue = ""
      swapIndexI = 0
      swapIndexJ = 0
      didSwap = False
      for i,column in enumerate(listOfClickables):
         for j,click in enumerate(column):
            if isinstance(click,Sender) and click.selected and swapValue == "":
               swapValue = click.text
               swapIndexI = i
               swapIndexJ = j
            if isinstance(click,Receiver) and click.selected and swapValue != "":
               (listOfClickables[swapIndexI])[swapIndexJ] = click.text
               click.text = swapValue
               click.hasValue = True
               didSwap = True
               break
      return didSwap
   def printPointsSpent(self,args):
      return str(self.character.pointsSpent)
   def printAbility(self,args):
      if args[0] == "str":
         return str(self.character.str)
      elif args[0] == "con":
         return str(self.character.con)
      elif args[0] == "dex":
         return str(self.character.dex)
      elif args[0] == "int":
         return str(self.character.int)
      elif args[0] == "wis":
         return str(self.character.wis)
      elif args[0] == "cha":
         return str(self.character.cha)
   def printAbilityMod(self,args):
      if args[0] == "str":
         return str(self.character.strMod)
      elif args[0] == "con":
         return str(self.character.conMod)
      elif args[0] == "dex":
         return str(self.character.dexMod)
      elif args[0] == "int":
         return str(self.character.intMod)
      elif args[0] == "wis":
         return str(self.character.wisMod)
      elif args[0] == "cha":
         return str(self.character.chaMod)
   
pygame.key.set_repeat(500,100)
window = creationWindow()   
window.creationLoop()