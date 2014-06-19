import characterGenerator,pygame,drawUtils,time
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
   def focusFunction(self,bool):
      self.focused = bool
   def runFunctions(self):
      if self.function != "":
         for i,f in enumerate(self.function):
            print "function: " + str(f)
            print "functionArgs: " + str(self.functionArgs[i])
            f(self.functionArgs[i])
      else:
         print "function is not set!"

#You can click it, but all it does is be displayed
class Label(Clickable):
   def display(self):
      (x,y,l,h) = self.boundaries
      pygame.draw.rect(MAINWINDOW, WHITE,  self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y))

#Same as label, but the text of the label is updated dynamically
class VariableLabel(Label):
   def __init__(self,var,boundaries=(0,0,0,0)):
      self.variable = var
      Clickable.__init__(self,self.variable)
   def display(self):
      if len(self.variable) == 1 or self.variable[1] == "":
         self.text = str(self.variable[0])
      else:
         self.text = str(self.variable[0]) + "(" + str(self.variable[1]) + ")"
      Label.display(self)

#Hidden
class Hidden(Clickable):
   def display(self):
      (x,y,l,h) = self.boundaries
      pygame.draw.rect(MAINWINDOW, DARKGREY,  self.boundaries) 
      d = allFont.render(self.text, 1, BLACK)
      MAINWINDOW.blit(d,(x,y)) 

#Clicking it applies focus, focused TextBox receives characters
class TextBox(Clickable):
   def __init__(self,text="default"):
      Clickable.__init__(self,text)
      self.maxLength = 13
      self.variable = "" #where to write this value
   def display(self):
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
            print "Dropdown found"
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
   def refreshMenu(self):
      MAINWINDOW.fill(BGCOLOR)
      for tab in self.listOfTabs:
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
      t.header = Clickable("Race")
      t.header.function = [self.setFocus,self.setFocus]
      t.header.functionArgs = [["race"],["subrace"]]
      listOfClickables = [Clickable("Dwarf"), Clickable("Elf"), Clickable("Halfling"), Clickable("Human"), Clickable("Dragonborn"), Clickable("Drow"), Clickable("Gnome"), Clickable("Halfelf"), Clickable("Halforc"), Clickable("Kender"), Clickable("Tiefling"), Clickable("Warforged")]
      self.setSpacing(listOfClickables,(110,0))
      nameWidth = 105
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

      #defining function for the subrace clickable
      t.listOfClickables = listOfClickables
      
      t.listOfPages.append(sectionGnomeSubRace)
      t.listOfPages.append(sectionHalflingSubRace)
      t.listOfPages.append(sectionElfSubRace)
      t.listOfPages.append(sectionDwarfSubRace)
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
      xPageStart = 215
      yPageStart = 5
      nameWidth = 105
      longNameWidth = 155
      numberWidth = 20
      longNumberWidth = 55
      descriptionWidth = 800
      #-----Default Section-----------------------------------------------------------------
      # Player Name  ______________             Character Name ______________              |
      # Race         ______________             Class (level)  ______________              |
      # Vision       ______________             Alignment      ______________              |
      #-------------------------------------------------------------------------------------
      sectionBasics = Page()
      sectionBasics.text = "basics"
      sectionBasics.boundaries = (xPageStart-5,yPageStart-5,(nameWidth+5)*3+(longNameWidth+5)+5,65)
      raceLabel = VariableLabel(self.character.race)
      classLabel = VariableLabel(self.character.classLevels)
      basicColumns = [[Label("Player Name"), Label("Race"), Label("Vision")],
                      [TextBox(""), raceLabel, Label("")],
                      [Label("Character Name"), Label("Class(level)"), Label("Alignment")],
                      [TextBox(""), classLabel, Label("")]]
      columnWidthList = [nameWidth,longNameWidth,nameWidth,nameWidth]
      self.setHorizontalSpacing(sectionBasics,basicColumns,(xPageStart,yPageStart),columnWidthList)
      
      #-------------------------------------------------------------------------------------
      # Strength     _______ _______           Intelligence   _______ _______              |
      # Constitution _______ _______           Wisdom         _______ _______              |
      # Dexterity    _______ _______           Charisma       _______ _______              |
      #-------------------------------------------------------------------------------------
      sectionAttibutes = Page()
      sectionAttibutes.text = "attributes"
      sectionAttibutes.boundaries = (xPageStart-5+(nameWidth+5)*3+(longNameWidth+5)+5,yPageStart-5,(nameWidth+5)*2+(numberWidth+5)*4+5 ,65)
      attributeColumns = [[Label("Strength"), Label("Constitution"), Label("Dexterity")],
                          [Label(""), Label(""), Label("")],
                          [Label(""), Label(""), Label("")],
                          [Label("Intelligence"), Label("Wisdom"), Label("Charisma")],
                          [Label(""), Label(""), Label("")],
                          [Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth,numberWidth,numberWidth,nameWidth,numberWidth,numberWidth]
      self.setHorizontalSpacing(sectionAttibutes,attributeColumns,(xPageStart+(nameWidth+5)*3+(longNameWidth+5)+5,yPageStart),columnWidthList)    
      yPageStart = yPageStart + 65
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
      yPageStart = yPageStart + 45
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
      yPageStart = yPageStart + 125
      
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
      yPageStart = yPageStart + 105
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
      yPageStart = yPageStart + 105
      
      #append them to the list in the order in which they should be drawn
      t.listOfPages.append(sectionRacialTraits)
      t.listOfPages.append(sectionClassFeatures)
      t.listOfPages.append(sectionSkills)
      t.listOfPages.append(sectionProficiencies)
      t.listOfPages.append(sectionLanguages)
      t.listOfPages.append(sectionVarious)
      t.listOfPages.append(sectionAttibutes)
      t.listOfPages.append(sectionBasics)
      
      self.listOfTabs.append(t)
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
   def setFocus(self,args):
      if args[0] == "race":
         textToSearchFor = str(self.character.race[0])
      elif args[0] == "subrace":
         textToSearchFor = str(self.character.race[0].subraceString)
      else:
         textToSearchFor = args[0]
      print "searching for: " + str(textToSearchFor)
      for tab in self.listOfTabs:
         for click in tab.listOfClickables:
            if click.text == textToSearchFor:
               click.focused = True
         for page in tab.listOfPages:
            for click in page.listOfClickables:
               if click.text == textToSearchFor:
                  click.focused = True
                  
pygame.key.set_repeat(500,100)
window = creationWindow()   
window.creationLoop()