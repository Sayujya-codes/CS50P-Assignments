import string

#took help to remove puncations from the string
#source: geekforgeeks

great = input("What's the Greating? ").lower().strip().translate(str.maketrans('', '', string.punctuation))

splitted = great.split()

if splitted[0] == "hello":
    print("$0")

elif great[0] == "h":
    print("$20")

else:
    print("$100")
