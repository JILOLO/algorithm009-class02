学习笔记

# 数组
数组是一种数据结构。Leetcode上tag成数组的题有很多，但是一打开大部分都用到了其他的编程思想，比如哈希表，滑动窗口，动态规划，甚至回溯什么的。这次作业给的题基本上就是考察数组的，我觉得就是在考察 for， while， if 的使用，是最基础也最重要的。需要背的：

- 优化版的Two Sum

- ```python
store = 0
for i in range(len(nums)):
    nums[i], nums[store] = nums[store], nums[i]
    store += 1
```
- ```python
left, right = 0, len(nums)
while left < right:
    pass
    # if, for, while...
    left += 1
    right -= 1
```
# 链表
迭代，递归，dummy node...，注意边界条件。大致分三步：
1. 记住节点
2. 改变.next
3. 返回头节点

