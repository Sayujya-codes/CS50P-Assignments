def main():
    n = get_name()
    convertt(n)

def get_name():
    names = input("Enter the camel case ")
    return names

def convertt(n):
    for i in n:
        print(i)

main()
