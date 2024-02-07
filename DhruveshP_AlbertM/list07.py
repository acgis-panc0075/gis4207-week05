import os
import sys
import arcpy

def list_all_feature_classes(root_folder):

    if not root_folder:
        print("Usage: list_feature_classes.py <root_folder>")
        sys.exit()


    if not os.path.exists(root_folder):
        print(f"Error: Root folder '{root_folder}' does not exist.")
        sys.exit()

    print(f"List of feature classes in {root_folder} and its subfolders:")
    
    for folder_path, _, _ in os.walk(root_folder):

        abs_folder_path = os.path.abspath(folder_path)

        arcpy.env.workspace = abs_folder_path

        workspaces = arcpy.ListWorkspaces("*", "All")

        if workspaces:
            for workspace in workspaces:

                abs_workspace_path = os.path.abspath(workspace)
                print(f"Workspace: {abs_workspace_path}")

                feature_classes = arcpy.ListFeatureClasses()
                
                if feature_classes:
                    for feature_class in feature_classes:
                        abs_feature_class_path = os.path.abspath(os.path.join(abs_workspace_path, feature_class))
                        print(f"  {abs_feature_class_path}")
                else:
                    print("  No feature classes found in this workspace.")
        else:
            print(f"No workspaces found in {abs_folder_path}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: list_feature_classes.py <root_folder>")
        sys.exit()

    root_folder_path = sys.argv[1]

    list_all_feature_classes(root_folder_path)
