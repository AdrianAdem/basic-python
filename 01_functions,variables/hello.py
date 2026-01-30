def main():
    name = input("What's your name? ").strip().title()
    greet(name)

def greet(to="world"):
    print(f"hello, {to}")

if __name__ == "__main__":
    main()