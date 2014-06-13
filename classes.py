import string

class BaseClass:
   def __str__(self):
      return (string.split(str(self.__class__),".",1))[1]
   hitDice = 8
   proficiencyBonusPerLevel =   [1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6]
   numberOfAbilitiesToIncrease = 0
   spellsPerDayPerLevel = [[0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0]]
   featureList = [[],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  [],
                  []]
   featureListDescriptions = [[],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              [],
                              []]
   #Called to increment the level, and update the list of features, or change variables upon leveling up, if needed
   def levelUp(self):
      self.level = self.level + 1
      if "Ability Score Improvement" in self.featureList[self.level-1]:
         self.numberOfAbilitiesToIncrease = self.numberOfAbilitiesToIncrease + 2
      self.updateFeatures()
   def setFeatureList(self,index,value,description,secondIndex=""):
      if secondIndex != "":
         (self.featureList[index])[secondIndex] = value
         (self.featureListDescriptions[index])[secondIndex] = description
      else:
         self.featureList[index] = value
         self.featureListDescriptions[index] = description
   #used for classes that have numerical amounts in features that increase based on level (sneak attack goes from 1d6 to 7d6)
   def updateFeatures(self):
      return

   #Paths are used when the character has to choose between groups of features (Path of the Beserker vs Path of the Totem Warrior)
   pathsToChoose = []
   pathChosen = ""
   def choosePath(self,choice): 
      return
   
   #The constructor allows a level to be inputted so that you can create a lvl 5 character easily
   def __init__(self,level=1):
      self.level = 1
      self.armorProficiencies = []
      self.weaponProficiencies = []
      self.toolProficiencies = []
      self.savingThrows = []
      self.possibleSkills = []
      self.numberOfAttacks = 1
      self.skillsToChoose = 0
      for l in range(1,level):
         self.levelUp()
