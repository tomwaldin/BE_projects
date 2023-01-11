"""Program to plot risk assessment data from a csv file"""
# use directory cd "Desktop\Uni\2nd Pro\375\Assignment_1"

# import packages
import numpy as np
import matplotlib.pyplot as plt

# import data
data = np.genfromtxt('Risk_data.csv', delimiter=',')
data_cropped = data[1:,1:]
bridges = data_cropped[:,0]
pipes = data_cropped[:,1]
roads = data_cropped[:,2]
census = data_cropped[:,3]
#data clipped in 0.1m increments


# sea level rise data (produced by model equations with R^2 =< 0.9975)
xs = np.arange(0, 1.8, 0.1)
#xs = np.arange(0, 0.5, 0.1)
RCP_2_mean = 171.5*xs+2009.7
RCP_2_upper = 128.43*xs+2009.5
RCP_2_lower = 257.84*xs+2010
RCP_8_mean = -59.314*xs**2+168.47*xs+2009
RCP_8_upper = -33.693*xs**2+126.9*xs+2008.9
RCP_8_lower = 130.3*xs**2+250.06*xs+2009.2
RCP_2_upper_95 = -305.25*xs + 2010.5
RCP_2_lower_95 = 67.804*xs+2009.3

RCP_8_upper_95 = -163.9*xs**2-287.64*xs+2015.6
RCP_8_lower_95 = -9.5449*xs**2+67.509*xs+2008.9

z_score_33 = 0.43 

SD_RCP_2 = (RCP_2_upper - RCP_2_mean) / z_score_33
SD_RCP_8 = (RCP_8_upper - RCP_8_mean) / z_score_33


def construct_uncertainties(other, std, slr = projection):
    """takes variables of ### and returns ###"""
    RCP_2_array = []

    for i, std in SD_RCP_2:
        random_exposures = []
        for j in range(1000):
            random_pt = np.random.normal(RCP_2_mean[i], std) * 100
            exposure = np.interp(random_pt, np.arange(0, 310, 10), other)
            random_exposures.append(exposure)
        mean = np.mean(random_exposures)
        upper = np.percentile(random_exposures, 83)
        lower = np.percentile(random_exposures, 17)
        intermediate = [round(mean, 3), round(upper, 3), round(lower, 3)]
        RCP_2_array.append(intermediate)
    print(RCP_2_array)

z_score_95 = 1.96

#RCP_2_upper_95 = SD_RCP_2 * z_score_95 + RCP_2_mean
#RCP_2_lower_95 = -1 * SD_RCP_2 * z_score_95 + RCP_2_mean

#RCP_8_upper_95 = SD_RCP_8 * z_score_95 + RCP_8_mean
#RCP_8_lower_95 = -1 * SD_RCP_8 * z_score_95 + RCP_8_mean



#print(RCP_2_upper_95)
#print(RCP_2_upper)
print(RCP_2_mean)
#print(RCP_2_lower)
#print(RCP_2_lower_95)


# plot bridges
plt.figure(1)
axes = plt.axes()
axes.plot(RCP_2_mean, bridges[:len(xs)], label='RCP2', color='b')
axes.plot(RCP_2_upper_95, bridges[:len(xs)], label='likely range (+/-95%)', color='g', linewidth=1, linestyle='--')
axes.plot(RCP_2_lower_95, bridges[:len(xs)], color='b', linewidth=1, linestyle='--')
axes.plot(RCP_8_mean, bridges[:len(xs)], label='RCP8', color='r')
axes.plot(RCP_8_upper_95, bridges[:len(xs)], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(RCP_8_lower_95, bridges[:len(xs)], color='r', linewidth=1, linestyle='--')
plt.xlim(2020, 2120)
axes.set_title("Risk assement of bridges in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Number of bridges affected")
axes.grid(True)
axes.legend()
plt.show()

# plot pipes
plt.figure(2)
axes = plt.axes()
axes.plot(RCP_2_mean, pipes[:len(xs)], label='RCP2', color='b')
axes.plot(RCP_2_upper_95, pipes[:len(xs)], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(RCP_2_lower_95, pipes[:len(xs)], color='b', linewidth=1, linestyle='--')
axes.plot(RCP_8_mean, pipes[:len(xs)], label='RCP8', color='r')
axes.plot(RCP_8_upper_95, pipes[:len(xs)], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(RCP_8_lower_95, pipes[:len(xs)], color='r', linewidth=1, linestyle='--')
plt.xlim(2020, 2120)
axes.set_title("Risk assement of pipes in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Length of pipes affected (m)")
axes.grid(True)
axes.legend()
plt.show()

# plot roads
plt.figure(3)
axes = plt.axes()
axes.plot(RCP_2_mean, roads[:len(xs)], label='RCP2', color='b')
axes.plot(RCP_2_upper_95, roads[:len(xs)], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(RCP_2_lower_95, roads[:len(xs)], color='b', linewidth=1, linestyle='--')
axes.plot(RCP_8_mean, roads[:len(xs)], label='RCP8', color='r')
axes.plot(RCP_8_upper_95, roads[:len(xs)], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(RCP_8_lower_95, roads[:len(xs)], color='r', linewidth=1, linestyle='--')
#plt.xlim(2020, 2120)
axes.set_title("Risk assement of roads in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Length of roads affected (m)")
axes.grid(True)
axes.legend()
plt.show()

# plot census
plt.figure(4)
axes = plt.axes()
axes.plot(RCP_2_mean, census[:len(xs)], label='RCP2', color='b')
axes.plot(RCP_2_upper_95, census[:len(xs)], label='likely range (+/-95%)', color='b', linewidth=1, linestyle='--')
axes.plot(RCP_2_lower_95, census[:len(xs)], color='b', linewidth=1, linestyle='--')
axes.plot(RCP_8_mean, census[:len(xs)], label='RCP8', color='r')
axes.plot(RCP_8_upper_95, census[:len(xs)], label='likely range (+/-95%)', color='r', linewidth=1, linestyle='--')
axes.plot(RCP_8_lower_95, census[:len(xs)], color='r', linewidth=1, linestyle='--')
plt.xlim(2020, 2120)
axes.set_title("Risk assement of population in Christchurch")
axes.set_xlabel("Year")
axes.set_ylabel("Number of people affected")
axes.grid(True)
axes.legend()
plt.show()