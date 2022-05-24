import numpy as np 

patterns = [ 
    [1, 1, -1,-1], 
    [-1, -1, 1, 1]
]

q_states = 4
w = np.zeros((q_states, q_states))
for i in range(q_states): 
    for j in range(q_states): 
        if i != j:
            for pattern in patterns: 
                w[i][j] += pattern[i]*pattern[j]/q_states

states = np.array([-1, -1, -1, -1]) # np.zeros(q_states) 
states_prime = None 
for x in range(10): 
    states_prime = np.sign(np.matmul(w, states))
    print(states, states_prime)
    if np.array_equal(states_prime, states): 
        break
    states = states_prime
    

# print(states_prime, states)
