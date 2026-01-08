import numpy as np 

def pageRank(M, d:float = 0.85):
    """PageRank algorithm with explicit number of parameters. Returns ranking of
     nodes (pages) in the adjacency matrix.
      
    Parameters:
     M: nmppy array
        adjaceny matrix where M_i, j represents the link from 'j' to 'i'
         such that for all 'j' sum(i, M_i, j) = 1
    d: float , optional
        damping factor, by default 0.85
    Returns: 
    ------
    numpy array : A vector of ranks such that v_i is the i-th rank from [0, 1]
    
    """

    N = M.shape[1]
    w = np.ones(N) / N
    M_hat = d * M 
    v = M_hat @ w + (1 - d ) / N 
    while np.linalg.norm(w - v) >= 1e-10:
        w = v
        v = M_hat @ w + (1 - d) / N
    return v 

M = np.array([[0, 0, 0, .25],
              [0, 0, 0, .5],
              [0, 0.5, 1, 0],
              [0, 0.5, 1, 0]])
v = pageRank(M, 0.85)