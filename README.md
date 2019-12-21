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
    
    Protein-Rigid-Domains-Estimation is open source and distributed under OSI-approved MIT license. ::

Copyright (c) 2019 Linh Dang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
