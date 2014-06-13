import string
class NotEnoughMoneyException(Exception):
   def __str__(self):
      return ""
class Money():
   def convertToHighestValueCoins(self):
      self.convertToCopper()
      self.pp = self.cp / 1000
      self.cp = self.cp % 1000
      self.gp = self.cp / 100
      self.cp = self.cp % 100
      if self.useElectrum:
         self.ep = self.cp / 50
         self.cp = self.cp % 50
      self.sp = self.cp / 10
      self.cp = self.cp % 10
   def convertToCopper(self):
      self.cp = self.cp + self.pp*1000
      self.cp = self.cp + self.gp*100
      if self.useElectrum:
         self.cp = self.cp + self.ep*50
      self.cp = self.cp + self.sp*10
      self.pp = 0
      self.gp = 0
      self.ep = 0
      self.sp = 0
   def getTotalInCopper(self):
      return self.pp*1000 + self.gp*100 + self.ep*50 + self.sp*10 + self.cp
   def subtract(self,amount):
      if self.getTotalInCopper() >= amount:
         self.convertToCopper()
         self.cp = self.cp - amount
         self.convertToHighestValueCoins()
      else:
         raise NotEnoughMoneyException
   def __init__(self,cp=0,sp=0,ep=0,gp=0,pp=0,useEp=True):
      self.cp = cp
      self.sp = sp
      self.ep = ep
      self.gp = gp
      self.pp = pp
      self.useElectrum = useEp
class Item(): 
   def __init__(self):
      self.value = 0 #in copper
      self.weight = 0 #in pounds
      self.size = 0
      self.carried = False
      self.description = ""
   def __str__(self):
      return (string.split(str(self.__class__),".",1))[1]
class Equipable(Item):
   def __init__(self):
      Item.__init__(self)
      self.slot = ""
      self.equipped = False
   def equip():
      equipped = True
class Weapon(Equipable):
   def __init__(self):
      Equipable.__init__(self)
      self.slot = "Hand"
      self.damageDieType = 6
      self.damageDieNumber = 1
      self.damageType = "piercing"
      self.isFinesse = False
      self.isHeavy = False
      self.isLight = False
      self.specialRules = ""
      self.isThrown = False
      self.normalRange = 0
      self.maxRange = 0
      self.isTwoHanded = False
      self.isVersatile = False
      self.versatileDamageDieType = 8
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "slashing"
      self.type = "simple"
