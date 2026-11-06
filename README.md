# Collatz Graph

Take any positive integer. If it is even, divide by 2. If it is odd, multiply by 3 and add 1. Repeat. The Collatz conjecture says you always eventually reach 1, no matter where you start. Nobody has proved it for all numbers, but it has been checked for enormous ranges.

This small tool treats those steps as edges in a directed graph. You can follow a number forward to 1, look at the reverse directions (which numbers can lead to a given number), and find the longest chain inside a range.

## Requirements

Python 3.9+. No third-party packages.

## Usage

```bash
python collatz_graph.py seq 27
```

Prints the full sequence starting from 27 until it hits 1.

```bash
python collatz_graph.py longest 1000
```

Finds which number <= 1000 produces the longest sequence and prints it.

```bash
python collatz_graph.py reverse 10
```

Shows every number that maps directly to 10 in one Collatz step (the reverse neighbors).

```bash
python collatz_graph.py tree 50
```

Builds the reverse adjacency list for numbers 1 to 50 and prints a few stats plus sample edges.

## How the reverse step works

From any n you can always go back to 2n (the even predecessor).
You can also go back to (n-1)/3 when that value is a positive odd integer and actually produces n under the normal rule.

## License

MIT. Do whatever you want with it.
