from mainPackage.Functions import RigidDomainFinder
from GraphPackage.Graph_Config import List_Colors
if __name__ == '__main__':
    rf = RigidDomainFinder()
    # VMD likewise xyz format
    PredictedLabels, ProtG = rf.segment_by_xyzFormat('./data/lysozyme.xyz')
    print(PredictedLabels)