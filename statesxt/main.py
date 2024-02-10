import argparse
import warnings
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
            ".gitignore",
            "execute_json.py",
            "last_run_data.json",
            "pyproject.toml",
            "pytest.ini",
            "README.md",
        ]
        self.scriptdir = os.path.dirname(os.path.realpath(__file__))
        self.maindir = os.getcwd()  # Get the current working directory
        self.ansi = {
            "warn": "\u001b[33m",
            "success": "\u001b[32m",
            "bold": "\033[1m",
            "underline": "\033[4m",
            "reset": "\033[0m",
        }

    def generate(self):
        rate = 0
        for p in self.tree:
            sourcepath = os.path.join(self.scriptdir, p)
            destpath = os.path.join(self.maindir, p)

            if any(res := [os.path.isdir(destpath), os.path.isfile(destpath)]):
                if res[0]:
                    message = "Folder"
                elif res[1]:
                    message = "File"
                warnings.warn(
                    f"{self.ansi['warn']}{message} already exist: {self.ansi['bold']}/{p}{self.ansi['reset']}",
                    UserWarning,
                    stacklevel=2,
                )
            elif os.path.isdir(sourcepath):
                shutil.copytree(sourcepath, destpath)
                rate += 1
            elif os.path.isfile(sourcepath):
                shutil.copy2(sourcepath, destpath)
                rate += 1
            else:
                warnings.warn(
                    f"{self.ansi['warn']}Path does not exist: {self.ansi['bold']}/{p}{self.ansi['reset']}",
                    UserWarning,
                    stacklevel=2,
                )

        if rate == len(self.tree):
            print(f"\n{self.ansi['success']}All templates created in: {self.ansi['bold']}{self.maindir}{self.ansi['reset']}\n")
        elif rate > 1:
            print(
                f"\n{self.ansi['success']}{rate} template/-s created in: {self.ansi['bold']}{self.maindir}{self.ansi['warn']}, but {len(self.tree)-rate} failed.{self.ansi['reset']}\n"
            )
        else:
            print(f"\n{self.ansi['warn']}All templates failed to create in: {self.ansi['bold']}{self.maindir}{self.ansi['reset']}\n")

    def remove(self):
        rate = 0
        for p in self.tree:
            sourcepath = os.path.join(self.maindir, p)
            if os.path.isdir(sourcepath):
                shutil.rmtree(sourcepath)
                rate += 1
            elif os.path.isfile(sourcepath):
                os.remove(sourcepath)
                rate += 1
            else:
                warnings.warn(
                    f"{self.ansi['warn']}Path does not exist: {self.ansi['bold']}/{p}{self.ansi['reset']}",
                    UserWarning,
                    stacklevel=2,
                )

        if rate == len(self.tree):
            print(f"\n{self.ansi['success']}All templates removed from: {self.ansi['bold']}{self.maindir}{self.ansi['reset']}\n")
        elif rate > 1:
            print(
                f"\n{self.ansi['success']}{rate} template/-s removed from: {self.ansi['bold']}{self.maindir}{self.ansi['warn']}, but {len(self.tree)-rate} failed.{self.ansi['reset']}\n"
            )
        else:
            print(f"\n{self.ansi['warn']}All templates failed to remove from: {self.ansi['bold']}{self.maindir}{self.ansi['reset']}\n")

    def cli(self):
        parser = argparse.ArgumentParser(description="Generate Directories")
        parser.add_argument("opt", help="Generate Directories")

        args = parser.parse_args()

        if str(args.opt).lower() == "gen":
            self.generate()
        elif str(args.opt).lower() == "rem":
            self.remove()
        else:
            print("statesxt does not has such command.")


def main():
    StateSXT().cli()


if __name__ == "__main__":
    main()
