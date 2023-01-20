from fileinput import filename
import glob 
import os

all_files = glob.glob("../webApps/*.js")
print("starting")
for file_name in all_files:
    line_num=0

    print("running")
    print(file_name)

    f =open(file_name, 'r')
    output_f = open("../webApps/tempFile.js", 'w')
    name = file_name.rindex('/')+1
    baseName = file_name[name:-3]
    logName= baseName+ "_log.txt"
    for line in f:
        if(line_num==16):
            output_f.write(line)
            output_f.write("import { Debugout } from './debugout.js';\n")
            output_f.write('const bugout = new Debugout({ realTimeLoggingOn: true,useTimestamps: true,includeSessionMetadata: true,logFilename: "'+ logName +'"});\n')
        elif(line_num==212):
            output_f.write('bugout.log = /** @type{!function(this:Console, ...*): undefined} */ (print);\n')
            output_f.write("bugout.warn = bugout.error = /** @type{!function(this:Console, ...*): undefined} */ (typeof printErr !== 'undefined' ? printErr : print);\n")
            line_num=line_num+1
        elif(line_num==286):
            output_f.write("var out = Module['print'] || bugout.log.bind(bugout);\n")
        elif(line_num==287):
            output_f.write("var err = Module['printErr'] || bugout.warn.bind(bugout);\n")
        elif(line_num==2399):
            output_f.write("console.log(bugout.getLog());\n")
            output_f.write("bugout.downloadLog()\n")
            output_f.write(line)
        else:
            output_f.write(line) 

        line_num=line_num+1      

    output_f.close 
    os.rename("../webApps/tempFile.js",file_name)


html = glob.glob("../webApps/*.html")
print("editing html files")

for hfile in html:
    line_num=1

    print("running")
    print(hfile)

    f =open(hfile, 'r')
    name = hfile.rindex('/')+1
    baseName = hfile[name:-5]
    print(baseName)

    outf= open("../webApps/tempFile.html", 'w')

    for line in f:
        if(line_num==1292):
            outf.write('<script async type="module" src="'+ baseName +'.js"></script> <>')
        else:
            outf.write(line)
        line_num=line_num+1
        
    os.rename("../webApps/tempFile.html",hfile)




