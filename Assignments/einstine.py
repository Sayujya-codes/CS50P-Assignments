def main():
    mass = int(input("What's m? "))
    e = calculate(mass)
    print(e)
def calculate(mass):
    c = 300000000
    e = mass * c**2
    return e

main()
