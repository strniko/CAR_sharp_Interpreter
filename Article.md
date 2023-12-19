[[File:CAR-sharp-logo.png.png|thumb|right|alt=The CAR# logo|The official logo of CAR#]]
{{wrongtitle|title=CAR#}}
'''CAR#''' is a [[esoteric programming language]] from 2023 by [[User:Niko Strauch]] inspired by [[brainfuck]]. Similar to [[brainfuck]] CAR# works by moving a cursor across a two dimensional array. The name CAR# originates from the ''car'' like cursor and the grid is represented by the ''#''.
==Versions==
===v.1===
At the point of 12/17/2023 there only exists version 1, or short ''v.1''. Every feature labelled with ''v.2'' is currently in the process of making. v.1 features 10 simple control commands and a BIOS GUI.

===v.2 (in development)===
The coming v.2 will feature at least 12 10 simple control commands, a BIOS GUI and hopefully a visual debugging GUI.

==Syntax and commands==
CAR# v.1 only uses ''10 single letter commands'' to control the car across a ''1024 by 1024 array'' starting in the top left corner facing down (180°).
{| class="wikitable"
|+ Command List
|-
! CAR# Command !! Description !! Release Version !! Notes
|-
| ^ || Moves the car one cell foreword || v.1 ||
|-
| / || Turns the car 90° clockwise || v.1 ||
|-
| \ || Turns the car 90° counter clockwise || v.1 || Sometimes the backslash gets recognised as a control character. In this case use \\.
|-
| + || Adds one to the cell that the car is standing on || v.1 ||
|-
| - || Subtracts one of the currently occupied cell || v.1 ||
|-
| = || Outputs the raw integer value of the current cell || v.1 ||
|-
| > || Outputs the value of the current cell as a ASCII character || v.1 ||
|-
| < || Each time this command is called it replaces the value of the current cell with the current ''input character'' || v.1 ||
|-
| [...] || while the value of the current cell is not zero the commands in the brackets get called || v.1 || Due to ''infinite loops'' not working in v.1 you have to decrease the value of the cell in the loop.
|-
| {...} || copies the value of the current cell and repeats the operations in the brackets this amount of times || v.2 ||
|}

==Examples==
===[[Hello, World!]]===
This is the standard program for almost every programming language. It outputs the words ''Hello, World!''. Note that this version of Hello, World! is very stupid and bad designed.
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++>^
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>^
 +++++++++++++++++++++++++++++++++>^
===Cat===
This is a very simple program that repeats the ''input''.
 <[><]
==Interpreters, external links and more==
I myself wrote a small CAR# v.1 interpreter in Python and as far as I know this is the only one in existence. Feel free to write and publish other or better interpreters to the [https://github.com/strniko/CAR_sharp_Interpreter GitHub].
More coming soon!!!

[[User:Niko Strauch|Niko Strauch]] ([[User talk:Niko Strauch|talk]]) 18:08, 17 December 2023 (UTC)

[[Category:Languages]] [[Category:Implemented]] [[Category:Cell-based]]
