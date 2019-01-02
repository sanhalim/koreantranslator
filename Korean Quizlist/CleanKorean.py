'''
Created on Mar 27, 2018

@author: Sanha Lim
'''
# import codecs

def openfile(fname):
    data = []
#     f = open(fname)
    f = open(fname, 'r', encoding="utf-8")
    wList = f.readlines()
    for x in wList:
        data.append(x.strip())
    f.close()
    return data

def cleankorean(fname):
    data1 = openfile(fname)
    f = open("fixedkorean.txt", 'w', encoding ="utf-16")
    for x in data1:
        if x == "":
            continue
        f.write(x+"\n")
        
            

if __name__ == '__main__':
    cleankorean("korean.txt")