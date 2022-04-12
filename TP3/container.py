from layer import * 

class Container: 

    def __init__(self, *args: Layer): 
        self.layers = args

    def __call__(self, input: np.ndarray): 
        res = input
        for layer in self.layers: 
            res = layer(res)
        return res 


# TODO: me da numeros un poco grandes, me gustaria estudiarlo un poco mas 
# Supongo que pasa porque las capas son demasiado largas (elegi 30, 40, 50, 10)
# Con capas mas chicas me da mejor 
# La logica multiplicativa me da o 

x = Container(
    DenseNoBiasLayer(1, activation="sigmoid"), 
    DenseNoBiasLayer(2, activation="sigmoid"), 
    DenseNoBiasLayer(3, activation="sigmoid"),
    DenseNoBiasLayer(6, activation="id")
)

res = x(np.random.rand(3))
print(len(res))
print(res)

