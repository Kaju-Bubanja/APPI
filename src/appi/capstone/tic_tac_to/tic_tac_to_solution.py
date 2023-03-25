import random


class Board:
    def __init__(self):
        self.tiles = {0: None, 1: None, 2: None,
                      3: None, 4: None, 5: None,
                      6: None, 7: None, 8: None}

    def update_board(self, choice, player_symbol):
        if not self.tiles[choice]:
            self.tiles[choice] = player_symbol
            return True
        return False

    # Check if a player has won
    def has_won(self, player_symbol):
        tiles = self.tiles
        for i in range(3):
            if tiles[i] == player_symbol and tiles[i + 3] == player_symbol and \
                    tiles[i + 6] == player_symbol:  # check for vertical win
                return player_symbol
            elif tiles[(i * 3)] == player_symbol and tiles[(i * 3) + 1] == player_symbol and \
                    tiles[(i * 3) + 2] == player_symbol:  # check for horizontal win
                return player_symbol

        # check for diagonal wins
        if tiles[0] == player_symbol and tiles[4] == player_symbol and tiles[8] == player_symbol:
            return player_symbol
        elif tiles[2] == player_symbol and tiles[4] == player_symbol and tiles[6] == player_symbol:
            return player_symbol

    def board_is_full(self):
        for value in self.tiles.values():
            if not value:
                return False
        return True

    def show(self):
        print("{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n".format(self.tiles[0], self.tiles[1], self.tiles[2],
                                                                  self.tiles[3], self.tiles[4], self.tiles[5],
                                                                  self.tiles[6], self.tiles[7], self.tiles[8]))


class Player:
    # give the player a constructor which takes the player_symbol and name as arguments
    def __init__(self, player_symbol, name):
        self.name = name
        self.player_symbol = player_symbol

    def get_move(self):
        raise NotImplementedError


class Human(Player):
    # create a constructor which initializes the the player symbol and it's name
    def __init__(self):
        super().__init__("X", self.__class__.__name__)

    def get_move(self):
        return int(input("Chose a location between 0-8"))


class Computer(Player):
    # create a constructor which initializes the the player symbol and it's name
    def __init__(self):
        super().__init__("O", self.__class__.__name__)

    def get_move(self):
        return random.randint(0, 8)


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    # check if the game is over
    def game_over(self):
        if self.board.board_is_full() or self.board.has_won(self.player1.player_symbol) or \
                self.board.has_won(self.player2.player_symbol):
            return True
        return False

    # check if the move is legal if not ask for another move
    def make_move(self, player):
        could_update_board = False
        while not could_update_board:
            move = player.get_move()
            could_update_board = self.board.update_board(move, player.player_symbol)

    def play(self):
        current_player = self.player1
        while not self.game_over():
            self.board.show()
            self.make_move(current_player)
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1
        self.board.show()
        if self.board.has_won(self.player1.player_symbol):
            print(f"Congratulations {self.player1.name} you won!")
        elif self.board.has_won(self.player2.player_symbol):
            print(f"Congratulations {self.player2.name} you won!")
        else:
            print("It's a draw")
        print("Thank you for playing")


def main():
    human = Human()
    computer = Computer()
    game = Game(human, computer)
    game.play()


if __name__ == '__main__':
    main()
