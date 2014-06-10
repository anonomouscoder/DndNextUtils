class BaseRace:
   raceString = "BaseRace"
   abiltyAdjustment = []
   abilitiesToChoose = 0
   size = "medium"
   speed = 30
   vision = "normal"
   languages = []
   languagesToChoose = 0
   languagesToChooseFrom = []
   subraces = []
   weaponProficiencies = []
   traits = [""]
   def chooseSubRace(self,choice):
      return
   def __init__(self,choice):
      self.chooseSubRace(choice)
#
class Dwarf(BaseRace):
   raceString = "Dwarf"
   abiltyAdjustment = ["con"]
   speed = 25
   vision = "darkvision"
   languages = ["common","dwarvish"]
   languagesToChoose = 1
   languagesToChooseFrom = ["gnomish","orcish","primordial"]
   weaponProficiencies = ["battleaxe","handaxe","throwing hammer","warhammer"]
   traits = ["Dwarven Resilience","Stonecunning"]
   subraces = ["Hill Dwarf","Mountain Dwarf"]
   def chooseSubRace(self,choice):
      if choice == self.subraces[0]: # Hill Dwarf
         self.abiltyAdjustment.append("str")
         self.traits.append("Dwarven Toughness")
      elif choice == self.subraces[1]: # Mountain Dwarf
         self.abiltyAdjustment.append("wis")
         self.traits.append("Armor Mastery")
#
class Elf(BaseRace):
   raceString = "Elf"
   abiltyAdjustment = ["dex"]
   vision = "lowlight"
   languages = ["common","elvish"]
   languagesToChoose = 1
   weaponProficiencies = ["longSword","shortSword","shortbow","longbow"]
   traits = ["Keen Senses","Fey Ancestry","Trance"]
   subraces = ["High Elf","Wood Elf"]
   def chooseSubRace(self,choice):
      if choice == self.subraces[0]: # High Elf
         self.abiltyAdjustment.append("int")
         self.traits.append("Cantrip")
         self.languagesToChoose = self.languagesToChoose + 1
      elif choice == self.subraces[1]: # Wood Elf
         self.abiltyAdjustment.append("wis")
         self.speed = self.speed + 5
         self.traits.append("Mask of the Wild")
#
class Halfling(BaseRace):
   raceString = "Halfling"
   abiltyAdjustment = ["dex"]
   size = "small"
   speed = 25
   languages = ["common","halfling"]
   traits = ["Lucky","Brave","Halfling Nimbleness"]
   subraces = ["Lightfoot","Stout"]
   def chooseSubRace(self,choice):
      if choice == self.subraces[0]: # Lightfoot
         self.abiltyAdjustment.append("cha")
         self.traits.append("Naturally Stealthy")
         self.languagesToChoose = self.languagesToChoose + 1
      elif choice == self.subraces[1]: # Stout
         self.abiltyAdjustment.append("con")
         self.traits.append("Stout Resilience")
#
class Human(BaseRace):
   raceString = "Human"
   abiltyAdjustment = ["str","con","dex","int","wis","cha"]
   languages = ["common"]
   languagesToChoose = 1
#
class Dragonborn(BaseRace):
   raceString = "Dragonborn"
   abiltyAdjustment = ["str","cha"]
   languages = ["common","draconic"]
   traits = ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
#
class Drow(BaseRace):
   raceString = "Drow"
   abiltyAdjustment = ["dex","cha"]
   vision = "darkvision"
   languages = ["common","elvish","undercommon"]
   traits = ["Keen Senses","Sunlight Sensitivity","Fey Ancestry","Lolth-Touched Magic","Trance"]
#
class Gnome(BaseRace):
   raceString = "Gnome"
   abiltyAdjustment = ["int"]
   speed = 25
   size = "small"
   vision = "lowlight"
   languages = ["common","gnomish"]
   traits = ["Gnome Cunning"]
   subraces = ["Forest Gnome","Rock Gnome"]
   def chooseSubRace(self,choice):
      if choice == self.subraces[0]: # Lightfoot
         self.abiltyAdjustment.append("dex")
         self.traits.append("Natural Illusionist")
         self.traits.append("Speak with Small Beasts")
      elif choice == self.subraces[1]: # Stout
         self.abiltyAdjustment.append("con")
         self.traits.append("Artificer's love")
         self.traits.append("Tinker")
#
class Halfelf(BaseRace):
   raceString = "Half-elf"
   abiltyAdjustment = ["cha"]
   abilitiesToChoose = 1
   vision = "lowlight"
   languages = ["common","elvish"]
   languagesToChoose = 1
   traits = ["Keen Senses","Fey Ancestry"]
#
class Halforc(BaseRace):
   raceString = "Half-orc"
   abiltyAdjustment = ["str","str","con"]
   vision = "darkvision"
   languages = ["common","orcish"]
   traits = ["Menacing"]
#
class Kender(BaseRace):
   raceString = "Kender"
   abiltyAdjustment = ["dex","cha"]
   speed = 25
   size = "small"
   languages = ["common","kenderspeak"]
   traits = ["Fearless","Taunt","Kender Pocket"]
#
class Tiefling(BaseRace):
   raceString = "Tiefling"
   abiltyAdjustment = ["int","cha"]
   vision = "lowlight"
   languages = ["common","infernal"]
   traits = ["Hellish Resistance","Infernal Wrath"]
#
class Warforged(BaseRace):
   raceString = "Warforged"
   abiltyAdjustment = ["str","con"]
   languages = ["common"]
   languagesToChoose = 1
   traits = ["Composite Plating","Living Construct"]
#