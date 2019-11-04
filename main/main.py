import numpy as np
from Functions import run_Alg




if __name__=='__main__':
    Path2DisMx1 = '../ADK/dist_1.txt'
    Path2DisMx2 = '../ADK/dist_2.txt'
    Path2XYZ1 = '../ADK/xyz_1.txt'
    Path2XYZ2 = '../ADK/xyz_2.txt'
    # M1 = np.loadtxt(Path2DisMx1)
    # M2 = np.loadtxt(Path2DisMx2)
    # M = np.zeros((2,M1.shape[0], M1.shape[1]))
    # M[0,:,:] = M1
    # M[1,:,:] = M2
    XYZ_1 = np.loadtxt(Path2XYZ1)
    XYZ_2 = np.loadtxt(Path2XYZ2)
    XYZ = np.zeros((2, XYZ_1.shape[0], XYZ_1.shape[1]))
    XYZ[0, :, :] = XYZ_1
    XYZ[1, :, :] = XYZ_2

    PrdLabls = run_Alg(XYZ)
    print(PrdLabls)