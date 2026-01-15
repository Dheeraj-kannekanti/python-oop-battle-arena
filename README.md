 ⚔️ Python OOP Battle Arena

A terminal-based combat simulation designed to demonstrate the core pillars of **Object-Oriented Programming (OOP)** in Python. This project features a battle between a Warrior and a Mage, utilizing modular classes and controlled data access.

 🚀 OOP Concepts Implemented

 **Abstraction**: Used the `ABC` module to create a `Fighter` base class. This ensures any character type (Warrior, Mage, etc.) *must* implement their own `attack` logic.
 **Encapsulation**: Protected the `__health` attribute using double underscores (private variables). Access is strictly controlled through a `get_health()` method to prevent external tampering.
 **Inheritance**: The `Warrior` and `Mage` classes inherit shared attributes and methods from the `Fighter` parent class, reducing code duplication.
 **Polymorphism**: Both subclasses use the same `attack` method name but execute different logic (Physical vs. Magic damage calculation).
 **Composition**: Implemented a "Has-A" relationship where a `Fighter` object contains a `Weapon` object, allowing for modular equipment management.

 🛠️ Project Structure

| Class | Role | OOP Principle |
| `Weapon` | Defines damage and name of equipment. | **Composition** |
| `Fighter` | The abstract blueprint for all combatants. | **Abstraction** |
| `Warrior` | Physical attacker using standard weapon damage. | **Inheritance** |
| `Mage` | Magic attacker with a +5 damage bonus. | **Polymorphism** |


 🎮 How to Run
1. Ensure you have Python installed.
2. Clone this repository: git clone https://github.com/Dheeraj-kannekanti/python-oop-battle-arena.git
3. Navigate to the folder and run the script:
python main.py

### What should we do next?

Would you like to learn how to **Document your code** using **Docstrings** (so other developers can see help text for your classes), or should we move on to **Exception Handling** to prevent the game from crashing if a user enters a wrong value?
