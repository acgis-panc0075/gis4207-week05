import os
import arcpy
from arcpy import env

script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)
env.workspace = "../../../../data/sanfrancisco"
featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
    print (fc)

