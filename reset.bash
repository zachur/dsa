#!/bin/bash

if [ -e "./lib/__pycache__" ]; then 
    rm -f "$file_to_remove"
fi

if [ -e "./lib/base/__pycache__" ]; then
    rm -r ./lib/base/__pycache__
fi

if [ -e "./lib/merge/__pycache__" ]; then
    rm -r ./lib/merge/__pycache__
fi

if [ -e "./lib/search/__pycache__" ]; then
    rm -r ./lib/search/__pycache__
fi

if [ -e "./lib/sort/__pycache__" ]; then
    rm -r ./lib/sort/__pycache__
fi

if [ -e "./dataset/example.db" ]; then
    rm ./dataset/example.db
fi

if [ -e "./dataset/output.txt" ]; then
    rm ./dataset/output.txt
fi
