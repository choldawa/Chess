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

#stockfish = Stockfish("/home/choldawa/stockfish-10-64")
# stockfish = Stockfish("/home/choldawa/stockfish-10-linux/Linux/stockfish_10_x64")


game_file = sys.argv[1] #which file to read games from
X = int(sys.argv[2]) #how many instances in order to add node (limits tree growing big/sparse)
limit = int(sys.argv[3]) #how many games to read in


#read in mainline file
with open(game_file, "r") as file_in:
    mainlineList = []
    for line in file_in:
        mainlineList.append(line)
#extract each string of moves
stringList = []
for mainLine in mainlineList:
    stringList.append(mainLine.split())


if(limit > len(stringList)):
    limit = len(stringList)-1

#start timer
start = timeit.default_timer()

g = nx.DiGraph()
g.add_node('')
cnt = 0
for string in stringList[:limit]:
    if(cnt%200 == 0):
        print("strings processed:", cnt, ", time:", timeit.default_timer()-start)
    board = chess.Board()
    moveString = '^ \+'
    parentFen = ''
    for move in string:
        print(move)
        try:
            count = 0
            countWhite = 0
            countTie = 0
            countBlack = 0
            moveString += move + ' \+'
            board.push_san(move) #push the move to the board
            currFen = board.fen() #get the fen from the board

        #run grep command to get counts and outcomes
            # command = 'grep -I "{}"  {}  | grep -o ".$" | sort | uniq -c'.format(moveString, game_file)
            # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
            # output = process.communicate()
            # counts = re.findall('\d+',str(output))
            #
            # if('0' in counts[1::2]):
            #      countWhite = counts[0::2][counts[1::2].index('0')]
            # else:
            #     countTie = 0
            # if('1' in counts[1::2]):
            #      countBlack = counts[0::2][counts[1::2].index('1')]
            # else:
            #     countTie = 0
            # if('2' in counts[1::2]):
            #     countTie = counts[0::2][counts[1::2].index('2')]
            # else:
            #     countTie = 0
            #
            # count = int(countWhite) + int(countBlack) + int(countTie)
        #check if fen is new, if yes, and count is high, add new node
            if(currFen not in g.nodes): #only add nodes if the sequence has not yet occured and they are frequent enough
                command = 'grep -I "{}"  {}  | grep -o ".$" | sort | uniq -c'.format(moveString, game_file)
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
                output = process.communicate()
                counts = re.findall('\d+',str(output))

                if('0' in counts[1::2]):
                     countWhite = counts[0::2][counts[1::2].index('0')]
                else:
                    countTie = 0
                if('1' in counts[1::2]):
                     countBlack = counts[0::2][counts[1::2].index('1')]
                else:
                    countTie = 0
                if('2' in counts[1::2]):
                    countTie = counts[0::2][counts[1::2].index('2')]
                else:
                    countTie = 0

                count = int(countWhite) + int(countBlack) + int(countTie)
                print(move, count)
                if(count >=X):
                    print(move, "count>X")
                    board = chess.Board(currFen)
                    # stockfish.set_fen_position(currFen)
                    # print('sf', stockfish.get_evaluation()['value'])
                    score = engine.analyse(board, chess.engine.Limit(time=0.05))
                    g.add_node(currFen,
                               # score = stockfish.get_evaluation()['value'],
                               score = score["score"],
                               count = count,
                               whiteWins = countWhite,
                               blackWins = countBlack,
                               tie = countTie,
                               movelistCount = {parentFen:count}) #make a dict of parent IDs and count
                              # movelist = [[moveString]]) #make a list of moveStrings
                    g.add_edge(parentFen, currFen)
                    parentFen = currFen
                    print(move, "added")
                else:
                    break
        #if fen is not new, check if movestring in list of movestrings, if not, add it and add count
            elif(parentFen not in nx.get_node_attributes(g, 'movelistCount')[currFen]):
                print(move, "ELIF")
                command = 'grep -I "{}"  {}  | grep -o ".$" | sort | uniq -c'.format(moveString, game_file)
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
                output = process.communicate()
                counts = re.findall('\d+',str(output))

                if('0' in counts[1::2]):
                     countWhite = counts[0::2][counts[1::2].index('0')]
                else:
                    countTie = 0
                if('1' in counts[1::2]):
                     countBlack = counts[0::2][counts[1::2].index('1')]
                else:
                    countTie = 0
                if('2' in counts[1::2]):
                    countTie = counts[0::2][counts[1::2].index('2')]
                else:
                    countTie = 0

                count = int(countWhite) + int(countBlack) + int(countTie)
                print(move,count)
                if(count>=X):
                    print(move, "count>X")
            # elif(count>=X):
            #     if(parentFen not in nx.get_node_attributes(g, 'movelistCount')[currFen]):
                    #nx.get_node_attributes(g, 'movelist')[currFen] = nx.get_node_attributes(g, 'movelist')[currFen].append([moveString])
                    nx.get_node_attributes(g, 'movelistCount')[currFen][parentFen] = count
#                     nx.get_node_attributes(g, 'movelistWhiteWins')[currFen][parentFen] = countWhite
#                     nx.get_node_attributes(g, 'movelistBlackWins')[currFen][parentFen] = countBlack
#                     nx.get_node_attributes(g, 'movelistTie')[currFen][parentFen] = countTie
#                     g.nodes[currFen]['count'] = nx.get_node_attributes(g, 'count')[currFen]+count
                    g.nodes[currFen]['whiteWins'] = nx.get_node_attributes(g, 'whiteWins')[currFen]+countWhite
                    g.nodes[currFen]['blackWins'] = nx.get_node_attributes(g, 'blackWins')[currFen]+countBlack
                    g.nodes[currFen]['tie'] = nx.get_node_attributes(g, 'tie')[currFen]+countTie
                    g.add_edge(parentFen, currFen)
                    print(move, "updated")
                else:
                    break

            elif(parentFen in nx.get_node_attributes(g, 'movelistCount')[currFen]):
                parentFen = currFen
            else:
                break
        except: #skip any errors in the notation that cannot be pushed to a board
            break
    cnt+=1
stop = timeit.default_timer()
print('Time: ', stop - start)
print("totalNodes:",len(g))

nx.write_gpickle(g,"{}{}.gpickle".format(game_file,limit))
