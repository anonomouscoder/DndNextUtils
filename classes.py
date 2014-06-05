import unitTest,time,calendar
from unitTest import UnitTest

class BaseClass:
   classString = "BaseClass"
   hitDice = 8
   level = 1
   proficiencyBonusPerLevel =   [1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6]
   armorProficiencies = []
   weaponProficiencies = []
   toolProficiencies = []
   savingThrows = []
   possibleSkills = []
   skillsToChoose = 0
   numberOfAttacks = 1
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
      for l in range(1,level):
         self.levelUp()
#
class Barbarian(BaseClass):
   level = 1
   classString = "Barbarian"
   hitDice = 12
   ragesPerLevel =               [2,2,3,3,3,4,4,4,4,4,4,5,5,5,5,5,6,6,6,99]
   rageDamagePerLevel =          [2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4]
   armorProficiencies = ["light","medium","shield"]
   weaponProficiencies = ["simple","martial"]
   toolProficiencies = ["landMount"]
   savingThrows = ["str","con"]
   possibleSkills = ["athletics","intimidation","survival"]
   skillsToChoose = 1
   featureList = [["Rage ("+str(ragesPerLevel[level])+"/rest, +"+str(rageDamagePerLevel[level-1])+" dmg)","Thick Hide"],
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
#
class Bard(BaseClass):
   level = 1
   classString = "Bard"
   hitDice = 6
   spellsKnownPerLevel =         [0,2,3,3,4,4,5,5,6,6,7,7, 8, 8, 9, 9,10,10,11,11]
   callToBattleDieUsed =         [4,4,4,4,4,6,6,6,8,8,8,8,10,10,10,10,12,12,12,12]
   armorProficiencies = ["light"]
   weaponProficiencies = ["simple","crossbowHand","crossbowLight","longSword","rapier","shortSword"]
   toolProficiencies = ["musicalInstruments"]
   savingThrows = ["int","cha"]
   possibleSkills = ["any"]
   skillsToChoose = 3
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

   featureListDescriptions = [[["Inteligence checks of 9 or lower are a 10, if they pertain to Arcana, History, Nature, or Religion"],["Call To Battle = + 1d"+str(callToBattleDieUsed[level-1])+" to damage rolls","Inspire Competence = Add your proficiency bonus to one of the 6 abilities","Range: 25ft, Duration: 10m, Needs concentration and voice"]],
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
#
class Cleric(BaseClass):
   level = 1
   classString = "Cleric"
   hitDice = 8
   channelDivinityPerLevel =  [0,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3]
   divineStrikeDicePerLevel = [0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2]
   armorProficiencies = ["light","medium"]
   weaponProficiencies = ["simple"]
   toolProficiencies = ["kitHealer"]
   savingThrows = ["wis","cha"]
   possibleSkills = ["insight","medicine","persuasion","religion"]
   skillsToChoose = 1
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
                  ["Turn Undead","Channel Divinity ("+str(channelDivinityPerLevel[level-1])+"/rest)"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  [],
                  [],
                  ["Ability Score Improvement", "Divine Strike ("+str(divineStrikeDicePerLevel[level-1])+"d8)"],
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
#
class Druid(BaseClass):
   classString = "Druid"
   hitDice = 8
   armorProficiencies = ["padded","leather","hide","shieldWood"]
   weaponProficiencies = ["club","dagger","dart","javelin","mace","quarterstaff","scimitar","sickle","sling","spear"]
   toolProficiencies = ["kitHerbalism"]
   savingThrows = ["wis"]
   possibleSkills = ["animal handling","nature","religion","survival"]
   skillsToChoose = 1
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
         self.featureList[2] = "Circle Spells","Natural Recovery"
         self.featureListDescriptions[2] = ["Gain a cantrip"],["Once a day: short rest to recover spell slots up to Druid Level/2 of spell levels"]
         self.featureList[6] = "Land's Stride"
         self.featureListDescriptions[6] = ["Move through non-magical difficult terrain without extra movement","ADV on magic plants to impede movement"]
         self.featureList[10] = "Nature's Ward"
         self.featureListDescriptions[10] = ["Immune to Charm/Fright from elemental/fey creatures"],["Immune to poison and disease"]
         if self.landChosen == self.landToChoose[0]: #Coast
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Augury","Mirror Image"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Water Breathing","Water Walk"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Freedom of Movement","Solid Fog"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Scrying","True Seeing"]
         elif self.landChosen == self.landToChoose[1]: #Desert
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Blur","Silence"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Create Food and Water","Protection from Energy"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Blight","Hallucinatory Terrain"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Control Winds","Wall of Stone"]
         elif self.landChosen == self.landToChoose[2]: #Forest
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Augury","Barkskin"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Call Lightning","Plant Growth"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Divination","Freedom of Movement"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Commune with Nature","Plant Door"]
         elif self.landChosen == self.landToChoose[3]: #Grassland
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Augury","Pass without Trace"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Daylight","Haste"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Air Walk","Divination"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Dream","Insect Plague"]
         elif self.landChosen == self.landToChoose[4]: #Mountain
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Spider Climb","Spike Growth"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Elemental Mantle","Meld into Stone"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Confusion","Stoneskin"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Passwall","Wall of Stone"]
         elif self.landChosen == self.landToChoose[5]: #Swamp
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Augury","Locate Object"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Water Walk","Stinking Cloud"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Freedom of Movement","Locate Creature"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Insect Plague","Scrying"]
         elif self.landChosen == self.landToChoose[6]: #Tundra
            self.featureList[3] = "Circle Spells"
            self.featureListDescriptions[3] = ["Augury","Spike Growth"]
            self.featureList[5] = "Circle Spells"
            self.featureListDescriptions[5] = ["Sleet Storm","Slow"]
            self.featureList[7] = "Circle Spells"
            self.featureListDescriptions[7] = ["Freedom of Movement","Ice Storm"]
            self.featureList[9] = "Circle Spells"
            self.featureListDescriptions[9] = ["Commune with Nature","Cone of Cold"]
      elif choice == self.pathsToChoose[1]: # Circle of the Moon
         self.pathChosen = choice
         self.featureList[2] = "Battle Wild Shape"
         self.featureListDescriptions[2] = ["Use Wild Shape as part of any action except spell casting","Gain ability to change into a dire wolf or panther"]
         self.featureList[6] = "Mauler Shapes"
         self.featureListDescriptions[6] = ["Gain ability to change into a brown bear or tiger"]
         self.featureList[10] = "Monstrous Shapes"
         self.featureListDescriptions[10] = ["Gain ability to change into a cave bear or triceratops"]

   landToChoose = ["Coast","Desert","Forest","Grassland","Mountain","Swamp","Tundra"]
   landChosen = ""
   def chooseLand(self,choice):
      if choice == self.landToChoose[0] or choice == self.landToChoose[1] or choice == self.landToChoose[2] or choice == self.landToChoose[3] or choice == self.landToChoose[4] or choice == self.landToChoose[5] or choice == self.landToChoose[6]:
         self.landChosen = choice
