import argparse
import warnings
import shutil
import os


class StateSXT:
    def __init__(self) -> None:
        self.tree = [
            ".github",
            "base",
            "database",
            "testcases",
            "utils",
            ".env-template",
            ".gitignore",
            "execute_json.py",
            "track.json",
            "pyproject.toml",
            "pytest.ini",
            "README.md",
            "tox.ini",
        ]
        self.scriptdir = os.path.dirname(os.path.realpath(__file__))
        self.maindir = os.getcwd()  # Get the current working directory
        self.ansi = {
            "error": "\033[91m\033[1m",
            "info": "\033[94m",
            "success": "\u001b[32m",
            "warn": "\u001b[33m",
            "bold": "\033[1m",
            "reset": "\033[0m",
            "underline": "\033[4m",
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
                    f"{self.ansi['warn']}{message} already exist: /{p}{self.ansi['reset']}",
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
                    f"{self.ansi['warn']}Path does not exist: /{p}{self.ansi['reset']}",
                    UserWarning,
                    stacklevel=2,
                )

        if rate == len(self.tree):
            print(f"\n{self.ansi['success']}All templates created in {self.maindir}{self.ansi['reset']}")
        elif rate > 1:
            print(
                f"\n{self.ansi['success']}{rate} template/-s created in {self.maindir}{self.ansi['warn']}, but {len(self.tree)-rate} failed.{self.ansi['reset']}"
            )
        else:
            print(f"\n{self.ansi['error']}All templates failed to create in {self.maindir}{self.ansi['reset']}")

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
                    f"{self.ansi['warn']}Path /{p} does not exist{self.ansi['reset']}",
                    UserWarning,
                    stacklevel=2,
                )

        if rate == len(self.tree):
            print(f"\n{self.ansi['success']}All templates removed from {self.maindir}{self.ansi['reset']}")
        elif rate > 1:
            print(
                f"\n{self.ansi['success']}{rate} template/-s removed from {self.maindir}{self.ansi['warn']}, but {len(self.tree)-rate} failed.{self.ansi['reset']}"
            )
        else:
            print(f"\n{self.ansi['error']}All templates failed to remove from {self.maindir}{self.ansi['reset']}")

    def page(self, page_name: str):
        # check if the parent folder exists
        parent_folder = "testcases"
        if os.path.exists(os.path.join(self.maindir, parent_folder)):
            # check if a folder with name as the inputted page name does not exist
            page_name_path = page_name.lower().strip().replace(' ', '_')
            if not os.path.exists(os.path.join(self.maindir, f"{parent_folder}\{page_name_path}")):
                # Get the path to the template folder
                template_folder = os.path.join(self.scriptdir, "template")

                # Define the destination folder based on the page name
                destpath = os.path.join(self.maindir, f"{parent_folder}\{page_name_path}")

                # Copy the template folder to the destination
                shutil.copytree(template_folder, destpath)

                # Rename files inside the copied folder and modify their content
                for root, dirs, files in os.walk(destpath):
                    if "__pycache__" in root:
                        continue  # Skip processing the __pycache__ folder and its contents

                    for name in files:
                        # Get the full path of the file
                        file_path = os.path.join(root, name)
                        # Read the content of the file
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        # Replace 'example' with the page name in lowercase
                        content = content.replace("example", page_name.lower().replace(" ", "_"))
                        # Replace 'Example' with the page name in title case
                        content = content.replace("Example", page_name.title().replace(" ", ""))
                        # Write the modified content back to the file
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(content)

                print(f"\n{self.ansi['success']}New page template created in {self.maindir}{self.ansi['reset']}")
            else:
                print(f"\n{self.ansi['error']}A page folder with name {page_name_path} already exist{self.ansi['reset']}")
        else:
            print(f"\n{self.ansi['error']}StateSXT could not find a /{parent_folder} folder in {self.maindir}{self.ansi['reset']}")

    def cli(self):
        parser = argparse.ArgumentParser(description="Generate Directories")
        parser.add_argument("opt", help="Action to perform: 'gen' for generating, 'rem' for removing, 'page' to generate a page template", choices=["gen", "rem", "create-page"])
        parser.add_argument("--version", "-v", action="version", version="StateSXT 0.3.9")
        args = parser.parse_args()

        if str(args.opt).lower() == "gen":
            self.generate()
        elif str(args.opt).lower() == "rem":
            self.remove()
        elif str(args.opt).lower() == "create-page":
            page_name = "example"
            page_name = str(input(f"\U0001F4D3 {self.ansi['info']}Page name [{self.ansi['success']}{page_name}{self.ansi['info']}]: {self.ansi['reset']}"))
            self.page(page_name)
        else:
            print("statesxt does not has such command.")


def main():
    StateSXT().cli()


if __name__ == "__main__":
    main()
