import numpy as np


def load_attr():
    attr_file = 'list_attr_celeba.csv'

    attr = np.genfromtxt(attr_file, skip_header=1, usecols=[21], delimiter=',')
    # attr = np.genfromtxt(attr_file, skip_header=1, usecols=[23], delimiter=',')
    # attr = np.genfromtxt(attr_file, skip_header=1, usecols=[16], delimiter=',')
    # attr = np.genfromtxt(attr_file, skip_header=1, usecols=[40], delimiter=',')
    # attr = np.genfromtxt(attr_file, skip_header=1, usecols=[32], delimiter=',')
    attr[attr == -1] = 0

    return attr

