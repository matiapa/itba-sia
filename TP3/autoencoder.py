from container import * 
from grapher import * 
import gzip 
import random

items_size = 1000
f = gzip.open('train-images-idx3-ubyte.gz','r')
labels_f = gzip.open('train-labels-idx1-ubyte.gz','r')
labels = []

labels_f.read(8)
for i in range(0, items_size):   
    buf = labels_f.read(1)
    label = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    labels.append(label)

image_size = 28
f.read(16)
buf = f.read(image_size * image_size * items_size)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(items_size, image_size, image_size, 1)

## DATA
xi = data.reshape((-1, 784))/255
labels = labels 

x = [1, 1, 1, 1, 1]

container = Container(
    "quadratic", 
    DenseBiasLayer(500, activation="tanh", eta=0.0001), 
    DenseNoBiasLayer(784, activation="id", eta=0.0001), 
)

i = 0 
epochs = 10000
from_ex = 0
to_ex = 100
for t in range(epochs):
    print(t/epochs*100, "%")
    for xi_mu in xi[from_ex:to_ex]:
        res, loss = container(xi_mu, xi_mu, True)


xs = [] 
ys = []
value = [x[0] for x in labels[from_ex:to_ex]] 
for xi_mu in xi[from_ex:to_ex]:         
    res, loss = container(xi_mu, xi_mu, True)
    xs.append(container.layers[0].last_z[0])
    ys.append(container.layers[0].last_z[1])

    # res = res.reshape((28, 28))
    # image = np.asarray(res).squeeze()
    # plt.imshow(image)
    # # plt.title("Number {}".format(label[0]))
    # i += 1
    # plt.show()

# RANDOM COLORS
no_of_colors=10
color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)]) for j in range(no_of_colors)]

from matplotlib.colors import ListedColormap
colours = ListedColormap(color)
scatter = plt.scatter(xs, ys, c=value, cmap=colours)
plt.legend(*scatter.legend_elements())
plt.show()