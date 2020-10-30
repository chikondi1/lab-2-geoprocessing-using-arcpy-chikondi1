#this imports the env class which will make it easier to retrieve files, also known as setting environment properties
from arcpy import env

#this sets the folder that will be used to select files from
env.workspace = "C:\Users\PhotonUser\Desktop\OneDrive\Files\Data Lab_2_Geoprocessing_Python"

#this runs the buffer tool to create a 500m buffer around facilities shapefile
arcpy.Buffer_analysis("C:/Users/PhotonUser/My Files/OneDrive/Files/Data Lab_2_Geoprocessing_Python/facilities.shp", "C:/Users/PhotonUser/My Files/OneDrive/Files/Data Lab_2_Geoprocessing_Python/Results/facilities_buffer.shp", "500 METERS", "", "", "ALL")

#assign values to the shapefile variables
in_features = "bike_routes.shp"
clip_features = "zip.shp"
out_features = "bike_Clip.shp"
xy_tolerance = ""

#run clipping tool to clip the shapefiles, which will create a suitability output
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)



