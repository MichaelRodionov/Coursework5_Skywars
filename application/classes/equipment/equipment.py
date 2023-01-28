import json
from dataclasses import dataclass

import marshmallow
import marshmallow_dataclass

from random import uniform
from typing import List

from config import Config


# ----------------------------------------------------------------
# dataclasses
@dataclass
class Weapon:
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    class Meta:
        unknown = marshmallow.EXCLUDE

    @property
    def damage(self) -> float:
        return uniform(self.min_damage, self.max_damage)


@dataclass
class Armor:
    name: str
    defence: float
    stamina_per_turn: float

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


# ----------------------------------------------------------------
# concrete class Equipment
class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name: str) -> Weapon:
        """
        Method to get Weapon object by weapon's name
        :param weapon_name: str name of weapon
        :return: Weapon object
        """
        return next(filter(lambda weapon: weapon.name == weapon_name, self.equipment.weapons))

    def get_armor(self, armor_name: str) -> Armor:
        """
        Method to get Armor object by armor's name
        :param armor_name: str name of armor
        :return: Armor object
        """
        return next(filter(lambda armor: armor.name == armor_name, self.equipment.armors))

    def get_weapons_names(self) -> list[Weapon]:
        """
        Method to get list of Weapon's objects
        :return: list[Weapon]
        """
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> list[Armor]:
        """
        Method to get list of Armor's objects
        :return: list[Armor]
        """
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        Method to convert equipment json data to objects
        :return: EquipmentData object
        """
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        with open(Config.equipment_path, encoding='utf-8') as f:
            data = json.load(f)
        return equipment_schema().load(data)
