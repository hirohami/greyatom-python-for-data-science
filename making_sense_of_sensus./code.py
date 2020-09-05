# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.append((data),(new_record),axis = 0)
#a = np.shape(data)
#print(a)
#b = np.shape(census)
#print(b)
age = census[:,0]

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
a = np.round(age_mean,2)
print(a)

age_std = np.std(age)
b = np.round(age_std,2)
print(b)

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_O = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

avg_pay_high = 0.43
avg_pay_low = 0.14

print(avg_pay_high)
print(avg_pay_low)


