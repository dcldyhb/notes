---
title: LeetCode 每日一题
date: 2023-10-31
tags:
  - LeetCode
  - 编程
  - 算法
categories:
  - 个人学习
  - 编程
---

# LeetCode 每日一题

## 2025-10-31

[3289.数字小镇中的捣蛋鬼](https://leetcode.cn/problems/the-two-sneaky-numbers-of-digitville/)

### 问题描述

在数字小镇 **Digitville** 中，存在一个数字列表 `nums`，其中包含从 `0` 到 `n - 1` 的整数。每个数字本应**只出现一次**，然而，有**两个**顽皮的数字额外多出现了一次，使得列表变得比正常情况下更长。

为了恢复 **Digitville** 的和平，作为小镇中的名侦探，请你找出这两个顽皮的数字。

返回一个长度为 2 的数组，包含这两个数字（顺序任意）。

```cpp
class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        int n = nums.size() - 2;
        vector<int> count(n,0);
        vector<int> result;
        for (int num : nums) {
            if (count[num] == 0) {
                count[num]++;
            }
            else {
                result.push_back(num);
            }
        }

        return result;
    }
};
```