#Melee Weapons
class MeleeWeapon(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.isReach = False
      self.isMounted = False
#Simple Melee Weapons
class Club(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 10
      self.weight = 3
      self.damageDieType = 4
      self.damageType = "bludgeoning"
      self.isLight = True
class Dagger(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 200
      self.weight = 1
      self.damageDieType = 4
      self.damageType = "piercing"
      self.isFinesse = True
      self.isLight = True
      self.isThrown = True
      self.normalRange = 20
      self.maxRange = 60
class GreatClub(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 20
      self.weight = 10
      self.damageDieType = 8
      self.damageType = "bludgeoning"
      self.isTwoHanded = True
class HandAxe(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 500
      self.weight = 3
      self.damageDieType = 6
      self.damageType = "slashing"
      self.isLight = True
      self.isLight = True
      self.isThrown = True
      self.normalRange = 20
      self.maxRange = 60
class LightHammer(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 200
      self.weight = 3
      self.damageDieType = 4
      self.damageType = "bludgeoning"
      self.isLight = True
      self.isLight = True
      self.isThrown = True
      self.normalRange = 20
      self.maxRange = 60
class Mace(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 500
      self.weight = 4
      self.damageDieType = 6
      self.damageType = "bludgeoning"
class QuarterStaff(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 20
      self.weight = 4
      self.damageDieType = 6
      self.damageType = "bludgeoning"
      self.isVersatile = True
      self.versatileDamageDieType = 8
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "bludgeoning"
class Sicle(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 100
      self.weight = 2
      self.damageDieType = 4
      self.damageType = "slashing"
      self.isLight = True
class Spear(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 100
      self.weight = 4
      self.damageDieType = 6
      self.damageType = "piercing"
      self.isThrown = True
      self.normalRange = 20
      self.maxRange = 60
      self.isVersatile = True
      self.versatileDamageDieType = 8
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "piercing"
class UnarmedStrike(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 0
      self.weight = 0
      self.damageDieType = 1
      self.damageType = "bludgeoning"
#Martial Melee Weapons
class BattleAxe(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 5
      self.damageDieType = 8
      self.damageType = "slashing"
      self.isVersatile = True
      self.versatileDamageDieType = 10
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "slashing"
      self.type = "martial"
class Flail(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 6
      self.damageDieType = 8
      self.damageType = "bludgeoning"
      self.type = "martial"
class Glaive(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 9
      self.damageDieType = 10
      self.damageType = "slashing"
      self.isHeavy = True
      self.isReach = True
      self.isTwoHanded = True
      self.type = "martial"
class GreatAxe(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 3000
      self.weight = 10
      self.damageDieType = 12
      self.damageType = "slashing"
      self.isHeavy = True
      self.isTwoHanded = True
      self.type = "martial"
class GreatSword(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 5000
      self.weight = 7
      self.damageDieNumber = 2
      self.damageDieType = 6
      self.damageType = "slashing"
      self.isHeavy = True
      self.isTwoHanded = True
      self.type = "martial"
class Halberd(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 6
      self.damageDieType = 10
      self.damageType = "slashing"
      self.isHeavy = True
      self.isReach = True
      self.isTwoHanded = True
      self.type = "martial"
class Lance(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 8
      self.damageDieType = 12
      self.damageType = "piercing"
      self.isMounted = True
      self.isReach = True
      self.type = "martial"
class Longsword(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1500
      self.weight = 4
      self.damageDieType = 8
      self.damageType = "slashing"
      self.isVersatile = True
      self.versatileDamageDieType = 10
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "slashing"
      self.type = "martial"
class Maul(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 10
      self.damageDieNumber = 2
      self.damageDieType = 6
      self.damageType = "bludgeoning"
      self.isHeavy = True
      self.isTwoHanded = True
      self.type = "martial"
class Morningstar(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1500
      self.weight = 5
      self.damageDieType = 8
      self.damageType = "piercing"
      self.type = "martial"
class Pike(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 500
      self.weight = 5
      self.damageDieType = 10
      self.damageType = "piercing"
      self.isReach = True
      self.isTwoHanded = True
      self.type = "martial"
class Rapier(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 2500
      self.weight = 2
      self.damageDieType = 8
      self.damageType = "piercing"
      self.isFinesse = True
      self.type = "martial"
class Scimitar(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 2500
      self.weight = 3
      self.damageDieType = 6
      self.damageType = "slashing"
      self.isFinesse = True
      self.isLight = True
      self.type = "martial"
class ShortSword(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1000
      self.weight = 2
      self.damageDieType = 6
      self.damageType = "piercing"
      self.isFinesse = True
      self.isLight = True
      self.type = "martial"
class Trident(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 500
      self.weight = 5
      self.damageDieType = 6
      self.damageType = "piercing"
      self.isThrown = True
      self.normalRange = 20
      self.maxRange = 60
      self.isVersatile = True
      self.versatileDamageDieType = 8
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "piercing"
      self.type = "martial"
class WarPick(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 500
      self.weight = 4
      self.damageDieType = 6
      self.damageType = "piercing"
      self.type = "martial"
class Warhammer(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 1500
      self.weight = 4
      self.damageDieType = 8
      self.damageType = "bludgeoning"
      self.isVersatile = True
      self.versatileDamageDieType = 10
      self.versatileDamageDieNumber = 1
      self.versatileDamageType = "bludgeoning"
      self.type = "martial"
class Whip(MeleeWeapon):
   def __init__(self):
      MeleeWeapon.__init__(self)
      self.value = 200
      self.weight = 4
      self.damageDieType = 8
      self.damageType = "bludgeoning"
      self.isReach = True
      self.specialRules = "Use DEX mod for attack, no mod for damage"
      self.type = "martial"
#Ranged Weapons
class RangedWeapon(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.needsAmmunition = True
      self.isLoading = False
      self.damageType = "slashing"
#Simple Ranged Weapons
class LightCrossbow(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 2500
      self.weight = 6
      self.damageDieType = 8
      self.normalRange = 80
      self.maxRange = 320
      self.isTwoHanded = True
      self.isLoading = True
class Dart(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 5
      self.weight = 1
      self.damageDieType = 4
      self.needsAmmunition = False
      self.isThrown = True
      self.normalRange = 30
      self.maxRange = 120
      self.isFinesse = True
class Javelin(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 50
      self.weight = 4
      self.damageDieType = 6
      self.needsAmmunition = False
      self.isThrown = True
      self.normalRange = 30
      self.maxRange = 120
class Shortbow(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 2500
      self.weight = 2
      self.damageDieType = 6
      self.normalRange = 80
      self.maxRange = 320
      self.isTwoHanded = True
class Sling(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 10
      self.weight = 0.5
      self.damageDieType = 4
      self.damageType = "bludgeoning"
      self.normalRange = 30
      self.maxRange = 120
#Martial Ranged Weapons
class Blowgun(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 1000
      self.weight = 2
      self.damageDieType = 1
      self.normalRange = 25
      self.maxRange = 100
      self.isLoading = True
      self.special = "???"
class Bolas(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 200
      self.weight = 1
      self.damageDieType = 1
      self.damageType = "bludgeoning"
      self.needsAmmunition = False
      self.isThrown = True
      self.normalRange = 30
      self.maxRange = 90
      self.special = "Large or smaller creature is restrained (DEX save DC 10 prevents, STR save DC 10 or 5 damage frees)"
class HandCrossbow(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 7500
      self.weight = 3
      self.damageDieType = 6
      self.normalRange = 30
      self.maxRange = 120
      self.isLoading = True
      self.isLight = True
class HeavyCrossbow(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 5000
      self.weight = 19
      self.damageDieType = 10
      self.normalRange = 100
      self.maxRange = 400
      self.isLoading = True
      self.isHeavy = True
      self.isTwoHanded = True
class Longbow(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 5000
      self.weight = 2
      self.damageDieType = 8
      self.normalRange = 150
      self.maxRange = 600
      self.isHeavy = True
      self.isTwoHanded = True
class Net(RangedWeapon):
   def __init__(self):
      RangedWeapon.__init__(self)
      self.value = 100
      self.weight = 3
      self.damageDieType = 0
      self.needsAmmunition = False
      self.isThrown = True
      self.normalRange = 20
      self.maxRange = 60
      self.special = "Target point, Large or smaller creature is restrained (DEX save DC 10 evades, STR save DC 10 or 5 damage frees)"

#Armor
class Armor(Equipable):
   def __init__(self):
      Equipable.__init__(self)
      self.slot = "Torso"
      self.maxDexBonus = 4
      self.ac = 0
      self.type = "light"
      self.speedDecrement = 0
      self.isStealthAtDisadvantage = False
class PaddedArmor(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 500
      self.weight = 5
      self.ac = 11
      self.isStealthAtDisadvantage = True
class LeatherArmor(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 1000
      self.weight = 8
      self.ac = 11
class DragonLeather(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 50000
      self.weight = 15
      self.ac = 12
class MithralShirt(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 500000
      self.weight = 10
      self.ac = 13
#Medium Armor
class HideArmor(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 1000
      self.weight = 10
      self.ac = 12
      self.maxDexBonus = 2
      self.type = "medium"
class StuddedLeather(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 2500
      self.weight = 13
      self.ac = 13
      self.maxDexBonus = 2
      self.type = "medium"
class ScaleMail(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 5000
      self.weight = 45
      self.ac = 14
      self.maxDexBonus = 2
      self.isStealthAtDisadvantage = True
      self.type = "medium"
class StuddedDragonLeather(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 50000
      self.weight = 20
      self.ac = 14
      self.maxDexBonus = 2
      self.type = "medium"
class DragonScale(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 50000
      self.weight = 50
      self.ac = 15
      self.maxDexBonus = 2
      self.isStealthAtDisadvantage = True
      self.type = "medium"
class MithrilScale(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 500000
      self.weight = 25
      self.ac = 15
      self.maxDexBonus = 2
      self.isStealthAtDisadvantage = True
      self.type = "medium"
# Heavy Armor
class RingMail(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 3000
      self.weight = 22
      self.ac = 14
      self.maxDexBonus = 0
      self.speedDecrement = 5
      self.isStealthAtDisadvantage = True
      self.type = "heavy"
class ChainMail(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 7500
      self.weight = 55
      self.ac = 16
      self.maxDexBonus = 0
      self.speedDecrement = 5
      self.isStealthAtDisadvantage = True
      self.type = "heavy"
class Splint(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 50000
      self.weight = 50
      self.ac = 17
      self.maxDexBonus = 0
      self.speedDecrement = 5
      self.isStealthAtDisadvantage = True
      self.type = "heavy"
class Banded(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 75000
      self.weight = 55
      self.ac = 17
      self.maxDexBonus = 0
      self.isStealthAtDisadvantage = True
      self.type = "heavy"
class Plate(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 500000
      self.weight = 65
      self.ac = 18
      self.maxDexBonus = 0
      self.speedDecrement = 5
      self.isStealthAtDisadvantage = True
      self.type = "heavy"
class MithrilPlate(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.value = 600000
      self.weight = 40
      self.ac = 18
      self.maxDexBonus = 0
      self.isStealthAtDisadvantage = True
      self.type = "heavy"
#Shields
class Buckler(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.slot = "Hand"
      self.value = 500
      self.weight = 4
      self.ac = 1
      self.maxDexBonus = 4
      self.type = "shield"
class Shield(Armor):
   def __init__(self):
      Armor.__init__(self)
      self.slot = "Hand"
      self.value = 1000
      self.weight = 8
      self.ac = 2
      self.maxDexBonus = 4
      self.type = "shield"

#Tool
class Tool(Item):
   def __init__(self):
      Item.__init__(self)
class ArtisansTools(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 500
      self.weight = 5
class ClimbersKit(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 2500
      self.weight = 5
class DisguiseKit(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 2500
      self.weight = 8
class GamingSet(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 100
      self.weight = 0.5
class HealersKit(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 500
      self.weight = 1
class MusicalInstrument(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 500
      self.weight = 3
class NavigatorsTools(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 2500
      self.weight = 2
class PoisonersKit(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 5000
      self.weight = 2
class TheivesTools(Tool):
   def __init__(self):
      Tool.__init__(self)
      self.value = 2500
      self.weight = 1

#Item
class Abacus(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 200
      self.weight = 2
class AcidVial(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2500
      self.weight = 1
class AdventurersKit(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 900
      self.weight = 39
class AlchemistsFireFlask(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50000
      self.weight = 1
class Ammunition(Item):
   def __init__(self):
      Item.__init__(self)
      self.amount = 1
class Arrow(Ammunition):
   def __init__(self):
      Ammunition.__init__(self)
      self.value = 5
      self.weight = 0.15
class Bolts20(Ammunition):
   def __init__(self):
      Ammunition.__init__(self)
      self.value = 5
      self.weight = 0.15
class Bullets20(Ammunition):
   def __init__(self):
      Ammunition.__init__(self)
      self.value = 0.2
      self.weight = 0.1
class Needles20(Ammunition):
   def __init__(self):
      Ammunition.__init__(self)
      self.value = 5
      self.weight = 0.05
class AntitoxinVial(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50000
      self.weight = 0
class Backpack(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 200
      self.weight = 2
class BallBearing(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1
      self.weight = 0.01
class Bedroll(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 5
class Bell(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 0
class Blanket(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 3
class BlockAndTackle(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 5
class Bucket(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 5
      self.weight = 2
class Caltrops(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 2
class Candle(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1
      self.weight = 0.1
class ScrollCase(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 1
class Chain(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 5
class Chalk(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1
      self.weight = 0
class CommonClothes(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 3
class CostumeClothes(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 4
class FineClothes(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1500
      self.weight = 6
class TravelersClothes(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 200
      self.weight = 4
class ComponentPouch(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2500
      self.weight = 2
class Crowbar(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 20
      self.weight = 5
class FishingTackle(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 4
class Flask(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2
      self.weight = 0
class GrapplingHook(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 200
      self.weight = 4
class Hammer(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 20
      self.weight = 2
class Sledgehammer(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 10
class HolySymbol(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 0
class HolyWaterFlask(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2500
      self.weight = 1
class Horse(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 7500
      self.weight = 0
class Hourglass(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 1
class HuntingTrap(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 15
class Ink(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 0
class InkPen(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2
      self.weight = 0
class Jug(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2
      self.weight = 9
class Ladder(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10
      self.weight = 20
class Lantern(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 1
class BullseyeLantern(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 3
class Lock(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 1
class MagnifyingGlass(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10000
      self.weight = 0
class Manacles(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 200
      self.weight = 2
class MessKit(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10
      self.weight = 1
class SteelMirror(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 0.5
class Oil(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10
      self.weight = 1
class Orb(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 2
class Paper(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 20
      self.weight = 0
class Parchment(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10
      self.weight = 0
class MinersPick(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 10
class Piton(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 5
      self.weight = 0.5
class BasicPoisonVial(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10000
      self.weight = 0
class Pole(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 5
      self.weight = 8
class IronPot(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10
      self.weight = 10
class PotionOfHealing(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50000
      self.weight = 1
class Pouch(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 1
class PortableRam(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 20
class DayRation(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 10
      self.weight = 1
class Robes(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 4
class Rod(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 2
class HempenRope(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 10
class SilkRope(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 5
class Sack(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1
      self.weight = 0.5
class MerchantScale(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 5
      self.weight = 3
class SealingWax(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 1
class Shovel(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 8
class SignalWhistle(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 5
      self.weight = 0
class SignetRing(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 500
      self.weight = 0
class Soap(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2
      self.weight = 1
class Spellbook(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 7500
      self.weight = 3
class IronSpike(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 0.2
      self.weight = 0.5
class Spyglass(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100000
      self.weight = 1
class Staff(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 4
class Tent(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 200
      self.weight = 20
class Tinderbox(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 50
      self.weight = 1
class Tome(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 2500
      self.weight = 5
class Torch(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1
      self.weight = 1
class Vial(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 100
      self.weight = 0
class Wand(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1000
      self.weight = 0.5
class Waterskin(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 20
      self.weight = 4
class Whetstone(Item):
   def __init__(self):
      Item.__init__(self)
      self.value = 1
      self.weight = 1