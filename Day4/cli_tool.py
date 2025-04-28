import argparse

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple CLI greeting tool")
    parser.add_argument("name", help="Your name")  # Required argument
    args = parser.parse_args()  # Parse the arguments
    greet(args.name)