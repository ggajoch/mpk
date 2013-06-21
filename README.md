mpk
===

something to visualize traffic in kraków



Requirements
===
Python (2.6 or 3) with re library.




Usage
===
File path.py opens map.svg file (with city description) and reads standard input (stdin) waiting for commands for changing routes.

Firstly, give the name of route or loop (it comes with "p" suffix), and then two numbers which determines Red and Green saturation. Te last parameter determines the width of route.
If you want to hide the line (or loop) then give one parameter - "-1".


Example
===
Go to example/ directory, and then:

$ python path.py < in > m.svg

And then just open 'm.svg' file with your favourite svg wiever.


