class Item(): 
   value = 0 #in copper
   weight = 0 #in pounds
   size = 0
   carried = False
class Equipable(Item):
   slot = ""
   equipped = False
   def equip():
      equipped = True
class Weapon(Equipable):
   slot = "Hand"
   damageDieType = 6
   damageDieNumber = 1
   damageType = "piercing"
   isFinesse = False
   isHeavy = False
   isLight = False
   specialRules = ""
   isThrown = False
   normalRange = 0
   maxRange = 0
   isTwoHanded = False
   isVersatile = False
   versatileDamageDieType = 8
   versatileDamageDieNumber = 1
   versatileDamageType = "slashing"
   type = "simple"
#Melee Weapons
class MeleeWeapon(Weapon):
   isReach = False
   isMounted = False
#Simple Melee Weapons
class Club(MeleeWeapon):
   value = 10
   weight = 3
   damageDieType = 4
   damageType = "bludgeoning"
   isLight = True
class Dagger(MeleeWeapon):
   value = 200
   weight = 1
   damageDieType = 4
   damageType = "piercing"
   isFinesse = True
   isLight = True
   isThrown = True
   normalRange = 20
   maxRange = 60
class GreatClub(MeleeWeapon):
   value = 20
   weight = 10
   damageDieType = 8
   damageType = "bludgeoning"
   isTwoHanded = True
class HandAxe(MeleeWeapon):
   value = 500
   weight = 3
   damageDieType = 6
   damageType = "slashing"
   isLight = True
   isLight = True
   isThrown = True
   normalRange = 20
   maxRange = 60
class LightHammer(MeleeWeapon):
   value = 200
   weight = 3
   damageDieType = 4
   damageType = "bludgeoning"
   isLight = True
   isLight = True
   isThrown = True
   normalRange = 20
   maxRange = 60
class Mace(MeleeWeapon):
   value = 500
   weight = 4
   damageDieType = 6
   damageType = "bludgeoning"
class QuarterStaff(MeleeWeapon):
   value = 20
   weight = 4
   damageDieType = 6
   damageType = "bludgeoning"
   isVersatile = True
   versatileDamageDieType = 8
   versatileDamageDieNumber = 1
   versatileDamageType = "bludgeoning"
class Sicle(MeleeWeapon):
   value = 100
   weight = 2
   damageDieType = 4
   damageType = "slashing"
   isLight = True
class Spear(MeleeWeapon):
   value = 100
   weight = 4
   damageDieType = 6
   damageType = "piercing"
   isThrown = True
   normalRange = 20
   maxRange = 60
   isVersatile = True
   versatileDamageDieType = 8
   versatileDamageDieNumber = 1
   versatileDamageType = "piercing"
class UnarmedStrike(MeleeWeapon):
   value = 0
   weight = 0
   damageDieType = 1
   damageType = "bludgeoning"
#Martial Melee Weapons
class BattleAxe(MeleeWeapon):
   value = 1000
   weight = 5
   damageDieType = 8
   damageType = "slashing"
   isVersatile = True
   versatileDamageDieType = 10
   versatileDamageDieNumber = 1
   versatileDamageType = "slashing"
   type = "martial"
class Flail(MeleeWeapon):
   value = 1000
   weight = 6
   damageDieType = 8
   damageType = "bludgeoning"
   type = "martial"
class Glaive(MeleeWeapon):
   value = 1000
   weight = 9
   damageDieType = 10
   damageType = "slashing"
   isHeavy = True
   isReach = True
   isTwoHanded = True
   type = "martial"
class GreatAxe(MeleeWeapon):
   value = 3000
   weight = 10
   damageDieType = 12
   damageType = "slashing"
   isHeavy = True
   isTwoHanded = True
   type = "martial"
class GreatSword(MeleeWeapon):
   value = 5000
   weight = 7
   damageDieNumber = 2
   damageDieType = 6
   damageType = "slashing"
   isHeavy = True
   isTwoHanded = True
   type = "martial"
class Halberd(MeleeWeapon):
   value = 1000
   weight = 6
   damageDieType = 10
   damageType = "slashing"
   isHeavy = True
   isReach = True
   isTwoHanded = True
   type = "martial"
