import arcpy
import os
import sys

def list_feature_classes(workspace, feature_type):

    if not arcpy.Exists(workspace):
        print(f"Error: Workspace '{workspace}' does not exist.")
        sys.exit()

    valid_feature_types = ['Point', 'Line', 'Polygon']
    if feature_type not in valid_feature_types:
        print(f"Error: Invalid FeatureType. Allowed values are {', '.join(valid_feature_types)}.")
        sys.exit()

    arcpy.env.workspace = workspace
    feature_classes = arcpy.ListFeatureClasses(feature_type=feature_type)

    if not feature_classes:
        print(f"No {feature_type} feature classes found in {workspace}.")
    else:
        print(f"List of {feature_type} feature classes in {workspace}:")
        for fc in feature_classes:
            print(fc)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: list03.py <Workspace> <FeatureType>")
        sys.exit()

    workspace_path = sys.argv[1]
    feature_type_arg = sys.argv[2]

    list_feature_classes(workspace_path, feature_type_arg)