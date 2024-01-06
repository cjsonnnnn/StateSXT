from statesxt.generate import create_directory_structure
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate Directories")
    parser.add_argument('gen', help="Generate Directories")

    args = parser.parse_args()
    print(f"\n\nargs: {args}")
    print(f"args.generate: {args.gen}\n\n")
    if args.gen:
        create_directory_structure()


if __name__ == '__main__':
    main()