class Lance(MeleeWeapon):
   value = 1000
   weight = 8
   damageDieType = 12
   damageType = "piercing"
   isMounted = True
   isReach = True
   type = "martial"
class Longsword(MeleeWeapon):
   value = 1500
   weight = 4
   damageDieType = 8
   damageType = "slashing"
   isVersatile = True
   versatileDamageDieType = 10
   versatileDamageDieNumber = 1
   versatileDamageType = "slashing"
   type = "martial"
class Maul(MeleeWeapon):
   value = 1000
   weight = 10
   damageDieNumber = 2
   damageDieType = 6
   damageType = "bludgeoning"
   isHeavy = True
   isTwoHanded = True
   type = "martial"
class Morningstar(MeleeWeapon):
   value = 1500
   weight = 5
   damageDieType = 8
   damageType = "piercing"
   type = "martial"
class Pike(MeleeWeapon):
   value = 500
   weight = 5
   damageDieType = 10
   damageType = "piercing"
   isReach = True
   isTwoHanded = True
   type = "martial"
class Rapier(MeleeWeapon):
   value = 2500
   weight = 2
   damageDieType = 8
   damageType = "piercing"
   isFinesse = True
   type = "martial"
class Scimitar(MeleeWeapon):
   value = 2500
   weight = 3
   damageDieType = 6
   damageType = "slashing"
   isFinesse = True
   isLight = True
   type = "martial"
class ShortSword(MeleeWeapon):
   value = 1000
   weight = 2
   damageDieType = 6
   damageType = "piercing"
   isFinesse = True
   isLight = True
   type = "martial"
class Trident(MeleeWeapon):
   value = 500
   weight = 5
   damageDieType = 6
   damageType = "piercing"
   isThrown = True
   normalRange = 20
   maxRange = 60
   isVersatile = True
   versatileDamageDieType = 8
   versatileDamageDieNumber = 1
   versatileDamageType = "piercing"
   type = "martial"
class WarPick(MeleeWeapon):
   value = 500
   weight = 4
   damageDieType = 6
   damageType = "piercing"
   type = "martial"
class Warhammer(MeleeWeapon):
   value = 1500
   weight = 4
   damageDieType = 8
   damageType = "bludgeoning"
   isVersatile = True
   versatileDamageDieType = 10
   versatileDamageDieNumber = 1
   versatileDamageType = "bludgeoning"
   type = "martial"
class Whip(MeleeWeapon):
   value = 200
   weight = 4
   damageDieType = 8
   damageType = "bludgeoning"
   isReach = True
   specialRules = "Use DEX mod for attack, no mod for damage"
   type = "martial"
#Ranged Weapons
class RangedWeapon(Weapon):
   needsAmmunition = True
   isLoading = False
   damageType = "slashing"
#Simple Ranged Weapons
class LightCrossbow(RangedWeapon):
   value = 2500
   weight = 6
   damageDieType = 8
   normalRange = 80
   maxRange = 320
   isTwoHanded = True
   isLoading = True
class Dart(RangedWeapon):
   value = 5
   weight = 1
   damageDieType = 4
   needsAmmunition = False
   isThrown = True
   normalRange = 30
   maxRange = 120
   isFinesse = True
class Javelin(RangedWeapon):
   value = 50
   weight = 4
   damageDieType = 6
   needsAmmunition = False
   isThrown = True
   normalRange = 30
   maxRange = 120
class Shortbow(RangedWeapon):
   value = 2500
   weight = 2
   damageDieType = 6
   normalRange = 80
   maxRange = 320
   isTwoHanded = True
class Sling(RangedWeapon):
   value = 10
   weight = 0.5
   damageDieType = 4
   damageType = "bludgeoning"
   normalRange = 30
   maxRange = 120
#Martial Ranged Weapons
class Blowgun(RangedWeapon):
   value = 1000
   weight = 2
   damageDieType = 1
   normalRange = 25
   maxRange = 100
   isLoading = True
   special = "???"
