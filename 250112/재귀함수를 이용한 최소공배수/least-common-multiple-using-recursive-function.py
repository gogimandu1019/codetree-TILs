from math import gcd

n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

def lcm(a,b):
    return a * b // gcd(a,b)

def recursive_lcm(nums, x):
    if x == 1:
        return nums[0]
    else:
        return lcm(nums[x-1], recursive_lcm(nums, x-1))

print(recursive_lcm(arr, n))