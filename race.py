import string,sys,inspect
class BaseRace:
   def __str__(self):
      return (string.split(str(self.__class__),".",1))[1]

   def chooseSubRace(self,choice):
      self.subraceString = choice
      return
   def __init__(self,choice=""):
      self.raceString = "BaseRace"
      self.abiltyAdjustment = []
      self.subRaceAbilityAdjustment = []
      self.abilitiesToChoose = 0
      self.size = "medium"
      self.speed = 30
      self.vision = "normal"
      self.languages = []
      self.languagesToChoose = 0
      self.languagesToChooseFrom = []
      self.subraces = []
      self.subraceString = ""
      self.weaponProficiencies = []
      self.traits = []
      self.traitDescriptions = [[""]]
      self.subRaceTraits = []
      self.subRaceTraitDescriptions = [[""]]
#
class Dwarf(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Dwarf"
      self.abiltyAdjustment = ["con"]
      self.speed = 25
      self.vision = "darkvision"
      self.languages = ["common","dwarvish"]
      self.languagesToChoose = 1
      self.languagesToChooseFrom = ["gnomish","orcish","primordial"]
      self.weaponProficiencies = ["battleaxe","handaxe","throwing hammer","warhammer"]
      self.traits = ["Dwarven Resilience","Stonecunning"]
      self.traitDescriptions = [[""],[""]]
      self.subraces = ["Hill Dwarf","Mountain Dwarf"]
      self.chooseSubRace(choice)
   def chooseSubRace(self,choice):
      self.subraceString = choice
      if choice == self.subraces[0]: # Hill Dwarf
         self.subRaceAbilityAdjustment = ["str"]
         self.subRaceTraits = ["Dwarven Toughness"]
      elif choice == self.subraces[1]: # Mountain Dwarf
         self.subRaceAbilityAdjustment = ["wis"]
         self.subRaceTraits = ["Armor Mastery"]
#
class Elf(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Elf"
      self.abiltyAdjustment = ["dex"]
      self.vision = "lowlight"
      self.languages = ["common","elvish"]
      self.languagesToChoose = 1
      self.weaponProficiencies = ["longSword","shortSword","shortbow","longbow"]
      self.traits = ["Keen Senses","Fey Ancestry","Trance"]
      self.traitDescriptions = [[""],[""],[""]]
      self.subraces = ["High Elf","Wood Elf"]
      self.chooseSubRace(choice)
   def chooseSubRace(self,choice):
      self.subraceString = choice
      if choice == self.subraces[0]: # High Elf
         self.subRaceAbilityAdjustment = ["int"]
         self.subRaceTraits = ["Cantrip"]
         self.languagesToChoose = self.languagesToChoose + 1
      elif choice == self.subraces[1]: # Wood Elf
         self.subRaceAbilityAdjustment = ["wis"]
         self.speed = self.speed + 5
         self.subRaceTraits = ["Mask of the Wild"]
#
class Halfling(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Halfling"
      self.abiltyAdjustment = ["dex"]
      self.size = "small"
      self.speed = 25
      self.languages = ["common","halfling"]
      self.traits = ["Lucky","Brave","Halfling Nimbleness"]
      self.traitDescriptions = [[""],[""],[""]]
      self.subraces = ["Lightfoot","Stout"]
      self.chooseSubRace(choice)
   def chooseSubRace(self,choice):
      self.subraceString = choice
      if choice == self.subraces[0]: # Lightfoot
         self.subRaceAbilityAdjustment = ["cha"]
         self.subRaceTraits = ["Naturally Stealthy"]
         self.languagesToChoose = self.languagesToChoose + 1
      elif choice == self.subraces[1]: # Stout
         self.subRaceAbilityAdjustment = ["con"]
         self.subRaceTraits = ["Stout Resilience"]
#
class Human(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Human"
      self.abiltyAdjustment = ["str","con","dex","int","wis","cha"]
      self.languages = ["common"]
      self.languagesToChoose = 1
#
class Dragonborn(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Dragonborn"
      self.abiltyAdjustment = ["str","cha"]
      self.languages = ["common","draconic"]
      self.traits = ["Draconic Ancestry","Breath Weapon","Damage Resistance"]
      self.traitDescriptions = [[""],[""],[""]]
#
class Drow(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Drow"
      self.abiltyAdjustment = ["dex","cha"]
      self.vision = "darkvision"
      self.languages = ["common","elvish","undercommon"]
      self.traits = ["Keen Senses","Sunlight Sensitivity","Fey Ancestry","Lolth-Touched Magic","Trance"]
      self.traitDescriptions = [[""],[""],[""],[""],[""]]
#
class Gnome(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Gnome"
      self.abiltyAdjustment = ["int"]
      self.speed = 25
      self.size = "small"
      self.vision = "lowlight"
      self.languages = ["common","gnomish"]
      self.traits = ["Gnome Cunning"]
      self.subraces = ["Forest Gnome","Rock Gnome"]
      self.chooseSubRace(choice)
   def chooseSubRace(self,choice):
      self.subraceString = choice
      if choice == self.subraces[0]: # Lightfoot
         self.subRaceAbilityAdjustment = ["dex"]
         self.subRaceTraits = ["Natural Illusionist","Speak with Small Beasts"]
         self.subRaceTraitDescriptions = [[""],[""]]
      elif choice == self.subraces[1]: # Stout
         self.subRaceAbilityAdjustment = ["con"]
         self.subRaceTraits = ["Artificer's love","Tinker"]
         self.subRaceTraitDescriptions = [[""],[""]]
#
class Halfelf(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Half-elf"
      self.abiltyAdjustment = ["cha"]
      self.abilitiesToChoose = 1
      self.vision = "lowlight"
      self.languages = ["common","elvish"]
      self.languagesToChoose = 1
      self.traits = ["Keen Senses","Fey Ancestry"]
      self.traitDescriptions = [[""],[""]]
#
class Halforc(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Half-orc"
      self.abiltyAdjustment = ["str","str","con"]
      self.vision = "darkvision"
      self.languages = ["common","orcish"]
      self.traits = ["Menacing"]
      self.traitDescriptions = [[""]]
#
class Kender(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Kender"
      self.abiltyAdjustment = ["dex","cha"]
      self.speed = 25
      self.size = "small"
      self.languages = ["common","kenderspeak"]
      self.traits = ["Fearless","Taunt","Kender Pocket"]
      self.traitDescriptions = [[""],[""]]
#
class Tiefling(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Tiefling"
      self.abiltyAdjustment = ["int","cha"]
      self.vision = "lowlight"
      self.languages = ["common","infernal"]
      self.traits = ["Hellish Resistance","Infernal Wrath"]
      self.traitDescriptions = [[""],[""]]
#
class Warforged(BaseRace):
   def __init__(self,choice=""):
      BaseRace.__init__(self,choice)
      self.raceString = "Warforged"
      self.abiltyAdjustment = ["str","con"]
      self.languages = ["common"]
      self.languagesToChoose = 1
      self.traits = ["Composite Plating","Living Construct"]
      self.traitDescriptions = [[""],[""]]
#
def getClassFromString(string):
   classmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
   rtn = BaseRace()
   print "test string: " + string
   for c in classmembers:
      if str(string).lower() == str(c[0]).lower():
         rtn = c[1]()
   return rtn
