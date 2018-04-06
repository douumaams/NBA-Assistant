import os
import random
import requests
from random import randint

def read_inputs(fileName):
    file = open(fileName, "r")
    inputs = []
    i = 0
    j = 0

    for line in file:
        line_splited = line.split("\n")
        inputs.append(line_splited[0])
        i = i + 1


    file.close()
    return inputs

if __name__=="__main__":
	inputs = read_inputs("./../res/inputs.txt")
	print(inputs)
