from abc import ABCMeta, abstractmethod


class Player:
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_move(self):
        pass

    def get_num_pieces(self):
        pass
