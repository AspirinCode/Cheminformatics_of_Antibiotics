#!/bin/bash

for file in */*/*.com; do # for which file extensions in which directory
   sed -i -e 's/b3lyp/m062x/g' $file # use sed to replace one string with another for example b3lyp with m062x
   sed -i -e 's/B3LYP/m062x/g' $file
done
