# https://leetcode.com/problems/paint-fence

# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.

def solution(n, k):
    if n == 1:
        return k
    same, diff = k, k*(k-1)
    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff


n = 3
k = 3
print(solution(3, k))