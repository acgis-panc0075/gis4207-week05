import sys
import arcpy
import os

def describe_feature_class(feature_class):

    if not arcpy.Exists(feature_class):
        print(f"{feature_class} does not exist.")
        sys.exit()

    desc = arcpy.da.Describe(feature_class)
    base_name = os.path.basename(feature_class)
    catalog_path = desc['catalogPath']
    data_type = desc['dataType']

    print(f'{desc["baseName"].ljust(15)}: {base_name}')
    print(f'{desc["catalogPath"].ljust(15)}: {catalog_path}')
    print(f'{desc["dataType"].ljust(15)}: {data_type}')


    print("\nField Report:")
    print(f'{"Field Name".ljust(15)}{"Field Type".ljust(15)}{"Length".rjust(9)}')
    print('-' * 15 + ' ' + '-' * 15 + ' ' + '-' * 9)

    for field in desc["fields"]:
        field_name = field.name.ljust(15)
        field_type = field.type.ljust(15)
        field_length = str(field.length).rjust(9)
        print(f'{field_name}{field_type}{field_length}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: describe06.py <FeatureClassName>")
        sys.exit()

    feature_class_path = sys.argv[1]

    describe_feature_class(feature_class_path)