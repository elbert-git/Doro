#this file is just to create a function that will print text in with colour easily

#colour dictionary
Colours = {
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
    "reset": "\u001b[0m",
}

def CPrint(colour, text):
    print(Colours[colour] + text)
        
