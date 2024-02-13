import os
import sys

def list_feature_classes(root_folder, datatype, out_file_name):
    try:
        import arcpy
    except ImportError:
        print("Error: arcpy module not available.")
        return

    arcpy.env.workspace = root_folder

    feature_classes = []
    for dirpath, dirnames, filenames in arcpy.da.Walk(root_folder, datatype=datatype):
        for filename in filenames:
            feature_classes.append(os.path.join(dirpath, filename))

    with open(out_file_name, 'w') as out_file:
        out_file.write(f"{datatype} feature classes in and below {root_folder}:\n")
        for feature_class in feature_classes:
            out_file.write(f"{feature_class}\n")

if __name__ == "_main_":

    if len(sys.argv) != 4:
        print("Usage: list_feature_classes.py <root_folder> <Point|Polyline|Polygon> <out_file_name>")
        sys.exit()

    root_folder_path = sys.argv[1]
    datatype = sys.argv[2]
    out_file_name = sys.argv[3]

    if not os.path.exists(root_folder_path) or datatype not in ['Point', 'Polyline', 'Polygon']:
        print("Error: Invalid root_folder or datatype.")
        sys.exit()


        list_feature_classes(root_folder_path, datatype,out_file_name)


