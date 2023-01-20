import glob

all_files = glob.glob("single-exec/*.c")

for file_name in all_files:

    # Read the file
    
    temp_name = file_name.replace('single-exec/','').replace('.c','')
    temp_name = temp_name +"_mod.c"
    with open(file_name, 'r') as f:
        with open('raw_programs/'+temp_name,'w') as conv_f:
            conv_f.write('#include <stdio.h>\n')
            for line in f:
                if 'return' in line :
                    val = line[line.find('return')+6:line.find(';')]
                    space = line[0:line.find('return')]
                    conv_f.write(space + 'printf("%d\\n",'+val+'); ')
                    conv_f.write(line)
                elif '#include <stdio.h>' in line :
                    #do nothing 
                    line=line
                else :
                    conv_f.write(line)
                

