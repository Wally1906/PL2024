import re 
import sys

def main(args):
    with open(args,"r") as ficheiro:
        counter = 0
        state = False
        file = ficheiro.read()
        capture = re.findall(r'(on|off|=|\d+)', file, re.IGNORECASE)
        for elem in capture:
            if elem.isnumeric() and state == True:
                counter += int(elem)
            elif elem.lower() == "on":
                state = True 
            elif elem.lower() == "off":
                state = False
            else:
                print("Total: " + str(counter))        
                
if __name__ == "__main__":
    main(sys.argv[1])