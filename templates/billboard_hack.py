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

    # Apply Histogram equalization
    Ist = histogram_eq(Ist)
    
    # Compute homography
    H, A = dlt_homography(Iyd_pts, Ist_pts)
    
    # Define billboard polygon
    vertices = np.array([[x, y] for x, y in zip(Iyd_pts[0], Iyd_pts[1])])
    billboard = Path(vertices)
    
    # Insert Soldiers Tower picture into Young-Dundas picture
    h, w, _ = Iyd.shape
    for y in range(h):
        for x in range(w):
            if billboard.contains_points([[x,y]]):
                p = H.dot(np.array([x, y, 1]))
                xp, yp, _ = p / p[2]
                val = bilinear_interp(Ist, np.array([[xp], [yp]]))
                Iyd[y, x] = np.array([val, val, val])
    
    # Uncomment to see picture
    #plt.imshow(Ihack)
    #plt.show()
    #imwrite('billboard_hacked_2.jpg', Iyd);

    return Iyd

if __name__ == '__main__':
    billboard_hack()
