# Protein-Rigid-Domains-Estimation
    Given the protein structural conformations, this program estimates the rigid domains in this protein.

# Python packages dependencies:
    biopython
    csb
    louvain
    matplotlib
    numpy
    python-igraph
    scikit-learn
    scipy

# Usage

from Functions import run_Alg
PredictedLabels = run_Alg(XYZs)

Input: XYZs is 3D matrix (M x N x 3), where M is the number of conformations, N is the number of amino acids in protein, each row of matrix N x 3 is the coordinate
of Carbon-alpha in three dimensional space.

Output: PredictedLabels is a vector length N which contains the index of rigid domain for each amino acid in the protein.