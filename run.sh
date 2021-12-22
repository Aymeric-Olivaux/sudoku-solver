#!/bin/bash


if [ $1 = "test" ]
then
  exec python -m unittest
fi
