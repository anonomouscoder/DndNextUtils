class BaseBackground:
   backgroudString = "BaseBackground"
   skills = []
   toolProficiencies = []
   toolsToChoose = 0
   traits = [""]
   additionalLanguages = 0
#
class Artisan(BaseBackground):
   backgroudString = "Artisan"
   traits = ["Guild Membership"]
   skills = ["insight","persuasion","search"]
   toolsToChoose = 2
   additionalLanguages = 1
#
class BountyHunter(BaseBackground):
   backgroudString = "BountyHunter"
   traits = ["Bounty Board"]
   skills = ["perception","search","stealth"]
   toolProficiencies = ["landMount"]
   additionalLanguages = 2
#
class Charlatan(BaseBackground):
   backgroudString = "Charlatan"
   traits = ["False Identity"]
   skills = ["deception","insight","sleight of hand"]
   toolProficiencies = ["kitDisguise","gaming set"]
   additionalLanguages = 1
#
class Commoner(BaseBackground):
   backgroudString = "Commoner"
   traits = ["Salt of the Earth"]
   skills = ["animal handling","athletics","survival"]
   toolProficiencies = ["Artisan's tools","gaming set","landMount"]
#
class Guide(BaseBackground):
   backgroudString = "Guide"
   traits = ["Wanderer"]
   skills = ["athletics","nature","survival"]
   toolProficiencies = ["kitClimbing","landMount","navigator's tools"]
#
class GuildThief(BaseBackground):
   backgroudString = "GuildThief"
   traits = ["Thieves' Cant"]
   skills = ["deception","sleight of hand","stealth"]
   toolProficiencies = ["kitDisguise","thieves' tools","poisoner's kit"]
#
class Jester(BaseBackground):
   backgroudString = "Jester"
   traits = ["Licensed Fool"]
   skills = ["acrobatics","performance","sleight of hand"]
   toolProficiencies = ["gaming set","musical instrument"]
#
class Minstrel(BaseBackground):
   backgroudString = "Minstrel"
   traits = ["Noted Performer"]
   skills = ["history","performance","persuasion"]
   toolProficiencies = ["kitDisguise","musical instrument"]
   additionalLanguages = 1
#
class Noble(BaseBackground):
   backgroudString = "Noble"
   traits = ["Retainers"]
   skills = ["history","insight","persuasion"]
   toolProficiencies = ["gaming set","landMount"]
   additionalLanguages = 1
#
class Priest(BaseBackground):
   backgroudString = "Priest"
   traits = ["Temple Services"]
   skills = ["history","insight","religion"]
   toolProficiencies = ["kitHealer"]
   additionalLanguages = 2
#
class Sage(BaseBackground):
   backgroudString = "Sage"
   traits = ["Researcher"]
   skills = ["arcana","history","search"]
   additionalLanguages = 3
#
class Soldier(BaseBackground):
   backgroudString = "Soldier"
   traits = ["Military Rank"]
   skills = ["athletics","intimidation","survival"]
   toolProficiencies = ["gaming set","landMount","landVehicle"]
#
class Spy(BaseBackground):
   backgroudString = "Spy"
   traits = ["Contact"]
   skills = ["deception","search","stealth"]
   toolProficiencies = ["kitDisguise","thieves' tools"]
   additionalLanguages = 1
#
class Thug(BaseBackground):
   backgroudString = "Thug"
   traits = ["Bad Reputation"]
   skills = ["athletics","deception","intimidation"]
   toolProficiencies = ["gaming set","landMount"]
   additionalLanguages = 1
#