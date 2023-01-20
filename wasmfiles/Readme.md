# Notes on how to run tool

Run bash script : "bash generate_mutants.sh" while inside testprograms


## Changes made from orgianl
* No longer runs tests in multiple browsers - this speeds up run time
* Tried to make file paths more universal

## potential problems 
* I get a warning error when running chrome through terminal - 

 WARNING: lavapipe is not a conformant vulkan implementation, testing use only.
[1032819:1032819:0117/142200.920331:ERROR:viz_main_impl.cc(186)] Exiting GPU process due to errors during initialization
WARNING: lavapipe is not a conformant vulkan implementation, testing use only.

- But everthing seems to run fine otherwise