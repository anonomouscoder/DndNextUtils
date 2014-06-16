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
class Page():
   def __init__(self,clickables = []):
      self.boundaries = (0,0,0,0)
      self.backgroundColor = GREY
      self.listOfClickables = clickables
   def display(self):
      (x,y,l,h) = self.boundaries
      pygame.draw.rect(MAINWINDOW, self.backgroundColor,  self.boundaries) 
      for click in self.listOfClickables:
         click.display()
#Add a bunch of clickables to a Tab
class Tab():
   def __init__(self):
      self.header = ""
      self.listOfClickables = []
      self.listOfPages = []
      self.focused = False
   def display(self):
      for i in self.listOfClickables:
         i.display()
      for i in self.listOfPages:
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
      #-----Default Section-----------------------------------------------------------------------------------
      # Player Name ______________ Character Name ______________ | Strength     ___ ___ Intelligence ___ ___ |
      # Race        ______________ Class (level)  ______________ | Constitution ___ ___ Wisdom       ___ ___ |
      # Vision      ______________ Alignment      ______________ | Dexterity    ___ ___ Charisma     ___ ___ |
      #---------------------------------------------------------------------------------------------------------------------------------------
      # Exp(Next)         _______ _______ | Hp        ___ ___ | Initiative ___ | Languages      ______________ ______________ ______________ |
      # AC (no armor)     _______ _______ | Hit dice  ___ ___ | Speed      ___ | ______________ ______________ ______________ ______________ |
      #---------------------------------------------------------------------------------------------------------------------------------------
      # Proficiency bonus ______________ ______________ | ___ Acrobatics(DEX)     ___ Insight(WIS)      ___ Persuasion(CHA)      |
      # Saving Throws     ______________ ______________ | ___ Animal Handling(WIS)___ Intimidation(CHA) ___ Religion(INT)        |
      # Tools             ______________ ______________ | ___ Arcana(INT)         ___ Medicine(WIS)     ___ Search(INT)          |
      # Armor             ______________ ______________ | ___ Athletics(STR)      ___ Nature(INT)       ___ Sleight of Hand(DEX) |
      # Weapon            ______________ ______________ | ___ Deception(CHA)      ___ Perception(WIS)   ___ Stealth(DEX)         |
      #                                                   ___ History(INT)        ___ Performance(CHA)  ___ Survival(WIS)        |
      #---------------------------------------------------------------------------------------------------------------------------
      # Class Features Description                                                         |
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      #-------------------------------------------------------------------------------------
      # Racial Traits  Description                                                         |
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      # ______________ ____________________________________________________________________|
      #-------------------------------------------------------------------------------------
      
      # -----Weapon Section-------------------------
      # Weapon Attacks                             | 
      # Name            Attack   Damage   Type     | 
      # ______________  ___      _______  _______  | 
      # ______________  ___      _______  _______  | 
      # ______________  ___      _______  _______  | 
      # ______________  ___      _______  _______  | 
      # --------------------------------------------
      
      # -----Spell Section---------------------------------------------------------------------
      # Spell attacks                                                                         |
      # Name            Attack   Damage                                                       |
      # ______________  _______  _______                                                      |
      # ______________  _______  _______                                                      |
      # ______________  _______  _______                                                      |
      # ______________  _______  _______                                                      |
      # ---------------------------------------------------------------------------------------
      # Spell DC ___                                                                      |
      # # Spells per day    Spells Used                                                       |  
      # 1 _______           _______                                                           |
      # 2 _______           _______                                                           |
      # 3 _______           _______                                                           |
      # 4 _______           _______                                                           |
      # 5 _______           _______                                                           |
      # 6 _______           _______                                                           |
      # 7 _______           _______                                                           |
      # 8 _______           _______                                                           |
      # 9 _______           _______                                                           |
      # ---------------------------------------------------------------------------------------
      # Known Spells                                                                          |
      # # Names                                                                               |
      # c ___________________________________________________________________________________ |
      # 1 ___________________________________________________________________________________ |
      # 2 ___________________________________________________________________________________ |
      # 3 ___________________________________________________________________________________ |
      # 3 ___________________________________________________________________________________ |
      # 4 ___________________________________________________________________________________ |
      # 5 ___________________________________________________________________________________ |
      # 6 ___________________________________________________________________________________ |
      # 7 ___________________________________________________________________________________ |
      # 8 ___________________________________________________________________________________ |
      # 9 ___________________________________________________________________________________ |
      # ---------------------------------------------------------------------------------------
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
      sectionBasics.boundaries = (xPageStart-5,yPageStart-5,990,65)
      basicColumns = [[Label("Player Name"), Label("Race"), Label("Vision")],
                      [Label(""), Label(""), Label("")],
                      [Label("Character Name"), Label("Class(level)"), Label("Alignment")],
                      [Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth,nameWidth,nameWidth,nameWidth]
      self.setHorizontalSpacing(sectionBasics,basicColumns,(xPageStart,yPageStart),columnWidthList)
      
      t.listOfPages.append(sectionBasics)
      #-------------------------------------------------------------------------------------
      # Strength     _______ _______           Intelligence   _______ _______              |
      # Constitution _______ _______           Wisdom         _______ _______              |
      # Dexterity    _______ _______           Charisma       _______ _______              |
      #-------------------------------------------------------------------------------------
      sectionAttibutes = Page()
      sectionAttibutes.boundaries = (xPageStart-5+(nameWidth+5)*4+5,yPageStart-5,990,65)
      attributeColumns = [[Label("Strength"), Label("Constitution"), Label("Dexterity")],
                          [Label(""), Label(""), Label("")],
                          [Label(""), Label(""), Label("")],
                          [Label("Intelligence"), Label("Wisdom"), Label("Charisma")],
                          [Label(""), Label(""), Label("")],
                          [Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth,numberWidth,numberWidth,nameWidth,numberWidth,numberWidth]
      self.setHorizontalSpacing(sectionAttibutes,attributeColumns,(xPageStart+(nameWidth+5)*4+5,yPageStart),columnWidthList)
      t.listOfPages.append(sectionAttibutes)      
      yPageStart = yPageStart + 65
      #-------------------------------------------------------------------------------------
      # Experience (Next) _______ _______ | Hp        _______ _______ | Initiative _______ |
      # AC (no armor)     _______ _______ | Hit dice  _______ _______ | Speed      _______ |
      #-------------------------------------------------------------------------------------
      sectionVarious = Page()
      sectionVarious.boundaries = (xPageStart-5,yPageStart-5,990,45)
      variousColumns = [[Label("Exp, Next"), Label("AC, no Armor")],
                        [Label(""), Label("")],
                        [Label(""), Label("")],
                        [Label("HP"), Label("Hit Dice")],
                        [Label(""), Label("")],
                        [Label(""), Label("")],
                        [Label("Initiative"), Label("Speed")],
                        [Label(""), Label("")]]
      columnWidthList = [nameWidth,
                         longNumberWidth,
                         longNumberWidth,
                         nameWidth,
                         numberWidth,
                         numberWidth,
                         nameWidth,
                         numberWidth]
      self.setHorizontalSpacing(sectionVarious,variousColumns,(xPageStart,yPageStart),columnWidthList)
      t.listOfPages.append(sectionVarious)      
      #-------------------------------------------------------------------------------------
      # Languages      ______________ ______________ ______________ ______________         |
      # ______________ ______________ ______________ ______________ ______________         |
      #-------------------------------------------------------------------------------------
      sectionLanguages = Page()
      sectionLanguages.boundaries = (xPageStart-5+(nameWidth+5)*3+(longNumberWidth+5)*2+(numberWidth+5)*3+5,yPageStart-5,990,45)
      languageColumns = [[Label("Languages"), Label("")],
                         [Label(""), Label("")],
                         [Label(""), Label("")],
                         [Label(""), Label("")]]
      columnWidthList = [nameWidth,
                         nameWidth,
                         nameWidth,
                         nameWidth]
      self.setHorizontalSpacing(sectionLanguages,languageColumns,(xPageStart+(nameWidth+5)*3+(longNumberWidth+5)*2+(numberWidth+5)*3+5,yPageStart),columnWidthList)
      t.listOfPages.append(sectionLanguages)
      yPageStart = yPageStart + 45
      #-------------------------------------------------------------------------------------
      # Proficiency bonus _______                                                          |
      # Saving Throws   ______________ ______________                                      |
      # Tools           ______________ ______________                                      |
      # Armor           ______________ ______________                                      |
      # Weapon          ______________ ______________                                      |
      #-------------------------------------------------------------------------------------
      sectionProficiencies = Page()
      sectionProficiencies.boundaries = (xPageStart-5,yPageStart-5,longNameWidth+nameWidth*2+5*4,125)
      proficiencyColumns = [[Label("Proficiency bonus"), Label("Saving Throws"), Label("Tools"), Label("Armor"), Label("Weapon")],
                            [Label(""), Label(""), Label(""), Label(""), Label("")],
                            [Label(""), Label(""), Label(""), Label(""), Label("")]]
      columnWidthList = [longNameWidth,
                         nameWidth,
                         nameWidth]
      self.setHorizontalSpacing(sectionProficiencies,proficiencyColumns,(xPageStart,yPageStart),columnWidthList)
      t.listOfPages.append(sectionProficiencies)
      #-------------------------------------------------------------------------------------
      # _______ Acrobatics(DEX)     _______ Insight(WIS)      _______ Persuasion(CHA)      |
      # _______ Animal Handling(WIS)_______ Intimidation(CHA) _______ Religion(INT)        |
      # _______ Arcana(INT)         _______ Medicine(WIS)     _______ Search(INT)          |
      # _______ Athletics(STR)      _______ Nature(INT)       _______ Sleight of Hand(DEX) |
      # _______ Deception(CHA)      _______ Perception(WIS)   _______ Stealth(DEX)         |
      # _______ History(INT)        _______ Performance(CHA)  _______ Survival(WIS)        |
      #------------------------------------------------------------------------------------|
      sectionSkills = Page()
      
      sectionSkills.boundaries = (xPageStart-5+longNameWidth+nameWidth*2+5*4,yPageStart-5,990,125)
      skillsColumns = [[Label(""), Label(""), Label(""), Label(""), Label(""), Label("")],
                       [Label("Acrobatics(DEX)"), Label("Animal Handling(WIS)"), Label("Arcana(INT)"), Label("Athletics(STR)"), Label("Deception(CHA)"), Label("History(INT)")],
                       [Label(""), Label(""), Label(""), Label(""), Label(""), Label("")],
                       [Label("Insight(WIS)"), Label("Intimidation(CHA)"), Label("Medicine(WIS)"), Label("Nature(INT)"), Label("Perception(WIS)"), Label("Performance(CHA)")],
                       [Label(""), Label(""), Label(""), Label(""), Label(""), Label("")],
                       [Label("Persuasion(CHA)"), Label("Religion(INT)"), Label("Search(INT)"), Label("Sleight of Hand(DEX)"), Label("Stealth(DEX)"), Label("Survival(WIS)")]]
      columnWidthList = [numberWidth,
                         longNameWidth,
                         numberWidth,
                         longNameWidth,
                         numberWidth,
                         longNameWidth]
      self.setHorizontalSpacing(sectionSkills,skillsColumns,(xPageStart+longNameWidth+nameWidth*2+5*4,yPageStart),columnWidthList)
      t.listOfPages.append(sectionSkills)
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
      sectionClassFeatures.boundaries = (xPageStart-5,yPageStart-5,990,105)
      featureColumns = [[Label("Class Features"), Label(""), Label(""), Label(""), Label("")],
                        [Label("Descriptions"), Label(""), Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth,
                         descriptionWidth]
      self.setHorizontalSpacing(sectionClassFeatures,featureColumns,(xPageStart,yPageStart),columnWidthList)
      t.listOfPages.append(sectionClassFeatures)
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
      sectionRacialTraits.boundaries = (xPageStart-5,yPageStart-5,990,105)
      traitColumns = [[Label("Racial Traits"), Label(""), Label(""), Label(""), Label("")],
                      [Label("Descriptions"), Label(""), Label(""), Label(""), Label("")]]
      columnWidthList = [nameWidth,
                         descriptionWidth]
      self.setHorizontalSpacing(sectionRacialTraits,traitColumns,(xPageStart,yPageStart),columnWidthList)
      t.listOfPages.append(sectionRacialTraits)
      yPageStart = yPageStart + 105
      
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
               char = event.unicode
               self.menuKeyboardDown(char)
            if mouseClicked == True:
               self.menuMouseClickedLogic(mousex,mousey)
      pygame.quit()
      sys.exit()
      
window = creationWindow()   
window.creationLoop()
time.sleep(4)