
def cost_starts_at(vertex, costs):
    vertices = len(costs)
    table = [[-1] * (2**vertices) for _ in range(vertices)]
    table[vertex][1 << vertex] = 0
    for v in range(vertices):
        table[v][1 << v] = costs[vertex][v]

    def recurse(v, state):
        if table[v][state] != -1:
            return table[v][state]
        ret = float('inf')
        for prev in range(vertices):
            if prev == v:
                continue
            if state & (1 << prev):
                cand = recurse(prev, state ^ (1 << v)) + costs[prev][v]
                ret = min(ret, cand)
        table[v][state] = ret
        return ret

    ans = float('inf')
    for v in range(vertices):
        cost_to_visit_all = recurse(v, (1 << vertices)-1)
        ans = min(ans, cost_to_visit_all + costs[v][vertex])
    return ans


def solve(costs):
    ans = float('inf')
    ans_vertex = -1
    for v in range(len(costs)):
        cand = cost_starts_at(v, costs)
        if cand < ans:
            ans = cand
            ans_vertex = v
    return ans, ans_vertex


with open("input1.txt", "r") as file:
    vertices = int(file.readline())
    costs = [[]] * vertices
    i = 0
    while True:
        line = file.readline()
        if not line:
            break
        costs[i] = [int(num) for num in line.split(' ')]
        # costs[i] = list(map(lambda x: int(x), line.split(' ')))
        i += 1
    print(solve(costs))
    # for i, line in enumerate(iter(file.readline, "")):
    #     costs[i] = list(map(lambda x: int(x), line.split(' ')))
    # print(solve(costs))




