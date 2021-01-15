import math
import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        # Your character's initial hitpoints are 10 + your character's constitution modifier.
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        return self._throw_x_times_keep_best_y(4, 3)

    def _throw_x_times_keep_best_y(self, times: int, keep: int) -> int:
        return sum(sorted([self._throw_dice() for x in range(times)])[1:keep + 1])

    def _throw_dice(self, faces=6):
        return random.randint(1, faces)


def modifier(constitution: int):
    """Calculates your characters modifier.

    You find your character's constitution modifier by
    - subtracting 10 from your character's constitution
    - divide by 2
    - and round down.
    """
    return math.floor((constitution - 10) / 2)
