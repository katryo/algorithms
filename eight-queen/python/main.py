from itertools import repeat


def solve():
    def backtrack(cur, rest, results):
        if not rest:
            results.append(cur)
        for j, row in enumerate(rest):
            diagonal_hit = False
            for i in range(len(cur)):
                if abs(cur[i]-row) == abs(len(cur)-i):
                    diagonal_hit = True
                    break
            if diagonal_hit:
                continue
            backtrack(cur + [row], rest[:j] + rest[j+1:], results)

    ans = []
    backtrack([], list(range(8)), ans)
    return ans


def show(positions):
    for position in positions:
        print('================')
        for i in range(len(position)):
            l = list(repeat(' ', 8))
            l[position[i]] = 'Q'
            row = '|'.join(l)
            print(row)
        print('================')


if __name__ == '__main__':
    positions = solve()
    show(positions)

