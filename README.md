# Carcassonne Board Generator

![Example of run](data/preview.gif)

This program uses the [Wave Function Collapse](https://github.com/mxgmn/WaveFunctionCollapse) algorithm to generate random, legal boards
for the game [Carcassonne](https://en.wikipedia.org/wiki/Carcassonne_(board_game)).

Since this is in Python, the best performance comes from an array implementation (it seems pointers are
more common), using numpy. Rendering is done with PyGame, which uses [SDL](https://www.libsdl.org/).

## Running

```
wfc <N> <M>
```

You can specify the $(N, M)$ dimensions of the board via the CLI.
