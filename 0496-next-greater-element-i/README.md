<h2><a href="https://leetcode.com/problems/next-greater-element-i">496. Next Greater Element I</a></h2><h3>Easy-Arrays</h3><hr><p>The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.</p>

<p>You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.</p>

<p>For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.</p>

<p>Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,1,2], nums2 = [1,3,4,2]
<strong>Output:</strong> [-1,3,-1]
<strong>Explanation:</strong> The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,4], nums2 = [1,2,3,4]
<strong>Output:</strong> [3,-1]
<strong>Explanation:</strong> The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
</pre>

<p><strong>Constraints:</strong></p>

<ul>
  <li>1 <= nums1.length <= nums2.length <= 1000</li>
  <li>0 <= nums1[i], nums2[i] <= 104</li>
  <li>All integers in nums1 and nums2 are unique.</li>
  <li>All the integers of nums1 also appear in nums2.</li>
</ul>

<p><strong>Follow up:</strong> Could you find an O(nums1.length + nums2.length) solution?</p>
