import glob
from operator import contains

all_files = glob.glob("Wat_Diff/*.txt")

with open("../../watErrorsFound.txt","a") as out:
    for file_name in all_files:
        # Read the file
        with open(file_name) as f:
            count = 0
            for line in f:
                count=count+1
            if count > 4:
                out.write(file_name+"\n")


