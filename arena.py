from abc import ABC, abstractmethod
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Fighter(ABC):
    def __init__(self, name, health, weapon):
        self.name = name
        self.__health = health
        self.weapon = weapon
    def take_damage(self, amount):
        self.__health -= amount
        print(f"{self.name} took {amount} Damage, current health: {self.__health}")
    @abstractmethod
    def attack(self, opponent):
        pass
    @property
    def health(self):
        """This is a 'Getter' property"""
        return self.__health

class Warrior(Fighter):
    def attack(self, opponent):
        print(f" 🗡️  {self.name} swings their {self.weapon.name}!")
        opponent.take_damage(self.weapon.damage)

class Mage(Fighter):
    def attack(self, opponent):
        massMove = self.weapon.damage + 5
        print(f" ⚔️  {self.name} casts a spell with {self.weapon.name}!")
        opponent.take_damage(massMove)

if __name__ == "__main__":
    BloodReaper = Weapon("Blood reaper", 12)
    GhostKnife = Weapon("Ghost knife", 8)
    
    arthur = Warrior("Arthur", 50, GhostKnife)
    merlin = Mage("Merlin", 60, BloodReaper)

    print("--- THE BATTLE BEGINS ---")
    print(f"---Arthur vs Merlin---")
    print(f"Initial health\nArthur: {arthur.health}\nMerlin: {merlin.health} ")
    while arthur.health > 0 and merlin.health > 0:
        arthur.attack(merlin)
        if merlin.health <= 0:
            print(f"\n🏆 {arthur.name} is Victorious! ")
            break
            
        merlin.attack(arthur)
        if arthur.health <= 0:
            print(f"\n🏆 {merlin.name} is Victorious!")
            break
