import sys
sys.path.append("..")

from container import * 
from grapher import * 
import numpy
import sklearn

# Read data from file

psi = [[],[],[],[],[],[],[],[],[],[]]   # 10 x 35
zeta = numpy.identity(10).tolist()

with open("../inputs/digits_map_train_set.txt", "r") as f:
    line_num = 0 
    for line in f.readlines():
        psi_num = line_num // 7
        for pixel in line.split(" "):
            psi[psi_num].append(int(pixel))
        line_num +=1

for p in psi:
    print(len(p))

epochs = 50

container = Container(
    "quadratic", 
    DenseBiasLayer(50, activation="sigmoid", eta=0.01),
    DenseBiasLayer(10, activation="id", eta=0.01),
)

errors = [] 
i = 0

for epoch in range(epochs): 
    print(f'---------------- Epoch {epoch} ----------------')

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    error = 0
    psi_num = 0
    for psi_mu, zeta_mu in zip(psi, zeta):
        res, loss = container(psi_mu, zeta_mu, True)
        error += loss

        # res = [round(x) for x in res]
        # error += sum(np.square(np.subtract(res, zeta_mu)))
        
        # print(psi_mu)
        print(f'Num: {psi_num}')
        print([round(x) for x in res])
        print([round(x) for x in zeta_mu])
        print('-------')
        psi_num += 1

    i += 1
 
    errors.append(error)
    if error < 1e-9: 
        break 

plt.plot(range(len(errors)), errors, 'k-')
plt.yscale("log")
plt.show()