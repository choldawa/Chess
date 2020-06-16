#install.packages("rchess")
#devtools::install_github("hrbrmstr/pigeon")
install.packages("rlang", dependencies = TRUE) 
library(pigeon)
library(rchess)
library(tidyverse)

pgn = system.file("extdata/pgn/kasparov_vs_topalov.pgn", package = "rchess")
pgn = readLines(pgn, warn = FALSE)
pgn = paste(pgn, collapse = "\n")
cat(pgn)

chss = Chess$new()
chss$load_pgn(pgn)
chss$history()
df_hist = chss$moves(verbose = TRUE)
df_hist
plot(chss)
#legal moves
chss$moves()



pgn <- "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6
4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6
8. c3 O-O 9. h3 Nb8  10. d4 Nbd7
11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7
14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5
Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4"
chss <- Chess$new()
chss$load_pgn(pgn)

plot(chss)
chss$moves()
