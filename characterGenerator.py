import random,classes,race,equipment
import background
from classes import *
from race import *
from background import *
from equipment import *

class Character:
   #utilities
   def getAbilityMod(self,ability):
      if ability == "str":
         return (self.str-10)/2
      if ability == "con":
         return (self.con-10)/2
      if ability == "dex":
         return (self.dex-10)/2
      if ability == "int":
         return (self.int-10)/2
      if ability == "wis":
         return (self.wis-10)/2
      if ability == "cha":
         return (self.cha-10)/2
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
   def setStats(self,listOfStats):
      self.str = listOfStats[0]
      self.con = listOfStats[1]
      self.dex = listOfStats[2]
      self.int = listOfStats[3]
      self.wis = listOfStats[4]
      self.cha = listOfStats[5]
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
   #creation utilities
   def combineProficiencies(self):
      #proficiency bonus
      self.proficiency = 0
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
   def combineAc(self):
      self.ac = 0
      maxDex = self.getAbilityMod("dex")
      for armor in self.armors:
         if armor.equipped:
            self.ac = self.ac + armor.ac
            if maxDex > armor.maxDexBonus:
               maxDex = armor.maxDexBonus
      self.ac = self.ac + maxDex
      self.acNoArmor = 10 + self.getAbilityMod("dex")
   def __init__(self,rollForStats=True,listOfStats=[10,10,10,10,10,10],orderOfStats=["str","con","dex","int","wis","cha"],listOfClassesToLevelUp = [Barbarian()],name="Unnamed",race=Dwarf("Mountain Dwarf"),background=Artisan(),listOfSkills=[]):
   
      self.str = 0;self.con = 0;self.dex = 0;self.int = 0;self.wis = 0;self.cha = 0
      self.hitPoints = 0
      self.classLevels = []
      self.totalLevel = 0
      self.proficiency = 0; self.skills = []
      self.background = BaseBackground()
      self.race = BaseRace("")
      self.armorClass = 0
      self.spells = 0
      self.armorProficiencies = []; self.weaponProficiencies = []; self.toolProficiencies = []
      self.weapons = []; self.armors = []; self.tools = []; self.items = []
      self.money = Money()
      self.setCharacterName(name)
      if rollForStats:
         self.rollStats(orderOfStats)
      else:
         self.setStats(listOfStats)
      self.addRace(race)
      self.addBackground(background)
      for i in listOfClassesToLevelUp:
         self.addClassLevel(i)
      for i in listOfSkills:
         self.addSkill(i)
      self.combineProficiencies()
      self.combineAc()
   def printStats(self):
      print self.characterName + " the " + self.race.raceString 
      for i in self.classLevels:
         print "Class: " + str(i) + " Level: " + str(i.level)
      print "HP: " + str(self.hitPoints)
      print "STR:" + str(self.str) + " (" + str((self.str - 10)/2) + ") INT:" + str(self.int) + " (" + str((self.int - 10)/2) + ")"
      print "CON:" + str(self.con) + " (" + str((self.con - 10)/2) + ") WIS:" + str(self.wis) + " (" + str((self.wis - 10)/2) + ")"
      print "DEX:" + str(self.dex) + " (" + str((self.dex - 10)/2) + ") CHA:" + str(self.cha) + " (" + str((self.cha - 10)/2) + ")"
      print "AC = " + str(self.ac) + ", AC (No Armor) = " + str(self.acNoArmor)
      abilityScoreIncreasesSum = 0
      for i in self.classLevels:
         abilityScoreIncreasesSum = abilityScoreIncreasesSum + i.numberOfAbilitiesToIncrease
      if abilityScoreIncreasesSum != 0:
         print "Ability score increases available = " + str(abilityScoreIncreasesSum)
      print "----------------------------------"
      print "Money"
      if self.money.useElectrum == True:
         print "pp: " + str(self.money.pp) + " gp:" + str(self.money.gp) + " ep:" + str(self.money.ep) + " sp:" + str(self.money.sp) + " cp:" + str(self.money.cp)
      else:
         print "pp: " + str(self.money.pp) + " gp:" + str(self.money.gp) + " sp:" + str(self.money.sp) + " cp:" + str(self.money.cp)
      print "Total value: " + str(self.money.getTotalInCopper()) + " cp"
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
            for feature,descriptions in zip(i.featureList[j],i.featureListDescriptions[j]):
               if feature != "Ability Score Improvement":
                  print feature
                  for descriptionLine in descriptions:
                     print " -" + descriptionLine
      print "----------------------------------"
      print "Proficiencies (+" + str(self.proficiency) + ")"
      if len(self.skills) != 0:
         print "-Skills"
         for i in self.skills:
            print " " + i      
      if len(self.armorProficiencies) != 0:
         print "-Armor:"
         for i in self.armorProficiencies:
            print " " + i
      if len(self.weaponProficiencies) != 0:
         print "-Weapons:"
         for i in self.weaponProficiencies:
            print " " + i
      if len(self.toolProficiencies) != 0:
         print "-Tools:"
         for i in self.toolProficiencies:
            print " " + i
      print "----------------------------------"
      totalWeight = 0
      for i in self.armors:
         if i.carried == True:
            totalWeight = totalWeight + i.weight
      for i in self.weapons:
         if i.carried == True:
            totalWeight = totalWeight + i.weight
      for i in self.tools:
         if i.carried == True:
            totalWeight = totalWeight + i.weight
      for i in self.items:
         if i.carried == True:
            totalWeight = totalWeight + i.weight
      carriedBuffer = []
      carriedBuffer.append("Carried Items (" + str(totalWeight) + " lbs)")
      if len(self.armors) != 0:
         buffer = []
         buffer.append("-Armor:")
         for i in self.armors:
            if i.equipped == True:
               buffer.append(" (E)" + str(i))
            elif i.carried == True:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               carriedBuffer.append(i)
      if len(self.weapons) != 0:
         buffer = []
         buffer.append("-Weapons:")
         for i in self.weapons:
            if i.equipped == True:
               buffer.append(" (E)" + str(i))
               buffer.append("  base damage: " + str(i.damageDieNumber) + "d" + str(i.damageDieType) + " ("+str(i.damageType)+")")
               if i.specialRules != "":
                  buffer.append("Special rules: " + str(i.specialRules))
            elif i.carried == True:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               carriedBuffer.append(i)
      if len(self.tools) != 0:
         buffer = []
         buffer.append("-Tools:")
         for i in self.weapons:
            if i.carried == True:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               carriedBuffer.append(i)
      if len(self.items) != 0:
         buffer = []
         buffer.append("-Items:")
         for i in self.weapons:
            if i.carried == True:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               carriedBuffer.append(i)
      if len(carriedBuffer) > 1:
         for i in carriedBuffer:
            print i
            
      nonCarriedBuffer = []
      nonCarriedBuffer.append("Non-carried Items")
      if len(self.armors) != 0:
         buffer = []
         buffer.append("-Armor:")
         for i in self.armors:
            if i.carried == False:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               nonCarriedBuffer.append(i)
      if len(self.weapons) != 0:
         buffer = []
         buffer.append("-Weapons:")
         for i in self.weapons:
            if i.carried == False:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               nonCarriedBuffer.append(i)
      if len(self.tools) != 0:
         buffer = []
         buffer.append("-Tools:")
         for i in self.tools:
            if i.carried == False:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               nonCarriedBuffer.append(i)
      if len(self.items) != 0:
         buffer = []
         buffer.append("-Items:")
         for i in self.items:
            if i.carried == False:
               buffer.append(" " + str(i))
         if len(buffer) > 1:
            for i in buffer:
               nonCarriedBuffer.append(i)
      if len(nonCarriedBuffer) > 1:
         for i in nonCarriedBuffer:
            print i
      print "----------------------------------"
   #classes
   def addClassLevel(self,classToLevelUp):
      foundAt = self.findClassLevel(classToLevelUp) 
      if foundAt != -1:
         i = self.classLevels[foundAt]
      else:
         self.classLevels.append(classToLevelUp.__class__())   #add the class (level 1)
         i = self.classLevels[len(self.classLevels)-1]
         if self.totalLevel == 0:
            self.hitPoints = self.hitPoints + i.hitDice + self.getAbilityMod("con")
         else:
            self.hitPoints = self.hitPoints + self.rollDie(i.hitDice) + self.getAbilityMod("con")
         classToLevelUp.level = classToLevelUp.level -1        #reduce the amount leveled up by 1
         self.totalLevel = self.totalLevel + 1
      for j in range(classToLevelUp.level):
         i.levelUp()
         self.totalLevel = self.totalLevel + 1
         self.hitPoints = self.hitPoints + self.rollDie(i.hitDice) + self.getAbilityMod("con")
   def findClassLevel(self,classToFind):
      index = -1
      for i,cl in enumerate(self.classLevels):
         if str(cl) == str(classToFind):
            index = i
      return index
   def choosePath(self,classToChooseFrom,path):
      index = self.findClassLevel(classToChooseFrom)
      if index != -1:
         self.classLevels[index].choosePath(path)
   def callClassFunction(self,function,arguments):
      if function == "chooseAnimals":
         #find barbarian classlevel
         index = self.findClassLevel(Barbarian())
         if index != -1:
            self.classLevels[index].chooseAnimals(arguments)
      elif function == "chooseLand":
         #find druid classlevel
         index = self.findClassLevel(Druid())
         if index != -1:
            self.classLevels[index].chooseLand(arguments)
      elif function == "chooseFightingStyle":
         #find fighter/paladin/ranger classlevel
         index  = self.findClassLevel(Fighter())
         index2 = self.findClassLevel(Paladin())
         index3 = self.findClassLevel(Ranger())
         if index != -1:
            self.classLevels[index].chooseFightingStyle(arguments)
         elif index2 != -1:
            self.classLevels[index2].chooseFightingStyle(arguments)
         elif index != -1:
            self.classLevels[index3].chooseFightingStyle(arguments)
      elif function == "chooseElements":
         #find Monk classlevel
         index = self.findClassLevel(Monk())
         if index != -1:
            self.classLevels[index].chooseElements(arguments)
   #name
   def setCharacterName(self,name):
      self.characterName = name
   #races
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
   #backgrounds/skills
   def addBackground(self,background):
      self.background = background
      for i in self.background.skills:
         self.skills.append(i)
   def addSkill(self,choice):
      #compile list of possible skills
      for i in self.classLevels:
         if i.skillsToChoose > 0:
            for j in i.possibleSkills:
               if j == choice:
                  i.skillsToChoose = i.skillsToChoose - 1
                  self.skills.append(j)
   #equipment
   def buyItem(self,item):
      try:
         self.money.subtract(item.value)
         self.addItem(item)
      except NotEnoughMoneyException:
         print "Could not buy " + str(item) + " -- Not enough money!"
   def addItem(self,item):
      if isinstance(item,Weapon):
         self.weapons.append(item)
      elif isinstance(item,Armor):
         self.armors.append(item)
      elif isinstance(item,Tool):
         self.tools.append(item)
      else:
         self.items.append(item)
   def findItem(self,item):
      index = -1
      if isinstance(item,Weapon):
         searchthough = self.weapons 
      elif isinstance(item,Armor):
         searchthough = self.armors 
      elif isinstance(item,Tool):
         searchthough = self.tools 
      else:
         searchthough = self.items 
      for i,cl in enumerate(searchthough):
         if isinstance(cl,item.__class__):
            index = i
      return index
   def equipItem(self,item):
      index = -1
      if isinstance(item,Weapon) or isinstance(item,Armor):
         index = self.findItem(item)
      if index != -1:
         if isinstance(item,Weapon):
            self.weapons[index].equipped = True
            self.weapons[index].carried = True
         elif isinstance(item,Armor):
            self.armors[index].equipped = True
            self.armors[index].carried = True
   def buyEquip(self,item):
      self.buyItem(item)
      self.equipItem(item)
         
orderOfStats = ["str","con","dex","wis","int","cha"]
listOfClasses = [Fighter()]
listOfSkills = ["athletics"]
race = Dwarf("Mountain Dwarf")
c = Character(False,[11,18,18,11,11,11],[], listOfClasses, "Urist", race, Sage, listOfSkills)
c.money.useElectrum = False
c.money = Money(256004,0,0,0,0,False)
c.buyEquip(BattleAxe())
c.buyEquip(ChainMail())
c.buyItem(Shield())
c.combineAc()
#c.printStats()