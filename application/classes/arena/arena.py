from typing import Optional, Any

from application.classes.unit.unit import BaseUnit


# ----------------------------------------------------------------
# base class Arena
class BaseArena(type):
    """
    Base arena class done with Singleton pattern
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# ----------------------------------------------------------------
# concrete class Arena
class Arena(metaclass=BaseArena):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = ''

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        """
        Method to start fight
        :param player: hero unit
        :param enemy: enemy unit
        :return: None
        """
        self.player: BaseUnit = player
        self.enemy: BaseUnit = enemy
        self.game_is_running: bool = True

    def _check_players_hp(self) -> Optional[str]:
        """
        Method to check unit's hp
        :return: None or string result of game
        """
        if self.player.hp > 0 and self.enemy.hp > 0:
            return None

        if self.player.hp > 0 and self.enemy.hp <= 0:
            self.battle_result = 'Игрок выиграл битву'

        elif self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = 'Ничья!'

        elif self.player.hp <= 0 and self.enemy.hp > 0:
            self.battle_result = 'Противник выиграл битву'
        return self._end_game()

    def _stamina_regeneration(self) -> None:
        """
        Method to count unit's stamina regeneration
        :return: None
        """
        units: tuple[BaseUnit, BaseUnit] = (self.player, self.enemy)
        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina
            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def next_turn(self) -> str:
        """
        Method to make next turn of game
        :return:
        """
        result: Optional[str] = self._check_players_hp()
        if result is not None:
            return result
        if self.game_is_running:
            self._stamina_regeneration()
            return self.enemy.hit(self.player)

    def _end_game(self) -> str:
        """
        Method to finish the game
        :return: string result
        """
        self._instances: dict = {}
        self.game_is_running: bool = False
        return self.battle_result

    def player_hit(self) -> str:
        """
        Method to hit a unit
        :return: string result
        """
        result: Optional[str] = self._check_players_hp()
        if not result:
            result: Any = self.player.hit(self.enemy)
            next_turn: str = self.next_turn()
            return f'{result}\n{next_turn}'
        return result

    def player_use_skill(self) -> str:
        """
        Method to use unit's skill
        :return: string result
        """
        result = self._check_players_hp()
        if not result:
            result: str = self.player.use_skill(self.enemy)
            next_turn: str = self.next_turn()
            return f'{result}\n{next_turn}'
        return result
