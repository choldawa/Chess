import sys
import networkx as nx
import matplotlib as plt
import numpy as np
import re
import chess
import subprocess
import timeit
import pickle
import stockfish
from stockfish import Stockfish
import chess
import chess.engine
engine = chess.engine.SimpleEngine.popen_uci("/home/choldawa/stockfish-10-linux/Linux/stockfish_10_x64")

p1 = sys.argv[1]
p2 = sys.argv[2]

g = nx.read_gpickle(p1)
h = nx.read_gpickle(p2)
print("totalNodes:",len(g), "||, ", "totalNodes:",len(h))

g1 = list(g.nodes())[1]
h1 = list(h.nodes())[1]

f = nx.compose(g,h)
for gnode in g:
    if(gnode == ''):
        pass
    elif gnode in h:
        if(nx.get_node_attributes(g, 'movelistCount')[gnode].items() == nx.get_node_attributes(h, 'movelistCount')[gnode].items()):
            pass
        else:
            #add the movelist, sum the count, sum win/loss/tie
            nx.get_node_attributes(f, 'movelistCount')[gnode] = nx.get_node_attributes(h, 'movelistCount')[gnode].update(nx.get_node_attributes(g, 'movelistCount')[gnode])

print("totalNodes Merged:",len(f))
nx.write_gpickle(f,"merged.gpickle")
