from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
import marshmallow as marshmallow

from application.classes.skill.skill import Skill
from application.classes.equipment.equipment import Weapon, Armor
from random import uniform, randint
from typing import Optional, Any


# ----------------------------------------------------------------
# unit dataclass
@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill

    class Meta:
        unknown = marshmallow.EXCLUDE


# ----------------------------------------------------------------
# abstract unit class
class BaseUnit(ABC):

    def __init__(self, name: str, unit_class: UnitClass):
        self.name: str = name
        self.unit_class: UnitClass = unit_class
        self.__hp: float = unit_class.max_health
        self.__stamina: float = unit_class.max_stamina
        self.weapon: Optional[Weapon] = None
        self.armor: Optional[Armor] = None
        self._is_skill_used: bool = False

    @property
    def hp(self) -> float:
        """
        Getter for hp attribute
        :return: hp
        """
        return round(self.__hp, 1)

    @hp.setter
    def hp(self, value: float) -> None:
        """
        Setter for hp attribute
        :param value: new value for hp attribute
        :return:
        """
        self.__hp = value

    @property
    def stamina(self) -> float:
        """
        Getter for stamina attribute
        :return: stamina
        """
        return round(self.__stamina, 1)

    @stamina.setter
    def stamina(self, value) -> None:
        """
        Setter for stamina attribute
        :param value: new value for stamina attribute
        :return:
        """
        self.__stamina = value

    def equip_weapon(self, weapon: Weapon) -> str:
        """
        Equip hero with a weapon
        :param weapon: object of class Weapon
        :return: result of method - str
        """
        self.weapon: Weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        """
        Equip hero with an armor
        :param armor: object of class Armor
        :return: result of method - str
        """
        self.armor: Armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit) -> float:
        """
        Method to count damage value and manage stamina level
        :param target: object of enemy unit
        :return: damage value
        """
        attack_damage: float = uniform(self.weapon.min_damage, self.weapon.max_damage) * self.unit_class.attack
        target_armor: float = target.armor.defence * target.unit_class.armor

        if attack_damage > target_armor:
            if target.stamina >= target.armor.stamina_per_turn:
                target.stamina -= self.armor.stamina_per_turn
                if target.stamina < 0:
                    target.stamina = 0
                damage: float = attack_damage - target_armor
            else:
                damage: float = attack_damage
            damage = round(damage, 1)
            self.stamina -= self.weapon.stamina_per_hit
            target.get_damage(damage)
        else:
            damage: float = 0
        return damage

    def get_damage(self, damage: float) -> Optional[float]:
        """
        Method to count received damage
        :param damage: damage value
        :return: None or enemy hp level after attack
        """
        if damage > 0:
            self.hp = self.hp - damage
            if self.hp < 0:
                self.hp = 0
            return self.hp
        return None

    @abstractmethod
    def hit(self, target: BaseUnit) -> Any:
        """
        Abstract method of hit action
        :param target: object of unit
        :return: Nothing
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        Method to use skill
        :param target: object of enemy unit
        :return: string result
        """
        if self._is_skill_used:
            return 'Навык использован'
        self._is_skill_used: bool = True
        return self.unit_class.skill.use(user=self, target=target)


# ----------------------------------------------------------------
# concrete units classes
class PlayerUnit(BaseUnit):
    """
    Class of hero unit
    """
    def hit(self, target: BaseUnit) -> str:
        """
        Method to hit enemy
        :param target: object of enemy unit
        :return: string result of action
        """
        if self.stamina > self.weapon.stamina_per_hit:
            damage: float = self._count_damage(target)
            if damage == 0:
                return f"{self.name} используя {self.weapon.name} наносит удар, " \
                       f"но {target.armor.name} cоперника его останавливает."
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и " \
                   f"наносит {damage} урона."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


class EnemyUnit(BaseUnit):
    """
    Class of enemy unit
    """
    def hit(self, target: BaseUnit) -> str:
        """
        Method to hit hero
        :param target: object of hero unit
        :return: string result of action
        """
        if not self._is_skill_used and self.stamina >= self.unit_class.skill.stamina and randint(0, 100) < 10:
            return self.use_skill(target)
        if self.stamina > self.weapon.stamina_per_hit:
            damage: float = self._count_damage(target)
            if damage == 0:
                return f"{self.name} используя {self.weapon.name} наносит Вам удар, " \
                       f"но Ваш {target.armor.name} его останавливает."
            return f"{self.name} используя {self.weapon.name} пробивает Ваш {target.armor.name} и " \
                   f"наносит Вам {damage} урона."
        return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
