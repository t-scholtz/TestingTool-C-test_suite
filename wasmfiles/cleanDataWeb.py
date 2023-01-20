import glob

#all_files = [glob.glob("brave_out/*.txt"),glob.glob("chrome_out/*.txt"),glob.glob("edge_out/*.txt"),glob.glob("firefox_out/*.txt"),glob.glob("opera_out/*.txt")]

all_files = [glob.glob("chrome_out/*.txt")]

for folder in all_files:
    for file_name in folder:
        inFile = open(file_name,"r")
        data = inFile.readlines()
        newFile = open(file_name,"w")
        for line in data[1:-1]:
            temp =line.strip('"').replace('"','')
            if "] " in line:
                newFile.write(""+temp[temp.index(']')+2:].strip('"'))
            else:
                newFile.write(""+temp.strip('"'))

        newFile.close()
