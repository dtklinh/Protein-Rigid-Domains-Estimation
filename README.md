# Protein-Rigid-Domains-Estimation
    Given the protein structural conformations, this program estimates the rigid domains in this protein.
# Compatibility
    Ubuntu version at least 16.04 LTS
    Python 3
# Python packages dependencies:
    biopython
    csb
    louvain
    matplotlib
    numpy
    python-igraph
    scikit-learn
    scipy
# other package dependencies:
    clustal omega
    (sudo apt-get install -y clustalo)

# Usage
    There are two ways to use this software.
    The users could either calculate rigid domains via a PDB file 
    which contains all protein conformations or a list of PDBIDs.
    For example:
    First, we initializeRea an object RigidDomainFinder
    RDF = RigidDomainFinder(AA_cutoff_neighborhood = 7.5, init_membership = None, merging_threshold=1.0)
        # parameters:
            AA_cutoff_neighborhood: value of cutoff neighborhood between 
                two amino acids (in Angstrom), default value is 7.5
            init_membership: a list of labels of initial segmentation. 
                For example: [0, 0, 0, 1, 1, 2, 2, 1,...]. The defualt value is None
            merging_threshold: the value of merging threshold in the post-processing. 
                The default value is 1.0
    # Then, we run the algorithm
    # Method 1: given the list of PDBIDs
    PredLabels = RDF.segment_by_PDBIDs(['1ake_A', '4ake_A'])
    
    # Method 2: given a path to PDB file. 
        This file contains all models of a protein chain. An example could be found at file 'adk.pdb'
    Path2PDBFile = 'adk.pdb'
    PredLabels = RDF.segment_by_PDBFile(Path2PDBFile,'ADK','A')
    
    # Notice: when two or more protein conformations have different size, 
        we use Clustal Omega to allign those sequences
    # An example of how to use the software could be found at mainPackage/main.py
    
    
Protein-Rigid-Domains-Estimation is open source and distributed under OSI-approved MIT license. ::

Copyright (c) 2019 Linh Dang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
