import matplotlib.pyplot as plt
import numpy as np
import font


ncols = 5
nrows = 6

# create the plots
fig = plt.figure()
axes = [ fig.add_subplot(nrows, ncols, r * ncols + c+1) for r in range(0, nrows) for c in range(0, ncols) ]

# remove the x and y ticks
for t in range(100): 
    std = t/100
    for (ax, i) in zip(axes, range(len(axes))):
        ary = 1-font.to_bin_array(font.font[i])*1.0
        ary += np.random.normal(0, std, (7, 5)) # add noise 
        ax.imshow(ary, cmap='gray') # show picture as is 
        ax.set_xticks([])
        ax.set_yticks([])
    fig.suptitle("σ = "+str(std))
    plt.savefig("noise{}".format(t))