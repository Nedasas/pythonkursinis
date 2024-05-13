1. Introduction
a. Application Overview
This coursework paper presents a Python program for a simple two-player battleship game. The program allows players to place their battleships on a grid and take turns attacking each other's ships until one player wins by sinking their opponent's battleship.

b. Running the Program
Save the provided code in a file named BattleShip.py. 
Additionally, download the file named initial_state.txt where you can input the location of the ships (IMPORTANT: Player 1 has to destroy Player 2's battleship and Player 2 has to destroy Player 1's destroyer) and final_state.txt which writes the last games winnner. 
Then, execute the program by running the command python BattleShip.py.

c. Program Usage
Once the program is running, follow the on-screen prompts. Players will take turns entering coordinates to attack their opponent's ships. The game continues until one player sinks the other's battleship.

2. Body/Analysis
a. Functional Requirements Coverage
The program implements the following functional requirements:

Placing Ships: Players can pick the location of their battleships in the initial_state.txt file.
Taking Turns: Players alternate turns to attack each other's ships.
Detecting Hits and Misses: The program accurately detects whether an attack hits or misses an opponent's ship.
Checking Ship Sinking: When a ship receives enough hits, the program correctly identifies it as sunk and a player is awarded the victory.


3. Results and Summary
a. Results (Functional Requirement)
The program successfully simulates a battleship game, enabling players to engage in strategic combat.
Challenges during implementation included accurately tracking ship positions and hits, as well as ensuring smooth turn-taking mechanics.
Despite these challenges, the program effectively detects hits and misses, allowing for a competitive gaming experience.

b. Conclusions (Functional Requirement)
The program has achieved a successful implementation of a classic battleship game in Python, providing players with an engaging gaming experience.
As a result of this work, players can enjoy strategic gameplay, accurately tracking hits and misses as they attempt to sink their opponent's battleship.
Looking ahead, the program has promising future prospects, with potential for enhancements such as improved user interfaces, additional game modes, and multiplayer support to further enrich the gaming experience.

c. Extensibility
To extend the application, several enhancements could be considered:

Enhanced User Interface: Improve the user interface with graphics and animations for a more immersive experience.
Additional Game Modes: Introduce different game modes or variations to add complexity and replay value.
Multiplayer Support: Implement network functionality to allow players to compete against each other over the internet.
4. Optional: Resources, References
The program does not rely on external libraries or resources beyond Python's standard library.
