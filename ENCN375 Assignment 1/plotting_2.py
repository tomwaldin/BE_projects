"""Program to plot risk assessment data from a csv file"""
# use directory cd "Desktop\Uni\2nd Pro\375\Assignment_1"

# import packages
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

# import data
data = np.genfromtxt('Risk_data.csv', delimiter=',')
data_cropped = data[1:,1:]
bridges = data_cropped[:,0]
pipes = data_cropped[:,1]
roads = data_cropped[:,2]
census = data_cropped[:,3]
#data clipped in 0.1m increments

# sea level rise data
data_slr = np.genfromtxt('slr_projection.csv', delimiter=',')
years = data_slr[2:,0]
rcp2_mean = data_slr[2:,1]
rcp2_upper = data_slr[2:,2]
rcp2_lower = data_slr[2:,3]
rcp8_mean = data_slr[2:,4]
rcp8_upper = data_slr[2:,5]
rcp8_lower = data_slr[2:,6]

std2_list = []
std8_list = []
for i in range(11):
    std2 = (rcp2_upper[i] - rcp2_mean[i]) / 1.96
    std8 = (rcp8_upper[i] - rcp8_mean[i]) / 1.96
    std2_list.append(std2)
    std8_list.append(std8)
stds = std2_list, std8_list

def construct_uncertainties(variable, stds, data_slr):
    """Contructs uncertainty"""
    
    rcp2_std, rcp8_std = stds
    rcp2_mean = data_slr[2:,1]
    rcp8_mean = data_slr[2:,4]
    
    rcp2_array = []
    for i, std in enumerate(rcp2_std):
        population = []
        for j in range(1000):
            random_point = np.random.normal(rcp2_mean[i], std) * 100
            value = np.interp(random_point, np.arange(0, 300, 10), variable)
            population.append(value)
        mean = np.mean(population)
        upper = np.percentile(population, 95)
        lower = np.percentile(population, 5)
        array_row = [round(mean, 3), round(upper, 3), round(lower, 3)]
        rcp2_array.append(array_row)

    rcp8_array = []
    for i, std in enumerate(rcp8_std):
        population = []
        for j in range(1000):
            random_point = np.random.normal(rcp8_mean[i], std) * 100
            value = np.interp(random_point, np.arange(0, 300, 10), variable)
            population.append(value)
        mean = np.mean(population)
        upper = np.percentile(population, 95)
        lower = np.percentile(population, 5)
        array_row = [round(mean, 3), round(upper, 3), round(lower, 3)]
        rcp8_array.append(array_row)
    return rcp2_array, rcp8_array

bridges_array = np.array(construct_uncertainties(bridges, stds, data_slr))
pipes_array = np.array(construct_uncertainties(pipes, stds, data_slr))
roads_array = np.array(construct_uncertainties(roads, stds, data_slr))
people_array = np.array(construct_uncertainties(census, stds, data_slr))

