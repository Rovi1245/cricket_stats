class Player:
    def __init__(self, player_name, country, matches, runs):
        self.player_name = player_name
        self.country = country
        self.matches = matches
        self.__runs = runs  # Use __runs for private attribute
        
    def get_runs(self):
        return self.__runs
    
    def set_runs(self, runs):
        if runs < 0:
            print("Enter a value greater than 0")
        else:
            self.__runs = runs
            
    def calculate_average(self):
        if self.matches > 0:
            avg = self.__runs // self.matches
            print(avg)
        else:
            print("Matches cannot be zero.")
        
class Strikerate(Player):
    def __init__(self, runs, balls):
        # Initialize parent class with default values for player_name, country, and matches
        super().__init__("Unknown", "Unknown", 1, runs)
        self.balls = balls
        
    def calculate_strikerate(self):
        if self.balls > 0:
            strike_rate = (self.get_runs() / self.balls) * 100
            return strike_rate
        else:
            return "Balls faced cannot be zero."

# Create a Player object
p = Player("rohan", "india", 10, 453)

# Create a Strikerate object
s = Strikerate(453, 200)

# Print the strike rate using the Strikerate object
print(s.calculate_strikerate())
