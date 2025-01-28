que = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

if que == "42":
    print("yes")

elif que == "forty two":
    print("yes")

elif que == "forty-two":
    print("yes")

else:
    print("NO")

