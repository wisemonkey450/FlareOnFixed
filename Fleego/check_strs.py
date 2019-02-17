import r2pipe
import struct
import os
import sys

def get_list_files():
    return os.listdir("./EXE")

def main():
    #list of files
    files = get_list_files();
    sessions = []
    #Change to the file dir
    os.chdir("./EXE")

    for filename in files:
        sessions.append(r2pipe.open(filename))

    #Analyze each individual binary
    for ses in sessions:
        #Analyze
        ses.cmd("aaaaaa")

        #Look for strings....
        print ses.cmd("izz ~Iron")

        #Exit
        ses.quit()

    #Reset
    os.chdir("..")

if __name__ == "__main__":
    main()
