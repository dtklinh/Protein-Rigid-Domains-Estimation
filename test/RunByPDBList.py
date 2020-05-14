from mainPackage.Functions import RigidDomainFinder
if __name__ == '__main__':
    rf = RigidDomainFinder()
    PredictedLabels = rf.segment_by_PDBIDs(['4ake_A', '1ake_A'])
    print(PredictedLabels)
