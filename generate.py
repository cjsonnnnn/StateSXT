import os

def create_directory_structure():
    main_directory = os.getcwd()  # Get the current working directory

    # Create a folder in the main directory
    folder_name = "example_folder"
    folder_path = os.path.join(main_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Create some files in the folder
    for i in range(1, 4):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as file:
            file.write(f"This is file {i}")

    print(f"Directory structure created in: {main_directory}/{folder_name}")
