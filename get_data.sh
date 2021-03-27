#!/bin/bash
if kaggle datasets download -d sgonkaggle/youtube-trend-with-subscriber && unzip youtube-trend-with-subscriber.zip; then
    head -n 2 USvideos_modified.csv
    grep -v -e "^$" - USvideos_modified.csv
    COUNT=$(wc -l "USvideos_modified.csv")
    echo "${COUNT}"
    head -n -1 "USvideos_modified.csv" | shuf > "data_shuf"
    head -n 544 data_shuf > data_test
    head -n 1088 data_shuf | tail -n 544 > data_dev
    head -n +1089 data_shuf > data_train
    echo "Shuffled dataset"
    wc -l data_shuf
    echo "Test dataset"    wc -l data_test
    echo "Dev dataset"
    wc -l data_dev
    echo "Train dataset"
    wc -l data_train
    python main.py USvideos_modified.csv
fi