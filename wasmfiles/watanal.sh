#!/bin/bash
rm watErrorsFound.txt
echo "Wat Differences found" >> watErrorsFound.txt
cd differences


DIR="Wat_Diff"

for folder in *; do
    cd $folder
        
    python3 ../../watStuff.py

    cd ..
done
