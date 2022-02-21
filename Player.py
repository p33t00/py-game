from Participant import Participant


class Player(Participant):
    __name = ''

    def change_name(self, name):
        self.__name = name
