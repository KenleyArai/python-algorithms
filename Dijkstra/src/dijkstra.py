from collections import deque, defaultdict
import collections
from heapq import heappush, heappop


def create_adj_matrix(vertices):
    graph = collections.defaultdict(lambda: collections.defaultdict(int))

    for u, v, w in vertices:
        graph[u][v] = w

    return graph


def create_adj_list(vertices):
    graph = collections.defaultdict(list)
    for u, v, w in vertices:
        graph[u].append((v, w))

    return graph


def init_ss(graph, s):
    dist = [float('Inf')]*len(graph)
    dist[s] = 0
    parent = [False]*len(graph)
    return dist, parent


def min_dist(graph, dist, spt, verts):
    return min(verts, key=lambda vertex: vertex[0])


def dijk(graph, s):
    def _relax(u, v):
        if D[u] + graph[u][v] < D[v]:
            D[v], P[v], = D[u] + graph[u][v], u
            return True

    D = defaultdict(lambda: float('Inf'))
    D[s] = 0

    P, Q, S = {}, [(0, s)], set()

    while Q:
        _, u = heappop(Q)

        if not (u in S):
            S.add(u)

            for v in graph[u]:
                _relax(u, v)
                heappush(Q, (D[v], v))
    return D


def prim(G, s):
    P, Q = {}, [(0, None, s)]

    while Q:

        _, p, u = heappop(Q)

        if not (u in P):
            P[u] = p
            for v, w in G[u]:
                heappush(Q, (w, u, v))
    return P


A = [
    (0, 1, 1),
    (1, 0, 1),
    (0, 3, 3),
    (3, 0, 3),
    (0, 2, 4),
    (2, 0, 4),
    (1, 3, 2),
    (3, 1, 2),
    (2, 3, 5),
    (3, 2, 5),
]

G = create_adj_matrix(A)
# print(G)

#print(dijk(G, 0))

G = create_adj_list(A)
# print(G)

print(prim(G, 0))
