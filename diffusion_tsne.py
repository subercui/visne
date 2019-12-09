import numpy as np
from knn import KNN
from diffusion import Diffusion
from sklearn import preprocessing
from evaluate import compute_map_and_print
import pandas as pd
import scanpy as sc
import scipy.io as sio
from scipy.sparse import csr_matrix
from anndata import AnnData
# verbosity: errors (0), warnings (1), info (2), hints (3)


def main():
    sc.settings.verbosity = 3
    sc.logging.print_versions()
    results_file = 'data/zeisel.h5ad'  # the file that will store the analysis results

    sc.settings.set_figure_params(dpi=80)

    filename = './data/retina.npz'
    loaded = np.load(filename)
    X, labels = loaded['data'], loaded['labels']
    X = np.log10(1 + X)

    adata = AnnData(X)
    adata.obs_names_make_unique()

    return adata


if __name__ == '__main__':
    main()
