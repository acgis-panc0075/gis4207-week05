import os
import sys
import arcpy

def list_all_workspaces(root_folder):
    if not root_folder:
        print("Usage: list_workspaces.py <root_folder>")
        sys.exit()

    if not os.path.exists(root_folder):
        print(f"Error: Root folder '{root_folder}' does not exist.")
        sys.exit()

    print(f"List of workspaces in {root_folder} and its subfolders:")
    
    for folder_path, _, _ in os.walk(root_folder):
        abs_folder_path = os.path.abspath(folder_path)

        arcpy.env.workspace = abs_folder_path

        workspaces = arcpy.ListWorkspaces("*", "All")

        if workspaces:
            for workspace in workspaces:
                abs_workspace_path = os.path.abspath(workspace)
                print(abs_workspace_path)
        else:
            print(f"No workspaces found in {abs_folder_path}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: list_workspaces.py <root_folder>")
        sys.exit()

    root_folder_path = sys.argv[1]

    list_all_workspaces(root_folder_path)