

This is the result of a failed attempt to prototype my simulator in Python first before
completing it in C. Unfortunately, the conversion process ended up being much more difficult
than what I thought it would be, and as a result, I've spent all of my time recently trying
to get the C code to work instead of writing an analysis of the results. I have submitted
my Python code, the C code that I wrote (it compiles, but generates a seg fault), and
the two graphs I created in the hopes of obtaining at least some marks.

Python code:
psim.py - the executable that accepts the command line parameters
sim.py - called by psim and actually runs the simulation and returns the results
script.py - small script I used for calling psim with different protocols and p values
plot_data.py - small script for extracting data from text files and creating graphs