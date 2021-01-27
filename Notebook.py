import os.path
from os import path
############################################
print("")
print("          Notebook v1.5")
############################################
os.chdir("C:/")
if(path.exists("Notebook") == False):
    os.mkdir("Notebook")
############################################
def create():
    os.chdir("C:/Notebook")
    name = input("> Notebook Name = ")
    if(path.exists(name) == False):
        os.mkdir(name)
        print(">> Notebook created!")
    else:
        print(">> There is already a notebook with this name!")
############################################
def delete():
    os.chdir("C:/Notebook")
    name = input("> Notebook Name = ")
    if(path.exists(name) == True):
        os.remove(name)
        print(">> Notebook deleted!")
    else:
        print(">> No notebook with this name found!")
############################################    
def write():
    os.chdir("C:/Notebook")
    name = input("> Notebook Name = ")
    if(path.exists(name) == True):
        noteName = input("> Note Name = ")
        os.chdir("C:/Notebook/"+name)
        writeFile = open(noteName+".txt","w")
        print("")
        print(">> Notebook/"+name+"/"+noteName+" editing...")
        print("----------------------------------------------")
        content = input("> ")
        print("----------------------------------------------")
        writeFile.write(content)
        print(">> Editing successful!")
    else:
        print(">> No notebook with this name found!")
############################################
def read():
    os.chdir("C:/Notebook") 
    name = input("> Notebook Name = ")
    if(path.exists(name) == True):
        os.chdir("C:/Notebook/"+name)
        noteName = input("> Note Name = ")
        noteName = noteName+".txt"
        if(path.exists(noteName) == True):
            os.chdir("C:/Notebook/"+name)
            readFile = open(noteName)
            print("")
            print(">> Notebook/"+name+"/"+noteName+" reading...")
            print("----------------------------------------------")
            print(readFile.read())
            print("----------------------------------------------")
        else:
            print(">> No notebook with this name found!")
    else:
        print(">> No notebook with this name found!")
############################################
def show():
    print(">> .notebooks or .notes")
    option = input("> ")
    os.chdir("C:/Notebook")
    if(option == ".notebooks"):
        print(">> ",os.listdir())
    elif(option == ".notes"):
        name = input("> Notebook Name = ")
        if(path.exists(name) == True):
            os.chdir("C:/Notebook/"+name)
            print(">> ",os.listdir())
        else:
            print(">> No notebook with this name found!")
############################################
while True:
    print("")
    menu = input("> ")
    print("")
    if(menu == ".create" or menu == ".crt"):
        create()
    elif(menu == ".delete" or menu == ".dlt"):
        delete()
    elif(menu == ".write" or menu == ".wrt"):
        write()
    elif(menu == ".read"):
        read()
    elif(menu == ".show" or menu == ".shw"):
        show()
    elif(menu == ".exit" or menu == ".ex"):
        exit()
############################################