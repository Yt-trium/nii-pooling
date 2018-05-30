#!/bin/bash
for filename in ./Dataset/*.nii ; do
    echo $filename;
    echo ${filename::-4};
    echo 'python nii-pooling.py ${filename::-4}';
    python3 nii-pooling.py ${filename::-4};
done