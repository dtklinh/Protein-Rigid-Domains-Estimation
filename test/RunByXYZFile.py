from mainPackage.Functions import RigidDomainFinder
if __name__ == '__main__':
    rf = RigidDomainFinder()
    # VMD likewise xyz format
    PredictedLabels = rf.segment_by_xyzFormat('./data/lysozyme.xyz')
    print(PredictedLabels)