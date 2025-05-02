# 🧱 Tetris OOP 🕹️

[![Tetris Gameplay](Insert GIF or image link of the game here)](Insert game page link here if available)

🎮 This is a classic Tetris game developed using the **Pygame** library in Python, utilizing **Object-Oriented Programming (OOP)** principles. This project was created as my initial practical exercise in the world of game development with Pygame, with the goal of **in-depth self-learning** of the library and understanding game programming principles.

## 🕹️ How to Play

The game runs on your computer after installing Pygame.

### ⌨️ Controls:

* **Left Arrow:** Move the block to the left.
* **Right Arrow:** Move the block to the right.
* **Down Arrow:** Increase the falling speed of the block.
* **Up Arrow:** Rotate the block.
* **Space:** Drop the block directly down.

### 🎯 Goal:

Arrange the falling blocks to create complete rows without gaps. When a complete row is formed, it disappears, and you score points. The game ends when the blocks stack up to the top of the screen.

## 👨‍💻 OOP Principles in the Project

This project was implemented using Object-Oriented Programming principles to create organized, modular, and maintainable code:

* **Classes:** The game is built with different classes representing the main game components, such as:
    * `Shape`: An abstract class for representing the different block shapes.
    * `Cube`: A class for representing the square block (O).
    * `Line`: A class for representing the straight block (I).
    * `Pluse`: A class for representing the plus-shaped block (T).
    * `GameBoard`: **(Planned)** A class that will manage the game board, cell states, and interaction with the blocks.
    * `Game`: **(Planned)** A class that will manage the game loop, user input, scoring, and more.
* **Inheritance:** Each block type (Cube, Line, Pluse) inherits from the `Shape` class and implements its unique behavior (different shapes, rotation options).
* **Encapsulation:** Each class is responsible for its data and behavior, which makes it easier to manage the game state and prevent direct and uncontrolled access to data. Although some classes are still under development, this principle guides the system design.

## 📚 The Self-Learning Journey with Pygame

This project was an **exciting first step** for me in the world of game development using the Pygame library. It was a **self-learning challenge** where I had to explore the library's documentation, understand basic concepts of graphics and interaction, and apply them practically. The process included:

* Understanding the game lifecycle in Pygame (**initialization**, **game loop**, **event handling**, **drawing**).
* Handling user input (keyboard).
* Implementing game logic (block movement, rotation, collision detection, line clearing, scoring).
* Using Pygame's coordinate system and drawing shapes and colors.

## 🛠️ Installation and Running

1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
2.  **Download the game files** (if they are not already on your computer).
3.  **Navigate to the game directory** in the terminal.
4.  **Run the game:**
    ```bash
    python main.py
    ```
    (Replace `main.py` with the name of your main game execution file).

## 🤝 Contribution

If you have ideas for improvements, found bugs, or just want to contribute, you are welcome to open an Issue or send a Pull Request!

## 📧 Contact

omergrau@gmail.com
