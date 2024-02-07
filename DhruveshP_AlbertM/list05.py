import os
import sys

def list_folders(root_folder):

    if not root_folder:
        print("Usage: list05.py <root_folder>")
        sys.exit()

 
    if not os.path.exists(root_folder):
        print(f"Error: Root folder '{root_folder}' does not exist.")
        sys.exit()

    print(f"List of folders in {root_folder} and its subfolders:")
    for folder_path, _, _ in os.walk(root_folder):
        print(folder_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: list05.py <root_folder>")
        sys.exit()

    root_folder_path = sys.argv[1]

    list_folders(root_folder_path)
