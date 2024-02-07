import sys
import importlib

def list_feature_classes(workspace):
    try:
        arcpy = importlib.import_module('arcpy')
    except ImportError:
        print("ArcPy is not available.")
        sys.exit()

    if not arcpy.Exists(workspace):
        print(f"Error: Workspace '{workspace}' does not exist.")
        sys.exit()

    arcpy.env.workspace = workspace

    feature_classes = arcpy.ListFeatureClasses()

    for feature_class in feature_classes:
        print(feature_class)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: list_feature_classes.py <WorkspacePath>")
        sys.exit()

    workspace_path = sys.argv[1]

    list_feature_classes(workspace_path)
