import random

def main():
    with open("Happy.TXT") as f:
        gdWrds = f.read().splitlines()

    print(end="God says... ")

    for x in range(0, 30):
        wrds = random.choice(gdWrds)
        print(wrds, end=" ")

    wrds = random.choice(gdWrds)
    print(wrds + ".\n")

main()
