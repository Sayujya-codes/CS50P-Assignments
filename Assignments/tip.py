def main():
    total = int(input("What's the total bill? "))
    percentage = int(input("Tip percentage? "))

    tip = (percentage / 100 ) * total
    print(f"${tip:.2f}")

main()

