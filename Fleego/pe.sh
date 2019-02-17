#! /bin/sh

for file in $(ls *.exe)
do
    readpe $file | grep -A 10 ".text" | grep "Size:"
done
