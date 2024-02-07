import arcpy

input_file= r'..\..\..\data\Canada\province.shp'

desc = arcpy.Describe(input_file)

print(f"BaseName: {desc.baseName}")
print(f"CatalogPath: {desc.catalogPath}")
print(f"DataType: {desc.dataType}")