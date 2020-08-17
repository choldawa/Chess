import chess
import chess.engine
engine = chess.engine.SimpleEngine.popen_uci("/home/choldawa/stockfish-10-linux/Linux/stockfish_10_x64")

board = chess.Board("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
info = engine.analyse(board, chess.engine.Limit(time=0.05))
print("Score:", info["score"])

import stockfish
from stockfish import Stockfish

stockfish = Stockfish("/home/choldawa/stockfish-10-linux/Linux/stockfish_10_x64")

stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
print(stockfish.get_best_move())
print(stockfish.is_move_correct('a2a3'))

print(stockfish.get_evaluation())
