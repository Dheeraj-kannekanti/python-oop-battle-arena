# ⚔️ Python OOP Battle Arena

A terminal-based combat simulation designed to demonstrate the core pillars of **Object-Oriented Programming (OOP)** in Python. This project features a battle between a Warrior and a Mage, utilizing modular classes and controlled data access.

## 🚀 OOP Concepts Implemented

* **Abstraction**: Used the `ABC` module to create a `Fighter` base class, ensuring all character types implement an `attack` logic.
* **Encapsulation**: Protected the `__health` attribute using private variables. Access is controlled through a `@property` decorator (getter).
* **Inheritance**: `Warrior` and `Mage` classes inherit shared attributes and methods from the `Fighter` parent class.
* **Polymorphism**: Both subclasses use the same `attack` method name but execute unique damage calculations.
* **Composition**: Implemented a "Has-A" relationship where a `Fighter` object contains a `Weapon` object.

---

## 🛠️ Project Structure

| Class | Role | OOP Principle |
| :--- | :--- | :--- |
| `Weapon` | Defines damage and name of equipment. | **Composition** |
| `Fighter` | The abstract blueprint for all combatants. | **Abstraction** |
| `Warrior` | Physical attacker using standard weapon damage. | **Inheritance** |
| `Mage` | Magic attacker with a +5 damage bonus. | **Polymorphism** |

---

## 🎮 How to Run

1. **Ensure you have Python installed.**
2. **Clone this repository:**
   git clone [https://github.com/Dheeraj-kannekanti/python-oop-battle-arena.git]
   
4. Navigate to folder : cd python-oop-battle-arena
5. Run the script : python arena.py
6. 
7. 
