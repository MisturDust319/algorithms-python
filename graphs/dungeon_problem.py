# the dungeon problem is a pathfinding problem
# a r * c grid of of n rows and columns
# represents a "dungeon" that must be navigated from the start square to the end
# if possible, and each grid squares may be empty or obstructed
from data_structures import GraphAdjacencySet as Graph
from collections import deque

# first a grid representing the dugneon
# '.' represents an open space
# '#' an obstacle
# 's' the start
# 'e' the exit
dungeon = [
    ['s', '.', '#', '#', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '#', '.', '.'],
    [',', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'e', '.', '.', '.'],
]

# create a class of graph that can parse the grid
class DungeonGraph(Graph):
    def __init__(self, grid):
        # get the size of the grid
        self.r = r = len(grid)
        self.c = c = len(grid[0])
        # get the number of elements in the grid
        self.n = n = r * c
        # these are used to calculate adjacent nodes
        dx = 1
        dy = c

        # init an adjacency hash of n items
        super().__init__(n)

        for j in range(r):
            for i in range(c):
                current_item = grid[j][i]
                if current_item is not "#":
                    # the grid must be 'flattened' into n unique ids
                    # get the current id
                    u = i + j * c

                    # note if the current node is the start or end node
                    if current_item is "s":
                        self.start = u
                    elif current_item is "e":
                        self.end = u
                    # check for horizontal solutions
                    if i > 0 and grid[j][i-1] is not "#":
                        self.addEdge(u, u-dx)
                    if i < c-1 and grid[j][i+1] is not "#":
                        self.addEdge(u, u+dx)
                    # check for vertical solutions
                    if j > 0 and grid[j-1][i] is not "#":
                        self.addEdge(u, u-dy)
                    if j < r-1 and grid[j+1][i] is not "#":
                        self.addEdge(u, u+dy)

    def bfs(self):
        # a queue to pop found nodes onto
        # use the start position to begin your search
        queue = deque()
        queue.appendleft([self.start])
        # used to track visited nodes
        visited = { k : False for k in range(self.cardinality) }

        while queue:
            path = queue.pop()
            # the current node is the final element on the current path
            u = path[-1]

            # if the current node is the exit tile, return the current path
            if u == self.end:
                return path

            # mark the current node as visited
            visited[u] = True

            # otherwise, queue up adjacent nodes, if any
            for v in self.adjacencies[u]:
                # only go to unvisited nodes
                if not visited[v]:
                    # copy the current path
                    new_path = list(path)
                    # append the adjacent node to it
                    new_path.append(v)
                    # add it to the queue
                    queue.appendleft(new_path)

        # if there is no path, return an empty list
        return []


def driver():
    graph = DungeonGraph(dungeon)

    print("Path to exit:")
    path = graph.bfs()
    print(path) if len(path) else print("No path")

if __name__ == "__main__":
    driver()