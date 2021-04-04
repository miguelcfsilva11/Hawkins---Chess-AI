# Hawkins - Chess AI
<img src="image/hawkins-logo-full.png" width="546" height="200">

"Hawkins" is an open-source, competitive Chess AI powered by multiple tree search algorithms. It makes use of various optimization techniques, mostly extensions of alpha-beta pruning and other traditional chess engine methods. It comes with its own GUI (which was heavily inspired by [Nick Zuber's](https://github.com/nickzuber/chs) board design) and many levels of difficulty.

# Engine Performance

Hawkins plays at a really high-level, even when compared to the strongest AIs ever built with Python. In this particular game, Hawkins went head to head with Stockfish's fifth level on [lichess](https://lichess.org/) (rated ~2000 ELO), and won after dozens of well-crafted moves.

<img src="image/Stockfish_vs_Hawkins.gif" width="300" height="300">

**Stockfish vs Hawkins, 0-1** ([PGN](image/Stockfish_vs_Hawkins.pgn))

# Run It

Hawkins runs on both Unix and Windows terminals. In order to put the engine to test, you must either download the source code or install its package, which is available via [PyPI](https://pypi.org/project/hawkins/).

To install it:

`
  pip install hawkins
  `
  
After the installation process, run the following command to start playing:

`
  python -m hawkins.chessboard
  ` 
