#!/usr/bin/env python3
"""
Collatz Graph Explorer
A small pure-Python tool that treats the Collatz conjecture as a directed graph.
You can compute forward sequences, build reverse trees, find the longest chain
in a range, and print simple adjacency info.
"""

from collections import defaultdict, deque
import argparse
import sys


def collatz_next(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def forward_sequence(start: int, max_steps: int = 10000) -> list[int]:
    """Return the Collatz sequence starting from `start` until we hit 1 (or max_steps)."""
    seq = [start]
    n = start
    steps = 0
    while n != 1 and steps < max_steps:
        n = collatz_next(n)
        seq.append(n)
        steps += 1
    return seq


def reverse_neighbors(n: int) -> list[int]:
    """
    Numbers that can reach n in one Collatz step.
    Always: 2*n (even predecessor)
    Sometimes: (n-1)/3 if that is integer and odd and positive.
    """
    preds = [2 * n]
    if (n - 1) % 3 == 0:
        candidate = (n - 1) // 3
        if candidate > 0 and candidate % 2 == 1 and collatz_next(candidate) == n:
            preds.append(candidate)
    return preds


def build_reverse_tree(limit: int) -> dict[int, list[int]]:
    """
    Build a reverse adjacency list for numbers up to `limit`.
    Keys are numbers; values are lists of their reverse neighbors still <= limit.
    """
    graph = defaultdict(list)
    for n in range(1, limit + 1):
        for p in reverse_neighbors(n):
            if p <= limit:
                graph[n].append(p)
    return graph


def longest_chain_in_range(limit: int) -> tuple[int, int, list[int]]:
    """
    Find the number <= limit with the longest Collatz sequence.
    Returns (number, length, sequence).
    """
    best_n = 1
    best_len = 1
    best_seq = [1]
    for n in range(1, limit + 1):
        seq = forward_sequence(n)
        if len(seq) > best_len:
            best_len = len(seq)
            best_n = n
            best_seq = seq
    return best_n, best_len, best_seq


def print_sequence(seq: list[int]) -> None:
    print(" -> ".join(str(x) for x in seq))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Explore the Collatz conjecture as a directed graph."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # sequence
    p_seq = sub.add_parser("seq", help="Print the forward Collatz sequence for a number")
    p_seq.add_argument("n", type=int, help="Starting number")

    # longest
    p_long = sub.add_parser("longest", help="Find the longest sequence for numbers up to N")
    p_long.add_argument("limit", type=int, help="Upper bound (inclusive)")

    # reverse
    p_rev = sub.add_parser("reverse", help="Show reverse neighbors of a number")
    p_rev.add_argument("n", type=int, help="Number")

    # tree stats
    p_tree = sub.add_parser("tree", help="Build reverse tree up to limit and show basic stats")
    p_tree.add_argument("limit", type=int, help="Upper bound")

    args = parser.parse_args()

    if args.command == "seq":
        if args.n < 1:
            print("Number must be positive.", file=sys.stderr)
            sys.exit(1)
        seq = forward_sequence(args.n)
        print(f"Sequence for {args.n} (length {len(seq)}):")
        print_sequence(seq)

    elif args.command == "longest":
        if args.limit < 1:
            print("Limit must be positive.", file=sys.stderr)
            sys.exit(1)
        n, length, seq = longest_chain_in_range(args.limit)
        print(f"Longest sequence under {args.limit}: starts at {n}, length {length}")
        print_sequence(seq)

    elif args.command == "reverse":
        if args.n < 1:
            print("Number must be positive.", file=sys.stderr)
            sys.exit(1)
        preds = reverse_neighbors(args.n)
        print(f"Numbers that map to {args.n} in one step: {preds}")

    elif args.command == "tree":
        if args.limit < 1:
            print("Limit must be positive.", file=sys.stderr)
            sys.exit(1)
        graph = build_reverse_tree(args.limit)
        total_edges = sum(len(v) for v in graph.values())
        print(f"Reverse graph for 1..{args.limit}")
        print(f"  nodes with at least one reverse edge: {len(graph)}")
        print(f"  total reverse edges: {total_edges}")
        # show a few interesting nodes
        print("\nSample reverse neighbors:")
        for n in [1, 2, 3, 5, 10, 16]:
            if n <= args.limit:
                print(f"  {n} <- {graph.get(n, [])}")


if __name__ == "__main__":
    main()
