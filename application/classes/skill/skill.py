from abc import ABC, abstractmethod

from application.classes.unit.unit import BaseUnit


# ----------------------------------------------------------------
# abstract class Skill
class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Abstract getter of name
        :return: string of skill's name
        """
        return self.name

    @property
    @abstractmethod
    def stamina(self) -> float:
        """
        Abstract getter of stamina
        :return: float skill's stamina value
        """
        return self.stamina

    @property
    @abstractmethod
    def damage(self) -> float:
        """
        Abstract getter of damage
        :return: float skill's damage value
        """
        return self.damage

    @abstractmethod
    def skill_effect(self):
        """
        Abstract method for skill effect
        :return: Nothing
        """
        pass

    def _is_stamina_enough(self) -> bool:
        """
        Method to count if unit's stamina is enough to use his skill
        :return: bool value
        """
        return self.user.stamina > self.stamina

    def use(self, user, target) -> str:
        """
        Method to use user's skill on enemy
        :param user: hero unit
        :param target: enemy unit
        :return:
        """
        self.user: BaseUnit = user
        self.target: BaseUnit = target

        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


# ----------------------------------------------------------------
# concrete skills classes
class FuryPunch(Skill):
    """
    Class of concrete skill
    """
    name = 'Свирепый пинок'
    stamina = 6.0
    damage = 12.0

    def skill_effect(self) -> str:
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона."


class HardShot(Skill):
    """
    Class of concrete skill
    """
    name = 'Мощный укол'
    stamina = 5.0
    damage = 15.0

    def skill_effect(self) -> str:
        """
        Method of skill effect
        :return: string result of using skill
        """
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона."


class HiddenBlade(Skill):
    """
    Class of concrete skill
    """
    name = 'Скрытый клинок'
    stamina = 6.0
    damage = 20.0

    def skill_effect(self) -> str:
        """
        Method of skill effect
        :return: string result of using skill
        """
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона."


class OrcFury(Skill):
    """
    Class of concrete skill
    """
    name = 'Яростный орк'
    stamina = 10.0
    damage = 35.0

    def skill_effect(self) -> str:
        """
        Method of skill effect
        :return: string result of using skill
        """
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона."
