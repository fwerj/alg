#!/usr/bin/env python
def fringe(subgraph, graph):
    """
    a-b-d-e
     \|
      c
    >>> graph = [
    ...     frozenset({"a", "b"}),
    ...     frozenset({"b", "c"}),
    ...     frozenset({"b", "d"}),
    ...     frozenset({"a", "c"}),
    ...     frozenset({"d", "e"}),
    ... ]
    >>> subgraph = [
    ...     frozenset({"a", "b"}),
    ...     frozenset({"b", "c"}),
    ... ]
    >>> fringe(subgraph, graph) # doctest: +SKIP
    {frozenset({'c', 'a'}), frozenset({'d', 'b'})}
    """
    subgraph = set(subgraph)
    if not subgraph <= set(graph):
        raise ValueError("{} is not subgraph of {}".format(subgraph, graph))
    subgraph_vertices = frozenset.union(*subgraph)
    near_edges = {k for k in graph if k & subgraph_vertices}
    return near_edges - subgraph

def farfringe(subgraph, graph):
    """
    a-b-d-e
     \|
      c
    >>> graph = {
    ...     frozenset({"a", "b"}),
    ...     frozenset({"b", "c"}),
    ...     frozenset({"b", "d"}),
    ...     frozenset({"a", "c"}),
    ...     frozenset({"d", "e"}),
    ... }
    >>> subgraph = {
    ...     frozenset({"a", "b"}),
    ...     frozenset({"b", "c"}),
    ... }
    >>> farfringe(subgraph, graph) # doctest: +SKIP
    {frozenset({'d', 'b'})}
    """
    subgraph = set(subgraph)
    if not subgraph <= set(graph):
        raise ValueError("{} is not subgraph of {}".format(subgraph, graph))
    subgraph_vertices = frozenset.union(*subgraph)
    near_edges = {k for k in graph if len(k & subgraph_vertices) == 1}
    return near_edges - subgraph


def prim(graph):
    """
    https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9F%D1%80%D0%B8%D0%BC%D0%B0
    https://en.wikipedia.org/wiki/Prim%27s_algorithm
    >>> a = {
    ...     frozenset({"d", "a"}): 5,
    ...     frozenset({"d", "b"}): 9,
    ...     frozenset({"d", "e"}): 15,
    ...     frozenset({"d", "f"}): 6,
    ...     frozenset({"b", "a"}): 7,
    ...     frozenset({"e", "b"}): 7,
    ...     frozenset({"c", "b"}): 8,
    ...     frozenset({"c", "e"}): 5,
    ...     frozenset({"f", "e"}): 8,
    ...     frozenset({"e", "g"}): 9,
    ...     frozenset({"f", "g"}): 11,
    ... }
    >>> prim(a) # doctest:
    [
        frozenset({"a", "d"}),
        frozenset({"f", "d"}),
        frozenset({"a", "b"}),
        frozenset({"b", "e"}),
        frozenset({"c", "e"}),
        frozenset({"g", "e"}),
    ]
    """
    tree = [min(graph, key=graph.get)]
    for i in range(2, len(frozenset.union(*graph))):
        tree.append(min(farfringe(tree, graph), key=graph.get))
    return tree
