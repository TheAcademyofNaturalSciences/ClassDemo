from rasterstats import zonal_stats
import csv
import os

# Store the name of the shapefiles in a variable
## Must update working dir
path = "C:/Users/msc94/Documents/GitHub/ClassDemo/DemoData"

os.chdir(path)

loc_catch = path + "/DemoData/local_catchment.shp"
landcover = path + "/DemoData/nlcd_clip.tif"
watershed = path + "/DemoData/watersheds.shp"

# Create catagory maps for the output data (type: dictionary)

cmap_lu = {11: 'Open Water'
    , 21: 'Developed Open Space'
    , 22: 'Developed Low Intensity'
    , 23: 'Developed Medium Intensity'
    , 24: 'Developed High Intensity'
    , 31: 'Barren Land'
    , 41: 'Deciduous Forest'
    , 42: 'Evergreen Forest'
    , 43: 'Mixed Forest'
    , 52: 'Shrub/Scrub'
    , 71: 'Grassland/Herbaceous'
    , 81: 'Pasture/Hay'
    , 82: 'Cultivated Crops'
    , 90: 'Woody Wetlands'
    , 95: 'Emergent Herbaceous Wetlands'}

cmap_ws = (	'Still Creek'
,	'Wissahickon Creek'
,	'Stony Creek'
,	'Mill Creek North'
,	'Locust Creek'
,	'Tulpehocken Creek'
,	'Pine Creek'
,	'Saucony Creek'
,	'West Branch Schuylkill River'
,	'Mill Creek South'
,	'unamed trib of Cacoosing Creek'
,	'Trout Creek'
)

# Run the raster stats function for the local catchment

lulc_stats_c = zonal_stats(loc_catch, landcover
    ,nodata_value=-2147483647
    ,categorical=True
    ,catagory_map=cmap_lu
    )

# write the output of lulc_stats for the local catchment to a csv
carry = 0
myFile = open('local_lulc_py.csv', 'w')
myFile.writelines('{0},{1},{2},{3}{4}'.format('watershed','lu_type','lu_code','area_sqm','\n'))
for ws in lulc_stats_c:
    for key, value in ws.items():
        myFile.writelines('{0},{1},{2},{3}{4}'.format(cmap_ws[carry], cmap_lu[key], str(key), str(value * 900),'\n'))
    carry += 1
myFile.close()

# Now do the same thing with the watershed shapefile
# Run the raster stats for the watershed
lulc_stats_w = zonal_stats(watershed, landcover
    ,nodata_value=-2147483647
    ,categorical=True
    ,catagory_map=cmap_lu
    )

# write the output of lulc_stats for the watershed to a csv
carry = 0
myFile = open('watershed_lulc_py.csv', 'w')
myFile.writelines('{0},{1},{2},{3}{4}'.format('watershed','lu_type','lu_code','area_sqm','\n'))
for ws in lulc_stats_w:
    for key, value in ws.items():
        myFile.writelines('{0},{1},{2},{3}{4}'.format(cmap_ws[carry], cmap_lu[key], str(key), str(value * 900),'\n'))
    carry += 1
myFile.close()