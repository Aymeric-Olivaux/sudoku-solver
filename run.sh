#!/bin/bash


if [ $1 = "test" ]
then
  exec python -m unittest
fi


if [ $1 = "start" ]
then
    cd $HOME
    echo $PATH
    exec /home/aymeric/Documents/SudokuSolver/venv/bin/python /home/aymeric/Documents/SudokuSolver/src/main.py 
fi