#
class Barbarian(BaseClass):
   hitDice = 12
   ragesPerLevel =               [2,2,3,3,3,4,4,4,4,4,4,5,5,5,5,5,6,6,6,99]
   rageDamagePerLevel =          [2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4]
   featureList = [["Rage (2/rest, +2 dmg)","Thick Hide"],
                  ["Feral Instinct","Reckless Attack"],
                  ["Barbarian Path"],
                  ["Ability Score Improvement"],
                  ["Extra Attack","Fast Movement"],
                  ["Path Feature"],
                  ["Feral Reflexes"],
                  ["Brutal Critical"],
                  ["Ability Score Improvement"],
                  ["Path feature"],
                  ["Relentless Rage"],
                  ["Furious Resilience"],
                  ["Ability Score Improvement"],
                  ["Path feature"],
                  ["Simmering Rage"],
                  ["Ability Score Improvement"],
                  ["Will to Live"],
                  ["Ability Score Improvement"],
                  ["Primal Might"],
                  ["Death-Defying Rage"]]
   featureListDescriptions = [[["ADV on Strength checks and Saving throws","Gain temporary hitpoints = 2*Barbarian level"],["if no armor: AC = 10 + DexMod + ConMod"]],
                              [["ADV on Initiative"],["ADV on Attack rolls, if not raging: enemies get ADV on attack rolls"]],
                              [["Path of Beserker", "Path of Totem Warrior"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["You can attack an extra time"],["You gain 10 Speed while wearing light, medium, or no armor"]],
                              [[""]],
                              [["Take a turn during a surprise round if you rage that round"]],
                              [["Roll an additional damage die for critical hits"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["Raging + drop to 0 hp and don't die, DC10 Con check: pass = 1 hp instead"]],
                              [["ADV on raging saving throws"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["Rage can last through a full boring turn"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["ADV on death rolls"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Minimum total for any Strength check or saving throw is your strength score"]],
                              [["Raging prevents unconsciousness", "6 death roll failures required to die during this"]]]
   def updateFeatures(self):   
      self.featureList[0] = ["Rage ("+str(self.ragesPerLevel[self.level-1])+"/rest, +"+str(self.rageDamagePerLevel[self.level-1])+" dmg)","Thick Hide"]

   pathsToChoose = ["Path of the Berserker","Path of the Totem Warrior"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Path of the Berserker
         self.pathChosen = choice
         self.featureList[2] = ["Fearless Rage"]
         self.featureListDescriptions[2] = [["Immune to fear while raging"]]
         self.featureList[5] = ["Mindless Rage"]
         self.featureListDescriptions[5] = [["Immune to charm while raging"]]
         self.featureList[9] = ["Unchecked Fury"]
         self.featureListDescriptions[9] = [["If you miss a melee attack, immediately make one retry"]]
         self.featureList[13] = ["Brutal Rage"]
         self.featureListDescriptions[13] = [["You may take 5 damage at start of a raging turn. If you do, add another weapon damage die"]]
         
      elif choice == self.pathsToChoose[1]: # Path of the Totem Warrior
         self.pathChosen = choice
         self.featureList[2] = ["Totem Spirit: " + str(self.animalChosen[0])]
         self.featureListDescriptions[2] = ["Bear","Cougar","Hawk","Wolf"]
         if self.animalChosen[0] == self.animalToChoose[0]: #Bear
            self.featureListDescriptions[2] = [["Roll hitdice twice when regaining health"]]
         elif self.animalChosen[0] == self.animalToChoose[1]:#Cougar
            self.featureListDescriptions[2] = [["Speed increases 5","You gain proficiency in acrobatics"]]
         elif self.animalChosen[0] == self.animalToChoose[2]:#Hawk
            self.featureListDescriptions[2] = [["Jump double your normal distance","ADV on Raging dex-based attack rolls"]]
         elif self.animalChosen[0] == self.animalToChoose[3]:#Wolf
            self.featureListDescriptions[2] = [["You gain proficiency in perception"]]
         self.featureList[5] = ["Spirit Rage: " + str(self.animalChosen[1])]
         self.featureListDescriptions[5] = ["Bear","Cougar","Hawk","Wolf"]
         if self.animalChosen[1] == self.animalToChoose[0]: #Bear
            self.featureListDescriptions[5] = [["You may expend up to 2 hitdice to regain HP when entering rage"]]
         elif self.animalChosen[1] == self.animalToChoose[1]:#Cougar
            self.featureListDescriptions[5] = [["While raging, opportunity attacks have DISADV against you"]]
         elif self.animalChosen[1] == self.animalToChoose[2]:#Hawk
            self.featureListDescriptions[5] = [["While raging, you have resistance to falling damage","Jump triple your normal distance"]]
         elif self.animalChosen[1] == self.animalToChoose[3]:#Wolf
            self.featureListDescriptions[5] = [["While raging, you sense the location of any creature within 15 feet"]]
         self.featureList[9] = ["Spirit Vitality"]
         self.featureListDescriptions[9] = [["While raging, regain 5 HP if you are at less than half health"]]
         self.featureList[13] = ["Guiding Totem"]
         self.featureListDescriptions[13] = [["You gain proficiency in Wisdom saving throws","Hidden threats do not gain ADV on you"]]

   animalToChoose = ["Bear","Cougar","Hawk","Wolf"]
   animalChosen = ["",""]
   def chooseAnimals(self,choices):
      totem,rage = choices
      if totem == self.animalToChoose[0] or totem == self.animalToChoose[1] or totem == self.animalToChoose[2] or totem == self.animalToChoose[3]:
         self.animalChosen[0] = totem
      if rage == self.animalToChoose[0] or rage == self.animalToChoose[1] or rage == self.animalToChoose[2] or rage == self.animalToChoose[3]:
         self.animalChosen[1] = rage

   def __init__(self,level=1):
      self.armorProficiencies = ["light","medium","shields"]
      self.weaponProficiencies = ["simple","martial"]
      self.toolProficiencies = ["landMount"]
      self.savingThrows = []
      self.possibleSkills = []
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Bard(BaseClass):
   hitDice = 6
   spellsKnownPerLevel =         [0,2,3,3,4,4,5,5,6,6,7,7, 8, 8, 9, 9,10,10,11,11]
   callToBattleDieUsed =         [4,4,4,4,4,6,6,6,8,8,8,8,10,10,10,10,12,12,12,12]
   spellsPerDayPerLevel = [[0,0,0,0,0],
                           [2,0,0,0,0],
                           [3,0,0,0,0],
                           [3,0,0,0,0],
                           [4,2,0,0,0],
                           [4,2,0,0,0],
                           [4,3,0,0,0],
                           [4,3,0,0,0],
                           [4,3,2,0,0],
                           [4,3,2,0,0],
                           [4,3,3,0,0],
                           [4,3,3,0,0],
                           [4,3,3,1,0],
                           [4,3,3,1,0],
                           [4,3,3,2,0],
                           [4,3,3,2,0],
                           [4,3,3,3,1],
                           [4,3,3,3,1],
                           [4,3,3,3,2],
                           [4,3,3,3,2]]
   featureList = [["Bardic Knowledge","Bardic Performance"],
                  ["Spellcasting"],
                  ["Bard College", "Expertise"],
                  ["Ability Score Improvement"],
                  ["Jack of All Trades"],
                  ["Bard College Benefit"],
                  ["Countercharm"],
                  ["Extra Attack"],
                  [],
                  ["Ability Score Improvement"],
                  ["Battle Magic"],
                  ["Bard College Benefit"],
                  [],
                  ["Ability Score Improvement"],
                  ["Bard College Benefit"],
                  ["Improved Dispel"],
                  [],
                  ["Bard College Benefit"],
                  ["Ability Score Improvement"],
                  ["Magical Secrets"]]

   featureListDescriptions = [[["Inteligence checks of 9 or lower are a 10, if they pertain to Arcana, History, Nature, or Religion"],["Call To Battle = + 1d4 to damage rolls","Inspire Competence = Add your proficiency bonus to one of the 6 abilities","Range: 25ft, Duration: 10m, Needs concentration and voice"]],
                              [["DC = 8 + CHA mod", "If you hold an instrument, Add proficency bonus to DC","2 Cantrips known"]],
                              [["College of Valor", "College of Wit"],["Gain +5 bonus to any 4 skill or tool proficiencies"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Add half of your proficiency bonus to skills that you are not proficient in"]],
                              [[""]],
                              [["Bardic performance: Affected creatures have advantage on saving throws against charm or fright"]],
                              [["You can attack an extra time"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Any Bard spell with casting time of 1 action now takes 1 swift action"]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["Learn the dispel magic spell","Double proficiency bonus for this spell"]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Learn 5 spells from any spellbook (cantrip - lvl5 only) as Bard spells"]]]
   def updateFeatures(self):
      self.featureListDescriptions[0] = [["Inteligence checks of 9 or lower are a 10, if they pertain to Arcana, History, Nature, or Religion"],["Call To Battle = + 1d"+str(self.callToBattleDieUsed[self.level])+" to damage rolls","Inspire Competence = Add your proficiency bonus to one of the 6 abilities","Range: 25ft, Duration: 10m, Needs concentration and voice"]]
      if self.pathChosen == "College of Valor":
         self.featureListDescriptions[5] = [["Give allies = + 1d"+str(self.callToBattleDieUsed[self.level])+" more HP during short rests"]]
         
   pathsToChoose = ["College of Valor", "College of Wit"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # College of Valor
         self.pathChosen = choice
         self.armorProficiencies = ["light","medium"]
         self.weaponProficiencies = ["simple","martial"]
         self.featureList[2] = ["War College Training", "Expertise"]
         self.featureListDescriptions[2] = [["Per turn you can use the help action as part of the attack action"],["Gain +5 bonus to any 4 skill or tool proficiencies"]]
         self.featureList[5] = ["Song of Rest"]
         self.featureListDescriptions[5] = [["Give allies = + 1d"+str(self.callToBattleDieUsed[self.level])+" more HP during short rests"]]
         self.featureList[11] = ["Coordinate Allies"]
         self.featureListDescriptions[11] = [["Use reaction to give advantage to attack against a specific creature that has been attacked"]]
         self.featureList[14] = ["Words of Warning"]
         self.featureListDescriptions[14] = [["Use reaction to give advantage to allies Strength, Dexterity, or Wisdom saving throw"]]
         self.featureList[17] = ["Rally"]
         self.featureListDescriptions[17] = [["Learn cure mass wounds, cast it 1/day for free","This spell removes charm, fright, paralysis, and stun. Everyone can stand up or move its speed"]]
         
      elif choice == self.pathsToChoose[1]: # College of Wit
         self.pathChosen = choice
         self.featureList[2] = ["Fascinating Performance", "Expertise"]
         self.featureListDescriptions[2] = [["Charm non-hostile creatures within 50ft","Combat breaks effect"],["Gain +5 bonus to any 4 skill or tool proficiencies"]]
         self.featureList[5] = ["Eviscerating Wit"]
         self.featureListDescriptions[5] = [["Plant doubt (disadvantage on all ability checks) to all hostile creatures in 50ft","Cha saving throw breaks spell"]]
         self.featureList[11] = ["Seeds of Doubt"]
         self.featureListDescriptions[11] = [["Target creature must succeed Wisdom saving throw to attack you directly", "New attack/spell ends the effect, charm immunity is affects this spell"]]
         self.featureList[14] = ["Inspire Dread"]
         self.featureListDescriptions[14] = [["All hostile creatures on the start of their turn must succeed a Wisdom saving throw or be frightened"]]
         self.featureList[17] = ["Seeds of Confusion"]
         self.featureListDescriptions[17] = [["Learn the confusion spell, cast it 1/day for free", "Choose the creatures affected, use an action to choose the behavior of the confusion"]]
   def __init__(self,level=1):
      self.armorProficiencies = ["light"]
      self.weaponProficiencies = ["simple","crossbowHand","crossbowLight","longSword","rapier","shortSword"]
      self.toolProficiencies = ["musicalInstruments"]
      self.savingThrows = ["int","cha"]
      self.possibleSkills = ["athletics","acrobatics","sleight of hand","stealth","arcana","history","nature","religion","search","animal handling","insight","medicine","perception","survival","deception","intimidation","performance","persuasion"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 3
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Cleric(BaseClass):
   hitDice = 8
   channelDivinityPerLevel =  [0,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3]
   divineStrikeDicePerLevel = [0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2]
   spellsPerDayPerLevel = [[2,0,0,0,0,0,0,0,0],
                           [3,0,0,0,0,0,0,0,0],
                           [4,2,0,0,0,0,0,0,0],
                           [4,3,2,0,0,0,0,0,0],
                           [4,3,3,0,0,0,0,0,0],
                           [4,3,3,1,0,0,0,0,0],
                           [4,3,3,2,0,0,0,0,0],
                           [4,3,3,3,1,0,0,0,0],
                           [4,3,3,3,2,0,0,0,0],
                           [4,3,3,3,2,1,0,0,0],
                           [4,3,3,3,2,1,0,0,0],
                           [4,3,3,3,2,1,1,0,0],
                           [4,3,3,3,2,1,1,0,0],
                           [4,3,3,3,2,1,1,1,0],
                           [4,3,3,3,2,1,1,1,0],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1]]
   featureList = [["Divine Domain","Spellcasting"],
                  ["Turn Undead","Channel Divinity (0/rest)"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  [],
                  [],
                  ["Ability Score Improvement", "Divine Strike (0d8)"],
                  [],
                  ["Divine Intervention"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  [],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  [],
                  ["Ability Score Improvement"],
                  ["Domain Benefit"]]
   featureListDescriptions = [[["Knowledge","Life","Light","Nature","War"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]],
                              [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"],["Once per turn, deal bonus (radiant/necrotic) damage"]],
                              [[""]],
                              [["Call upon your god for help when your need is great","Succeeds if 1d100 < Cleric level","Cooldown of 1 week"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]]]

   def updateFeatures(self):
      if self.pathChosen == "": 
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
      if self.pathChosen == self.pathsToChoose[1]: # Life
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Restore Health ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
      elif self.pathChosen == self.pathsToChoose[2]: # Light
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Radiance of the Dawn ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
         self.featureList[5] = ["Channel Divinity: Revelation of Truth ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
      elif self.pathChosen == self.pathsToChoose[4]: # War
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Guided Strike ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
      self.featureList[7] = ["Ability Score Improvement", "Divine Strike ("+str(self.divineStrikeDicePerLevel[self.level-1])+"d8)"]
   pathsToChoose = ["Knowledge", "Life","Light","Nature","War"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Knowledge
         self.pathChosen = choice
      elif choice == self.pathsToChoose[1]: # Life
         self.pathChosen = choice
         self.featureList[0] = ["Domain Spells","Disciple of Life","Spellcasting"]
         self.featureListDescriptions[0] = [["Bless","Cure Wounds"],["Healing spells gain an addition 2 + spell level"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]]
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Restore Health ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
         self.featureListDescriptions[1] = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["Heal HP equal to 5 * Cleric Level","Only affects living creatures at less than half HP"]]
         self.featureList[2] = ["Domain Spells"]
         self.featureListDescriptions[2] = [["Lesser Restoration","Spiritual Weapon"]]
         self.featureList[4] = ["Domain Spells"]
         self.featureListDescriptions[4] = [["Beacon of Hope","Prayer"]]
         self.featureList[6] = ["Domain Spells"]
         self.featureListDescriptions[6] = [["Death Ward","Guardian of Faith"]]
         self.featureList[8] = ["Domain Spells"]
         self.featureListDescriptions[8] = [["Mass Cure Wounds","Raise Dead"]]
         self.featureList[19] = ["Supreme Healing"]
         self.featureListDescriptions[19] = [["Maximize all die rolls while healing"]]
         self.armorProficiencies = ["light","medium","heavy","shields"]
      elif choice == self.pathsToChoose[2]: # Light
         self.pathChosen = choice
         self.featureList[0] = ["Bonus Spells","Domain Spells","Flare","Spellcasting"]
         self.featureListDescriptions[0] = [["Gain the light and sacred flame cantrips"],["Burning Hands","Faerie Fire"],["Use reaction to cause attacker to have DISADV"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]]
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Radiance of the Dawn ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
         self.featureListDescriptions[1] = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["Dispel magical darkness in 25ft","Enemies make a Constitution save, fail = 2d10+ Cleric Level radiant damage, success = half damage"]]
         self.featureList[2] = ["Domain Spells"]
         self.featureListDescriptions[2] = [["Flaming Sphere","Scorching Ray"]]
         self.featureList[4] = ["Domain Spells"]
         self.featureListDescriptions[4] = [["Daylight","Fireball"]]
         self.featureList[5] = ["Channel Divinity: Revelation of Truth ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
         self.featureListDescriptions[5] = [["Any Illusion within 25ft is dispelled if it's level <= Cleric level / 2"]]
         self.featureList[6] = ["Domain Spells"]
         self.featureListDescriptions[6] = [["Guardian of Faith","Wall of Fire"]]
         self.featureList[8] = ["Domain Spells"]
         self.featureListDescriptions[8] = [["Flame Strike","True Seeing"]]
         self.featureList[10] = ["Domain Spells"]
         self.featureListDescriptions[10] = [["Sunbeam"]]
         self.featureList[14] = ["Domain Spells"]
         self.featureListDescriptions[14] = [["Sunburst"]]
         self.featureList[19] = ["Corona of Light"]
         self.featureListDescriptions[19] = [["Bright light - 50ft radius (Enemies take DISADV against Fire/Radiant damage)","Dim light - 25ft beyond","1 minute duration"]]
      elif choice == self.pathsToChoose[3]: # Nature
         self.pathChosen = choice
      elif choice == self.pathsToChoose[4]: # War
         self.pathChosen = choice
         self.featureList[0] = ["Domain Spells","War Priest","Spellcasting"]
         self.featureListDescriptions[0] = [["Divine Favor","Shield of Faith"],["Attack a single extra time in a turn","Can be used up to WISMOD"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]]
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Guided Strike ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
         self.featureListDescriptions[1] = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["After making attack roll, add +10 to roll"]]
         self.featureList[2] = ["Domain Spells"]
         self.featureListDescriptions[2] = [["Magic Weapon","Spiritual Weapon"]]
         self.featureList[4] = ["Domain Spells"]
         self.featureListDescriptions[4] = [["Holy Vigor","Prayer"]]
         self.featureList[6] = ["Domain Spells"]
         self.featureListDescriptions[6] = [["Divine Power","Freedom of Movement"]]
         self.featureList[8] = ["Domain Spells"]
         self.featureListDescriptions[8] = [["Flame Strike","Hold Monster"]]
         self.featureList[19] = ["Avatar of Battle"]
         self.featureListDescriptions[19] = [["Gain resistance to Bludgeoning, Piercing, and Slashing damage"]]
         self.armorProficiencies = ["light","medium","heavy","shields"]
         weaponProficiencies = ["simple","martial"]
   def __init__(self,level=1):
      self.armorProficiencies = ["light","medium"]
      self.weaponProficiencies = ["simple"]
      self.toolProficiencies = ["kitHealer"]
      self.savingThrows = ["wis","cha"]
      self.possibleSkills = ["insight","medicine","persuasion","religion"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Druid(BaseClass):
   hitDice = 8
   spellsPerDayPerLevel = [[2,0,0,0,0,0,0,0,0],
                           [3,0,0,0,0,0,0,0,0],
                           [4,2,0,0,0,0,0,0,0],
                           [4,3,0,0,0,0,0,0,0],
                           [4,3,2,0,0,0,0,0,0],
                           [4,3,3,0,0,0,0,0,0],
                           [4,3,3,1,0,0,0,0,0],
                           [4,3,3,2,0,0,0,0,0],
                           [4,3,3,3,1,0,0,0,0],
                           [4,3,3,3,2,0,0,0,0],
                           [4,3,3,3,2,1,0,0,0],
                           [4,3,3,3,2,1,0,0,0],
                           [4,3,3,3,2,1,1,0,0],
                           [4,3,3,3,2,1,1,0,0],
                           [4,3,3,3,2,1,1,1,0],
                           [4,3,3,3,2,1,1,1,0],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1]]
   featureList = [["Druidic","Spellcasting"],
                  ["Druid Circle","Wild Shape"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Circle feature"],
                  ["Beast Speech"],
                  ["Wild Shape Improvement"],
                  [],
                  ["Circle feature"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Thousand Faces"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Evergreen"],
                  ["Ability Score Improvement"],
                  ["Beast Spells"]]
   featureListDescriptions = [[["Read/Leave hidden messages in secret language of Druids"],["2 cantrips","DC = 8 + WISmod","Present magic focus to add proficiency bonus to DC"]],
                              [["Circle of the Land","Circle of the Moon"],["Transform into a bat, cat, deer, dog, fish, hawk, horse, owl, raven, snake, toad, or weasel"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [["You can speak in beast form, but no spellcasting"]],
                              [["???"]],
                              [[""]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["Use Wild Shape to change to the same size and type as you"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["For every 10 years that pass, you age only 1 year"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Cast spells in Wild shape. Apply proficiency bonus if you had focus when you used Wild Shape"]]]
   pathsToChoose = ["Circle of the Land", "Circle of the Moon"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Circle of the Land
         self.pathChosen = choice
         self.featureList[1] = ["Circle Spells","Natural Recovery","Wild Shape"]
         self.featureListDescriptions[1] = [["Gain a cantrip"],["Once a day: short rest to recover spell slots up to Druid Level/2 of spell levels"],["Transform into a bat, cat, deer, dog, fish, hawk, horse, owl, raven, snake, toad, or weasel"]]
         self.featureList[5] = ["Land's Stride"]
         self.featureListDescriptions[5] = [["Move through non-magical difficult terrain without extra movement","ADV on magic plants to impede movement"]]
         self.featureList[9] = ["Nature's Ward"]
         self.featureListDescriptions[9] = [["Immune to Charm/Fright from elemental/fey creatures"],["Immune to poison and disease"]]
         if self.landChosen == self.landToChoose[0]: #Coast
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Augury","Mirror Image"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Water Breathing","Water Walk"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Freedom of Movement","Solid Fog"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Scrying","True Seeing"]]
         elif self.landChosen == self.landToChoose[1]: #Desert
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Blur","Silence"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Create Food and Water","Protection from Energy"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Blight","Hallucinatory Terrain"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Control Winds","Wall of Stone"]]
         elif self.landChosen == self.landToChoose[2]: #Forest
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Augury","Barkskin"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Call Lightning","Plant Growth"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Divination","Freedom of Movement"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Commune with Nature","Plant Door"]]
         elif self.landChosen == self.landToChoose[3]: #Grassland
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Augury","Pass without Trace"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Daylight","Haste"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Air Walk","Divination"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Dream","Insect Plague"]]
         elif self.landChosen == self.landToChoose[4]: #Mountain
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Spider Climb","Spike Growth"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Elemental Mantle","Meld into Stone"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Confusion","Stoneskin"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Passwall","Wall of Stone"]]
         elif self.landChosen == self.landToChoose[5]: #Swamp
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Augury","Locate Object"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Water Walk","Stinking Cloud"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Freedom of Movement","Locate Creature"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Insect Plague","Scrying"]]
         elif self.landChosen == self.landToChoose[6]: #Tundra
            self.featureList[2] = ["Circle Spells"]
            self.featureListDescriptions[2] = [["Augury","Spike Growth"]]
            self.featureList[4] = ["Circle Spells"]
            self.featureListDescriptions[4] = [["Sleet Storm","Slow"]]
            self.featureList[6] = ["Circle Spells"]
            self.featureListDescriptions[6] = [["Freedom of Movement","Ice Storm"]]
            self.featureList[8] = ["Circle Spells"]
            self.featureListDescriptions[8] = [["Commune with Nature","Cone of Cold"]]
      elif choice == self.pathsToChoose[1]: # Circle of the Moon
         self.pathChosen = choice
         self.featureList[1] = ["Battle Wild Shape","Wild Shape"]
         self.featureListDescriptions[1] = [["Use Wild Shape as part of any action except spell casting","Gain ability to change into a dire wolf or panther"],["Transform into a bat, cat, deer, dog, fish, hawk, horse, owl, raven, snake, toad, or weasel"]]
         self.featureList[5] = ["Mauler Shapes"]
         self.featureListDescriptions[5] = [["Gain ability to change into a brown bear or tiger"]]
         self.featureList[9] = ["Monstrous Shapes"]
         self.featureListDescriptions[9] = [["Gain ability to change into a cave bear or triceratops"]]

   landToChoose = ["Coast","Desert","Forest","Grassland","Mountain","Swamp","Tundra"]
   landChosen = ""
   def chooseLand(self,choice):
      if choice == self.landToChoose[0] or choice == self.landToChoose[1] or choice == self.landToChoose[2] or choice == self.landToChoose[3] or choice == self.landToChoose[4] or choice == self.landToChoose[5] or choice == self.landToChoose[6]:
         self.landChosen = choice
   def __init__(self,level=1):
      self.armorProficiencies = ["padded","leather","hide","shieldWood"]
      self.weaponProficiencies = ["club","dagger","dart","javelin","mace","quarterstaff","scimitar","sickle","sling","spear"]
      self.toolProficiencies = ["kitHerbalism"]
      self.savingThrows = ["wis"]
      self.possibleSkills = ["animal handling","nature","religion","survival"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Fighter(BaseClass):
   hitDice = 10
   superiorityDicePerLevel =  [0,0,2,2,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4]
   featureList = [["Fighting style","Second Wind"],
                  ["Action Surge"],
                  ["Martial Path"],
                  ["Ability Score Improvement"],
                  ["Extra Attack"],
                  ["Ability Score Improvement"],
                  ["Martial Path benefit"],
                  ["Ability Score Improvement"],
                  ["Defy Death"],
                  ["Martial Path benefit"],
                  ["Extra Attack"],
                  ["Ability Score Improvement"],
                  ["Indomitable"],
                  ["Ability Score Improvement"],
                  ["Martial Path benefit"],
                  ["Ability Score Improvement"],
                  ["Improved Action Surge"],
                  ["Ability Score Improvement"],
                  ["Martial Path benefit"],
                  ["Extra Attack"]]
   featureListDescriptions = [[["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"],["Gain temporary (1d6 + Fighter Level) HP "]],
                              [["Once per rest, use an extra action"]],
                              [["Path of the Weaponmaster", "Path of the Warrior"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["You can attack an extra time"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Make a DC 15 Con save if you go to 0 HP, success gives you 1 HP"]],
                              [[""]],
                              [["You can attack an extra time"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["ADV on all saving throws"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Action Surge gains an additional use per rest"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["You can attack an extra time"]]]
   fightingStyleOptions = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
   fightingStylesChosen = ["",""]
   def chooseFightingStyle(self,choices):
      first, second = choices
      firstIndex = 0
      secondIndex = 9
      if first == "":
         self.fightingStylesChosen[0] = first
         self.setFeatureList(firstIndex, ["Fighting style","Second Wind"],[["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"],["Gain temporary (1d6 + Fighter Level) HP "]])
      elif first == self.fightingStyleOptions[0]: # Archery
         self.fightingStylesChosen[0] = first
         self.setFeatureList(firstIndex, ["Fighting Style: Archery","Second Wind"],[["+1 to attack rolls with ranged weapons"],["Gain temporary (1d6 + Fighter Level) HP "]])
      elif first == self.fightingStyleOptions[1]: # Defense
         self.fightingStylesChosen[0] = first
         self.setFeatureList(firstIndex, ["Fighting Style: Defense","Second Wind"],[["+1 to AC while wearing armor"],["Gain temporary (1d6 + Fighter Level) HP "]])
      elif first == self.fightingStyleOptions[2]: # Great Weapon Fighting
         self.fightingStylesChosen[0] = first
         self.setFeatureList(firstIndex, ["Fighting Style: Great Weapon Fighting","Second Wind"],[["If you miss with a 2 handed weapon, enemy takes STR mod as damage"],["Gain temporary (1d6 + Fighter Level) HP "]])
      elif first == self.fightingStyleOptions[3]: # Protection
         self.fightingStylesChosen[0] = first
         self.setFeatureList(firstIndex, ["Fighting Style: Protection","Second Wind"],[["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"],["Gain temporary (1d6 + Fighter Level) HP "]])
      elif first == self.fightingStyleOptions[4]: # Two-Weapon Fighting
         self.fightingStylesChosen[0] = first
         self.setFeatureList(firstIndex, ["Fighting Style: Two-Weapon Fighting","Second Wind"],[["Add your ability mod to the damage of the second attack"],["Gain temporary (1d6 + Fighter Level) HP "]])
      
      if second == "":
         self.fightingStylesChosen[1] = second
      elif second == self.fightingStyleOptions[0]: # Archery
         self.fightingStylesChosen[1] = second
      elif second == self.fightingStyleOptions[1]: # Defense
         self.fightingStylesChosen[1] = second
      elif second == self.fightingStyleOptions[2]: # Great Weapon Fighting
         self.fightingStylesChosen[1] = second
      elif second == self.fightingStyleOptions[3]: # Protection
         self.fightingStylesChosen[1] = second
      elif second == self.fightingStyleOptions[4]: # Two-Weapon Fighting
         self.fightingStylesChosen[1] = second

      #if Path of Warrior is chosen, change the features and descriptions
      if self.pathChosen == self.pathsToChoose[1]:
         if second == "":
            self.setFeatureList(secondIndex, ["Martial Path benefit"],[[""]])
         elif second == self.fightingStyleOptions[0]: # Archery
            self.setFeatureList(secondIndex, ["Additional Fighting Style: Archery"],[["+1 to attack rolls with ranged weapons"]])
         elif second == self.fightingStyleOptions[1]: # Defense
            self.setFeatureList(secondIndex, ["Additional Fighting Style: Defense"],[["+1 to AC while wearing armor"]])
         elif second == self.fightingStyleOptions[2]: # Great Weapon Fighting
            self.setFeatureList(secondIndex, ["Additional Fighting Style: Great Weapon Fighting"],[["If you miss with a 2 handed weapon, enemy takes STR mod as damage"]])
         elif second == self.fightingStyleOptions[3]: # Protection
            self.setFeatureList(secondIndex, ["Additional Fighting Style: Protection"],[["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"]])
         elif second == self.fightingStyleOptions[4]: # Two-Weapon Fighting
            self.setFeatureList(secondIndex, ["Additional Fighting Style: Two-Weapon Fighting"],[["Add your ability mod to the damage of the second attack"]])
   def updateFeatures(self):
      if self.pathChosen == self.pathsToChoose[0]: # Path of the Weaponmaster
         self.featureListDescriptions[2] = [["Gain "+str(self.superiorityDicePerLevel[self.level-1])+"d6 superiority dice to use on maneuvers, Compare die roll to (MOD)","Dirty Trick:(WIS) gain ADV on attack","Spring Away:(DEX) move half speed","Trip:(STR) target is prone","If roll is less than mod, add pips to damage"]]
      return
   pathsToChoose = ["Path of the Weaponmaster", "Path of the Warrior"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Path of the Weaponmaster
         self.pathChosen = choice
         self.setFeatureList(2,  ["Combat Superiority"],          [["Gain "+str(self.superiorityDicePerLevel[self.level-1])+"d6 superiority dice to use on maneuvers, Compare die roll to (MOD)","Dirty Trick:(WIS) gain ADV on attack","Spring Away:(DEX) move half speed","Trip:(STR) target is prone","If roll is less than mod, add pips to damage"]])
         self.setFeatureList(6,  ["Advanced Maneuvers"],          [["Bell Ringer:(CON) target loses reactions, has DISADV on next attack","Drive Back:(STR) Push target 15ft","Hamstring:(DEX) Reduce target speed 15ft, all attacks against target gain ADV"]])
         self.setFeatureList(9,  ["Improved Combat Superiority"], [["Use d10s for superiority dice"]])
         self.setFeatureList(14, ["Relentless"],                  [["If you start the turn no superiority dice, gain 2 at the end of it"]])

      elif choice == self.pathsToChoose[1]: # Path of the Warrior
         self.pathChosen = choice
         self.setFeatureList(2,  ["Improved Critical"],    [["Count rolls of 19 as criticals"]])
         self.setFeatureList(6,  ["Superior Critical"],    [["Count rolls of 18 as criticals"]])
         self.setFeatureList(14,  ["Devastating Critical"], [["Impose a secondary effect on critical hits, based on damage type:","Bludgeoning:Stun target on a CON save of DC 10+STR mod","Slashing:Target's speed drops to 0","Piercing:Target takes 1d6+(FighterLvl/2) damage per turn, tending to the wound stops this"]])
         self.setFeatureList(18, ["Survivor"],             [["Recover 5+CON mod HP at the start of your turn if you are at less than half HP"]])
   def __init__(self,level=1):
      self.armorProficiencies = ["light","medium","heavy","shields"]
      self.weaponProficiencies = ["simple","martial"]
      self.toolProficiencies = ["landMount"]
      self.savingThrows = ["str","con"]
      self.possibleSkills = ["acrobatics","athletics","intimidation"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Mage(BaseClass):
   hitDice = 6
   spellsPerDayPerLevel = [[2,0,0,0,0,0,0,0,0],
                           [3,0,0,0,0,0,0,0,0],
                           [4,2,0,0,0,0,0,0,0],
                           [4,3,0,0,0,0,0,0,0],
                           [4,3,2,0,0,0,0,0,0],
                           [4,3,3,0,0,0,0,0,0],
                           [4,3,3,1,0,0,0,0,0],
                           [4,3,3,2,0,0,0,0,0],
                           [4,3,3,3,1,0,0,0,0],
                           [4,3,3,3,2,0,0,0,0],
                           [4,3,3,3,2,1,0,0,0],
                           [4,3,3,3,2,1,0,0,0],
                           [4,3,3,3,2,1,1,0,0],
                           [4,3,3,3,2,1,1,0,0],
                           [4,3,3,3,2,1,1,1,0],
                           [4,3,3,3,2,1,1,1,0],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1],
                           [4,3,3,3,2,1,1,1,1]]
   featureList = [["Wizardry"],
                  ["Arcane Tradition"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Tradition benefit"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Tradition benefit"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  ["Tradition benefit"],
                  [],
                  ["Spell Mastery"],
                  ["Ability Score Improvement"],
                  ["Tradition benefit"]]
   featureListDescriptions = [[["3 Cantrips, 4 level 1 spells, each level add 2 valid spells","DC 8 + INT mod (+proficiency if holding a magic focus)"]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [[""]],
                              [["Choose a level 1 and level 2 Mage spell to cast at will","Spend 8 hours of rest to change either, or both"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]]]
   pathsToChoose = ["School of Enchantment", "School of Evocation","School of Illusion"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # School of Enchantment
         self.pathChosen = choice
         self.setFeatureList(1, ["Aura of Antipathy"],[["Any creature within 10ft has DISADV to attack you"]])
         self.setFeatureList(4, ["Instinctive Charm"],[["Change attack target of any creature within 50ft to be closest target","WIS saving throw negates effect"]])
         self.setFeatureList(11,["Split Enchantment"],[["Single-target enchantment spells, can now target a 2nd target"]])
         self.setFeatureList(15,["Rapid Enchantment"],[["Casting time of a enchantment reduced from 1 action to 1 swift action"]])
         self.setFeatureList(19,["Alter Memories"],   [["Charmed creatures think behavior is non-magical","Use an action to force creature to forget (1+CHA mod) hours (INT save negates)","Even it can't forget, make a deception(CHA) check (DC = its INT save roll) to add new memories"]])
      elif choice == self.pathsToChoose[1]: # School of Evocation
         self.pathChosen = choice
         self.setFeatureList(1, ["Scult Spells"],        [["Evocation spells can now target (spell level + 1) number of targets","They automatically pass saving throws","They take no damage if they would normally take only half"]])
         self.setFeatureList(4, ["Potent Cantrip"],      [["If an evocation cantrip fails, the creature takes half damage and no effect"]])
         self.setFeatureList(11,["Overchannel"],         [["Deal maximum damage with a spell of level 3 or lower","Upon 2nd time casting this without rest make a DC 15(+5 each subsequent time) CON check", "Failure drops you to 0 HP"]])
         self.setFeatureList(15,["Empowered Evocation"], [["Add your INT mod to damage of evocation spells"]])
         self.setFeatureList(19,["Evocation Master"],    [["Fireball and Lightning bolt spells are free to cast"]])
      elif choice == self.pathsToChoose[2]: # School of Illusion
         self.pathChosen = choice
         self.setFeatureList(1, ["Improved Minor Tricks"], [["Learn minor illusion cantrip, and use with ghost sound and silent image as a single spell"]])
         self.setFeatureList(4, ["Disappearing Trick"],    [["Always have the invisibility spell prepared","Use your reaction after taking damage to cast invisibility"]])
         self.setFeatureList(11,["Illusionary Self"],      [["You can create an illusionary copy of yourself instantly","If you are attacked before your first turn, this is cast and you take no damage"]])
         self.setFeatureList(15,["Illusionary Reality"],   [["Choose one inanimate, nonmagical object that is part of an illusion to make real","Remains real until end of your next turn, cannot directly harm anyone"]])
         self.setFeatureList(19,["Illusion Master"],       [["You can cast major image for free"]])
   def __init__(self,level=1):
      self.armorProficiencies = []
      self.weaponProficiencies = ["dagger","dart","sling","quarterstaff","crossbowLight"]
      self.toolProficiencies = []
      self.savingThrows = ["int","wis"]
      self.possibleSkills = ["arcana","history","religion"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Monk(BaseClass):
   hitDice = 8
   unarmedStrkeDiePerLevel =  [6,6,6,6,8,8,8,8,8,8,10,10,10,10,10,10,12,12,12,12]
   kiPointsPerLevel =         [2,2,3,3,3,4,4,4,5,5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]
   featureList = [["Flurry of Blows","Unarmed Strike","Unarmored Defense"],
                  ["Supreme Flurry","Slow Fall"],
                  ["Monastic Tradition","Step of the Wind"],
                  ["Ability Score Improvement"],
                  ["Stunning Strike"],
                  ["Tradition feature"],
                  ["Uncanny Dodge"],
                  ["Improved Flurry of Blows","Improved Step of the Wind"],
                  ["Ability Score Improvement"],
                  ["Purity of Body"],
                  ["Tradition feature"],
                  ["Ability Score Improvement"],
                  ["Tongue of Sun and Moon"],
                  ["Diamond Soul"],
                  ["Ability Score Improvement"],
                  ["Timeless Body"],
                  ["Tradition feature"],
                  ["Ability Score Improvement"],
                  ["Empty Body"],
                  ["Perfect Self"]]
   featureListDescriptions = [[["Use your attack action to make 2 unarmed attacks","Spend an Ki point to make an additional attack"],["Unarmed strike is a finesse weapon that deals 1d6 bludgeoning damage"],["While wearing no armor, AC = 10 + DEX mod + WIS mod"]],
                              [["Use a Ki point to gain ADV on all attacks this turn"],["Reduce fall damage by Monk Level","Use a Ki point to reduce fall damage by 5 * Monk Level instead"]],
                              [[""],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Critical hits may cause creature to be stunned (CON save DC 8 + WIS + proficiency negates)"]],
                              [[""]],
                              [["On a DEX saving throw to only take half damage, take none on success, half on failure"]],
                              [["Flurry of Blows now gives 2 extra attacks"],["Step of the Wind's Ki power allows vertical movement or over liquids"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Immune to disease and poison"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["You understand all languages, and all speaking creatures understand you"]],
                              [["ADV on all saving throws against spells"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["You no longer suffer the drawbacks of old age, and cannot age magically","You no longer need food or water"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Use 4 Ki points to become incorporeal and invisible for 1 minute"]],
                              [["Regain 1 Ki point at the beginning of each turn"]]]
   def updateFeatures(self):
      self.featureListDescriptions[0] = [["Use your attack action to make 2 unarmed attacks","Spend an Ki point to make an additional attack"],["Unarmed strike is a finesse weapon that deals 1d"+str(self.unarmedStrkeDiePerLevel[self.level-1])+" bludgeoning damage"],["While wearing no armor, AC = 10 + DEX mod + WIS mod"]]
   elementsToChoose = ["Fire","Air","Earth","Water"]
   elementsChosen = ["","",""]
   def chooseElements(self,choices):
      disciple,power,master = choices
      if disciple == self.elementsToChoose[0] or disciple == self.elementsToChoose[1] or disciple == self.elementsToChoose[2] or disciple == self.elementsToChoose[3]:
         self.elementsChosen[0] = disciple
      if power == self.elementsToChoose[0] or power == self.elementsToChoose[1] or power == self.elementsToChoose[2] or power == self.elementsToChoose[3]:
         self.elementsChosen[1] = power
      if master == self.elementsToChoose[0] or master == self.elementsToChoose[1] or master == self.elementsToChoose[2] or master == self.elementsToChoose[3]:
         self.elementsChosen[2] = master
   pathsToChoose = ["Way of the Four Elements", "Way of the Open Hand"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Way of the Four Elements
         self.pathChosen = choice
         index = 2
         if   self.elementsChosen[0] == "": 
            self.setFeatureList(index, ["Disciple of the Elements","Step of the Wind"],                              [[""],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]])
         elif self.elementsChosen[0] == self.elementsToChoose[0]: # Fire
            self.setFeatureList(index, ["Disciple of the Elements: Fire Riposte","Step of the Wind"],                [["Hit by a melee attack, Use reaction and a Ki point to give 1d10+Monk Level fire damage to attacker","DEX save halves damage"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]])
         elif self.elementsChosen[0] == self.elementsToChoose[1]: # Air
            self.setFeatureList(index, ["Disciple of the Elements: Wind Riposte","Step of the Wind"],                [["Hit by a melee attack, Use reaction and a Ki point to push attacker 20 feet (STR save halves distance)"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]])
         elif self.elementsChosen[0] == self.elementsToChoose[2]: # Earth
            self.setFeatureList(index, ["Disciple of the Elements:Iron Root Defense","Step of the Wind"],            [["Spend a Ki point to root yourself and reduce damage by Monk Level"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]])
         elif self.elementsChosen[0] == self.elementsToChoose[3]: # Water
            self.setFeatureList(index, ["Disciple of the Elements:Shelter of the Flowing River","Step of the Wind"], [["Spend a Ki point to gain ADV on STR, DEX, or CON saving throw"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]])
         
         index = 5
         if   self.elementsChosen[1] == "": 
            self.setFeatureList(index, ["Elemental Power"],                       [[""]])
         elif self.elementsChosen[1] == self.elementsToChoose[0]: # Fire
            self.setFeatureList(index, ["Elemental Power:Flames of the Phoenix"], [["Spend 1 Ki point to emit 15ft cone of 1d10 + Monk Level fire damage (DEX halves)"]])
         elif self.elementsChosen[1] == self.elementsToChoose[1]: # Air
            self.setFeatureList(index, ["Elemental Power:Vortex Punch"],          [["Spend 1 Ki point to emit a 50ft line of 1d6 + Monk Level bludgeoning damage (STR halves)", "Knock all hit targets prone (STR negates)"]])
         elif self.elementsChosen[1] == self.elementsToChoose[2]: # Earth
            self.setFeatureList(index, ["Elemental Power:Grasp of Stone"],        [["When you hit, spend a Ki point to grapple enemy (STR negates)","Your unarmed attacks automatically hit while grappled"]])
         elif self.elementsChosen[1] == self.elementsToChoose[3]: # Water
            self.setFeatureList(index, ["Elemental Power:Crashing Waves"],        [["When you hit, spend a Ki point to push enemy 20ft (STR halves)"]])
         
         index = 10
         if   self.elementsChosen[2] == "": 
            self.setFeatureList(index, ["Elemental Master"],                       [[""]])
         elif self.elementsChosen[2] == self.elementsToChoose[0]: # Fire
            self.setFeatureList(index, ["Elemental Master:Vengeful Flame"],        [["When you drop to 0 HP, spend a Ki point: every creature in 25ft takes 1d10 + Monk Level fire damage (DEX halves)"]])
         elif self.elementsChosen[2] == self.elementsToChoose[1]: # Air
            self.setFeatureList(index, ["Elemental Master:Warrior's Gale"],        [["Spend a Ki point to gain a flight speed of 50ft"]])
         elif self.elementsChosen[2] == self.elementsToChoose[2]: # Earth
            self.setFeatureList(index, ["Elemental Master:Touch of Stony Doom"],   [["When you hit, spend a Ki point to make the target vulnerable to bludgeoning damage for 1 minute (CON negates)"]])
         elif self.elementsChosen[2] == self.elementsToChoose[3]: # Water
            self.setFeatureList(index, ["Elemental Master:Spirit of the Tsunami"], [["Spend 1 Ki point to emit 15ft cone of 1d10 + Monk Level bludgeoning damage, and is knocked prone (CON halves)"]])
         
         self.setFeatureList(16, ["Fist of the Four Elements"], [["Spend 1 Ki point to add 1d10 of cold, fire, lightning, or thunder damage to your melee attack"]])
      elif choice == self.pathsToChoose[1]: # Way of the Open Hand
         self.pathChosen = choice
         self.setFeatureList(2, ["Deflect Missles"],          [["Use reaction to reduce damage from ranged attack by 1d10+DEX mod, if 0 you may catch it","Use a Ki point to reduce by a further 1d10"]])
         self.setFeatureList(5, ["Wholeness of Body"],        [["Regain HP by 2 * Monk Level"]])
         self.setFeatureList(10,["Improved Flurry of Blows"], [["Spending a Ki point on Flurry of Blows also gains you an effect:","Sweep: If it hits, knock the target prone","Knockback: If it hits, push the target up to 10ft away","Daze: if it hits, target cannot make reactions"]])
         self.setFeatureList(16,["Quivering Palm"],           [["Spend 3 Ki points to mark a target for death","Use an action any time in at most (Monk Level) days","CON save DC = 8 + WIS + proficiency: failure causes target to die","Cooldown is 1 week"]])
   def __init__(self,level=1):
      self.armorProficiencies = []
      self.weaponProficiencies = ["club","dagger","handaxe","crossbowLight","longspear","quarterstaff","shortSword","sling","spear","unarmedStrike"]
      self.toolProficiencies = []
      self.savingThrows = ["dex","wis"]
      self.possibleSkills = ["acrobatics","athletics","religion"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Paladin(BaseClass):
   hitDice = 10
   spellsPerDayPerLevel = [[0,0,0,0,0],
                           [2,0,0,0,0],
                           [3,0,0,0,0],
                           [3,0,0,0,0],
                           [4,2,0,0,0],
                           [4,2,0,0,0],
                           [4,3,0,0,0],
                           [4,3,0,0,0],
                           [4,3,2,0,0],
                           [4,3,2,0,0],
                           [4,3,3,0,0],
                           [4,3,3,0,0],
                           [4,3,3,1,0],
                           [4,3,3,1,0],
                           [4,3,3,2,0],
                           [4,3,3,2,0],
                           [4,3,3,3,1],
                           [4,3,3,3,1],
                           [4,3,3,3,2],
                           [4,3,3,3,2]]
   featureList = [["Divine Sense","Lay on Hands"],
                  ["Divine Smite","Fighting Style","Spellcasting"],
                  ["Divine Health","Oath"],
                  ["Ability Score Improvement"],
                  ["Extra Attack"],
                  ["Aura of Protection"],
                  ["Ability Score Improvement"],
                  ["Oath feature"],
                  [],
                  ["Aura of Courage"],
                  ["Improved Divine Smite"],
                  ["Ability Score Improvement"],
                  [],
                  ["Cleansing Touch"],
                  ["Aura of Resolve"],
                  ["Ability Score Improvement"],
                  [],
                  ["Oath feature"],
                  ["Ability Score Improvement"],
                  ["Oath feature"]]
   featureListDescriptions = [[["Within 50ft you can sense celestial, fiendish, or undead creatures, or con/desecrated land"],["Heal up to 5*Paladin Level of HP or spend 5 of this HP to cure a disease/neutralize a poison"]],
                              [["Expend 1 paladin spell to deal (1+spell level)d8","Deals 1d8 extra for undead or fiendish creatures"],["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"],["DC = 8 + CHA mod, + proficiency if holy symbol present"]],
                              [["You are immune to disease"],["Oath of Devotion", "Oath of Vengeance"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["You can attack an extra time"]],
                              [["If a creatrure must make a saving throw within 10ft, you may grant your CHA bonus to its roll"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [["Friendly creatures within 10ft cannot be frightened"]],
                              [["You gain +1d8 damage to all attacks"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["Use action to end one magical effect on yourself or creature that you touch"]],
                              [["Friendly creatures within 10ft cannot be charmed"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]]]
   fightingStyleOptions = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
   fightingStylesChosen = ""
   def chooseFightingStyle(self,first):
      firstIndex = 1
      divineSmiteDes = ["Expend 1 paladin spell to deal (1+spell level)d8","Deals 1d8 extra for undead or fiendish creatures"]
      spellCastingDes = ["DC = 8 + CHA mod, + proficiency if holy symbol present"]
      if first == "":
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, ["Divine Smite","Fighting Style", "Spellcasting"], [divineSmiteDes,["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"],spellCastingDes])
      elif first == self.fightingStyleOptions[0]: # Archery
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, ["Divine Smite","Fighting Style: Archery", "Spellcasting"], [divineSmiteDes,["+1 to attack rolls with ranged weapons"],spellCastingDes])
      elif first == self.fightingStyleOptions[1]: # Defense
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, ["Divine Smite","Fighting Style: Defense", "Spellcasting"], [divineSmiteDes,["+1 to AC while wearing armor"],spellCastingDes])
      elif first == self.fightingStyleOptions[2]: # Great Weapon Fighting
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, ["Divine Smite","Fighting Style: Great Weapon Fighting", "Spellcasting"], [divineSmiteDes,["If you miss with a 2 handed weapon, enemy takes STR mod as damage"],spellCastingDes])
      elif first == self.fightingStyleOptions[3]: # Protection
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, ["Divine Smite","Fighting Style: Protection", "Spellcasting"], [divineSmiteDes,["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"],spellCastingDes])
      elif first == self.fightingStyleOptions[4]: # Two-Weapon Fighting
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, ["Divine Smite","Fighting Style: Two-Weapon Fighting", "Spellcasting"], [divineSmiteDes,["Add your ability mod to the damage of the second attack"],spellCastingDes])
      
   pathsToChoose = ["Oath of Devotion", "Oath of Vengeance"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Oath of Devotion
         self.pathChosen = choice
         self.setFeatureList(2, ["Divine Health","Oath Spells","Channel Divinity"], [["You are immune to disease"],["Protection from Evil","Sanctuary"],["Sacred Weapon: weapon is gains magical +CHA to attack, emits 20ft bright light 20ft dim","Turn Undead: Undead within 25ft make WIS save, or are turned"]])
         self.setFeatureList(4, ["Extra Attack","Oath Spells"],                     [["You can attack an extra time"],["Lesser Restoration, Zone of Truth"]])
         self.setFeatureList(7, ["Turn Fiends"],                                    [["Turn Undead also affects fiends"]])
         self.setFeatureList(8, ["Oath Spells"],                                    [["Beacon of Hope","Dispel magic"]])
         self.setFeatureList(12,["Oath Spells"],                                    [["Freedom of Movement","Guardian of Faith"]])
         self.setFeatureList(16,["Oath Spells"],                                    [["Commune","Flame Strike"]])
         self.setFeatureList(17,["Banishing Strike"],                               [["Smite feature banishes fiends who fail a CHA saving throw"]])
         self.setFeatureList(19,["Channel Divinity:Holy Nimbus"],                   [["Emit bright sunlight in 25ft, dim sunlight in 25ft beyond. enemies take 10 damage on turn start in bright light","While active, gain ADV on saves against fiends/undead spell casting"]])
         
      elif choice == self.pathsToChoose[1]: # Oath of Vengeance
         self.pathChosen = choice
         self.setFeatureList(2, ["Divine Health","Oath Spells","Channel Divinity"], [["You are immune to disease"],["Cause Fear","Hunter's Mark"],["Abjure Enemy:Frighten one enemy in 60ft, Undead/fiend have DISADV (WIS causes speed to be halved)","Vow of Enmity:Creature is hit within 10ft, Gain ADV on attack against attacker"]])
         self.setFeatureList(4, ["Extra Attack","Oath Spells"],                     [["You can attack an extra time"],["Hold Person","Misty Step"]])
         self.setFeatureList(7, ["Relentless Avenger"],                             [["Hitting a creature with an opportuntity attack allows you to move half your speed"]])
         self.setFeatureList(8, ["Oath Spells"],                                    [["Haste","Protection from Energy"]])
         self.setFeatureList(12,["Oath Spells"],                                    [["Air Walk","Dimension Door"]])
         self.setFeatureList(16,["Oath Spells"],                                    [["Hold Monster","Scrying"]])
         self.setFeatureList(17,["Soul of Vengeance"],                              [["When the creature under Vow of Enmity makes an attack, use reaction to make an attack"]])
         self.setFeatureList(19,["Channel Divinity:Avenging Angel"],                [["Undergo a transformation to gain flight (60ft), and frighten enemies in 30ft range (WIS negates)","Attacks versus the frightened creature have ADV"]])
   def __init__(self,level=1):
      self.armorProficiencies = ["light","medium","heavy","shields"]
      self.weaponProficiencies = ["simple","martial"]
      self.toolProficiencies = ["landMount"]
      self.savingThrows = ["con","cha"]
      self.possibleSkills = ["athletics","persuasion","religion"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 1
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Ranger(BaseClass):
   hitDice = 10
   spellsPerDayPerLevel = [[0,0,0,0,0],
                           [0,0,0,0,0],
                           [3,0,0,0,0],
                           [3,0,0,0,0],
                           [4,2,0,0,0],
                           [4,2,0,0,0],
                           [4,3,0,0,0],
                           [4,3,0,0,0],
                           [4,3,2,0,0],
                           [4,3,2,0,0],
                           [4,3,3,0,0],
                           [4,3,3,0,0],
                           [4,3,3,1,0],
                           [4,3,3,1,0],
                           [4,3,3,2,0],
                           [4,3,3,2,0],
                           [4,3,3,3,1],
                           [4,3,3,3,1],
                           [4,3,3,3,2],
                           [4,3,3,3,2]]
   featureList = [["Tracking"],
                  ["Favored Enemy","Fighting Style"],
                  ["Spellcasting"],
                  ["Ability Score Improvement"],
                  ["Extra Attack"],
                  ["Natural Explorer"],
                  ["Favored Enemy feature"],
                  ["Ability Score Improvement", "Land's Stride"],
                  [],
                  ["Hide in Plain Sight"],
                  ["Favored Enemy feature"],
                  ["Ability Score Improvement"],
                  [],
                  ["Master Stalker"],
                  ["Favored Enemy feature"],
                  ["Ability Score Improvement"],
                  [],
                  ["Unmatched Hunter"],
                  ["Ferral Senses"],
                  ["Terrain Superiority"]]
   featureListDescriptions = [[["Track other creatures using WIS check"]],
                              [["Colossus Slayer", "Horde Breaker"],["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]],
                              [["DC = 8 + WIS mod"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["You can attack an extra time"]],
                              [["You explore Wilderness at twice the normal rate, and cannot become lost","You find 1 days worth of food and mounts for up to 11 people"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"],["Move through non-magical terrain at no extra movement","Take no damage from thorns or other hazards plants possess"]],
                              [[""]],
                              [["Take 1 minute to add +10 to stealth checks as long as you remain still"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["Make a stealth check to hide without using an action","May choose to move silently, be tracked, be detected with tremorsense or with magic (if they can't see you)"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [[""]],
                              [["The first time you hit a surprised creature on the first round, triple the damage"]],
                              [["Being unable to see a target doesn't give you DISADV","You are aware of invisible creatures within 25ft"]],
                              [["Gain ADV on attacks and saves in wilderness environments"]]]
   fightingStyleOptions = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
   fightingStylesChosen = ""
   def chooseFightingStyle(self,first):
      firstIndex = 1
      if first == "":
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, "Fighting Style", ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"],1)
      elif first == self.fightingStyleOptions[0]: # Archery
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, "Fighting Style: Archery", ["+1 to attack rolls with ranged weapons"],1)
      elif first == self.fightingStyleOptions[1]: # Defense
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, "Fighting Style: Defense", ["+1 to AC while wearing armor"],1)
      elif first == self.fightingStyleOptions[2]: # Great Weapon Fighting
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, "Fighting Style: Great Weapon Fighting", ["If you miss with a 2 handed weapon, enemy takes STR mod as damage"],1)
      elif first == self.fightingStyleOptions[3]: # Protection
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, "Fighting Style: Protection", ["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"],1)
      elif first == self.fightingStyleOptions[4]: # Two-Weapon Fighting
         self.fightingStylesChosen = first
         self.setFeatureList(firstIndex, "Fighting Style: Two-Weapon Fighting", ["Add your ability mod to the damage of the second attack"],1)
      
   pathsToChoose = ["Path of the Colossus Slayer", "Path of the Horde Breaker"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Path of the Colossus Slayer
         self.pathChosen = choice
         self.setFeatureList(1, "Slayer's Momentum",     ["If you damage a creature with a weapon attack, deal +1d6 to that creature next attack"],0)
         self.setFeatureList(6, ["Steel Will"],          [["Gain ADV on saves versus being frightened"]])
         self.setFeatureList(10,["Staggering Attack"],   [["When you hit a creature with a weapon attack, gain ADV on all other attacks to that target this turn"]])
         self.setFeatureList(14,["Uncanny Dodge"],       [["On a DEX saving throw to only take half damage, take none on success, half on failure"]])
         
      elif choice == self.pathsToChoose[1]: # Path of the Horde Breaker
         self.pathChosen = choice
         self.setFeatureList(1, "Hordeslayer",           ["If you damage a creature with a weapon attack, deal +1d8 to each other creature you attack"],0)
         self.setFeatureList(6, ["Hunter's Mobility"],   [["Opportunity attacks against you have DISADV"]])
         self.setFeatureList(10,["Whirlwind Attack"],    [["Use your action to make a melee attack against each enemy creature within 5ft of you"]])
         self.setFeatureList(14,["Pack Awareness"],      [["If you are not surprised at the start of combat, allies within 25ft are not either"]])
   def __init__(self,level=1):
      self.armorProficiencies = ["light","medium","shields"]
      self.weaponProficiencies = ["simple","martial"]
      self.toolProficiencies = ["landMount"]
      self.savingThrows = ["dex","wis"]
      self.possibleSkills = ["animal handling","athletics","nature","perception","stealth","survival"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 3
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#
class Rogue(BaseClass):
   hitDice = 6
   sneakAttackDice = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7]
   featureList = [["Expertise", "Sneak Attack (1d6)"],
                  ["Cunning Action","Thieves' Cant"],
                  ["Rogue Style"],
                  ["Ability Score Improvement"],
                  ["Evasion"],
                  ["Rogue Style feature"],
                  ["Ability Score Improvement"],
                  ["Uncanny Dodge"],
                  ["Rogue Style feature"],
                  ["Ability Score Improvement"],
                  ["Reliable Talent"],
                  ["Blindsense"],
                  ["Rogue Style feature"],
                  ["Ability Score Improvement"],
                  ["Slippery Mind"],
                  ["Rogue Style feature"],
                  ["Ability Score Improvement"],
                  ["Elusive"],
                  ["Ability Score Improvement"],
                  ["Ace in the Hole"]]
   featureListDescriptions = [[["Gain +5 to all checks using up to 4 of your skill or tool proficiencies"],["Add damage to a strike if you have ADV or an able enemy of target is within 5ft"]],
                              [["You may take a second action on your turn to disengage, hide, or hustle"],["Hide messages in normal conversation"]],
                              [["Assassination", "Thievery"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Use your reaction to half the damage taken from a seen attack"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["On a DEX saving throw to only take half damage, take none on success, half on failure"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Treat rolls of 9 or lower as a 10 on proficiencies"]],
                              [["You are aware (through hearing) of the location of hidden/invisible creatures within 10ft"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Gain proficiency in Wisdom saving throws"]],
                              [[""]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Creatures can't gain advantage on you for attack rolls"]],
                              [["2 +1's to abilities OR choose 1 feat"]],
                              [["Once/rest, treat a roll failure as a roll of 20"]]]
   def updateFeatures(self):
      self.setFeatureList(0, "Sneak Attack ("+str(self.sneakAttackDice[self.level-1])+"d6)", ["Add damage to a strike if you have ADV or an able enemy of target is within 5ft"],1)

   pathsToChoose = ["Assassination", "Thievery"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Assassination
         self.pathChosen = choice
         self.setFeatureList(2, ["Assassinate"],            [["On first turn, gain ADV on any creature not yet taken a turn","Score an automatic critical against surprised enemies, use max result for sneak attack"]])
         self.setFeatureList(5, ["Poison Mastery"],         [["Spend 1 hour to make a tasteless, colorless, odorless liquid to do 1 of 3 things (CON save DC 10+INT mod)","Unconsciousness for 2d6+4 hours","Intoxication for 24 hours, HP max is halved","As if it was under a non-magical confusion spell"]])
         self.setFeatureList(8, ["Infiltration Expertise"], [["You can create false identities for yourself, takes 1 week and 25gp"]])
         self.setFeatureList(12,["Impostor"],               [["Spend 1 hour studying person to mimic them","You have advantage on any deception checks made to avoid detection"]])
         self.setFeatureList(15,["Death Strike"],           [["If you make an attack against a surprised creature, deal double the damage (CON save DC 10+DEX mod negates doubling)"]])
         toolProficiencies = ["kitThief","kitDisguise","kitPoisoners"]
      elif choice == self.pathsToChoose[1]: # Thievery
         self.pathChosen = choice
         self.setFeatureList(2, ["Burglary","Fast Hands"], [["Climbing doesn't half your speed","Long jump distance increases by 10ft, high jump by 5ft"],["Use your Cunning Action to make sleight of hand checks"]])
         self.setFeatureList(5, ["Decipher Script"],       [["Study a page of text for a minute to puzzle out the meaning","1 hour of text to discover the full meaning"]])
         self.setFeatureList(8, ["Supreme Sneak"],         [["Gain ADV on any ability check to hide if you move no more than half speed"]])
         self.setFeatureList(12,["Use Magic Device"],      [["Ignore all class, race, and level requirements on the use of magic items"]])
         self.setFeatureList(15,["Thief's Reflexes"],      [["Take 2 turns at the beginning of a battle (2nd is at initiative - 10)"]])

   def __init__(self,level=1):
      self.armorProficiencies = ["light","medium"]
      self.weaponProficiencies = ["simple","crossbowHand","crossbowLight","longSword","rapier","shortSword"]
      self.toolProficiencies = ["kitThief"]
      self.savingThrows = ["dex"]
      self.possibleSkills = ["athletics","deception","insight","intimitation","perception","performance","persuasion","search","sleight of hand","stealth"]
      self.numberOfAttacks = 1
      self.skillsToChoose = 4
      self.level = 1
      for l in range(1,level):
         self.levelUp()
#