# plot bridges
plt.figure(1)
axes = plt.axes()
axes.plot(years, bridges_array[0][:, 0], label='RCP2', color='b')
axes.plot(years, bridges_array[0][:, 1], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, bridges_array[0][:, 2], color='b', linewidth=1, linestyle='--')
axes.plot(years, bridges_array[1][:, 0], label='RCP8', color='r')
axes.plot(years, bridges_array[1][:, 1], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, bridges_array[1][:, 2], color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of bridges in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Number of bridges affected")
axes.grid(True)
axes.legend()
plt.show()

# plot pipes
plt.figure(2)
axes = plt.axes()
axes.plot(years, pipes_array[0][:, 0], label='RCP2', color='b')
axes.plot(years, pipes_array[0][:, 1], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, pipes_array[0][:, 2], color='b', linewidth=1, linestyle='--')
axes.plot(years, pipes_array[1][:, 0], label='RCP8', color='r')
axes.plot(years, pipes_array[1][:, 1], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, pipes_array[1][:, 2], color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of pipes in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Length of pipes affected (m)")
axes.grid(True)
axes.legend()
plt.show()

# plot roads
plt.figure(3)
axes = plt.axes()
axes.plot(years, roads_array[0][:, 0], label='RCP2', color='b')
axes.plot(years, roads_array[0][:, 1], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, roads_array[0][:, 2], color='b', linewidth=1, linestyle='--')
axes.plot(years, roads_array[1][:, 0], label='RCP8', color='r')
axes.plot(years, roads_array[1][:, 1], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, roads_array[1][:, 2], color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of roads in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Length of roads affected (m)")
axes.grid(True)
axes.legend()
plt.show()

# plot census
plt.figure(4)
axes = plt.axes()
axes.plot(years, people_array[0][:, 0], label='RCP2', color='b')
axes.plot(years, people_array[0][:, 1], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, people_array[0][:, 2], color='b', linewidth=1, linestyle='--')
axes.plot(years, people_array[1][:, 0], label='RCP8', color='r')
axes.plot(years, people_array[1][:, 1], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, people_array[1][:, 2], color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of population in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Number of people affected")
axes.grid(True)
axes.legend()
plt.show()

# import gpd data for percentage calculations
bridgesraw = gpd.read_file('data/infrastructure/bridges.shp')
pipesraw = gpd.read_file('data/infrastructure/potablewater_pipe.shp')
roadsraw = gpd.read_file('data/infrastructure/street_centre_line.shp')
censusraw = gpd.read_file('data/socioeconomic/2018-census-christchurch.shp')

# plot bridges as %
plt.figure(1)
axes = plt.axes()
axes.plot(years, bridges_array[0][:, 0] * 100 / len(bridgesraw), label='RCP2', color='b')
axes.plot(years, bridges_array[0][:, 1] * 100 / len(bridgesraw), label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, bridges_array[0][:, 2] * 100 / len(bridgesraw), color='b', linewidth=1, linestyle='--')
axes.plot(years, bridges_array[1][:, 0] * 100 / len(bridgesraw), label='RCP8', color='r')
axes.plot(years, bridges_array[1][:, 1] * 100 / len(bridgesraw), label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, bridges_array[1][:, 2] * 100 / len(bridgesraw), color='r', linewidth=1, linestyle='--')
axes.set_title("Percentage of bridges in Christchurch exposed")
axes.set_xlabel("Year")
axes.set_ylabel("Percentage of bridges affected (%)")
axes.grid(True)
axes.legend()
plt.show()

# plot pipes as %
plt.figure(2)
axes = plt.axes()
axes.plot(years, pipes_array[0][:, 0] * 100 / pipesraw.length.sum(), label='RCP2', color='b')
axes.plot(years, pipes_array[0][:, 1] * 100 / pipesraw.length.sum(), label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, pipes_array[0][:, 2] * 100 / pipesraw.length.sum(), color='b', linewidth=1, linestyle='--')
axes.plot(years, pipes_array[1][:, 0] * 100 / pipesraw.length.sum(), label='RCP8', color='r')
axes.plot(years, pipes_array[1][:, 1] * 100 / pipesraw.length.sum(), label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, pipes_array[1][:, 2] * 100 / pipesraw.length.sum(), color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of pipes in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Percentage of pipes affected (%)")
axes.grid(True)
axes.legend()
plt.show()

# plot roads as %
plt.figure(3)
axes = plt.axes()
axes.plot(years, roads_array[0][:, 0] * 100 / roadsraw.length.sum(), label='RCP2', color='b')
axes.plot(years, roads_array[0][:, 1] * 100 / roadsraw.length.sum(), label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, roads_array[0][:, 2] * 100 / roadsraw.length.sum(), color='b', linewidth=1, linestyle='--')
axes.plot(years, roads_array[1][:, 0] * 100 / roadsraw.length.sum(), label='RCP8', color='r')
axes.plot(years, roads_array[1][:, 1] * 100 / roadsraw.length.sum(), label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, roads_array[1][:, 2] * 100 / roadsraw.length.sum(), color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of roads in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Percentage of roads affected (%)")
axes.grid(True)
axes.legend()
plt.show()

# plot census as %
plt.figure(4)
axes = plt.axes()
axes.plot(years, people_array[0][:, 0] * 100 / censusraw['C18_CURPop'].sum(), label='RCP2', color='b')
axes.plot(years, people_array[0][:, 1] * 100 / censusraw['C18_CURPop'].sum(), label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(years, people_array[0][:, 2] * 100 / censusraw['C18_CURPop'].sum(), color='b', linewidth=1, linestyle='--')
axes.plot(years, people_array[1][:, 0] * 100 / censusraw['C18_CURPop'].sum(), label='RCP8', color='r')
axes.plot(years, people_array[1][:, 1] * 100 / censusraw['C18_CURPop'].sum(), label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(years, people_array[1][:, 2] * 100 / censusraw['C18_CURPop'].sum(), color='r', linewidth=1, linestyle='--')
axes.set_title("Risk assement of population in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Percentage of people affected (%)")
axes.grid(True)
axes.legend()
plt.show()