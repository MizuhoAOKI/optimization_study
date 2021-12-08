# Solve knapsack problem with Dynamic Programming
""" Problem : 
Ref : https://qiita.com/keisuke-ota/items/504d66092671a67c1040
"""

import math
from matplotlib import pyplot as plt
from matplotlib import colors

## Problem settings
# N : number of stuffs
# W : maximum weight
# N, W = map(int, input().split())
N, W = 6, 7

# w[i] : weight of stuff i
# v[i] : value of stuff i
w = [2, 1, 3, 2, 1, 5]
v = [3, 2, 6, 1, 3, 8]

## Prepare DP table
# Let dp[i][j] be the minimum total weight when you pick up several stuffs numbered from 1 to i so that total value equals to j.
# L = max(dp)
# Initialize DP table with +infinity.
L = max(v) * math.ceil(W/min(w)) # theoretical maximum value in total.
dp = [[math.inf]*(L+1) for _ in range(N+1)]

## Set initial state.
dp[0][0] = 0

## Fill DP table
# Select stuffs to minimize total weight.
for i in range(N):
    for j in range(L+1):  
        # update dp[i+1][j] with recurrence relationship
        if j - v[i] >= 0:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i])
        else:
            dp[i+1][j] = dp[i][j]

# Look into dp[N][j] and get the final answer.
for i, d in enumerate(dp[N]):
    if d <= W:
        maxv = i
print(f"Maximum value is {maxv}")

# Plog figure
fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])
# prepare color map
normal = colors.Normalize(0, L)
colours = plt.cm.hot_r(normal(dp))
the_table=plt.table(cellText=dp, loc='center', rowLabels=range(N+1), colLabels=range(L+1), cellColours=colours)
plt.show()