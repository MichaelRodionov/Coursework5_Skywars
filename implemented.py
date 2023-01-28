from application.classes.arena.arena import Arena
from application.classes.equipment.equipment import Equipment
from application.classes.skill.skill import FuryPunch, HardShot, HiddenBlade, OrcFury
from application.classes.unit.unit import UnitClass


# ----------------------------------------------------------------
# create instances
arena: Arena = Arena()
equipment: Equipment = Equipment()

WarriorClass: UnitClass = UnitClass(
    name='Воин',
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

AssassinClass: UnitClass = UnitClass(
    name='Ассасин',
    max_health=60.0,
    max_stamina=25.0,
    attack=1,
    stamina=0.8,
    armor=1.0,
    skill=HiddenBlade()
)

OrkClass: UnitClass = UnitClass(
    name='Орк',
    max_health=70.0,
    max_stamina=15.0,
    attack=2,
    stamina=1,
    armor=0.5,
    skill=OrcFury()
)

ThiefClass: UnitClass = UnitClass(
    name='Вор',
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot())

# ----------------------------------------------------------------
unit_classes: dict = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass,
    AssassinClass.name: AssassinClass,
    OrkClass.name: OrkClass
}
