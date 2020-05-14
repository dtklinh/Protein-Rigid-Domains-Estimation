from mainPackage.Functions import RigidDomainFinder
if __name__ == '__main__':
    rf = RigidDomainFinder()
    PredictedLabels = rf.segment_by_PDBFile('./data/adk.pdb','adk','A')
    print(PredictedLabels)