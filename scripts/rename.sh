#!/bin/bash
# simple script to batch rename files

for file in */*/*.com; do # for files in which directory with which extension
   mv $file ${file/chelpg/hf631gd.mk/}; # replace chelpg with hf631gd.mk for example
done
