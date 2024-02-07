import importlib
import sys
import os

def list_workspaces(root_folder):

    if 'arcpy' not in sys.modules:
        arcpy = importlib.import_module("arcpy")
    else:
        import arcpy


    if not arcpy.Exists(root_folder):
        print(f"Error: Root folder '{root_folder}' does not exist.")
        sys.exit()

    arcpy.env.workspace = root_folder
    workspaces = arcpy.ListWorkspaces("*", "Folder")

    if not workspaces:
        print(f"No workspaces found in {root_folder}.")
    else:
        print(f"List of workspaces in {root_folder}:")
        for workspace in workspaces:
            print(workspace)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: list_workspaces.py <RootFolder>")
        sys.exit()

    root_folder_path = sys.argv[1]


    list_workspaces(root_folder_path)