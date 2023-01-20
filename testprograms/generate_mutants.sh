#!/bin/bash
python conv.py

[ -d raw_output ] && rm -r raw_output
[ -d output ] && rm -r output
[ -d compiled_programs ] && rm -r compiled_programs

mkdir compiled_programs
mkdir raw_output
mkdir output

for file in raw_programs/*.c; do 
    if [ -f "$file" ]; then 
        base_file=$(basename $file)
        clang -fembed-bitcode -g $file -o compiled_programs/${base_file%.*}.o
    fi 
done

for file in compiled_programs/*.o; do 
    if [ -f "$file" ]; then 
        base_file=$(basename $file)
        mull-cxx --reporters Elements $file
        rm -r *.html
        mv *.json raw_output/${base_file%.*}.json
    fi 
done

python3 process_output.py

cd ../wasmfiles

[ -d mutantprograms ] && rm -r mutantprograms
mkdir mutantprograms

cd ../testprograms
cd output
for file in *.c; do
mv $file ../../wasmfiles/mutantprograms/
done

cd ..
cd raw_programs
for file in *.c; do
mv $file ../../wasmfiles/mutantprograms/
done

cd ../../wasmfiles
bash conv.sh



