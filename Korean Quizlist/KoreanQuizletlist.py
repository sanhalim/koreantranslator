'''
Created on Mar 27, 2018

@author: Sanha Lim
'''
from builtins import list
def openfile(fname):
    data = []
#     f = open(fname)
    f = open(fname, 'r', encoding="utf-16")
    wList = f.readlines()
    for x in wList:
        data.append(x.strip())
    f.close()
    return data

def openfile2(fname):
    data = []
#     f = open(fname)
    f = open(fname, 'r')
    wList = f.readlines()
    for x in wList:
        data.append(x.strip())
    f.close()
    return data

def englishnkoreanlist(fname, fname2):
    korean = openfile(fname2)
    english = openfile2(fname)
    list = []
    for x in english:
        list.append(korean[english.index(x)])
    for y in list:
        print(y)
        

if __name__ == '__main__':
    englishnkoreanlist("english.txt","fixedkorean.txt")