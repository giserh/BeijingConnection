# coding:utf-8
# version:python2.7
# Author:Yuhao Kang
# 
# Create random points
# Parameters: output file path, output shp name, input shp name, points count
# eg. BeijingConnection, OutputPt, 1WGS84transfer.shp,20
# 
# First, input parameters. Then create several random points on the map.
# After that, compute latitude and longitude of each point.
# Join points with polygons so that it can be known what region of the point belongs to.
# Finally, export latitude and longitude to json data.

# import arcpy
import os
from arcpy import env

file_output_path=arcpy.GetParameterAsText(0)
shp_output_pt=arcpy.GetParameterAsText(1)
shp_input_polygon=arcpy.GetParameterAsText(2)
pts_count=arcpy.GetParameterAsText(3)
# Create random points
arcpy.CreateRandomPoints_management(file_output_path,shp_output_pt,shp_input_polygon,"",int(pts_count),"","POINT","")
# Add field of latitude and longitude
env.workspace=file_output_path
arcpy.AddXY_management(shp_output_pt+".shp")
# Spatial join of points and polygons
target_features=shp_output_pt+".shp"
join_features=shp_input_polygon
output_class=str(file_output_path)+"\\"+str(shp_output_pt)+"Trans.shp"
arcpy.SpatialJoin_analysis(target_features,join_features,output_class)
# Export latitude and longitude to json
# arcpy.FeaturesToJSON_conversion(output_class,shp_output_pt+".json","FORMATTED")
# Export latitude and longitude to excel
arcpy.TableToExcel_conversion(output_class,shp_output_pt+".xls")
