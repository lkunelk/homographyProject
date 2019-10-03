import matplotlib.pyplot as plt

# Billboard hack script file.
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

def billboard_hack():
    """
    Hack and replace the billboard!

    Parameters:
    ----------- 

    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    # Bounding box in Y & D Square image.
    bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
    Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])

    Iyd = imread('../billboard/yonge_dundas_square.jpg')
    Ist = imread('../billboard/uoft_soldiers_tower_dark.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    #--- FILL ME IN ---

    # Let's do the histogram equalization first.
    Ist = histogram_eq(Ist)
    
    # Compute the perspective homography we need...
    H, A = dlt_homography(Ist_pts, Iyd_pts)
    
    # Main 'for' loop to do the warp and insertion - 
    # this could be vectorized to be faster if needed!
    h, w = Ist.shape
    
    for y in range(h):
        for x in range(w):
            p = H.dot(np.array([x, y, 1]))
            u, v, _ = p / p[2]
            Iyd[int(v), int(u)] = np.array([Ist[y,x], Ist[y,x], Ist[y,x]])

    # You may wish to make use of the contains_points() method
    # available in the matplotlib.path.Path class!

    #------------------

    plt.imshow(Iyd)
    plt.show()
    # imwrite(Ihack, 'billboard_hacked.png');
    Ihack = Iyd

    return Ihack

if __name__ == '__main__':
    billboard_hack()
