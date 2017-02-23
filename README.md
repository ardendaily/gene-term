#gene-term

ascii-aesthetics-cum-genetic-sequencing, in python

-----------

### originally

this is a totally weird project i threw together in a several-hour 
sprint. the program tries to ascend the value of rows of letters with 
basic genetic algorithms. it succeeds, depending on your definition of success. 

### but now

i decided to keep hacking at this, and it is currently unusable. 

i have refactored it to work on top of ArdenShell (dogfooding again), 
which forced me to continue working on ArdenShell (which is good)! 
changes include being able to set generation dimensions and target 
strings. the end-game here is an interactive gene splicer thingie for 
deriving interesting-looking strings. possible applications: making ASCII
textiles, finding cool-looking license plate numbers, etc. basically, 
"let's use genetic algorithms to paint with ASCII!!!"

i'm hitting a namespace bug, i think, where the current generations 
does not become the next generation, due to some poor variable passing
in and out of ardenshell. will continue to hack on both until both work.


### want to try it out?

`git clone https://github.com/ardendaily/gene-term.git`

`cd gene-term`

`python gene-term.py`

razzle dazzle!
