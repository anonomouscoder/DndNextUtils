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
         self.featureList[3] = "Totem Spirit: " + self.animalChosen[0]
         if self.animalChosen[0] == self.animalToChoose[0]: #Bear
            self.featureListDescriptions[2] = "Roll hitdice twice when regaining health"
         elif self.animalChosen[0] == self.animalToChoose[1]:#Cougar
            self.featureListDescriptions[2] = ["Speed increases 5","You gain proficiency in acrobatics"]
         elif self.animalChosen[0] == self.animalToChoose[2]:#Hawk
            self.featureListDescriptions[2] = ["Jump double your normal distance","ADV on Raging dex-based attack rolls"]
         elif self.animalChosen[0] == self.animalToChoose[3]:#Wolf
            self.featureListDescriptions[2] = "You gain proficiency in perception"
         self.featureList[5] = "Spirit Rage: " + self.animalChosen[1]
         if self.animalChosen[1] == self.animalToChoose[0]: #Bear
            self.featureListDescriptions[5] = "You may expend up to 2 hitdice to regain HP when entering rage"
         elif self.animalChosen[1] == self.animalToChoose[1]:#Cougar
            self.featureListDescriptions[5] = ["While raging, opportunity attacks have DISADV against you"]
         elif self.animalChosen[1] == self.animalToChoose[2]:#Hawk
            self.featureListDescriptions[5] = ["While raging, you have resistance to falling damage","Jump triple your normal distance"]
         elif self.animalChosen[1] == self.animalToChoose[3]:#Wolf
            self.featureListDescriptions[5] = "While raging, you sense the location of any creature within 15 feet"
         self.featureList[9] = "Spirit Vitality"
         self.featureListDescriptions[9] = "While raging, regain 5 HP if you are at less than half health"
         self.featureList[13] = "Guiding Totem"
         self.featureListDescriptions[13] = ["You gain proficiency in Wisdom saving throws","Hidden threats do not gain ADV on you"]

   animalToChoose = ["Bear","Cougar","Hawk","Wolf"]
   animalChosen = [[],[]]
   def chooseAnimals(self,choices):
      totem,rage = choices
      if totem == animalToChoose[0] or totem == animalToChoose[1] or totem == animalToChoose[2] or totem == animalToChoose[3]:
         self.animalChosen[0] = totem
      if rage == animalToChoose[0] or rage == animalToChoose[1] or rage == animalToChoose[2] or rage == animalToChoose[3]:
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
      featureListDescriptions[0] = ["Inteligence checks of 9 or lower are a 10, if they pertain to Arcana, History, Nature, or Religion"],["Call To Battle = + 1d"+self.callToBattleDieUsed[self.level]+" to damage rolls","Inspire Competence = Add your proficiency bonus to one of the 6 abilities","Range: 25ft, Duration: 10m, Needs concentration and voice"]
      if self.pathChosen == "College of Valor":
         self.featureListDescriptions[6] = "Give allies = + 1d"+self.callToBattleDieUsed[self.level]+" more HP during short rests"
         
   pathsToChoose = ["College of Valor", "College of Wit"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # College of Valor
         self.pathChosen = choice
         self.featureList[3] = "Bonus Proficiencies", "War College Training", "Expertise"
         self.featureListDescriptions[3] = ["Gain proficiency with medium armor and martial weapons"],["Per turn you can use the help action as part of the attack action"],["Gain +5 bonus to any 4 skill or tool proficiencies"]
         self.featureList[6] = "Song of Rest"
         self.featureListDescriptions[6] = "Give allies = + 1d"+self.callToBattleDieUsed[self.level]+" more HP during short rests"
         self.featureList[12] = "Coordinate Allies"
         self.featureListDescriptions[12] = "Use reaction to give advantage to attack against a specific creature that has been attacked"
         self.featureList[15] = "Words of Warning"
         self.featureListDescriptions[15] = "Use reaction to give advantage to allies Strength, Dexterity, or Wisdom saving throw"
         self.featureList[18] = "Rally"
         self.featureListDescriptions[18] = ["Learn cure mass wounds, cast it 1/day for free","This spell removes charm, fright, paralysis, and stun. Everyone can stand up or move its speed"]
         
      elif choice == self.pathsToChoose[1]: # College of Wit
         self.pathChosen = choice
         self.featureList[3] = "Fascinating Performance", "Expertise"
         self.featureListDescriptions[3] = ["Charm non-hostile creatures within 50ft","Combat breaks effect"],["Gain +5 bonus to any 4 skill or tool proficiencies"]
         self.featureList[6] = "Eviscerating Wit"
         self.featureListDescriptions[6] = ["Plant doubt (disadvantage on all ability checks) to all hostile creatures in 50ft","Cha saving throw breaks spell"]
         self.featureList[12] = "Seeds of Doubt"
         self.featureListDescriptions[12] = ["Target creature must succeed Wisdom saving throw to attack you directly", "New attack/spell ends the effect, charm immunity is affects this spell"]
         self.featureList[15] = "Inspire Dread"
         self.featureListDescriptions[15] = "All hostile creatures on the start of their turn must succeed a Wisdom saving throw or be frightened"
         self.featureList[18] = "Seeds of Confusion"
         self.featureListDescriptions[18] = ["Learn the confusion spell, cast it 1/day for free", "Choose the creatures affected, use an action to choose the behavior of the confusion"]
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
         self.featureList[6] = "Channel Divinity: Revelation of Truth ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
      elif self.pathChosen == self.pathsToChoose[4]: # War
         self.featureList[2] = "Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Guided Strike ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
      self.featureList[7] = ["Ability Score Improvement", "Divine Strike ("+str(self.divineStrikeDicePerLevel[self.level-1])+"d8)"]
   pathsToChoose = ["Knowledge", "Life","Light","Nature","War"]
   pathChosen = ""
   def choosePath(self,choice): 
      if choice == self.pathsToChoose[0]: # Knowledge
         self.pathChosen = choice
      elif choice == self.pathsToChoose[1]: # Life
         self.pathChosen = choice
         self.featureList[1] = "Domain Spells","Disciple of Life","Spellcasting"
         self.featureListDescriptions[1] = ["Bless","Cure Wounds"],["Healing spells gain an addition 2 + spell level"]["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]
         self.featureList[2] = "Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Restore Health ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
         self.featureListDescriptions[2] = ["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["Heal HP equal to 5 * Cleric Level","Only affects living creatures at less than half HP"]
         self.featureList[3] = "Domain Spells"
         self.featureListDescriptions[3] = ["Lesser Restoration","Spiritual Weapon"]
         self.featureList[5] = "Domain Spells"
         self.featureListDescriptions[5] = ["Beacon of Hope","Prayer"]
         self.featureList[7] = "Domain Spells"
         self.featureListDescriptions[7] = ["Death Ward","Guardian of Faith"]
         self.featureList[9] = "Domain Spells"
         self.featureListDescriptions[9] = ["Mass Cure Wounds","Raise Dead"]
         self.featureList[20] = "Supreme Healing"
         self.featureListDescriptions[20] = ["Maximize all die rolls while healing"]
         self.armorProficiencies = ["light","medium","heavy","shields"]
      elif choice == self.pathsToChoose[2]: # Light
         self.pathChosen = choice
         self.featureList[1] = "Bonus Spells","Domain Spells","Flare","Spellcasting"
         self.featureListDescriptions[1] = ["Gain the light and sacred flame cantrips"],["Burning Hands","Faerie Fire"],["Use reaction to cause attacker to have DISADV"]["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]
         self.featureList[2] = "Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Radiance of the Dawn ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
         self.featureListDescriptions[2] = ["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["Dispel magical darkness in 25ft","Enemies make a Constitution save, fail = 2d10+ Cleric Level radiant damage, success = half damage"]
         self.featureList[3] = "Domain Spells"
         self.featureListDescriptions[3] = ["Flaming Sphere","Scorching Ray"]
         self.featureList[5] = "Domain Spells"
         self.featureListDescriptions[5] = ["Daylight","Fireball"]
         self.featureList[6] = "Channel Divinity: Revelation of Truth ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
         self.featureListDescriptions[6] = ["Any Illusion within 25ft is dispelled if it's level <= Cleric level / 2"]
         self.featureList[7] = "Domain Spells"
         self.featureListDescriptions[7] = ["Guardian of Faith","Wall of Fire"]
         self.featureList[9] = "Domain Spells"
         self.featureListDescriptions[9] = ["Flame Strike","True Seeing"]
         self.featureList[11] = "Domain Spells"
         self.featureListDescriptions[11] = ["Sunbeam"]
         self.featureList[15] = "Domain Spells"
         self.featureListDescriptions[15] = ["Sunburst"]
         self.featureList[20] = "Corona of Light"
         self.featureListDescriptions[20] = ["Bright light - 50ft radius (Enemies take DISADV against Fire/Radiant damage)","Dim light - 25ft beyond","1 minute duration"]
      elif choice == self.pathsToChoose[3]: # Nature
         self.pathChosen = choice
      elif choice == self.pathsToChoose[4]: # War
         self.pathChosen = choice
         self.featureList[1] = "Domain Spells","War Priest","Spellcasting"
         self.featureListDescriptions[1] = ["Divine Favor","Shield of Faith"],["Attack a single extra time in a turn","Can be used up to WISMOD"]["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]
         self.featureList[2] = "Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Guided Strike ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
         self.featureListDescriptions[2] = ["All undead in 25ft must succeed WIS save (DC 10 + WIS + spellcasing bonus)","if target hitpoints <= cleric lvl * 5: target is destroyed else: target runs"],["After making attack roll, add +10 to roll"]
         self.featureList[3] = "Domain Spells"
         self.featureListDescriptions[3] = ["Magic Weapon","Spiritual Weapon"]
         self.featureList[5] = "Domain Spells"
         self.featureListDescriptions[5] = ["Holy Vigor","Prayer"]
         self.featureList[6] = "Channel Divinity: Revelation of Truth ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
         self.featureListDescriptions[6] = ["Any Illusion within 25ft is dispelled if it's level <= Cleric level / 2"]
         self.featureList[7] = "Domain Spells"
         self.featureListDescriptions[7] = ["Divine Power","Freedom of Movement"]
         self.featureList[9] = "Domain Spells"
         self.featureListDescriptions[9] = ["Flame Strike","Hold Monster"]
         self.featureList[20] = "Avatar of Battle"
         self.featureListDescriptions[20] = ["Gain resistance to Bludgeoning, Piercing, and Slashing damage"]
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
   def updateFeatures(self):
      if self.pathChosen == "": 
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
      if self.pathChosen == self.pathsToChoose[1]: # Life
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Restore Health ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
      elif self.pathChosen == self.pathsToChoose[2]: # Light
         self.featureList[1] = ["Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Radiance of the Dawn ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"]
         self.featureList[6] = "Channel Divinity: Revelation of Truth ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
      elif self.pathChosen == self.pathsToChoose[4]: # War
         self.featureList[2] = "Turn Undead("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)","Channel Divinity: Guided Strike ("+str(self.channelDivinityPerLevel[self.level-1])+"/rest)"
      self.featureList[7] = ["Ability Score Improvement", "Divine Strike ("+str(self.divineStrikeDicePerLevel[self.level-1])+"d8)"]
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