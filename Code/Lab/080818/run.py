#!C:\env\env\Scripts\python.exe

from main import main
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', dest="config_file", default="main.py")
parser.add_argument('-m', dest="comment")

args = parser.parse_args()

if os.path.exists(args.config_file):
    pass
else:
    print("File config does not exist ")
    exit(1)

main(args.comment)


