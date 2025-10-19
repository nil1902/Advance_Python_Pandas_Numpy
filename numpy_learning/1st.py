temparature =[32.5, 45.0, 50.5, 60.0, 72.5, 80.0, 85.5, 90.0, 95.5, 100.0]
humidity =[30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
total_temp=0
for i in  temparature:
    total_temp+=i
average_temp=total_temp/len(temparature)
print("Total Temperature:", total_temp)
print("Average Temperature:", average_temp)
total_humidity=0
for h in humidity:
    total_humidity+=h
average_humidity=total_humidity/len(humidity)
print("Average Humidity:", average_humidity)


# loops are vey much slow for larger dataset value , thats why numpy came in the market

import numpy as np
temparature_np = np.array(temparature)
humidity_np = np.array(humidity)
total_temp_np = np.sum(temparature_np)
average_temp_np = np.mean(temparature_np)
print("Total Temperature using Numpy:", total_temp_np)
print("Average Temperature using Numpy:", average_temp_np)

# numpy is faster than loops for larger dataset without usung loops, special functions are there in numpy to perform operations on entire array
# 50 times faster than loops and less memory consumption and easy math operations 