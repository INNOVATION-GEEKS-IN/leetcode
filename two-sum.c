// URL : https://leetcode.com/problems/two-sum/

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]
 

// Constraints:

// 2 <= nums.length <= 103
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    int i, j;
    int *ret = calloc(2, sizeof(int));
    for (i = 0; i < numsSize; i++)
    {
        int key = target - nums[i];
        for (j = i + 1; j < numsSize; j++)
            if (nums[j] == key)
            {
                ret[0] = i;
                ret[1] = j;
            }
    }
    *returnSize = 2;
    return ret;
}