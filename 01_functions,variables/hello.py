def main():
    # Output using our own function
    name = input("Enter your name: ").strip().title()
    
    # Call the function
    if name:
        hello(name)
    else:
        hello()

# Define the function
def hello(to="World"):
    print(f"Hello, {to}!")
    
# Call the main function  
if __name__ == "__main__":
    main()