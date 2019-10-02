import numpy as np

def histogram_eq(I):
    """
    Histogram equalization for greyscale image.

    Perform histogram equalization on the 8-bit greyscale intensity image I
    to produce a contrast-enhanced image J. Full details of the algorithm are
    provided in the Szeliski text.

    Parameters:
    -----------
    I  - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).

    Returns:
    --------
    J  - Contrast-enhanced greyscale intensity image, 8-bit np.array (i.e., uint8).
    """
    #--- FILL ME IN ---
    
    k = 2**8
    height, width = I.shape
    
    # Verify I is grayscale.
    if I.dtype != np.uint8:
        raise ValueError('Incorrect image format!')
    
    # compute histogram
    h = [0 for i in range(k)]
    for row in I:
        for val in row:
            h[val] += 1
    
    # compute pdf
    for i in range(1, k):
        h[i] += h[i-1]
    
    J = np.zeros(I.shape).astype(np.uint8)
    for row in range(height):
        for col in range(width):
            J[row, col] = round((h[I[row, col]] - h[0]) * (k-1) / (width * height - h[0]))
    
    return J

if __name__ == '__main__':
    A = np.array([[1,2],[3,4]]).astype(np.uint8)
    J = histogram_eq(A)
    print(J)
