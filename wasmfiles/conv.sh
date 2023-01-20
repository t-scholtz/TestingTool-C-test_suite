#!/bin/bash
STRING="mutant"
[ -d wasm ] && rm -r wasm
[ -d wat ] && rm -r wat
[ -d differences ] && rm -r differences
[ -d webApps ] && rm -r webApps
[ -d results ] && rm -r results

mkdir wasm
mkdir wat
mkdir differences
mkdir webApps
mkdir results

rm error_in_output.txt
echo "Differences in C vs Wasm:" >> error_in_output.txt


#Create wasm files
cd mutantprograms
for file in *.c; do
if [ -f "$file" ]; then 
        base_file=$(basename $file)
        emcc $file -s WASM=1 -o ../wasm/${base_file%.*}.html
    fi 
done

#Copy files and general file managment
cd ..
cp -a ./wasm/. ./webApps
cd wasm
find . -type f ! -iname "*.wasm" -delete

#Converts wasm to wat

for file in *.wasm; do
if [ -f "$file" ]; then 
        base_file=$(basename $file)
        wasm2wat $file -o ../wat/${base_file%.*}.wat
    fi 
done
cd ..

#Creates an output file for each core C program and creates a list of differents for each
cd mutantprograms
for file in *.c; do
if [[ "$file" != *"$STRING"* ]];then
	base_file=$(basename $file ".c")
	cd ../differences
 	mkdir $base_file

	cd $base_file
	mkdir C_Diff
	mkdir C_out
	mkdir Wat_Diff
	mkdir Wasm_out
	cd Wasm_out
	mkdir chrome_out
	cd ../../../mutantprograms
	for mutant in *.c; do
		if [[ "$mutant" == *"$STRING"* ]] && [[ "$mutant" == *"$base_file"* ]];then
			mutt_name=$(basename $mutant ".c")
			diff $file $mutant > ../differences/$base_file/C_Diff/"$mutt_name"_c.txt
	  	fi
	done
 

	cd ../wat
	for wat in *.wat; do
		if [[ "$wat" == *"$STRING"* ]] && [[ "$wat" == *"$base_file"* ]];then
			wat_name=$(basename $wat ".wat")
			wat_text="_wat"
			file_name="${wat_name} ${wat_txt}"
			diff "$base_file".wat $wat > ../differences/$base_file/Wat_Diff/"$file_name"_wat.txt
	  	fi
	done

	cd ../mutantprograms
	for cProg in *.c ; do
		if [[ "$cProg" == *"$base_file"* ]];then
			file_path=$(basename $cProg ".c")
			gcc $cProg -o $file_path.o
			(./$file_path.o > ../differences/$base_file/C_out/"$file_path".txt) & sleep 5 ; kill $!
		fi
	done
	#Generates output for wasm files
	cd ../webApps
  fi
done

cd ../js_editor
python3 js_editor.py
cp debugout.js ../webApps/

#create an external sever
cd ..
cd webApps	
gnome-terminal -- bash -c "python3 -m http.server; exec bash"
cd ..
cd differences

for prog in *; do
    cd ../webApps
   for fhtml in *.html; do
        if [[ "$fhtml" == *"$prog"* ]] ; then
            name=$(basename $fhtml ".html")
	        log_file=$name'_log.txt'
	        link='http://0.0.0.0:8000/'$fhtml
	        
			google-chrome $link &
			sleep 5
            DISPLAY=:0.0 wmctrl -c "Google Chrome"
           #Change file path here
         mv ~/Downloads/chrome/$log_file ../differences/$prog/Wasm_out/chrome_out/$log_file
			sleep 1


        fi
    done
    cd ../differences
done

cd ..
bash findErrors.sh