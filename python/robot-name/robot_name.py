import random
import string


class Robot:
    """
    Assumes a rather lower amount of robots used.
    For a higher amount of robots, a pre-generating approach would be more useful.
    It is a memory/cpu trade-off
    """
    usedNames = []

    def __init__(self):
        self.__name_set()

    def __del__(self):
        """
        free name when robot is not used anymore
        """
        Robot.usedNames.remove(self.name)

    def reset(self):
        """
        Reset name and give old name free for new usage
        (first free and then rename would have a small chance of giving the same name again,
        this would fail the test)
        """
        name_old = self.name
        self.__name_set()
        Robot.usedNames.remove(name_old)

    def __name_set(self):
        if len(Robot.usedNames) >= 67600:  # 2 times 26 letters and 3 times 10 digits
            raise Exception("Robot name space exhausted!")
        while True:
            proposal = Robot.__name_generate()
            if proposal not in self.usedNames:
                Robot.usedNames.append(proposal)
                self.name = proposal
                break

    @staticmethod
    def __name_generate():
        return random.choice(string.ascii_uppercase) + \
               random.choice(string.ascii_uppercase) + \
               random.choice(string.digits) + \
               random.choice(string.digits) + \
               random.choice(string.digits)
