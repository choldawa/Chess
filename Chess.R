# PseudoCode:
#   load pgn via rchess system.file?
#   get list of all moves in the game via chss$history()
#   store this as an array? 
#   initialize blank chess game via chss = Chess$new()
#   for each move in history:
#     push move to blank game via chss$move("Nbd7")
#     get all legal moves from there via chss$moves()
#     for each possible in moves:
#       push possible to hypothetical board via chss$move(possible)
#       get stockfish eval of that position <----- unsure on this, tbd
#       save stockfish eval to new array specific to this move
#       remove possible from board via chss$undo()
# take variance of each array of stockfish possibles for each move      


#install.packages("rchess")
#devtools::install_github("hrbrmstr/pigeon")
#install.packages("rlang", dependencies = TRUE) 
#install.packages("remotes")
#remotes::install_github("oganm/stockfisher")
#install.packages('subprocess',repos='http://cran.us.r-project.org')
library(pigeon)
library(rchess)
library(tidyverse)
library(bigchess)

pgn = system.file("extdata/pgn/kasparov_vs_topalov.pgn", package = "rchess")
pgn = readLines(pgn, warn = FALSE)
pgn = paste(pgn, collapse = "\n")
cat(pgn)

chss = Chess$new()
chss$load_pgn(pgn)



plot(chss)
#list of legal moves
chss$moves()
chss$moves(verbose = TRUE)

chss$history()
chss$history_detail()
#get fen 
chss$fen()
#add a new move to board
chss$move("Nbd7")
#moves can be concatenated, e.g. below
#chss$move("e5")$move("f4")$move("Qe7")$move("fxe5")
chss$undo()
plot(chss)


hist = chss$history()
test = Chess$new()
test$move(hist[1])
plot(test)
test$moves()
stockfish = startStockfish()

engine_path <- "./stockfish-10-64"
e <- uci_engine(engine_path)
ep <- uci_position(e, moves = "e2e4")
eg <- uci_go(e, depth = 10)

require(magrittr)
ap <- analyze_position(engine_path,san = "e4 e5 Nf3 Nc6 Bb5",depth = 10)
#ap$bestmove_lan
ap$bestmove_san
ap$score
ap$curpos_san
ap$bestline_san
#ap$bestline_lan

#load game from pgn string
pgn <- "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6
4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6
8. c3 O-O 9. h3 Nb8  10. d4 Nbd7
11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7
14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4"
#chss <- Chess$new(--add FEN here to load specific position--)
chss <- Chess$new()
chss$load_pgn(pgn)

plot(chss)
chss$moves()
