import glob

all_files = glob.glob("*.txt")

for file_name in all_files:
    inFile = open(file_name,"r")
    data = inFile.readlines()
    newFile = open(file_name,"w")
    for line in data:
        temp =line.strip('"').replace('"','')
        newFile.write(""+temp.strip('"'))

    newFile.close()