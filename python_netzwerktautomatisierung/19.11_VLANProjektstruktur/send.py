# Modul „send“ (send.py)# Funktion

def sendCommands(commandList, filename="Commands.txt"):
    with open(filename,"w") as file: 
        for command in commandList:
            file.write(command + "\n")
            print(command) #trotz file eine consolenausgabe
    return len(commandList)

