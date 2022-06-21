from container import * 
from layer import * 
import font

xi = font.get_font_as_xis()
zeta = xi

container = Container(
    "quadratic",
    DenseBiasLayer(20, activation="sigmoid", eta=0.0005),   
    DenseBiasLayer(10, activation="sigmoid", eta=0.0005),
    DenseNoBiasLayer(2, activation="sigmoid", eta=0.0005),      
    DenseBiasLayer(10, activation="sigmoid", eta=0.0005), 
    DenseBiasLayer(20, activation="sigmoid", eta=0.0005), 
    DenseNoBiasLayer(35, activation="sigmoid", eta=0.0005), 
)


errors = [] 
epochs = 300000
i = 0 
for epoch in range(epochs): 
    global_loss = 0 
    for psi_mu, zeta_mu in zip(xi, zeta):
        res, loss = container(psi_mu, zeta_mu, True)
        global_loss += loss 
    print("FINISH EPOCH {} - LOSS {}".format(epoch, global_loss))


# Create three subplots. You will use the leftest one to traverse the latent space
fig, ax = plt.subplots(1, 3)

# Optional: plot samples used for training in the latent space as dots, for reference
for char, label in zip(xi, font.labels): 

    # Try out a sample, and leave its latent representation in 'res'
    res = char
    i = 0 
    while (len(res) != 2): 
        res = container.layers[i](res)
        i += 1

    # plot res in ax[0], the leftest subplot
    ax[0].scatter(res[0], res[1], marker=".", c=["c"])
    ax[0].annotate(label, (res[0], res[1]))
     
bottleneck_at = i

# This function is trigger every time we 1) Click on ax[0]; or 2) Hover over ax[1]
def onaction(event):
    global flag
    ix, iy = event.xdata, event.ydata

    # This is the latent vector of the point we are currently in 
    # We must feed it to the decoder to obtain a representation 
    latent_vector = np.array([ix, iy])

    # Clear ax[1] and ax[2]
    ax[1].clear()
    ax[2].clear()

    # If we are hovering over ax[0], draw the decodification 
    if latent_vector[0] is not None and latent_vector[1] is not None:

        res = latent_vector
        i = bottleneck_at 
        while (len(res) != 35): 
            res = container.layers[i](res)
            i += 1
        decoded_img = res
        # decoded_img = container.layers[3](container.layers[2](latent_vector)) # decode 
        decoded_img = decoded_img.reshape(7, 5) # reshape 
        decoded_img = 1-decoded_img # alter color, if necessary
        ax[1].imshow(decoded_img, cmap='gray') # show picture as is 
        ax[2].imshow(2*np.sign(decoded_img-0.5)-1, cmap='gray') # show picture but only B and W pure
        plt.draw()

# button_press_event
# motion_notify_event
# cid = fig.canvas.mpl_connect('motion_notify_event', onaction) # Uncomment for hover
cid = fig.canvas.mpl_connect('button_press_event', onaction) # Uncomment for click

plt.show()
