from Bio.PDB.PDBParser import PDBParser
from Graph_Util_Funcs import ConstructRealClusterGraph
from Graph_Config import G_ConstructType, CutOffContact, List_Colors
from AssistantObjects import DynDomEntry
import numpy as np
from scipy import spatial
import sys
# def calDistanceMatrix(PDBID, ChainID, PDBFile):
#     parser = PDBParser(PERMISSIVE=1)
#     structure_id = PDBID
#     filename = PDBFile
#     structure = parser.get_structure(structure_id, filename)
#     for Model in structure:
#         for

def calc_DisMxs(XYZ):
    M = np.zeros((XYZ.shape[0],XYZ.shape[1], XYZ.shape[1]))
    for idx, xyz in enumerate(XYZ):
        M[idx, :, :] = spatial.distance_matrix(xyz, xyz)
    return M



def run_Alg(XYZ, Serial = 'ADK', cutoff_neighborhood = 7.5, init_membership = None, edge_weight_factors = None, merging_threshold=1.0):
    # DisMatrices: m x L x L --> m distance matrices of L x L
    DisMatrices = calc_DisMxs(XYZ)


    Mem = [0]*DisMatrices.shape[1]
    Entry = DynDomEntry(None, Mem, DisMatrices, XYZ)
    G = ConstructRealClusterGraph(Entry.DistanceMatrices, Entry.Membership,init_membership = init_membership,
                                  edge_weight_factors = edge_weight_factors,
                                  Construct_Type=G_ConstructType, cut_off_threshold=cutoff_neighborhood)
    SquareMatFeature = G.calc_squareMatFeature(Entry.DistanceMatrices)
    G.vs['color'] = [List_Colors[v['TrueLabel']] for v in G.vs]
    G['DynDomEntry'] = Entry
    G['SquareMatFeature'] = SquareMatFeature
    G.vs['OriginalIndex'] = [v.index for v in G.vs]
    G.es['OriginalIndex'] = [e.index for e in G.es]
    G_Org_Indexs = [i for v in G.vs for i in v['Cluster']]
    G['serial'] = Serial
    Membership = Mem
    delete_indexs = [i for i in range(len(Membership)) if i not in G_Org_Indexs]
    # do iteration
    Arr = G.do_work_iteration_2(rmsd_thres=3.5)
    Arr = G.do_merge_2(thres=merging_threshold, Arr_G=Arr)

    PredLabels = [-1] * len(Membership)
    for idx, c in enumerate(Arr):
        for v in c.vs:
            for i in v['Cluster']:
                PredLabels[i] = idx
    PredLabels = [i for j, i in enumerate(PredLabels) if j not in delete_indexs]
    return PredLabels

if __name__=="__main__":
    Path2DisMx1 = '../ADK/dist_1.txt'
    Path2DisMx2 = '../ADK/dist_2.txt'
    Path2XYZ1   = '../ADK/xyz_1.txt'
    Path2XYZ2   = '../ADK/xyz_2.txt'
    #M1 = np.loadtxt(Path2DisMx1)
    #M2 = np.loadtxt(Path2DisMx2)
    #M = np.zeros((2,M1.shape[0], M1.shape[1]))
    #M[0,:,:] = M1
    #M[1,:,:] = M2
    XYZ_1 = np.loadtxt(Path2XYZ1)
    XYZ_2 = np.loadtxt(Path2XYZ2)
    XYZ = np.zeros((2,XYZ_1.shape[0], XYZ_1.shape[1]))
    XYZ[0,:,:] = XYZ_1
    XYZ[1,:,:] = XYZ_2

    PrdLabls = run_Alg(XYZ)
    print(PrdLabls)


