# CAR# Interpreter

Hello, I'm Niko Strauch, the creator of the esoteric programming language, CAR#. This repository contains interpreters for CAR#.

## About CAR#

CAR# is an esoteric programming language I created in 2023. It's inspired by brainfuck and works by moving a cursor across a two-dimensional array. The name CAR# comes from the car-like cursor and the grid is represented by the `#`.

As of December 17, 2023, only version 1 (v.1) exists. Every feature labeled with v.2 is currently in the process of being developed.

For more information about CAR#, please visit the [CAR# Article](https://esolangs.org/wiki/CAR_sharp). 

## Commands

CAR# uses 10 single letter commands to control the car across a 1024 by 1024 array starting in the top left corner facing down.

Here are the commands used in CAR#:

- `^`   Moves the car one cell forward
- `/`   Turns the car 90° clockwise
- `\`   Turns the car 90° counter clockwise
- `+`   Adds one to the cell that the car is standing on
- `-`   Subtracts one from the currently occupied cell
- `=`   Outputs the raw integer value of the current cell
- `>`   Outputs the value of the current cell as an ASCII character
- `<`   Each time this command is called it replaces the value of the current cell with the current input character
- `[...]`   While the value of the current cell is not zero the commands in the brackets get called
- `{...}`   Copies the value of the current cell and repeats the operations in the brackets this amount of times (v.2 feature)

## Contributing
Feel free to contribute to this project by writing and publishing other or better interpreters. More coming soon!!!

