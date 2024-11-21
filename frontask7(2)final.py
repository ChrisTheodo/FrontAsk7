#######################################################
greekAlphabet = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

def encrypt(text, key):
    i = 0
    text = list(text)
    for u in text: 
        text[i] = greekAlphabet[(greekAlphabet.index(u) + int(key)) % 24]
        i = i+1
    return text 

def decrypt(text, key):
    i = 0
    text = list(text)
    for u in text:
        text[i] = greekAlphabet[(greekAlphabet.index(u) - int(key)) % 24]
        i = i+1
    return text 

print("What do u want to do?")
userInput = input(">>")
text = input("text: ")
key = input("key: ")
errorMsg = "TEXT ONLY IN CAPITAL GREEK LETTERS\nencrypt [text] [key]\ndecrypt [text] [key]"

if userInput == "encrypt":
    try: print(encrypt(text, key))
    except: print(errorMsg)
elif userInput == "decrypt":
    try: print(decrypt(text, key))
    except: print(errorMsg)
else: print(errorMsg)
    
