from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight

    def __lt__(self, other):
        return other.weight < self.weight  # Compare based on weight in descending order

def bound(u, n, W, arr):
    # Calculate the upper bound
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    # Add items to the knapsack until the weight limit is reached
    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    # Calculate the fractional contribution
    if j < n:
        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)

    return profit_bound

def knapsack(W, arr, n):
    # Sort items
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0)  #
    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():
        u = priority_queue.get()

        if u.level == -1:
            v = Node(0, 0, 0)  # Starting node
        elif u.level == n - 1:
            continue  # Skip if it is the last level
        else:
            v = Node(u.level + 1, u.profit, u.weight)

        v.weight += arr[v.level].weight
        v.profit += arr[v.level].value

        # update max
        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v_bound = bound(v, n, W, arr)
        # Add the node to the queue
        if v_bound > max_profit:
            priority_queue.put(v)

        v = Node(u.level + 1, u.profit, u.weight)
        v_bound = bound(v, n, W, arr)
        # Add the node to the priority queue
        if v_bound > max_profit:
            priority_queue.put(v)

    return max_profit

W = 10
arr = [
    Item(2, 40),
    Item(3.14, 50),
    Item(1.98, 100),
    Item(5, 95),
    Item(3, 30)
]
n = len(arr)

max_profit = knapsack(W, arr, n)
print("Max = ", max_profit)
