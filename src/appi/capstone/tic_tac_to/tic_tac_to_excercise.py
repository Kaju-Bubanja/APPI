import random


class Board:
    def __init__(self):
        self.tiles = {0: None, 1: None, 2: None,
                      3: None, 4: None, 5: None,
                      6: None, 7: None, 8: None}

    def update_board(self, choice, player_symbol):
        pass

    # Check if a player has won
    def has_won(self, player_symbol):
        pass

    def board_is_full(self):
        pass

    def show(self):
        print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n".format(self.tiles[0], self.tiles[1], self.tiles[2],
                                                                  self.tiles[3], self.tiles[4], self.tiles[5],
                                                                  self.tiles[6], self.tiles[7], self.tiles[8]))


class Player:
    # give the player a constructor which takes the player_symbol and name as arguments

    def get_move(self):
        raise NotImplementedError


class Human(Player):
    # create a constructor which initializes the the player symbol and it's name

    def get_move(self):
        pass


class Computer(Player):
    # create a constructor which initializes the the player symbol and it's name

    def get_move(self):
        pass


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    # check if the game is over
    def game_over(self):
        pass

    # check if the move is legal if not ask for another move
    def make_move(self, player):
        pass

    # Let players make moves until the game is over. Output at the end who won
    def play(self):
        pass


def main():
    human = Human()
    computer = Computer()
    game = Game(human, computer)
    game.play()


if __name__ == '__main__':
    main()
