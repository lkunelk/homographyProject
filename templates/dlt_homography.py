import numpy as np
from numpy.linalg import inv, norm
from scipy.linalg import null_space

def dlt_homography(I1pts, I2pts):
    """
    Find perspective Homography between two images.

    Given 4 points from 2 separate images, compute the perspective homography
    (warp) between these points using the DLT algorithm.

    Parameters:
    ----------- 
    I1pts  - 2x4 np.array of points from Image 1 (each column is x, y).
    I2pts  - 2x4 np.array of points from Image 2 (in 1-to-1 correspondence).

    Returns:
    --------
    H  - 3x3 np.array of perspective homography (matrix map) between image coordinates.
    A  - 8x9 np.array of DLT matrix used to determine homography.
    """
    # Create A Matrix
    A = np.zeros((1, 9))
    for i in range(4):
        x, y = I1pts[0][i], I1pts[1][i]
        u, v = I2pts[0][i], I2pts[1][i]
        row1 = np.array([-x, -y, -1,  0,  0,  0, u*x, u*y, u])
        row2 = np.array([ 0,  0,  0, -x, -y, -1, v*x, v*y, v])
        A = np.vstack((A, row1))
        A = np.vstack((A, row2))
    A = np.delete(A, 0, 0)
    
    # Solve for Homography matrix
    H = null_space(A)
    H = H.reshape((3,3))
    
    return H, A
