class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def doSomething(N, routes):
    uf = UnionFind(N)

    components = N
    for route in routes:
        city1, city2 = route
        root1 = uf.find(city1)
        root2 = uf.find(city2)

        if root1 != root2:
            uf.union(root1, root2)
            components -= 1

    if components == 1:
        return 0
    elif components > 1:
        return components - 1
    else:
        return -1

N = int(input()) 
routes = []
for i in range(n:=int(input())):
    routes.append(list(map(int, input().split())))
outputVal = doSomething(N, routes)
print (outputVal)
