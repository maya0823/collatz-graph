# Collatz Graph

Small pure-Python CLI that looks at the Collatz conjecture through graphs.

Every positive integer has a next number: if even, divide by 2; if odd, do 3n+1. The conjecture says you always reach 1. This tool treats those steps as edges in a directed graph so you can explore sequences, reverse trees, and longest chains.

## Requirements

Just Python 3.9+. No third-party packages.

## Usage

```bash
python collatz_graph.py seq 27
```

Prints the full sequence starting from 27 until it hits 1.

```bash
python collatz_graph.py longest 1000
```

Finds which number ≤ 1000 produces the longest sequence and prints it.

```bash
python collatz_graph.py reverse 10
```

Shows every number that maps directly to 10 in one Collatz step (the reverse neighbors).

```bash
python collatz_graph.py tree 50
```

Builds the reverse adjacency list for numbers 1–50 and prints a few stats plus sample edges.

## How the reverse step works

From any n you can always go back to 2n (the even predecessor).  
You can also go back to (n-1)/3 when that value is a positive odd integer and actually produces n under the normal rule.

That’s all the code needs.

## Why this exists

I wanted a tiny playground for mixing number theory with basic graph ideas—forward paths, reverse branching, longest path under a bound—without pulling in NetworkX or anything heavy. Everything stays in the standard library.

## License

MIT. Do whatever you want with it.
