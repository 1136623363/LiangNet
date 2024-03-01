import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torch.nn.utils.rnn import pad_sequence
from torch_geometric.nn import RGCNConv, GraphConv, FAConv
from torch.nn import Parameter
import numpy as np, itertools, random, copy, math
import math
import scipy.sparse as sp
from model_GCN import GCNII_lyc
import ipdb
from HypergraphConv import HypergraphConv
from torch_geometric.nn import GCNConv
from itertools import permutations
from torch_geometric.nn.pool.topk_pool import topk
from torch_geometric.nn import global_mean_pool as gap, global_max_pool as gmp, global_add_pool as gsp
from torch_geometric.nn.inits import glorot
from torch_geometric.nn.conv.gcn_conv import gcn_norm
from torch_geometric.utils import add_self_loops
from high_fre_conv import highConv
a = nn.Parameter(torch.ones(1000))
print(a)