# Chess [repo under construction]
#### What can we learn about risk-taking behavior from 1.4 billion chess games?


## Project Summary
Humans are social beings, and most of our decisions are influenced by considerations of how others will respond. Whether in poker or political negotiations, the riskiness of a decision is often determined by the variance of the other party's possible responses. Such socially-contingent decisions can be framed in terms of adversarial games, which differ from other risky situations such as lotteries because the risk arises from uncertainty about the opponent's decisions, and not some independent stochasticity in the world. 

We use chess as a lens through which we can study human risk-taking behavior in adversarial decision making. We develop a novel algorithm for calculating the riskiness of each move in a chess game, and apply it to data from over 1 billion online chess games. We find that players not only exhibit state-dependent risk preferences, but also change their risk-taking strategy depending on their opponent, and that this effect differs in experts and novices.


This is a snapshot of the beginning of a directed, acyclic graph that condenses billions of chess moves into hundreds of thousands of connected nodes. Our novel algorithm computes the riskiness of a move using the variance of possible response moves the opponent could make. 
<img width="1169" alt="Screen Shot 2021-02-03 at 2 48 35 PM" src="https://user-images.githubusercontent.com/17987950/132625935-eeab6641-5e68-439a-9371-7bff72537d1b.png">

