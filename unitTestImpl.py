import unitTest,time,equipment,classes
from unitTest import UnitTest
from equipment import Money
from classes import *


class ClassUnitTest(UnitTest):
   name = "Class Unit Tests"
   def run(self):
      self.BaseClassTests()
      self.BarbarianClassTests()
      self.BardClassTests()
      self.ClericClassTests()
      self.DruidClassTests()
      self.FighterClassTests()
      self.MageClassTests()
      self.MonkClassTests()
      self.PaladinClassTests()
      self.RangerClassTests()
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
            self.failTest("Class->common->choosePath->"+c.classString+"->path:"+str(c.pathChosen)+"->index "+str(index)+": '"+str(c.featureList[index])+"' found, '" + str(expectedFeatureList[i]) + "' expected")
         if c.featureListDescriptions[index] != expectedFeatureDescriptionsList[i]:
            self.failTest("Class->common->choosePath->"+c.classString+"->path:"+str(c.pathChosen)+"->index "+str(index)+": '"+str(c.featureListDescriptions[index])+"' found, '" + str(expectedFeatureDescriptionsList[i]) + "' expected")
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
      a = Barbarian()
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
         self.common_updateFeatures(a,level,index,newEntryList[i],[rageDes,thickHideDes])
      #choosePath
      b = Barbarian()
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
      self.common_choosePath(b,"Path of the Berserker",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
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
      #Life
      c = Cleric()
      indicesList = [0,2,4,6,8,19]
      expectedFeatureList =  [["Domain Spells","Disciple of Life","Spellcasting"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Supreme Healing"]]
      expectedFeatureDescriptionsList =  [[["Bless","Cure Wounds"],["Healing spells gain an addition 2 + spell level"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]],
                                          [["Lesser Restoration","Spiritual Weapon"]],
                                          [["Beacon of Hope","Prayer"]],
                                          [["Death Ward","Guardian of Faith"]],
                                          [["Mass Cure Wounds","Raise Dead"]],
                                          [["Maximize all die rolls while healing"]]]
      self.common_choosePath(c,"Life",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      expectedArmorProficiencies = ["light","medium","heavy","shields"]
      if c.armorProficiencies != expectedArmorProficiencies:
         self.failTest("Class->Cleric->Life->ArmorProficiencies: '"+str(c.armorProficiencies)+"' found, '"+str(expectedArmorProficiencies)+"' expected")
      #Light
      c = Cleric()
      indicesList = [0,2,4,6,8,10,14,19]
      expectedFeatureList =  [["Bonus Spells","Domain Spells","Flare","Spellcasting"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Corona of Light"]]
      expectedFeatureDescriptionsList =  [[["Gain the light and sacred flame cantrips"],["Burning Hands","Faerie Fire"],["Use reaction to cause attacker to have DISADV"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]],
                                          [["Flaming Sphere","Scorching Ray"]],
                                          [["Daylight","Fireball"]],
                                          [["Guardian of Faith","Wall of Fire"]],
                                          [["Flame Strike","True Seeing"]],
                                          [["Sunbeam"]],
                                          [["Sunburst"]],
                                          [["Bright light - 50ft radius (Enemies take DISADV against Fire/Radiant damage)","Dim light - 25ft beyond","1 minute duration"]]]
      self.common_choosePath(c,"Light",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      #War
      c = Cleric()
      indicesList = [0,2,4,6,8,19]
      expectedFeatureList =  [["Domain Spells","War Priest","Spellcasting"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Domain Spells"],
                              ["Avatar of Battle"]]
      expectedFeatureDescriptionsList =  [[["Divine Favor","Shield of Faith"],["Attack a single extra time in a turn","Can be used up to WISMOD"],["3 cantrips","DC = 8 + WISmod","Present holy symbol to add proficiency bonus to DC"]],
                                          [["Magic Weapon","Spiritual Weapon"]],
                                          [["Holy Vigor","Prayer"]],
                                          [["Divine Power","Freedom of Movement"]],
                                          [["Flame Strike","Hold Monster"]],
                                          [["Gain resistance to Bludgeoning, Piercing, and Slashing damage"]]]
      self.common_choosePath(c,"War",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      expectedArmorProficiencies = ["light","medium","heavy","shields"]
      if c.armorProficiencies != expectedArmorProficiencies:
         self.failTest("Class->Cleric->War->ArmorProficiencies: '"+str(c.armorProficiencies)+"' found, '"+str(expectedArmorProficiencies)+"' expected")
         
      expectedWeaponProficiencies = ["simple","martial"]
      if c.armorProficiencies != expectedArmorProficiencies:
         self.failTest("Class->Cleric->War->WeaponProficiencies: '"+str(c.weaponProficiencies)+"' found, '"+str(expectedWeaponProficiencies)+"' expected")
   #
   def DruidClassTests(self):
      #updateFeatures
      # Druid doesn't have any features that update with level
      
      #choosePath
      #Circle of the Moon
      c = Druid()
      indicesList = [1,5,9]
      expectedFeatureList =  [["Battle Wild Shape","Wild Shape"],
                              ["Mauler Shapes"],
                              ["Monstrous Shapes"]]
      expectedFeatureDescriptionsList =  [[["Use Wild Shape as part of any action except spell casting","Gain ability to change into a dire wolf or panther"],["Transform into a bat, cat, deer, dog, fish, hawk, horse, owl, raven, snake, toad, or weasel"]],
                                          [["Gain ability to change into a brown bear or tiger"]],
                                          [["Gain ability to change into a cave bear or triceratops"]]]
      self.common_choosePath(c,"Circle of the Moon",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      #Circle of the Land
      c = Druid()
      indicesList = [1,5,9]
      expectedFeatureList =  [["Circle Spells","Natural Recovery","Wild Shape"],
                              ["Land's Stride"],
                              ["Nature's Ward"]]
      expectedFeatureDescriptionsList =  [[["Gain a cantrip"],["Once a day: short rest to recover spell slots up to Druid Level/2 of spell levels"],["Transform into a bat, cat, deer, dog, fish, hawk, horse, owl, raven, snake, toad, or weasel"]],
                                          [["Move through non-magical difficult terrain without extra movement","ADV on magic plants to impede movement"]],
                                          [["Immune to Charm/Fright from elemental/fey creatures"],["Immune to poison and disease"]]]
      self.common_choosePath(c,"Circle of the Land",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      #chooseLand
      indicesList = [2,4,6,8]
      landList =              ["Coast","Desert","Forest","Grassland","Mountain","Swamp","Tundra"]
      expectedFeatureList =  [[["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]],
                              [["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]],
                              [["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]],
                              [["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]],
                              [["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]],
                              [["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]],
                              [["Circle Spells"], ["Circle Spells"], ["Circle Spells"], ["Circle Spells"]]]
      
      expectedFeatureDescriptionsList =  [[[["Augury","Mirror Image"]],       [["Water Breathing","Water Walk"]],                   [["Freedom of Movement","Solid Fog"]],       [["Scrying","True Seeing"]]],
                                          [[["Blur","Silence"]],              [["Create Food and Water","Protection from Energy"]], [["Blight","Hallucinatory Terrain"]],        [["Control Winds","Wall of Stone"]]],
                                          [[["Augury","Barkskin"]],           [["Call Lightning","Plant Growth"]],                  [["Divination","Freedom of Movement"]],      [["Commune with Nature","Plant Door"]]],
                                          [[["Augury","Pass without Trace"]], [["Daylight","Haste"]],                               [["Air Walk","Divination"]],                 [["Dream","Insect Plague"]]],
                                          [[["Spider Climb","Spike Growth"]], [["Elemental Mantle","Meld into Stone"]],             [["Confusion","Stoneskin"]],                 [["Passwall","Wall of Stone"]]],
                                          [[["Augury","Locate Object"]],      [["Water Walk","Stinking Cloud"]],                    [["Freedom of Movement","Locate Creature"]], [["Insect Plague","Scrying"]]],
                                          [[["Augury","Spike Growth"]],       [["Sleet Storm","Slow"]],                             [["Freedom of Movement","Ice Storm"]],       [["Commune with Nature","Cone of Cold"]]]]
      for i,land in enumerate(landList):
         c.chooseLand(land)
         if c.landChosen != land:
            self.failTest("Class->common->chooseLand->"+c.classString+": chosen land '"+str(c.landChosen)+"' seen + '"+str(land)+"'expected")
            
         self.common_choosePath(c,"Circle of the Land",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
   #
   def FighterClassTests(self):
      #updateFeatures
      #superiorityDicePerLevel =  [0,0,2,2,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4]
      c = Fighter()
      c.choosePath("Path of the Weaponmaster")
      index = 2
      levelList =    [1,3,7,10]
      dirtyTrickString = "Dirty Trick:(WIS) gain ADV on attack"
      springAwayString = "Spring Away:(DEX) move half speed"
      tripString = "Trip:(STR) target is prone"
      failString = "If roll is less than mod, add pips to damage"
      newEntryList =   [[["Gain 0d6 superiority dice to use on maneuvers, Compare die roll to (MOD)",dirtyTrickString,springAwayString,tripString,failString]],
                        [["Gain 2d6 superiority dice to use on maneuvers, Compare die roll to (MOD)",dirtyTrickString,springAwayString,tripString,failString]],
                        [["Gain 3d6 superiority dice to use on maneuvers, Compare die roll to (MOD)",dirtyTrickString,springAwayString,tripString,failString]],
                        [["Gain 4d6 superiority dice to use on maneuvers, Compare die roll to (MOD)",dirtyTrickString,springAwayString,tripString,failString]]]
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,["Combat Superiority"],newEntryList[i])
      
      #choosePath
      #Path of the Weaponmaster
      c = Fighter()
      indicesList = [6,9,14]
      expectedFeatureList =  [["Advanced Maneuvers"],
                              ["Improved Combat Superiority"],
                              ["Relentless"]]
      expectedFeatureDescriptionsList =  [[["Bell Ringer:(CON) target loses reactions, has DISADV on next attack","Drive Back:(STR) Push target 15ft","Hamstring:(DEX) Reduce target speed 15ft, all attacks against target gain ADV"]],
                                          [["Use d10s for superiority dice"]],
                                          [["If you start the turn no superiority dice, gain 2 at the end of it"]]]
      self.common_choosePath(c,"Path of the Weaponmaster",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      #Path of the Warrior
      c = Fighter()
      indicesList = [2,6,14,18]
      expectedFeatureList =  [["Improved Critical"],
                              ["Superior Critical"],
                              ["Devastating Critical"],
                              ["Survivor"]]
      expectedFeatureDescriptionsList =  [[["Count rolls of 19 as criticals"]],
                                          [["Count rolls of 18 as criticals"]],
                                          [["Impose a secondary effect on critical hits, based on damage type:","Bludgeoning:Stun target on a CON save of DC 10+STR mod","Slashing:Target's speed drops to 0","Piercing:Target takes 1d6+(FighterLvl/2) damage per turn, tending to the wound stops this"]],
                                          [["Recover 5+CON mod HP at the start of your turn if you are at less than half HP"]]]
      self.common_choosePath(c,"Path of the Warrior",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      #chooseStyle    fightingStyleOptions = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
      #Path of the Weaponmaster
      indicesList = [0,9]
      styleList =             [["Archery",""], ["Defense",""], ["Great Weapon Fighting",""], ["Protection",""],["Two-Weapon Fighting",""],["","Archery"]]
      expectedFeatureList =  [[["Fighting Style: Archery","Second Wind"],               ["Improved Combat Superiority"]],
                              [["Fighting Style: Defense","Second Wind"],               ["Improved Combat Superiority"]],
                              [["Fighting Style: Great Weapon Fighting","Second Wind"], ["Improved Combat Superiority"]],
                              [["Fighting Style: Protection","Second Wind"],            ["Improved Combat Superiority"]],
                              [["Fighting Style: Two-Weapon Fighting","Second Wind"],   ["Improved Combat Superiority"]],
                              [["Fighting style","Second Wind"],                        ["Improved Combat Superiority"]]]
      defaultDes = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
      secondWindDes = ["Gain temporary (1d6 + Fighter Level) HP "]
      improvedCombatSuperiorityDes = ["Use d10s for superiority dice"]
      archeryDes = ["+1 to attack rolls with ranged weapons"]
      defenseDes = ["+1 to AC while wearing armor"]
      greatWeaponFightingDes = ["If you miss with a 2 handed weapon, enemy takes STR mod as damage"]
      protectionDes = ["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"]
      twoWeaponFightingDes = ["Add your ability mod to the damage of the second attack"]
      expectedFeatureDescriptionsList =  [[[archeryDes,secondWindDes],             [improvedCombatSuperiorityDes]],
                                          [[defenseDes,secondWindDes],             [improvedCombatSuperiorityDes]],
                                          [[greatWeaponFightingDes,secondWindDes], [improvedCombatSuperiorityDes]],
                                          [[protectionDes,secondWindDes],          [improvedCombatSuperiorityDes]],
                                          [[twoWeaponFightingDes,secondWindDes],   [improvedCombatSuperiorityDes]],
                                          [[defaultDes,secondWindDes],             [improvedCombatSuperiorityDes]]]
      for i,style in enumerate(styleList):
         c = Fighter()
         c.choosePath("Path of the Weaponmaster")
         c.chooseFightingStyle(style)
         if c.fightingStylesChosen != style:
            self.failTest("Class->common->chooseStyle->"+c.classString+": '"+str(c.fightingStylesChosen)+"' seen + '"+str(style)+"'expected")
            
         self.common_choosePath(c,"Path of the Warrior",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
      #Path of the Warrior
      indicesList = [0,9]
      styleList =             [["Archery","Defense"], ["Defense","Great Weapon Fighting"], ["Great Weapon Fighting","Protection"], ["Protection","Two-Weapon Fighting"],["Two-Weapon Fighting","Archery"],["Archery",""],["","Archery"]]
      expectedFeatureList =  [[["Fighting Style: Archery","Second Wind"],               ["Additional Fighting Style: Defense"]],
                              [["Fighting Style: Defense","Second Wind"],               ["Additional Fighting Style: Great Weapon Fighting"]],
                              [["Fighting Style: Great Weapon Fighting","Second Wind"], ["Additional Fighting Style: Protection"]],
                              [["Fighting Style: Protection","Second Wind"],            ["Additional Fighting Style: Two-Weapon Fighting"]],
                              [["Fighting Style: Two-Weapon Fighting","Second Wind"],   ["Additional Fighting Style: Archery"]],
                              [["Fighting Style: Archery","Second Wind"],               ["Martial Path benefit"]],
                              [["Fighting style","Second Wind"],                        ["Additional Fighting Style: Archery"]]]
      expectedFeatureDescriptionsList =  [[[archeryDes,secondWindDes],             [defenseDes]],
                                          [[defenseDes,secondWindDes],             [greatWeaponFightingDes]],
                                          [[greatWeaponFightingDes,secondWindDes], [protectionDes]],
                                          [[protectionDes,secondWindDes],          [twoWeaponFightingDes]],
                                          [[twoWeaponFightingDes,secondWindDes],   [archeryDes]],
                                          [[archeryDes,secondWindDes],             [[""]]],
                                          [[defaultDes,secondWindDes],             [archeryDes]]]
      for i,style in enumerate(styleList):
         c = Fighter()
         c.choosePath("Path of the Warrior")
         c.chooseFightingStyle(style)
         if c.fightingStylesChosen != style:
            self.failTest("Class->common->chooseStyle->"+c.classString+": '"+str(c.fightingStylesChosen)+"' seen + '"+str(style)+"'expected")
            
         self.common_choosePath(c,"Path of the Warrior",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
   #
   def MageClassTests(self):
      #updateFeatures
      #choosePath
      # School of Enchantment
      c = Mage()
      indicesList = [1,4,11,15,19]
      expectedFeatureList =  [["Aura of Antipathy"],
                              ["Instinctive Charm"],
                              ["Split Enchantment"],
                              ["Rapid Enchantment"],
                              ["Alter Memories"]]
      expectedFeatureDescriptionsList =  [[["Any creature within 10ft has DISADV to attack you"]],
                                          [["Change attack target of any creature within 50ft to be closest target","WIS saving throw negates effect"]],
                                          [["Single-target enchantment spells, can now target a 2nd target"]],
                                          [["Casting time of a enchantment reduced from 1 action to 1 swift action"]],
                                          [["Charmed creatures think behavior is non-magical","Use an action to force creature to forget (1+CHA mod) hours (INT save negates)","Even it can't forget, make a deception(CHA) check (DC = its INT save roll) to add new memories"]]]
      self.common_choosePath(c,"School of Enchantment",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)

      # School of Evocation
      c = Mage()
      indicesList = [1,4,11,15,19]
      expectedFeatureList =  [["Scult Spells"],
                              ["Potent Cantrip"],
                              ["Overchannel"],
                              ["Empowered Evocation"],
                              ["Evocation Master"]]
      expectedFeatureDescriptionsList =  [[["Evocation spells can now target (spell level + 1) number of targets","They automatically pass saving throws","They take no damage if they would normally take only half"]],
                                          [["If an evocation cantrip fails, the creature takes half damage and no effect"]],
                                          [["Deal maximum damage with a spell of level 3 or lower","Upon 2nd time casting this without rest make a DC 15(+5 each subsequent time) CON check", "Failure drops you to 0 HP"]],
                                          [["Add your INT mod to damage of evocation spells"]],
                                          [["Fireball and Lightning bolt spells are free to cast"]]]
      self.common_choosePath(c,"School of Evocation",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      # School of Illusion
      c = Mage()
      indicesList = [1,4,11,15,19]
      expectedFeatureList =  [["Improved Minor Tricks"],
                              ["Disappearing Trick"],
                              ["Illusionary Self"],
                              ["Illusionary Reality"],
                              ["Illusion Master"]]
      expectedFeatureDescriptionsList =  [[["Learn minor illusion cantrip, and use with ghost sound and silent image as a single spell"]],
                                          [["Always have the invisibility spell prepared","Use your reaction after taking damage to cast invisibility"]],
                                          [["You can create an illusionary copy of yourself instantly","If you are attacked before your first turn, this is cast and you take no damage"]],
                                          [["Choose one inanimate, nonmagical object that is part of an illusion to make real","Remains real until end of your next turn, cannot directly harm anyone"]],
                                          [["You can cast major image for free"]]]
      self.common_choosePath(c,"School of Illusion",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
   #
   def MonkClassTests(self):
      #updateFeatures
      #   unarmedStrkeDiePerLevel =  [6,6,6,6,8,8,8,8,8,8,10,10,10,10,10,10,12,12,12,12]
      c = Monk()
      index = 0
      levelList =    [1,5,11,17]
      flurryOfBlowsDes = ["Use your attack action to make 2 unarmed attacks","Spend an Ki point to make an additional attack"]
      unarmoredDefenseDes = ["While wearing no armor, AC = 10 + DEX mod + WIS mod"]
      newEntryList =   [[flurryOfBlowsDes,["Unarmed strike is a finesse weapon that deals 1d6 bludgeoning damage"],unarmoredDefenseDes],
                        [flurryOfBlowsDes,["Unarmed strike is a finesse weapon that deals 1d8 bludgeoning damage"],unarmoredDefenseDes],
                        [flurryOfBlowsDes,["Unarmed strike is a finesse weapon that deals 1d10 bludgeoning damage"],unarmoredDefenseDes],
                        [flurryOfBlowsDes,["Unarmed strike is a finesse weapon that deals 1d12 bludgeoning damage"],unarmoredDefenseDes]]
      
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,["Flurry of Blows","Unarmed Strike","Unarmored Defense"],newEntryList[i])
      #choosePath
      # Way of the Four Elements
      c = Monk()
      indicesList = [2,5,10,16]
      
      expectedFeatureList =  [["Disciple of the Elements","Step of the Wind"],
                              ["Elemental Power"],
                              ["Elemental Master"],
                              ["Fist of the Four Elements"]]
      expectedFeatureDescriptionsList =  [[[""],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]],
                                          [[""]],
                                          [[""]],
                                          [["Spend 1 Ki point to add 1d10 of cold, fire, lightning, or thunder damage to your melee attack"]]]
      
      self.common_choosePath(c,"Way of the Four Elements",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      # Way of the Open Hand
      c = Monk()
      indicesList = [2,5,10,16]
      
      expectedFeatureList =  [["Deflect Missles"],
                              ["Wholeness of Body"],
                              ["Improved Flurry of Blows"],
                              ["Quivering Palm"]]
      expectedFeatureDescriptionsList =  [[["Use reaction to reduce damage from ranged attack by 1d10+DEX mod, if 0 you may catch it","Use a Ki point to reduce by a further 1d10"]],
                                          [["Regain HP by 2 * Monk Level"]],
                                          [["Spending a Ki point on Flurry of Blows also gains you an effect:","Sweep: If it hits, knock the target prone","Knockback: If it hits, push the target up to 10ft away","Daze: if it hits, target cannot make reactions"]],
                                          [["Spend 3 Ki points to mark a target for death","Use an action any time in at most (Monk Level) days","CON save DC = 8 + WIS + proficiency: failure causes target to die","Cooldown is 1 week"]]]
      
      self.common_choosePath(c,"Way of the Open Hand",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      #chooseElements   
      #elementsToChoose = ["Fire","Air","Earth","Water"]
      #elementsChosen = ["","",""]
      c = Monk()
      elementTripletList = [["Fire","Air","Earth"],["Water","Fire","Air"],["Earth","Water","Fire"],["Air","Earth","Water"]]
      
      discipleFire = ["Disciple of the Elements: Fire Riposte","Step of the Wind"]
      discipleFireDes = [["Hit by a melee attack, Use reaction and a Ki point to give 1d10+Monk Level fire damage to attacker","DEX save halves damage"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]]
      discipleAir =["Disciple of the Elements: Wind Riposte","Step of the Wind"]
      discipleAirDes = [["Hit by a melee attack, Use reaction and a Ki point to push attacker 20 feet (STR save halves distance)"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]]
      discipleEarth = ["Disciple of the Elements:Iron Root Defense","Step of the Wind"]
      discipleEarthDes = [["Spend a Ki point to root yourself and reduce damage by Monk Level"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]]
      discipleWater = ["Disciple of the Elements:Shelter of the Flowing River","Step of the Wind"]
      discipleWaterDes = [["Spend a Ki point to gain ADV on STR, DEX, or CON saving throw"],["Speed increase by 5ft","Use a Ki point to increase by 15ft"]]
      
      powerFire = ["Elemental Power:Flames of the Phoenix"]
      powerFireDes = [["Spend 1 Ki point to emit 15ft cone of 1d10 + Monk Level fire damage (DEX halves)"]]
      powerAir = ["Elemental Power:Vortex Punch"]
      powerAirDes = [["Spend 1 Ki point to emit a 50ft line of 1d6 + Monk Level bludgeoning damage (STR halves)", "Knock all hit targets prone (STR negates)"]]
      powerEarth = ["Elemental Power:Grasp of Stone"]
      powerEarthDes = [["When you hit, spend a Ki point to grapple enemy (STR negates)","Your unarmed attacks automatically hit while grappled"]]
      powerWater = ["Elemental Power:Crashing Waves"]
      powerWaterDes = [["When you hit, spend a Ki point to push enemy 20ft (STR halves)"]]
      
      masterFire = ["Elemental Master:Vengeful Flame"]
      masterFireDes = [["When you drop to 0 HP, spend a Ki point: every creature in 25ft takes 1d10 + Monk Level fire damage (DEX halves)"]]
      masterAir = ["Elemental Master:Warrior's Gale"]
      masterAirDes = [["Spend a Ki point to gain a flight speed of 50ft"]]
      masterEarth = ["Elemental Master:Touch of Stony Doom"]
      masterEarthDes = [["When you hit, spend a Ki point to make the target vulnerable to bludgeoning damage for 1 minute (CON negates)"]]
      masterWater = ["Elemental Master:Spirit of the Tsunami"]
      masterWaterDes = [["Spend 1 Ki point to emit 15ft cone of 1d10 + Monk Level bludgeoning damage, and is knocked prone (CON halves)"]]
      
      fist = ["Fist of the Four Elements"]
      fistDes = [["Spend 1 Ki point to add 1d10 of cold, fire, lightning, or thunder damage to your melee attack"]]
                
      
      expectedFeatureList =  [[discipleFire,  powerAir,   masterEarth, fist],
                              [discipleWater, powerFire,  masterAir,   fist],
                              [discipleEarth, powerWater, masterFire,  fist],
                              [discipleAir,   powerEarth, masterWater, fist]]
      
      expectedFeatureDescriptionsList =  [[discipleFireDes,  powerAirDes,   masterEarthDes, fistDes],
                                          [discipleWaterDes, powerFireDes,  masterAirDes,   fistDes],
                                          [discipleEarthDes, powerWaterDes, masterFireDes,  fistDes],
                                          [discipleAirDes,   powerEarthDes, masterWaterDes, fistDes]]
      for i,triplet in enumerate(elementTripletList):
         c.chooseElements(triplet)
         if c.elementsChosen != triplet:
            self.failTest("Class->common->chooseAnimal->"+c.classString+": chosen animals '"+str(c.elementsChosen)+"' seen + '"+str(triplet)+"'expected")
            
         self.common_choosePath(c,"Way of the Four Elements",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
   #
   def PaladinClassTests(self):
      #updateFeatures
      #choosePath
      # Oath of Devotion
      c = Paladin()
      indicesList = [2,4,7,8,12,16,17,19]
      
      expectedFeatureList =  [["Divine Health","Oath Spells","Channel Divinity"],
                              ["Extra Attack","Oath Spells"],
                              ["Turn Fiends"],
                              ["Oath Spells"],
                              ["Oath Spells"],
                              ["Oath Spells"],
                              ["Banishing Strike"],
                              ["Channel Divinity:Holy Nimbus"]]
      expectedFeatureDescriptionsList =  [[["You are immune to disease"],["Protection from Evil","Sanctuary"],["Sacred Weapon: weapon is gains magical +CHA to attack, emits 20ft bright light 20ft dim","Turn Undead: Undead within 25ft make WIS save, or are turned"]],
                                          [["You can attack an extra time"],["Lesser Restoration, Zone of Truth"]],
                                          [["Turn Undead also affects fiends"]],
                                          [["Beacon of Hope","Dispel magic"]],
                                          [["Freedom of Movement","Guardian of Faith"]],
                                          [["Commune","Flame Strike"]],
                                          [["Smite feature banishes fiends who fail a CHA saving throw"]],
                                          [["Emit bright sunlight in 25ft, dim sunlight in 25ft beyond. enemies take 10 damage on turn start in bright light","While active, gain ADV on saves against fiends/undead spell casting"]]]
      
      self.common_choosePath(c,"Oath of Devotion",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      # Oath of Vengeance
      c = Paladin()
      indicesList = [2,4,7,8,12,16,17,19]
      
      
      
      expectedFeatureList =  [["Divine Health","Oath Spells","Channel Divinity"],
                              ["Extra Attack","Oath Spells"],
                              ["Relentless Avenger"],
                              ["Oath Spells"],
                              ["Oath Spells"],
                              ["Oath Spells"],
                              ["Soul of Vengeance"],
                              ["Channel Divinity:Avenging Angel"]]
      expectedFeatureDescriptionsList =  [[["You are immune to disease"],["Cause Fear","Hunter's Mark"],["Abjure Enemy:Frighten one enemy in 60ft, Undead/fiend have DISADV (WIS causes speed to be halved)","Vow of Enmity:Creature is hit within 10ft, Gain ADV on attack against attacker"]],
                                          [["You can attack an extra time"],["Hold Person","Misty Step"]],
                                          [["Hitting a creature with an opportuntity attack allows you to move half your speed"]],
                                          [["Haste","Protection from Energy"]],
                                          [["Air Walk","Dimension Door"]],
                                          [["Hold Monster","Scrying"]],
                                          [["When the creature under Vow of Enmity makes an attack, use reaction to make an attack"]],
                                          [["Undergo a transformation to gain flight (60ft), and frighten enemies in 30ft range (WIS negates)","Attacks versus the frightened creature have ADV"]]]
      
      self.common_choosePath(c,"Oath of Vengeance",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      # chooseStyle
      indicesList = [1]
      styleList =             ["","Archery", "Defense", "Great Weapon Fighting", "Protection","Two-Weapon Fighting"]
      
      expectedFeatureList =  [[["Divine Smite","Fighting Style","Spellcasting"]],
                              [["Divine Smite","Fighting Style: Archery","Spellcasting"]],
                              [["Divine Smite","Fighting Style: Defense","Spellcasting"]],
                              [["Divine Smite","Fighting Style: Great Weapon Fighting","Spellcasting"]],
                              [["Divine Smite","Fighting Style: Protection","Spellcasting"]],
                              [["Divine Smite","Fighting Style: Two-Weapon Fighting","Spellcasting"]]]
                              
      divineSmiteDes = ["Expend 1 paladin spell to deal (1+spell level)d8","Deals 1d8 extra for undead or fiendish creatures"]
      defaultDes = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
      spellcastingDes = ["DC = 8 + CHA mod, + proficiency if holy symbol present"]
      improvedCombatSuperiorityDes = ["Use d10s for superiority dice"]
      archeryDes = ["+1 to attack rolls with ranged weapons"]
      defenseDes = ["+1 to AC while wearing armor"]
      greatWeaponFightingDes = ["If you miss with a 2 handed weapon, enemy takes STR mod as damage"]
      protectionDes = ["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"]
      twoWeaponFightingDes = ["Add your ability mod to the damage of the second attack"]
      expectedFeatureDescriptionsList =  [[[divineSmiteDes,defaultDes,spellcastingDes]],
                                          [[divineSmiteDes,archeryDes,spellcastingDes]],
                                          [[divineSmiteDes,defenseDes,spellcastingDes]], 
                                          [[divineSmiteDes,greatWeaponFightingDes,spellcastingDes]],
                                          [[divineSmiteDes,protectionDes,spellcastingDes]],  
                                          [[divineSmiteDes,twoWeaponFightingDes,spellcastingDes]]]
      for i,style in enumerate(styleList):
         c = Paladin()
         c.chooseFightingStyle(style)
         if c.fightingStylesChosen != style:
            self.failTest("Class->common->chooseStyle->"+c.classString+": '"+str(c.fightingStylesChosen)+"' seen + '"+str(style)+"'expected")
            
         self.common_choosePath(c,"Oath of Vengeance",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
   #
   def RangerClassTests(self):
      #updateFeatures
      #choosePath
      # Colossus Slayer
      c = Ranger()
      indicesList = [1,6,10,14]
      
      expectedFeatureList =  [["Slayer's Momentum","Fighting Style"],
                              ["Steel Will"],
                              ["Staggering Attack"],
                              ["Uncanny Dodge"]]
      expectedFeatureDescriptionsList =  [[["If you damage a creature with a weapon attack, deal +1d6 to that creature next attack"],["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]],
                                          [["Gain ADV on saves versus being frightened"]],
                                          [["When you hit a creature with a weapon attack, gain ADV on all other attacks to that target this turn"]],
                                          [["On a DEX saving throw to only take half damage, take none on success, half on failure"]]]
      
      self.common_choosePath(c,"Path of the Colossus Slayer",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      # Horde Breaker
      c = Ranger()
      indicesList = [1,6,10,14]
      
      expectedFeatureList =  [["Hordeslayer","Fighting Style"],
                              ["Hunter's Mobility"],
                              ["Whirlwind Attack"],
                              ["Pack Awareness"]]
      expectedFeatureDescriptionsList =  [[["If you damage a creature with a weapon attack, deal +1d8 to each other creature you attack"],["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]],
                                          [["Opportunity attacks against you have DISADV"]],
                                          [["Use your action to make a melee attack against each enemy creature within 5ft of you"]],
                                          [["If you are not surprised at the start of combat, allies within 25ft are not either"]]]
      
      self.common_choosePath(c,"Path of the Horde Breaker",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      
      # chooseStyle
      indicesList = [1]
      styleList =             ["","Archery", "Defense", "Great Weapon Fighting", "Protection","Two-Weapon Fighting"]
      
      expectedFeatureList =  [[["Slayer's Momentum","Fighting Style"]],
                              [["Slayer's Momentum","Fighting Style: Archery"]],
                              [["Slayer's Momentum","Fighting Style: Defense"]],
                              [["Slayer's Momentum","Fighting Style: Great Weapon Fighting"]],
                              [["Slayer's Momentum","Fighting Style: Protection"]],
                              [["Slayer's Momentum","Fighting Style: Two-Weapon Fighting"]]]
                              
      slayersMomentumDes = ["If you damage a creature with a weapon attack, deal +1d6 to that creature next attack"]
      defaultDes = ["Archery", "Defense","Great Weapon Fighting","Protection","Two-Weapon Fighting"]
      spellcastingDes = ["DC = 8 + CHA mod, + proficiency if holy symbol present"]
      improvedCombatSuperiorityDes = ["Use d10s for superiority dice"]
      archeryDes = ["+1 to attack rolls with ranged weapons"]
      defenseDes = ["+1 to AC while wearing armor"]
      greatWeaponFightingDes = ["If you miss with a 2 handed weapon, enemy takes STR mod as damage"]
      protectionDes = ["In 5ft, if visible creature makes attack roll, use reaction to give it DISADV"]
      twoWeaponFightingDes = ["Add your ability mod to the damage of the second attack"]
      expectedFeatureDescriptionsList =  [[[slayersMomentumDes,defaultDes]],
                                          [[slayersMomentumDes,archeryDes]],
                                          [[slayersMomentumDes,defenseDes]], 
                                          [[slayersMomentumDes,greatWeaponFightingDes]],
                                          [[slayersMomentumDes,protectionDes]],  
                                          [[slayersMomentumDes,twoWeaponFightingDes]]]
      for i,style in enumerate(styleList):
         c = Ranger()
         c.chooseFightingStyle(style)
         if c.fightingStylesChosen != style:
            self.failTest("Class->common->chooseStyle->"+c.classString+": '"+str(c.fightingStylesChosen)+"' seen + '"+str(style)+"'expected")
            
         self.common_choosePath(c,"Path of the Colossus Slayer",indicesList,expectedFeatureList[i],expectedFeatureDescriptionsList[i])
   #
   def RogueClassTests(self):
      #updateFeatures
      #sneakAttackDice = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7]
      expertiseDes = ["Gain +5 to all checks using up to 4 of your skill or tool proficiencies"]
      sneakAttackDes = ["Add damage to a strike if you have ADV or an able enemy of target is within 5ft"]
      c = Rogue()
      index = 0
      levelList =    [1,5,8,11,14,17,20]
      newEntryList =   [["Expertise", "Sneak Attack (1d6)"],
                        ["Expertise", "Sneak Attack (2d6)"],
                        ["Expertise", "Sneak Attack (3d6)"],
                        ["Expertise", "Sneak Attack (4d6)"],
                        ["Expertise", "Sneak Attack (5d6)"],
                        ["Expertise", "Sneak Attack (6d6)"],
                        ["Expertise", "Sneak Attack (7d6)"]]
      for i,level in enumerate(levelList):
         self.common_updateFeatures(c,level,index,newEntryList[i],[expertiseDes,sneakAttackDes])
      
      #choosePath
      # Assassination
      c = Rogue()
      indicesList = [2,5,8,12,15]
      
      expectedFeatureList =  [["Assassinate"],
                              ["Poison Mastery"],
                              ["Infiltration Expertise"],
                              ["Impostor"],
                              ["Death Strike"]]
      expectedFeatureDescriptionsList =  [[["On first turn, gain ADV on any creature not yet taken a turn","Score an automatic critical against surprised enemies, use max result for sneak attack"]],
                                          [["Spend 1 hour to make a tasteless, colorless, odorless liquid to do 1 of 3 things (CON save DC 10+INT mod)","Unconsciousness for 2d6+4 hours","Intoxication for 24 hours, HP max is halved","As if it was under a non-magical confusion spell"]],
                                          [["You can create false identities for yourself, takes 1 week and 25gp"]],
                                          [["Spend 1 hour studying person to mimic them","You have advantage on any deception checks made to avoid detection"]],
                                          [["If you make an attack against a surprised creature, deal double the damage (CON save DC 10+DEX mod negates doubling)"]]]
      
      self.common_choosePath(c,"Assassination",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
      toolProficienciesExpected = ["kitThief","kitDisguise","kitPoisoners"]
      if c.toolProficiencies != toolProficienciesExpected:
         self.failTest("Class->common->updateFeatures->"+c.classString+"->ToolProficiencies: '"+str(c.toolProficiencies)+"' found, '" + str(toolProficienciesExpected) + "' expected")
      
      # Thievery
      c = Rogue()
      indicesList = [2,5,8,12,15]   
      
      expectedFeatureList =  [["Burglary","Fast Hands"],
                              ["Decipher Script"],
                              ["Supreme Sneak"],
                              ["Use Magic Device"],
                              ["Thief's Reflexes"]]
      expectedFeatureDescriptionsList =  [[["Climbing doesn't half your speed","Long jump distance increases by 10ft, high jump by 5ft"],["Use your Cunning Action to make sleight of hand checks"]],
                                          [["Study a page of text for a minute to puzzle out the meaning","1 hour of text to discover the full meaning"]],
                                          [["Gain ADV on any ability check to hide if you move no more than half speed"]],
                                          [["Ignore all class, race, and level requirements on the use of magic items"]],
                                          [["Take 2 turns at the beginning of a battle (2nd is at initiative - 10)"]]]
      
      self.common_choosePath(c,"Thievery",indicesList,expectedFeatureList,expectedFeatureDescriptionsList)
#
class MoneyUnitTests(UnitTest):
   name = "Money Unit Tests"
   def run(self):
      self.conversionUnitTests()
   def checkExpectedValues(self,money,cp,sp,ep,gp,pp,failString):
      if money.cp != cp or money.sp != sp or money.ep != ep or money.gp != gp or money.pp != pp:
         self.failTest("Equipment->money->"+failString+"->(" + str(money.cp) +","+ str(money.sp) +","+ str(money.ep) +","+ str(money.gp) +","+ str(money.pp) +") seen ("+ str(cp) +","+ str(sp) +","+ str(ep) +","+ str(gp) +","+ str(pp) +") expected")
   def conversionUnitTests(self):
      #convertToCopper
      m = Money(2,3,4,5,6)
      m.convertToCopper()
      self.checkExpectedValues(m,6732,0,0,0,0,"Spread to copper")
      if m.getTotalInCopper() != 6732:
         self.failTest("Equipment->money->Spread to copper->Bad copper amount")
      #convertToHighestValueCoins
      m = Money(5000)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,0,0,0,5,"5000 cp to 5 pp")
      if m.getTotalInCopper() != 5000:
         self.failTest("Equipment->money->5000 cp to 5 pp->Bad copper amount")
      m = Money(0,5000)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,0,0,0,50,"5000 sp to 50 pp")
      if m.getTotalInCopper() != 50000:
         self.failTest("Equipment->money->5000 sp to 50 pp->Bad copper amount")
      m = Money(0,0,5000)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,0,0,0,250,"5000 ep to 250 pp")
      if m.getTotalInCopper() != 250000:
         self.failTest("Equipment->money->5000 ep to 250 pp->Bad copper amount")
      m = Money(0,0,0,5000)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,0,0,0,500,"5000 gp to 500 pp")
      if m.getTotalInCopper() != 500000:
         self.failTest("Equipment->money->5000 gp to 500 pp->Bad copper amount")
      m = Money(500)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,0,0,5,0,"500 cp to 5 gp")
      if m.getTotalInCopper() != 500:
         self.failTest("Equipment->money->500 cp to 5 gp->Bad copper amount")
      m = Money(50)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,0,1,0,0,"50 cp to 1 ep")
      if m.getTotalInCopper() != 50:
         self.failTest("Equipment->money->50 cp to 1 ep->Bad copper amount")
      m = Money(40)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,4,0,0,0,"40 cp to 4 sp")
      if m.getTotalInCopper() != 40:
         self.failTest("Equipment->money->40 cp to 4 sp->Bad copper amount")
      m = Money(50,0,0,0,0,False)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,0,5,0,0,0,"50 cp to 5 sp")
      if m.getTotalInCopper() != 50:
         self.failTest("Equipment->money->50 cp to 5 sp->Bad copper amount")
      m = Money(6582)
      m.convertToHighestValueCoins()
      self.checkExpectedValues(m,2,3,1,5,6,"Spread from copper")
      if m.getTotalInCopper() != 6582:
         self.failTest("Equipment->money->Spread from copper->Bad copper amount")
      
unitTestFramework = [ClassUnitTest(),MoneyUnitTests()]
for unitTestGroup in unitTestFramework:
   start = int(round(time.time() * 1000))
   unitTestGroup.run()
   stop = int(round(time.time() * 1000))
   print unitTestGroup.name + " took " + str(stop-start) + " milliseconds"