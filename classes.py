class BaseClass:
   classString = "BaseClass"
   hitDice = 8
   level = 0
   proficiencyBonusPerLevel =   [1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6]
   armorProficiencies = []
   weaponProficiencies = []
   toolProficiencies = []
   savingThrows = []
   possibleSkills = []
   skillsToChoose = 0
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
   #Called to increment the level, and update the list of features, if needed
   def levelUp(self):
      self.level = self.level + 1
      self.updateFeatures()
   #used for classes that have numerical amounts in features that increase based on level (sneak attack goes from 1d6 to 7d6
   def updateFeatures(self):
      return
#
class Barbarian(BaseClass):
   level = 0
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
   featureList = [["Rage ("+str(ragesPerLevel[level])+"/rest, +"+str(rageDamagePerLevel[level])+" dmg)","Thick Hide"],
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
   def updateFeatures(self):   
      self.featureList[0] = ["Rage ("+str(self.ragesPerLevel[self.level])+"/rest, +"+str(self.rageDamagePerLevel[self.level])+" dmg)","Thick Hide"]
#
class Bard(BaseClass):
   classString = "Bard"
   hitDice = 6
   spellsKnownPerLevel =         [0,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11]
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
#
class Cleric(BaseClass):
   level = 0
   classString = "Cleric"
   hitDice = 8
   channelDivinityPerLevel =     [0,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3]
   divineStrikeDicePerLevel =    [0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2]
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
                  ["Channel Divinity ("+str(channelDivinityPerLevel[level])+"/rest)"],
                  [],
                  ["Ability Score Improvement"],
                  [],
                  [],
                  [],
                  ["Ability Score Improvement", "Divine Strike ("+str(divineStrikeDicePerLevel[level])+"d8)"],
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
   def updateFeatures(self):
      self.featureList[1] = ["Channel Divinity ("+str(self.channelDivinityPerLevel[self.level])+"/rest)"]
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
#
class Figher(BaseClass):
   classString = "Figher"
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