from Bio.PDB.PDBParser import PDBParser
from Graph_Util_Funcs import ConstructRealClusterGraph
from Graph_Config import G_ConstructType, CutOffContact, List_Colors
from AssistantObjects import DynDomEntry

# def calDistanceMatrix(PDBID, ChainID, PDBFile):
#     parser = PDBParser(PERMISSIVE=1)
#     structure_id = PDBID
#     filename = PDBFile
#     structure = parser.get_structure(structure_id, filename)
#     for Model in structure:
#         for


def run_by_DisMxs(DisMatrices):
    # DisMatrices: m x L x L --> m distance matrices of L x L
    Mem = [0]*DisMatrices.shape[1]
    Entry = DynDomEntry(None, Mem, DisMatrices, None)
    G = ConstructRealClusterGraph(Entry.DistanceMatrices, Entry.Membership,
                                  Construct_Type=G_ConstructType, cut_off_threshold=CutOffContact)
    SquareMatFeature = G.calc_squareMatFeature(Entry.DistanceMatrices)
    G.vs['color'] = [List_Colors[v['TrueLabel']] for v in G.vs]
    G['DynDomEntry'] = Entry
    G['SquareMatFeature'] = SquareMatFeature
    G.vs['OriginalIndex'] = [v.index for v in G.vs]
    G.es['OriginalIndex'] = [e.index for e in G.es]

    # do iteration
    Arr = G.do_work_iteration_2(rmsd_thres=3.5)

    return None

if __name__=="__main__":

