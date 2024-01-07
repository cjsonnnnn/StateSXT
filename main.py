import argparse

import shutil
import os


class StateSXT:
    def __init__(self) -> None:
        self.tree = [
            "base",
            "database",
            "locators",
            "pages",
            "testcases",
            "utils",
            ".env-template",
        ]
        self.scriptdir = os.path.dirname(os.path.realpath(__file__))
        self.maindir = os.getcwd()  # Get the current working directory

    def generate(self):
        # looping through the tree list
        for p in self.tree:
            sourcepath = os.path.join(self.scriptdir, p)
            destpath = os.path.join(self.maindir, p)
            if os.path.isdir(sourcepath):
                print("isdir")
                shutil.copytree(sourcepath, destpath)
            elif os.path.isfile(sourcepath):
                print("isfile")
                shutil.copy2(sourcepath, destpath)
            else:
                raise ("Invalid path!")

        print(f"Directory structure created in: {self.maindir}")

    def remove(self):
        pass

    def cli(self):
        parser = argparse.ArgumentParser(description="Generate Directories")
        parser.add_argument("opt", help="Generate Directories")

        args = parser.parse_args()
        print(f"\n\nargs: {args}")
        print(f"args.opt: {args.opt}, type: {type(args.opt)}\n\n")

        if str(args.opt).lower() == "gen":
            self.generate()
        elif str(args.opt).lower() == "rem":
            self.remove()
        else:
            print("statesxt doesn't has such command.")


if __name__ == "__main__":
    StateSXT().cli()
