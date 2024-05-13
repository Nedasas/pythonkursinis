# Define ship types
class Ship:
    def __init__(self):
        self.hits = 0

    def hit(self):
        self.hits += 1
        return True

class Battleship(Ship):
    pass

class Destroyer(Ship):
    pass

# Factory pattern to create ships
class ShipFactory:
    @staticmethod
    def create_ship(ship_type):
        if ship_type == "battleship":
            return Battleship()
        elif ship_type == "destroyer":
            return Destroyer()
        else:
            raise ValueError("Invalid ship type")

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[0 for _ in range(10)] for _ in range(10)]  # Initialize empty board
        self.ship = None

    def place_ship(self, ship_type, position):
        if self.ship:
            raise ValueError("Ship already assigned to player")
        self.ship = ShipFactory.create_ship(ship_type)
        row, col = position
        if row >= 10 or col >= 10:
            raise ValueError("Invalid ship placement")
        self.board[row][col] = 1
        self.ship.positions = [(row, col)]  # Add ship position

    def receive_attack(self, opponent, position):
        row, col = position
        if opponent.board[row][col] == 1:
            if (row, col) in opponent.ship.positions:
                if opponent.ship.hit():
                    print(f"{self.name} hit {opponent.name}'s {type(opponent.ship).__name__}!")
                    return "hit"
                    if opponent.check_ship_sunk():
                        return "win"
        else:
            print(f"{self.name} missed!")
            return "miss"

    def check_ship_sunk(self):
        return self.ship.hits == 1

# Game class
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play_turn(self):
        print(f"\n{self.current_player.name}'s turn:")
        row = int(input("Enter row (0-9): "))
        col = int(input("Enter column (0-9): "))
        result = self.current_player.receive_attack(self.get_opponent(), (row, col))
        if result == "hit":
            if self.get_opponent().check_ship_sunk():
                return "win"
        elif result == "miss":
            self.switch_player()
        return result

    def get_opponent(self):
        return self.player2 if self.current_player == self.player1 else self.player1

# Write final game state to file
def write_final_state(filename, winner):
    with open(filename, "w") as file:
        file.write(f"Winner: {winner.name}")

# Read initial game state from file
def read_initial_state(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

# Main function
def main():
    initial_state = read_initial_state("initial_state.txt")
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1_ship_info = initial_state[0].strip().split()
    player2_ship_info = initial_state[1].strip().split()

    player1.place_ship(player1_ship_info[0], (int(player1_ship_info[1]), int(player1_ship_info[2])))
    player2.place_ship(player2_ship_info[0], (int(player2_ship_info[1]), int(player2_ship_info[2])))

    game = Game(player1, player2)

    while True:
        result = game.play_turn()
        if result == "win":
            print(f"\n{game.current_player.name} wins!")
            write_final_state("final_state.txt", game.current_player)
            break

if __name__ == "__main__":
    main()