#
class Fighter(BaseClass):
   classString = "Fighter"
   hitDice = 10
   superiorityDicePerLevel =  [0,0,2,2,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4]
   armorProfenciencies = ["all","shields"]
   weaponProfenciencies = ["simple","martial"]
   toolProfenciencies = ["landMount"]
   savingThrows = ["str","con"]
   possibleSkills = ["acrobatics","athletics","intimidation"]
   skillsToChoose = 1
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
   featureListDescriptions = [[["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"],["Gain temporary (1d6 + Figher Level) HP "]],
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
      if first == self.fightingStyleOptions[0]:   # Archery
         self.fightingStylesChosen[0] = first
         self.featureList[0] = ["Fighting Style: Archery","Second Wind"]
         self.featureListDescriptions[0] = ["+1 to attack rolls with ranged weapons"],["Gain temporary (1d6 + Figher Level) HP "]
      elif first == self.fightingStyleOptions[1]: # Defense
         self.fightingStylesChosen[0] = first
         self.featureList[0] = ["Fighting Style: Defense","Second Wind"]
         self.featureListDescriptions[0] = ["+1 to AC while wearing armor"],["Gain temporary (1d6 + Figher Level) HP "]
      elif first == self.fightingStyleOptions[2]: # Great Weapon Fighting
         self.fightingStylesChosen[0] = first
         self.featureList[0] = ["Fighting Style: Great Weapon Fighting","Second Wind"]
         self.featureListDescriptions[0] = ["If you miss with a 2 handed weapon, enemy takes STR mod as damage"],["Gain temporary (1d6 + Figher Level) HP "]
      elif first == self.fightingStyleOptions[3]: # Protection
         self.fightingStylesChosen[0] = first
         self.featureList[0] = ["Fighting Style: Protection","Second Wind"]
         self.featureListDescriptions[0] = ["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"],["Gain temporary (1d6 + Figher Level) HP "]
      elif first == self.fightingStyleOptions[4]: # Two-Weapon Fighting
         self.fightingStylesChosen[0] = first
         self.featureList[0] = ["Fighting Style: Two-Weapon Fighting","Second Wind"]
         self.featureListDescriptions[0] = ["Add your ability mod to the damage of the second attack"],["Gain temporary (1d6 + Figher Level) HP "]
      if self.pathChosen == pathsToChoose[1]:
         if second == self.fightingStyleOptions[0]:   # Archery
            self.fightingStylesChosen[1] = second
            self.featureList[0] = ["Fighting Style: Archery","Second Wind"]
            self.featureListDescriptions[0] = ["+1 to attack rolls with ranged weapons"],["Gain temporary (1d6 + Figher Level) HP "]
         elif second == self.fightingStyleOptions[1]: # Defense
            self.fightingStylesChosen[1] = second
            self.featureList[9] = ["Additional Fighting Style: Defense"]
            self.featureListDescriptions[9] = ["+1 to AC while wearing armor"]
         elif second == self.fightingStyleOptions[2]: # Great Weapon Fighting
            self.fightingStylesChosen[1] = second
            self.featureList[9] = ["Additional Fighting Style: Great Weapon Fighting"]
            self.featureListDescriptions[9] = ["If you miss with a 2 handed weapon, enemy takes STR mod as damage"]
         elif second == self.fightingStyleOptions[3]: # Protection
            self.fightingStylesChosen[1] = second
            self.featureList[9] = ["Additional Fighting Style: Protection","Second Wind"]
            self.featureListDescriptions[9] = ["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"]
         elif second == self.fightingStyleOptions[4]: # Two-Weapon Fighting
            self.fightingStylesChosen[1] = second
            self.featureList[9] = ["Additional Fighting Style: Two-Weapon Fighting"]
            self.featureListDescriptions[9] = ["Add your ability mod to the damage of the second attack"]
      
   def updateFeatures(self):
      if choice == self.pathsToChoose[0]: # Path of the Weaponmaster
         self.featureListDescriptions[2] = ["Gain "+str(self.superiorityDicePerLevel[self.level-1])+"d6 superiority dice to use on maneuvers, Compare die roll to (MOD)","Dirty Trick:(WIS) gain ADV on attack","Spring Away:(DEX) move half speed","Trip:(STR) target is prone","If roll is less than mod, add pips to damage"]
      return
   pathsToChoose = ["Path of the Weaponmaster", "Path of the Warrior"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Path of the Weaponmaster
         self.pathChosen = choice
         self.featureList[2] = "Combat Superiority"
         self.featureListDescriptions[2] = ["Gain "+str(self.superiorityDicePerLevel[self.level-1])+"d6 superiority dice to use on maneuvers, Compare die roll to (MOD)","Dirty Trick:(WIS) gain ADV on attack","Spring Away:(DEX) move half speed","Trip:(STR) target is prone","If roll is less than mod, add pips to damage"]
         self.featureList[6] = "Advanced Maneuvers"
         self.featureListDescriptions[6] = ["Bell Ringer:(CON) target loses reactions, has DISADV on next attack","Drive Back:(STR) Push target 15ft","Hamstring:(DEX) Reduce target speed 15ft, all attacks against target gain ADV"]
         self.featureList[9] = "Improved Combat Superiority"
         self.featureListDescriptions[9] = ["Use d10s for superiority dice"]
         self.featureList[14] = "Relentless"
         self.featureListDescriptions[14] = ["If you start the turn no superiority dice, gain 2 at the end of it"]

      elif choice == self.pathsToChoose[1]: # Path of the Warrior
         self.pathChosen = choice
         self.featureList[2] = "Improved Critical"
         self.featureListDescriptions[2] = ["Count rolls of 19 as criticals"]
         self.featureList[6] = "Superior Critical"
         self.featureListDescriptions[6] = ["Count rolls of 18 as criticals"]
         self.featureList[14] = "Devastating Critical"
         self.featureListDescriptions[14] = ["Impose a secondary effect on critical hits, based on damage type:","Bludgeoning:Stun target on a CON save of DC 10+STR mod","Slashing:Target's speed drops to 0","Piercing:Target takes 1d6+(FighterLvl/2) damage per turn, tending to the wound stops this"]
         self.featureList[18] = "Survivor"
         self.featureListDescriptions[18] = ["Recover 5+CON mod HP at the start of your turn if you are at less than half HP"]
#

class Mage(BaseClass):
   classString = "Mage"
   hitDice = 6
   armorProfenciencies = []
   weaponProfenciencies = ["dagger","dart","sling","quarterstaff","crossbowLight"]
   toolProfenciencies = []
   savingThrows = ["int","wis"]
   possibleSkills = ["arcana","history","religion"]
   skillsToChoose = 1
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
#
class Monk(BaseClass):
   classString = "Monk"
   hitDice = 8
   armorProfenciencies = []
   weaponProfenciencies = ["club","dagger","handaxe","crossbowLight","longspear","quarterstaff","shortSword","sling","spear","unarmedStrike"]
   toolProfenciencies = []
   savingThrows = ["dex","wis"]
   possibleSkills = ["acrobatics","athletics","religion"]
   skillsToChoose = 1
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
#
class Paladin(BaseClass):
   classString = "Paladin"
   hitDice = 10
   armorProfenciencies = ["all","shields"]
   weaponProfenciencies = ["simple","martial"]
   toolProfenciencies = ["landMount"]
   savingThrows = ["con","cha"]
   possibleSkills = ["athletics","persuasion","religion"]
   skillsToChoose = 1
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
                  ["Divine Smite","Fighting Style", "Spellcasting"],
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
#
class Ranger(BaseClass):
   classString = "Ranger"
   hitDice = 10
   armorProfenciencies = ["light","medium","shields"]
   weaponProfenciencies = ["simple","martial"]
   toolProfenciencies = ["landMount"]
   savingThrows = ["dex","wis"]
   possibleSkills = ["animal handling","athletics","nature","perception","stealth","survival"]
   skillsToChoose = 3
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
#
class Rogue(BaseClass):
   level = 0
   classString = "Rogue"
   hitDice = 6
   sneakAttackDice =             [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7]
   armorProficiencies = ["light","medium"]
   weaponProficiencies = ["simple","crossbowHand","crossbowLight","longSword","rapier","shortSword"]
   toolProficiencies = ["kitThief"]
   savingThrows = ["dex"]
   possibleSkills = ["athletics","deception","insight","intimitation","perception","performance","persuasion","search","sleight of hand","stealth"]
   skillsToChoose = 4
   featureList = [["Expertise, Sneak Attack ("+str(sneakAttackDice[level])+"d6)"],
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
   def updateFeatures(self):
      self.featureList[0] = ["Expertise, Sneak Attack ("+str(self.sneakAttackDice[self.level])+"d6)"]
#
class classUnitTest(UnitTest):
   def run(self):
      self.BaseClassTests()
      self.BarbarianClassTests()
      self.BardClassTests()
      self.ClericClassTests()
   def common_updateFeatures(self,c,level,index,expectedFeatures,expectedFeatureDescriptions):
      c.level = level
      c.updateFeatures()
      if c.featureList[index] != expectedFeatures:
         self.failTest("Class->common->updateFeatures->"+c.classString+"->level" + str(level)+"->index"+str(index)+": '"+str(c.featureList[index])+"' found, '" + str(expectedFeatures) + "' expected")
      if c.featureListDescriptions[index] != expectedFeatureDescriptions:
         self.failTest("Class->common->updateFeatures->"+c.classString+"->level" + str(level)+"->index"+str(index)+": '"+str(c.featureListDescriptions[index])+"' found, '" + str(expectedFeatureDescriptions) + "' expected")
   def common_choosePath(self,c,choice,indicesList,expectedFeatureList,expectedFeatureDescriptionsList):
      c.choosePath(choice)
      if c.pathChosen != choice:
         self.failTest("Class->common->choosePath->"+c.classString+": chosen path '"+c.pathChosen+"' seen + '"+choice+"'expected")
      for i,index in enumerate(indicesList):
         if c.featureList[index] != expectedFeatureList[i]:
            self.failTest("Class->common->choosePath->"+c.classString+"->index"+str(index)+": '"+str(c.featureList[index])+"' found, '" + str(expectedFeatureList[i]) + "' expected")
         if c.featureListDescriptions[index] != expectedFeatureDescriptionsList[i]:
            self.failTest("Class->common->choosePath->"+c.classString+"->index"+str(index)+": '"+str(c.featureListDescriptions[index])+"' found, '" + str(expectedFeatureDescriptionsList[i]) + "' expected")
   def BaseClassTests(self):
      c = BaseClass()
      #levelUp
      c.levelUp()
      if c.level != 2:
         self.failTest("Class->BaseClass->Levelup test")
      c.featureList =  [[],
                        [],
                        ["Ability Score Improvement"],
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
      c.levelUp()
      if c.numberOfAbilitiesToIncrease != 2:
         self.failTest("Class->BaseClass->AbilityModIncreases test")
      
      #__init__
      for i in range(1,20):
         c = BaseClass(i)
         if c.level != i:
            self.failTest("Class->BaseClass->__init__ failure on index " + str(i))
   #
   def BarbarianClassTests(self):
      c = Barbarian()
      #updateFeatures
      index = 0
      levelList =    [1,3,6,9,12,16,17,20]
      newEntryList =   [["Rage (2/rest, +2 dmg)","Thick Hide"],
                        ["Rage (3/rest, +2 dmg)","Thick Hide"],
                        ["Rage (4/rest, +2 dmg)","Thick Hide"],
                        ["Rage (4/rest, +3 dmg)","Thick Hide"],
                        ["Rage (5/rest, +3 dmg)","Thick Hide"],
                        ["Rage (5/rest, +4 dmg)","Thick Hide"],
                        ["Rage (6/rest, +4 dmg)","Thick Hide"],
                        ["Rage (99/rest, +4 dmg)","Thick Hide"]]
      rageDes = ["ADV on Strength checks and Saving throws","Gain temporary hitpoints = 2*Barbarian level"]
      thickHideDes = ["if no armor: AC = 10 + DexMod + ConMod"]
      
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],[rageDes,thickHideDes])
      #choosePath
      c = Barbarian()
      #-Path of the Berserker
      indicesList = [2,5,9,13]
      expectedFeatureList =  [["Fearless Rage"],
                              ["Mindless Rage"],
                              ["Unchecked Fury"],
                              ["Brutal Rage"]]
      expectedFeatureDescriptionsList =  [[["Immune to fear while raging"]],
                                          [["Immune to charm while raging"]],
                                          [["If you miss a melee attack, immediately make one retry"]],
                                          [["You may take 5 damage at start of a raging turn. If you do, add another weapon damage die"]]]
      self.common_choosePath(c,"Path of the Berserker",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      #-Path of the Totem Warrior
      spiritVitalityDes =  [["While raging, regain 5 HP if you are at less than half health"]]
      guidingTotemDes =    [["You gain proficiency in Wisdom saving throws","Hidden threats do not gain ADV on you"]]
      totemRageDefault =   ["Bear","Cougar","Hawk","Wolf"]
      
      c = Barbarian()
      indicesList = [2,5,9,13]
      expectedFeatureList =  [["Totem Spirit: "], ["Spirit Rage: "], ["Spirit Vitality"], ["Guiding Totem"]]
      expectedFeatureDescriptionsList =  [totemRageDefault, totemRageDefault, spiritVitalityDes, guidingTotemDes]
      self.common_choosePath(c,"Path of the Totem Warrior",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      #chooseAnimals
      indicesList = [2,5,9,13]
      animalPairList = [["Bear","Bear"],["Cougar","Cougar"],["Hawk","Hawk"],["Wolf","Wolf"],["Bear","Wolf"]]
      expectedFeatureList =  [[["Totem Spirit: Bear"],  ["Spirit Rage: Bear"],  ["Spirit Vitality"],["Guiding Totem"]],
                              [["Totem Spirit: Cougar"],["Spirit Rage: Cougar"],["Spirit Vitality"],["Guiding Totem"]],
                              [["Totem Spirit: Hawk"],  ["Spirit Rage: Hawk"],  ["Spirit Vitality"],["Guiding Totem"]],
                              [["Totem Spirit: Wolf"],  ["Spirit Rage: Wolf"],  ["Spirit Vitality"],["Guiding Totem"]],
                              [["Totem Spirit: Bear"],  ["Spirit Rage: Wolf"],  ["Spirit Vitality"],["Guiding Totem"]]]
      
      totemBearDes =       [["Roll hitdice twice when regaining health"]]
      rageBearDes =        [["You may expend up to 2 hitdice to regain HP when entering rage"]]
      totemCougarDes =     [["Speed increases 5","You gain proficiency in acrobatics"]]
      rageCougarDes =      [["While raging, opportunity attacks have DISADV against you"]]
      totemHawkDes =       [["Jump double your normal distance","ADV on Raging dex-based attack rolls"]]
      rageHawkDes =        [["While raging, you have resistance to falling damage","Jump triple your normal distance"]]
      totemWolfDes =       [["You gain proficiency in perception"]]
      rageWolfDes =        [["While raging, you sense the location of any creature within 15 feet"]]
      expectedFeatureDescriptionsList =  [[totemBearDes,  rageBearDes,  spiritVitalityDes,guidingTotemDes],
                                          [totemCougarDes,rageCougarDes,spiritVitalityDes,guidingTotemDes],
                                          [totemHawkDes,  rageHawkDes,  spiritVitalityDes,guidingTotemDes],
                                          [totemWolfDes,  rageWolfDes,  spiritVitalityDes,guidingTotemDes],
                                          [totemBearDes,  rageWolfDes,  spiritVitalityDes,guidingTotemDes]]
      for i,pair in enumerate(animalPairList):
         c.chooseAnimals(pair)
         if c.animalChosen != pair:
            self.failTest("Class->common->chooseAnimal->"+c.classString+": chosen animals '"+str(c.animalChosen)+"' seen + '"+str(pair)+"'expected")
            
         self.common_choosePath(c,"Path of the Totem Warrior",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
   #
   def BardClassTests(self):
      #updateFeatures
      c = Bard()
      c.choosePath("College of Valor")
      #callToBattleDieUsed =         [4,4,4,4,4,6,6,6,8,8,8,8,10,10,10,10,12,12,12,12]
      index = 0
      levelList =    [1,6,9,13,17]
      bardicKnowledgeDes = ["Inteligence checks of 9 or lower are a 10, if they pertain to Arcana, History, Nature, or Religion"]
      inspireCompetenceDes = "Inspire Competence = Add your proficiency bonus to one of the 6 abilities"
      bardicPerformanceDetails = "Range: 25ft, Duration: 10m, Needs concentration and voice"

      newEntryList =   [[bardicKnowledgeDes,["Call To Battle = + 1d4 to damage rolls", inspireCompetenceDes,bardicPerformanceDetails]],
                        [bardicKnowledgeDes,["Call To Battle = + 1d6 to damage rolls", inspireCompetenceDes,bardicPerformanceDetails]],
                        [bardicKnowledgeDes,["Call To Battle = + 1d8 to damage rolls", inspireCompetenceDes,bardicPerformanceDetails]],
                        [bardicKnowledgeDes,["Call To Battle = + 1d10 to damage rolls",inspireCompetenceDes,bardicPerformanceDetails]],
                        [bardicKnowledgeDes,["Call To Battle = + 1d12 to damage rolls",inspireCompetenceDes,bardicPerformanceDetails]]]
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,["Bardic Knowledge","Bardic Performance"],newEntryList[i])
      index = 5
      newEntryList =   [[["Give allies = + 1d4 more HP during short rests"]],
                        [["Give allies = + 1d6 more HP during short rests"]],
                        [["Give allies = + 1d8 more HP during short rests"]],
                        [["Give allies = + 1d10 more HP during short rests"]],
                        [["Give allies = + 1d12 more HP during short rests"]]]
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,["Song of Rest"],newEntryList[i])
      #choosePath
      # College of Valor
      c = Bard()
      indicesList = [2,5,11,14,17]
      expectedFeatureList =  [["War College Training", "Expertise"],
                              ["Song of Rest"],
                              ["Coordinate Allies"],
                              ["Words of Warning"],
                              ["Rally"]]
      expectedFeatureDescriptionsList =  [[["Per turn you can use the help action as part of the attack action"],["Gain +5 bonus to any 4 skill or tool proficiencies"]],
                                          [["Give allies = + 1d4 more HP during short rests"]],
                                          [["Use reaction to give advantage to attack against a specific creature that has been attacked"]],
                                          [["Use reaction to give advantage to allies Strength, Dexterity, or Wisdom saving throw"]],
                                          [["Learn cure mass wounds, cast it 1/day for free","This spell removes charm, fright, paralysis, and stun. Everyone can stand up or move its speed"]]]
      self.common_choosePath(c,"College of Valor",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      expectedArmorProficiencies = ["light","medium"]
      if c.armorProficiencies != expectedArmorProficiencies:
         self.failTest("Class->Bard->College of Valor->ArmorProficiencies: '"+str(c.armorProficiencies)+"' found, '"+str(expectedArmorProficiencies)+"' expected")
      expectedWeaponProficiencies = ["simple","martial"]
      if c.weaponProficiencies != expectedWeaponProficiencies:
         self.failTest("Class->Bard->College of Valor->WeaponProficiencies: '"+str(c.weaponProficiencies)+"' found, '"+str(expectedWeaponProficiencies)+"' expected")
      
      # College of Wit
      c = Bard()
      indicesList = [2,5,11,14,17]
      expectedFeatureList =  [["Fascinating Performance", "Expertise"],
                              ["Eviscerating Wit"],
                              ["Seeds of Doubt"],
                              ["Inspire Dread"],
                              ["Seeds of Confusion"]]
      expectedFeatureDescriptionsList =  [[["Charm non-hostile creatures within 50ft","Combat breaks effect"],["Gain +5 bonus to any 4 skill or tool proficiencies"]],
                                          [["Plant doubt (disadvantage on all ability checks) to all hostile creatures in 50ft","Cha saving throw breaks spell"]],
                                          [["Target creature must succeed Wisdom saving throw to attack you directly", "New attack/spell ends the effect, charm immunity is affects this spell"]],
                                          [["All hostile creatures on the start of their turn must succeed a Wisdom saving throw or be frightened"]],
                                          [["Learn the confusion spell, cast it 1/day for free", "Choose the creatures affected, use an action to choose the behavior of the confusion"]]]
      self.common_choosePath(c,"College of Wit",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
   #
   def ClericClassTests(self):
      #updateFeatures
      c = Cleric()
      #  channelDivinityPerLevel =  [0,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3]
      index = 1
      levelList =    [1,2,6,18]
      newEntryList =   [["Turn Undead(0/rest)","Channel Divinity (0/rest)"],
                        ["Turn Undead(1/rest)","Channel Divinity (1/rest)"],
                        ["Turn Undead(2/rest)","Channel Divinity (2/rest)"],
                        ["Turn Undead(3/rest)","Channel Divinity (3/rest)"]]
      newEntryDescription = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],[""]]
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],newEntryDescription)
      #  divineStrikeDicePerLevel = [0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2]
      index = 7
      levelList = [1,8,14]
      newEntryList =   [["Ability Score Improvement", "Divine Strike (0d8)"],
                        ["Ability Score Improvement", "Divine Strike (1d8)"],
                        ["Ability Score Improvement", "Divine Strike (2d8)"]]
      newEntryDescription = [["2 +1's to abilities OR choose 1 feat"],["Once per turn, deal bonus (radiant/necrotic) damage"]]
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],newEntryDescription)
      c.choosePath("Life")
      index = 1
      levelList =    [1,2,6,18]
      newEntryList =   [["Turn Undead(0/rest)","Channel Divinity: Restore Health (0/rest)"],
                        ["Turn Undead(1/rest)","Channel Divinity: Restore Health (1/rest)"],
                        ["Turn Undead(2/rest)","Channel Divinity: Restore Health (2/rest)"],
                        ["Turn Undead(3/rest)","Channel Divinity: Restore Health (3/rest)"]]
      newEntryDescription = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["Heal HP equal to 5 * Cleric Level","Only affects living creatures at less than half HP"]]
      
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],newEntryDescription)
      
      c = Cleric()
      c.choosePath("Light")
      index = 1
      levelList =    [1,2,6,18]
      newEntryList =   [["Turn Undead(0/rest)","Channel Divinity: Radiance of the Dawn (0/rest)"],
                        ["Turn Undead(1/rest)","Channel Divinity: Radiance of the Dawn (1/rest)"],
                        ["Turn Undead(2/rest)","Channel Divinity: Radiance of the Dawn (2/rest)"],
                        ["Turn Undead(3/rest)","Channel Divinity: Radiance of the Dawn (3/rest)"]]
      newEntryDescription = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["Dispel magical darkness in 25ft","Enemies make a Constitution save, fail = 2d10+ Cleric Level radiant damage, success = half damage"]]
      
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],newEntryDescription)
      index = 5
      newEntryList =   [["Channel Divinity: Revelation of Truth (0/rest)"],
                        ["Channel Divinity: Revelation of Truth (1/rest)"],
                        ["Channel Divinity: Revelation of Truth (2/rest)"],
                        ["Channel Divinity: Revelation of Truth (3/rest)"]]
      newEntryDescription = [["Any Illusion within 25ft is dispelled if it's level <= Cleric level / 2"]]
      
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],newEntryDescription)
      c = Cleric()
      c.choosePath("War")
      index = 1
      levelList =    [1,2,6,18]
      newEntryList =   [["Turn Undead(0/rest)","Channel Divinity: Guided Strike (0/rest)"],
                        ["Turn Undead(1/rest)","Channel Divinity: Guided Strike (1/rest)"],
                        ["Turn Undead(2/rest)","Channel Divinity: Guided Strike (2/rest)"],
                        ["Turn Undead(3/rest)","Channel Divinity: Guided Strike (3/rest)"]]
      newEntryDescription = [["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["After making attack roll, add +10 to roll"]]
      
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],newEntryDescription)
      
      #choosePath

   #
unitTestFramework = classUnitTest()

start = int(round(time.time() * 1000))
unitTestFramework.run()
stop = int(round(time.time() * 1000))
print "Class unit tests took " + str(stop-start) + " milliseconds"