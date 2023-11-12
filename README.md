# carcassonne

## TODO

- [x] process tile files into rule representation
    - all tiles have four associated values, representing the only legal ground type 
    that can ajoin each of its sides
    - there are three ground types (G)rass, (R)oad, (C)ity
    - example value: CastleEdge0.png || CCGG
        - these are clockwise from top, city city grass grass
    - these valid joining types are *reflective*: i.e., because CastleEdge0's top edge only
    accepts C, it's top edge itself is C
        - this means that the four values apply both to searching for new tiles and for
        describing the current tile
    - we can do these in a google sheet and then manipulate to maybe CSV for pandas?
- [x] create numpy representations
    - two grids so far: of Square objects and of entropy integers
- [x] lowest entropy 
    - to perform the collapse, we need to find the lowest entropies
- [ ] structure algorithm, including the lowest_entropy helper
    - can just scaffold all the steps and implement them incrementally
