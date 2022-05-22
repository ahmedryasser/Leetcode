class Solution {
    public int maxSubArray(int[] nums) {
        int currentArr =  nums[0];
        int maxArr = nums[0];
        for (int i = 1; i< nums.length; i++){
            currentArr = (nums[i]> (currentArr+nums[i]))? nums[i]:currentArr+nums[i];
            maxArr = (maxArr> currentArr)? maxArr: currentArr;
        }
        return maxArr;
    }
}