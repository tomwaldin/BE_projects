"""Program to create risk assement data in relation to sea level rise"""
# use directory cd "Desktop\Uni\2nd Pro\375\Assignment_1"

# import packages
import geopandas as gpd
import numpy as np

# import data
bridges = gpd.read_file('data/infrastructure/bridges.shp')
pipes = gpd.read_file('data/infrastructure/potablewater_pipe.shp')
roads = gpd.read_file('data/infrastructure/street_centre_line.shp')
census = gpd.read_file('data/socioeconomic/2018-census-christchurch.shp')

# create data lists
bridges_list = []
pipes_list = []
roads_list = []
census_list = []

# import each slr file and clip with variables 
for i in np.arange(0, 300, 10):
    
    print(i)
    
    slr_file = 'data/hazards/extreme_sea_level/esl_aep1_slr{}.shp'.format(i)
    slr = gpd.read_file(slr_file) 
    
    bridges_clip = gpd.clip(bridges, slr)
    bridges_list.append(len(bridges_clip))
    
    pipes_clip = gpd.clip(pipes, slr)
    pipes_list.append(pipes_clip.length.sum())    
    
    roads_clip = gpd.clip(roads, slr)
    roads_list.append(roads_clip.length.sum())
    
    census_clip = gpd.clip(census, slr)
    census_list.append(census_clip['C18_CURPop'].sum())

# print data to the shell
print(bridges_list)
print(pipes_list)
print(roads_list)
print(census_list)

# write to csv
risk_dict = {'Bridges' : bridges_list, 'Pipes' : pipes_list, 'Roads' : roads_list, 'Population' : census_list}
risk_data = gpd.GeoDataFrame(risk_dict)
risk_data.to_csv('Risk_data.csv') 