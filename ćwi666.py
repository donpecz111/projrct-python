import os
print("operating System:",os.name)

print("\nCurrent Working Directory:",os.getcwd())
print("\nList of files and directories on the current directory:")
print(os.listdir("."))
print("\nTest if a specified file exis or not:")
try:
    filename = "abc.txt"
    f = open(filename,'r')
    text= f.read()
    f.close()
except IOError:
    print('Not accessed or problem in reading:' +filename)