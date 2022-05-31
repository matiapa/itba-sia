import numpy as np 
import matplotlib.pyplot as plt
import imageio



patterns = [ 
    [
        -1, 1, -1, -1, 1, # K
        -1, 1, -1, 1, -1, 
        -1, 1, 1, -1, -1, 
        -1, 1, -1, 1, -1, 
        -1, 1, -1, -1, 1
    ], 
    [
        1, -1, -1, -1, -1, # L
        1, -1, -1, -1, -1, 
        1, -1, -1, -1, -1, 
        1, -1, -1, -1, -1,
        1, 1, 1, 1, 1
    ], 
    [
        -1, -1, 1, -1, -1, # I
        -1, -1, 1, -1, -1, 
        -1, -1, 1, -1, -1, 
        -1, -1, 1, -1, -1, 
        -1, -1, 1, -1, -1,
    ], 
    [
        1, 1, 1, 1, 1, # P
        1, -1, -1, -1, 1, 
        1, 1, 1, 1, 1, 
        1, -1, -1, -1, -1, 
        1, -1, -1, -1, -1,
    ]
]

part_p =     [
        1, 1, 1, -1, -1, # K
        1, -1, -1, -1, -1, 
        1, 1, 1, -1, -1, 
        1, -1, -1, -1, -1, 
        -1, -1, -1, -1, -1
    ]


def noise_with_p(pattern, p): 
    noisy_pattern = []
    for x in pattern: 
        rand = np.random.uniform(0, 1)
        if rand < p: 
            noisy_pattern.append(1 if x == -1 else -1)
        else: 
            noisy_pattern.append(x)
    return noisy_pattern

def noise_with_k(pattern, k): 
    indexes = np.random.choice(range(25), k, False)
    noisy_pattern = []
    for x in range(len(pattern)):
        if x in indexes: 
            noisy_pattern.append(1 if pattern[x] == -1 else -1)
        else:
            noisy_pattern.append(pattern[x])
    return noisy_pattern            
        

# Patron de consulta 
pattern = patterns[3]
states = noise_with_p(pattern, 0.1)

q_states = len(patterns[0])
w = np.zeros((q_states, q_states))
for i in range(q_states): 
    for j in range(q_states): 
        if i != j:
            for pattern in patterns: 
                w[i][j] += pattern[i]*pattern[j]/q_states


states_prime = states 
for x in range(20): 

    g = np.reshape(states_prime, (5, 5))
    plt.imshow(g, cmap='Greys',  interpolation='nearest')
    plt.savefig('hopfield{0}.png'.format(x))
    states_prime = np.sign(np.matmul(w, states))
    if np.array_equal(states_prime, states): 
        break
    states = states_prime




    


