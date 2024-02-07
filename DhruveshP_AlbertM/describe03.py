import arcpy
import sys
import os

def describe_feature_class(feature_class):
    if arcpy.Exists(feature_class):
        desc = arcpy.da.Describe(feature_class)

        base_name = os.path.basename(feature_class)
        catalog_path = desc['catalogPath']
        data_type = desc['dataType']

        print(f'{"BaseName":13} : {base_name}')
        print(f'{"CatalogPath":13} : {catalog_path}')
        print(f'{"DataType":13} : {data_type}')
    else:
        print(f"Feature class '{feature_class}' does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: describe03.py <FeatureClassName>")
    else:

        feature_class_path = sys.argv[1]

        describe_feature_class(feature_class_path)