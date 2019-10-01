import numpy as np
from numpy.linalg import inv

def bilinear_interp(I, pt):
    """
    Performs bilinear interpolation for a given image point.

    Given the (x, y) location of a point in an input image, use the surrounding
    4 pixels to conmpute the bilinearly-interpolated output pixel intensity.

    Note that images are (usually) integer-valued functions (in 2D), therefore
    the intensity value you return must be an integer (use round()).

    This function is for a *single* image band only - for RGB images, you will 
    need to call the function once for each colour channel.

    Parameters:
    -----------
    I   - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    pt  - 2x1 np.array of point in input image (x, y), with subpixel precision.

    Returns:
    --------
    b  - Interpolated brightness or intensity value (whole number >= 0).
    """
    if pt.shape != (2, 1):
        raise ValueError('Point size is incorrect.')

    # Find 4 nearest pixels
    x, y = pt[0,0], pt[1,0]
    pt1 = np.floor([x, y]).astype(np.int)
    pt2 = np.array([np.ceil(x),  np.floor(y)]).astype(np.int)
    pt3 = np.array([ np.floor(x), np.ceil(y)]).astype(np.int)
    pt4 = np.ceil( [x, y]).astype(np.int)
    
    # Interpolate in x direction
    vx1 = (1.0 - (x - pt1[0])) * I[pt1[1], pt1[0]] +\
                 (x - pt1[0])  * I[pt2[1], pt2[0]]
    vx2 = (1.0 - (x - pt1[0])) * I[pt3[1], pt3[0]] +\
                 (x - pt1[0])  * I[pt4[1], pt4[0]]
    
    # Interpolate in y direction
    b = (1.0 - (y - pt1[1])) * vx1 +\
               (y - pt1[1])  * vx2
    return np.round(b)

if __name__ == '__main__':
    I = np.array([[10,20],[30,40]])
    pt = np.array([[-1, 0]]).T
    print(bilinear_interp(I, pt))
