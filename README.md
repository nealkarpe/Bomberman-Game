# Bomberman

Terminal-based game without the help of any User Interface library like ncurses, pygame, etc.

### Prerequisites

* Install the package termcolor - "sudo pip3 install termcolor"

### Running

* Start the game using "python3.5 run.py"
* Terminal should be at regular zoom for best experience

### Controls

* W - Move Up
* A - Move Left
* S - Move Down
* D - Move Right
* B - Drop a bomb

### Objective

* You cannot destroy solid walls with bombs
* You can destroy brick walls with bombs
* The aim is to kill all the enemies
* You die if you bump into an enemy or if you get bombed

### Screenshots

#### The whole board is made up of simple ASCII characters displayed on terminal. Different colors are obtained by the termcolor library.

##### Bomb Counting Down
![bombcountdown](https://user-images.githubusercontent.com/31779922/34363978-2ae82d26-eaa7-11e7-8c15-88044e6a1dbf.png)

##### Bomb Explosion
![bombexplosion](https://user-images.githubusercontent.com/31779922/34363980-2b6445a0-eaa7-11e7-8486-fcc273e80fc4.png)

##### Game over by bumping into enemy
![deathbytouchingenemy](https://user-images.githubusercontent.com/31779922/34363981-2ba14ffe-eaa7-11e7-9c76-e68ad2cf5cbd.png)
