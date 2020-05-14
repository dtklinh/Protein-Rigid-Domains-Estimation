# Protein-Rigid-Domains-Estimation
    Given the protein structural conformations, this program estimates the rigid domains in this protein.
# Compatibility
    Ubuntu 16.04 LTS or later
    Python 3.5 or later
# Python packages dependencies:
    biopython (1.73 or later) from https://biopython.org/
    csb (1.2.5 or later) from https://csb.codeplex.com/
    louvain (0.6.1 or later) from https://pypi.python.org/pypi/louvain/
    matplotlib (only to draw praph) (3.0.3 or later) from matplotlib.org
    numpy (1.16.4 or later) from https://numpy.org/
    python-igraph (0.7.1 or later) from https://igraph.org/python/
    scikit-learn (0.21.3 or later) from https://scikit-learn.org/stable/
    scipy (1.3.1 or later) from https://www.scipy.org/
    MDAnalysis (0.20.1 or later) from https://www.mdanalysis.org
# other package dependencies:
    clustal omega
    (sudo apt-get install -y clustalo)

# Usage
    There are two ways to use this software.
    The users could either calculate rigid domains via a PDB file 
    which contains all protein conformations or a list of PDBIDs.
    For example:
    First, we initializeRea an object RigidDomainFinder
    RDF = RigidDomainFinder(AA_cutoff_neighborhood = 7.5, init_membership = None, merging_threshold=1.0,
                            rigidity_threshold=3.5)
        # parameters:
            AA_cutoff_neighborhood: value of cutoff neighborhood between 
                two amino acids (in Angstrom), default value is 7.5
            init_membership: a list of labels of initial segmentation. 
                For example: [0, 0, 0, 1, 1, 2, 2, 1,...]. The defualt value is None
            merging_threshold: the value of merging threshold in the post-processing. 
                The default value is 1.0
            rigidity_threshold: a RMSD threshold to decide if this domain is rigid
                Default value is 3.5 (in Angstrong)
    # Then, we run the algorithm
    # Method 1: given the list of PDBIDs
    PredLabels = RDF.segment_by_PDBIDs(Lst_PDBs=['1ake_A', '4ake_A'])
        # parameter: Lst_PDBs: a list contains all PDBIDs and their chainID
    # Method 2: given a path to PDB file. 
        This file contains all models of a protein chain. An example could be found at file 'adk.pdb'
    PredLabels = RDF.segment_by_PDBFile(Path2PDBFile='test/data/adk.pdb',PDBID='ADK',ChainID='A')
        # parameters:
            Path2PDBFile: a path 2 PDB file
            PDBID: any string (not important to the algorithm)
            ChainID: Chain ID of a protein
    # Method 3: given a path to VMD-like xyz format file
    PredLabels = rf.segment_by_xyzFormat('test/data/lysozyme.xyz')
    # Notice: when two or more protein conformations have different size, 
        we use Clustal Omega to allign those sequences
    # An example of how to use the software could be found at mainPackage/main.py
    # Hint: clone this project, open with Pycharm and run file mainPackage/main.py
        to have the impression how this algorithm works    
    
Protein-Rigid-Domains-Estimation is open source and distributed under OSI-approved MIT license. ::

Copyright (c) 2019 Linh Dang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