class Bolas(RangedWeapon):
   value = 200
   weight = 1
   damageDieType = 1
   damageType = "bludgeoning"
   needsAmmunition = False
   isThrown = True
   normalRange = 30
   maxRange = 90
   special = "Large or smaller creature is restrained (DEX save DC 10 prevents, STR save DC 10 or 5 damage frees)"
class HandCrossbow(RangedWeapon):
   value = 7500
   weight = 3
   damageDieType = 6
   normalRange = 30
   maxRange = 120
   isLoading = True
   isLight = True
class HeavyCrossbow(RangedWeapon):
   value = 5000
   weight = 19
   damageDieType = 10
   normalRange = 100
   maxRange = 400
   isLoading = True
   isHeavy = True
   isTwoHanded = True
class Longbow(RangedWeapon):
   value = 5000
   weight = 2
   damageDieType = 8
   normalRange = 150
   maxRange = 600
   isHeavy = True
   isTwoHanded = True
class Net(RangedWeapon):
   value = 100
   weight = 3
   damageDieType = 0
   needsAmmunition = False
   isThrown = True
   normalRange = 20
   maxRange = 60
   special = "Target point, Large or smaller creature is restrained (DEX save DC 10 evades, STR save DC 10 or 5 damage frees)"

#Armor
class Armor(Equipable):
   slot = "Torso"
   maxDexBonus = 4
   AC = 0
   type = "light"
   speedDecrement = 0
   isStealthAtDisadvantage = False
class PaddedArmor(Armor):
   value = 500
   weight = 5
   AC = 11
   isStealthAtDisadvantage = True
class LeatherArmor(Armor):
   value = 1000
   weight = 8
   AC = 11
class DragonLeather(Armor):
   value = 50000
   weight = 15
   AC = 12
class MithralShirt(Armor):
   value = 500000
   weight = 10
   AC = 13
#Medium Armor
class HideArmor(Armor):
   value = 1000
   weight = 10
   AC = 12
   maxDexBonus = 2
   type = "medium"
class StuddedLeather(Armor):
   value = 2500
   weight = 13
   AC = 13
   maxDexBonus = 2
   type = "medium"
class ScaleMail(Armor):
   value = 5000
   weight = 45
   AC = 14
   maxDexBonus = 2
   isStealthAtDisadvantage = True
   type = "medium"
class StuddedDragonLeather(Armor):
   value = 50000
   weight = 20
   AC = 14
   maxDexBonus = 2
   type = "medium"
class DragonScale(Armor):
   value = 50000
   weight = 50
   AC = 15
   maxDexBonus = 2
   isStealthAtDisadvantage = True
   type = "medium"
class MithrilScale(Armor):
   value = 500000
   weight = 25
   AC = 15
   maxDexBonus = 2
   isStealthAtDisadvantage = True
   type = "medium"
# Heavy Armor
class RingMail(Armor):
   value = 3000
   weight = 22
   AC = 14
   maxDexBonus = 0
   speedDecrement = 5
   isStealthAtDisadvantage = True
   type = "heavy"
class ChainMail(Armor):
   value = 7500
   weight = 55
   AC = 16
   maxDexBonus = 0
   speedDecrement = 5
   isStealthAtDisadvantage = True
   type = "heavy"
class Splint(Armor):
   value = 50000
   weight = 50
   AC = 17
   maxDexBonus = 0
   speedDecrement = 5
   isStealthAtDisadvantage = True
   type = "heavy"
class Banded(Armor):
   value = 75000
   weight = 55
   AC = 17
   maxDexBonus = 0
   isStealthAtDisadvantage = True
   type = "heavy"
class Plate(Armor):
   value = 500000
   weight = 65
   AC = 18
   maxDexBonus = 0
   speedDecrement = 5
   isStealthAtDisadvantage = True
   type = "heavy"
class MithrilPlate(Armor):
   value = 600000
   weight = 40
   AC = 18
   maxDexBonus = 0
   isStealthAtDisadvantage = True
   type = "heavy"
#Shields
class Buckler(Armor):
   slot = "Hand"
   value = 500
   weight = 4
   AC = 1
   maxDexBonus = 4
   type = "shield"
class Shield(Armor):
   slot = "Hand"
   value = 1000
   weight = 8
   AC = 2
   maxDexBonus = 4
   type = "shield"