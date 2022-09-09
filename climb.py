# numpy and matplotlib imported, seed set.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# initialize and populate all_walks
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
        
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
# np_aw = np.array(all_walks)

# Plot all walks
np_aw_t = np.transpose(np.array(all_walks))
# plt.plot(np_aw_t)
# plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# calculate odds of reaching 60
print(np.mean(ends>=60))