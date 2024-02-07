import arcpy

input_file = r'..\..\..\data\Canada\province.shp'

desc = arcpy.Describe(input_file)

print(f'{"BaseName":13} : {desc.baseName}')
print(f'{"CatalogPath":13} : {desc.catalogPath}')
print(f'{"DataType":13} : {desc.dataType}')