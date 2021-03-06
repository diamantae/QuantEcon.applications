"""
Compute the reservation wage in the McCall model.

"""

import numpy as np
from mccall_bellman_iteration import solve_mccall_model

def compute_reservation_wage(mcm):
    """
    Computes the reservation wage of an instance of the McCall model
    by finding the smallest w such that V(w) > U.

    If V(w) > U for all w, then the reservation wage w_bar is set to
    the lowest wage in mcm.w_vec.

    If v(w) < U for all w, then w_bar is set to np.inf.
    
    Parameters
    ----------
    mcm : an instance of McCallModel

    Returns
    -------
    w_bar : scalar
        The reservation wage
        
    """

    V, U = solve_mccall_model(mcm)
    w_idx = np.searchsorted(V - U, 0)  

    if w_idx == len(V) + 1:
        w_bar = np.inf
    else:
        w_bar = mcm.w_vec[w_idx]

    return w_bar





