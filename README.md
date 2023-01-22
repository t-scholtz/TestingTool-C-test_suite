# Notes on how to run tool

Run bash script : "bash generate_mutants.sh" while inside testprograms

# What the tool does

Tool takes in C programs. The C programs are examined, and if they do not print anything, a scipt is run which inserts print statements above every return command. The prinit statments prints the returned value as a string.

Then this new collection of modified C tests is ran throught the MULL Mutation tool. This gerenates mutants based a set of rules, but mostly by swapping arithimitc sysmbols, such as a muliiply with a divide.

From these mutants the corresponing wasm, wat and C object file are created. For each wasm file, the corresponing js file which runs it is edited, so that it runs debugout.js to download the web browser output as a text file.

The ouput from the C and wasm is then compared so to look for differnes.
If a difference is found, the test is then flagged.


The tool also looks through the changes to the mutants, and looks for dispraportional changes to the wat files. So if when generateing a mutant, only a single line of C code was change, but then the corresponding wat file had mutiple lines change, it will be flaged as a mutli - line wat change.

## Changes made from orgianl
* No longer runs tests in multiple browsers - this speeds up run time
* Tried to make file paths more universal

## potential problems 
* I get a warning error when running chrome through terminal - 

 WARNING: lavapipe is not a conformant vulkan implementation, testing use only.
[1032819:1032819:0117/142200.920331:ERROR:viz_main_impl.cc(186)] Exiting GPU process due to errors during initialization
WARNING: lavapipe is not a conformant vulkan implementation, testing use only.

- But everthing seems to run fine otherwise