import glob
from operator import contains

all_files = glob.glob("results/*.txt")

with open("error_in_output.txt","a") as out:
    out.write("Result Analysis:\n")
    for file_name in all_files:
        # Read the file
        with open(file_name) as f:
            programName=f.readline().strip()
            for line in f:
                line=line.strip()
                if "Diff Found" in line:
                    out.write(programName+" -- "+line+"\n")


