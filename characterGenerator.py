import random,classes,race
import background
from classes import *
from race import *
from background import *
class Character:
   #Variables
   str = 0;con = 0;dex = 0;int = 0;wis = 0;cha = 0
   hitPoints = 0
   classLevels = []
   proficiency = 0
   background = BaseBackground()
   race = BaseRace("")
   skills = []
   armorClass = 0
   spells = 0
   armorProficiencies = []
   weaponProficiencies = []
   toolProficiencies = []
   def rollDie(self,numberOfSides):
      r = random.randint(1,numberOfSides)
      return r
   def rollStats(self,orderOfStats):
      #get 6 stats
      listOfStats = []
      value = 0
      for i in range(6):
         least = 6
         value = 0
         for j in range(4):
            r = self.rollDie(6)
            if r < least:
               value = value + least
               least = r
            else:
               value = value + r
         value = value - 6 #subtract the inital least value
         listOfStats.append(value)
      listOfStats.sort(reverse=True)
      for i,stat in enumerate(orderOfStats):
         if stat == "str":
            self.str = listOfStats[i]
         elif stat == "con":
            self.con = listOfStats[i]
         elif stat == "dex":
            self.dex = listOfStats[i]
         elif stat == "int":
            self.int = listOfStats[i]
         elif stat == "wis":
            self.wis = listOfStats[i]
         elif stat == "cha":
            self.cha = listOfStats[i]
   #
   def addClassLevel(self,classToLevelUp):
      found = False
      for i in self.classLevels:
         if isinstance(i,classToLevelUp.__class__):
            found = True
            for j in range(classToLevelUp.level):
               i.levelUp()
            if i.level == 1:
               self.hitPoints = i.hitDice + ((self.con - 10)/2)
            else:
               self.hitPoints = self.hitPoints + self.rollDie(i.hitDice) + ((self.con - 10)/2)
      if found == False:
         self.classLevels.append(classToLevelUp)
         self.classLevels[len(self.classLevels)-1].level = classToLevelUp.level
         if self.hitPoints == 0:
            self.hitPoints = self.classLevels[0].hitDice + ((self.con - 10)/2)
         else:
            self.hitPoints = self.hitPoints + self.rollDie(i.hitDice) + ((self.con - 10)/2)
   def choosePath(self,classToChooseFrom,path):
      for i in self.classLevels:
         if isinstance(i,classToChooseFrom.__class__):
            i.choosePath(path)
   def addSkill(self,choice):
      #compile list of possible skills
      for i in self.classLevels:
         if i.skillsToChoose > 0:
            for j in i.possibleSkills:
               if j == choice:
                  i.skillsToChoose = i.skillsToChoose - 1
                  self.skills.append(j)
   def addRace(self,Race):
      self.race = Race
      for i in self.race.abiltyAdjustment:
         if i == "str":
            self.str = self.str + 1
         if i == "con":
            self.con = self.con + 1
         if i == "dex":
            self.dex = self.dex + 1
         if i == "int":
            self.int = self.int + 1
         if i == "wis":
            self.wis = self.wis + 1
         if i == "cha":
            self.cha = self.cha + 1
   def addSubRace(self,choice):
      oldLength = len(self.race.abiltyAdjustment)
      self.race.chooseSubRace(choice)
      if oldLength != len(self.race.abiltyAdjustment):
         i = self.race.abiltyAdjustment[len(self.race.abiltyAdjustment)]
         if i == "str":
            self.str = self.str + 1
         if i == "con":
            self.con = self.con + 1
         if i == "dex":
            self.dex = self.dex + 1
         if i == "int":
            self.int = self.int + 1
         if i == "wis":
            self.wis = self.wis + 1
         if i == "cha":
            self.cha = self.cha + 1
   def addBackground(self,choice):
      self.background = choice
      for i in self.background.skills:
         self.skills.append(i)
   def addToAbility(self,choice):
      incremented = False
      #make sure you can do it
      abilityScoreIncreasesSum = 0
      for i in self.classLevels:
         abilityScoreIncreasesSum = abilityScoreIncreasesSum + i.numberOfAbilitiesToIncrease
      if abilityScoreIncreasesSum != 0:
         #it's valid
         if choice == "str" and self.str < 20:
            self.str = self.str + 1
            incremented = True
         if choice == "con" and self.con < 20:
            self.con = self.con + 1
            incremented = True
         if choice == "dex" and self.dex < 20:
            self.dex = self.dex + 1
            incremented = True
         if choice == "int" and self.int < 20:
            self.int = self.int + 1
            incremented = True
         if choice == "wis" and self.wis < 20:
            self.wis = self.wis + 1
            incremented = True
         if choice == "cha" and self.cha < 20:
            self.cha = self.cha + 1
            incremented = True
      if incremented:
         for i in self.classLevels:
            if i.numberOfAbilitiesToIncrease > 0:
               i.numberOfAbilitiesToIncrease = i.numberOfAbilitiesToIncrease - 1
   
   def combineProficiencies(self):
      #proficiency bonus
      for i in self.classLevels:
         self.proficiency = self.proficiency + i.proficiencyBonusPerLevel[i.level-1]
            
      #armor
      for i in self.classLevels:
         for j in i.armorProficiencies:
            if j not in self.armorProficiencies:
               self.armorProficiencies.append(j)
      #weapons
      for i in self.classLevels:
         for j in i.weaponProficiencies:
            if j not in self.weaponProficiencies:
               self.weaponProficiencies.append(j)
      for i in self.race.weaponProficiencies:
         if i not in self.weaponProficiencies:
            self.weaponProficiencies.append(i)
      #tools
      for i in self.classLevels:
         for j in i.toolProficiencies:
            if j not in self.toolProficiencies:
               self.toolProficiencies.append(j)
      for i in self.background.toolProficiencies:
         if i not in self.toolProficiencies:
            self.toolProficiencies.append(i)
   def __init__(self,orderOfStats,listOfClassesToLevelUp,race,background,listOfSkills):
      self.rollStats(orderOfStats)
      for i in listOfClassesToLevelUp:
         self.addClassLevel(i)
      self.addRace(race)
      self.addBackground(background)
      for i in listOfSkills:
         self.addSkill(i)
      self.combineProficiencies()
   def printStats(self):
      print self.race.raceString
      for i in self.classLevels:
         print "Class: " + i.classString + " Level: " + str(i.level)
      print "HP: " + str(self.hitPoints)
      print "STR:" + str(self.str) + " (" + str((self.str - 10)/2) + ")"
      print "CON:" + str(self.con) + " (" + str((self.con - 10)/2) + ")"
      print "DEX:" + str(self.dex) + " (" + str((self.dex - 10)/2) + ")"
      print "INT:" + str(self.int) + " (" + str((self.int - 10)/2) + ")"
      print "WIS:" + str(self.wis) + " (" + str((self.wis - 10)/2) + ")"
      print "CHA:" + str(self.cha) + " (" + str((self.cha - 10)/2) + ")"
      abilityScoreIncreasesSum = 0
      for i in self.classLevels:
         abilityScoreIncreasesSum = abilityScoreIncreasesSum + i.numberOfAbilitiesToIncrease
      if abilityScoreIncreasesSum != 0:
         print "Ability score increases available = " + str(abilityScoreIncreasesSum)
      print "----------------------------------"
      print "Traits: "
      for i in self.race.traits:
         print i
      for i in self.background.traits:
         print i
      print "----------------------------------"
      print "Class Features:"
      for i in self.classLevels:
         for j in range(i.level):
            #print i.featureList
            #print i.featureListDescriptions
            for feature,descriptions in zip(i.featureList[j],i.featureListDescriptions[j]):
               if feature != "Ability Score Improvement":
                  print feature
                  for descriptionLine in descriptions:
                     print " -" + descriptionLine
      print "----------------------------------"
      print "Proficiencies (+" + str(self.proficiency) + ")"
      print "-Skills"
      for i in self.skills:
         print " " + i      
      print "-Armor:"
      for i in self.armorProficiencies:
         print " " + i
      print "-Weapons:"
      for i in self.weaponProficiencies:
         print " " + i
      print "-Tools:"
      for i in self.toolProficiencies:
         print " " + i
#
orderOfStats = ["str","con","dex","wis","int","cha"]
listOfClasses = [Barbarian(2)]
listOfSkills = ["athletics"]
race = Dwarf("Mountain Dwarf")
c = Character(orderOfStats, listOfClasses, race, Sage, listOfSkills)
c.choosePath(Barbarian(),"Path of the Berserker")
c.printStats()
c.addClassLevel(Barbarian(5))
c.combineProficiencies()
c.printStats()