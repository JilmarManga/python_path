# chatGPT solution

import random

class Character:
    """
    Represents a character in the game with a name, health points, and attack power.
    """
    def __init__(self, name: str, health: int, attack_power: tuple[int, int]):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent: "Character"):
        """
        Perform an attack on the opponent. Reduces opponent's health by a random damage value.
        """
        damage = random.randint(*self.attack_power)  # Random damage between min and max
        opponent.health -= damage
        opponent.health = max(0, opponent.health)  # Ensure health doesn't go below zero
        return damage

    def is_alive(self) -> bool:
        """
        Check if the character is still alive (health > 0).
        """
        return self.health > 0

def display_status(player: Character, opponent: Character):
    """
    Display the current health status of both player and opponent.
    """
    print(f"\n{player.name}'s Health: {player.health}")
    print(f"{opponent.name}'s Health: {opponent.health}\n")

def main():
    """
    Main game loop for the Battle War game.
    """
    # Initialize characters
    player = Character(name="Player", health=100, attack_power=(10, 20))
    system = Character(name="System", health=100, attack_power=(8, 18))

    print("Welcome to Battle War! 💥")
    print("You and the system will take turns attacking until one of you loses all health.\n")

    # Main game loop
    while player.is_alive() and system.is_alive():
        # Player's turn
        print("Your Turn! ⚔️")
        damage = player.attack(system)
        print(f"You dealt {damage} damage to the System!")
        display_status(player, system)

        # Check if the system is defeated
        if not system.is_alive():
            print("Congratulations! You defeated the System! 🎉")
            break

        # System's turn
        print("System's Turn! 💻")
        damage = system.attack(player)
        print(f"The System dealt {damage} damage to you!")
        display_status(player, system)

        # Check if the player is defeated
        if not player.is_alive():
            print("You were defeated by the System. Better luck next time! 😢")

    print("Game Over. Thanks for playing!")

if __name__ == "__main__":
    main()