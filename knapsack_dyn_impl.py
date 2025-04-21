def memKnapsack(i, wt, val, j):
    global f  # a global dp table for knapsack
    if f[i][j] < 0:
        if j < wt[i - 1]:
            val = memKnapsack(i - 1, wt, val, j)
        else:
            val = max(
                memKnapsack(i - 1, wt, val, j),
                memKnapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        f[i][j] = val
    return f[i][j]


def knapsack(w, wt, val, n):
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    return dp[n][w_], dp


def knapsack_with_example_solution(w: int, wt: list, val: list):
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError("must be either lists or tuples")

    num_items = len(wt)
    if num_items != len(val):
        msg = (f"Got {num_items} weights and {len(val)} values")
        raise ValueError(msg)
    for i in range(num_items):
        if not isinstance(wt[i], int):
            msg = (f"type {type(wt[i])} at index {i}")
            raise TypeError(msg)

    optimal_val, dp_table = knapsack(w, wt, val, num_items)
    example_optional_set: set = set()
    _build(dp_table, wt, num_items, w, example_optional_set)

    return optimal_val, example_optional_set


def _build(dp: list, wt: list, i: int, j: int, optimal_set: set):
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _build(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _build(dp, wt, i - 1, j - wt[i - 1], optimal_set)


val = [3, 2, 4, 4]
wt = [4, 3, 2, 3]
n = 4
w = 6
f = [[0] * (w + 1)] + [[0] + [-1] * (w + 1) for _ in range(n + 1)]
optimal_solution, _ = knapsack(w, wt, val, n)
print(optimal_solution)
print(memKnapsack(n, wt, val, w))  # switched the n and w

optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
assert optimal_solution == 8
assert optimal_subset == {3, 4}
print("Max = ", optimal_solution)
print("An optimal subset ", optimal_subset)