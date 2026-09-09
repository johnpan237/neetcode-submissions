class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> existingNums = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (existingNums.contains(nums[i])) {
                return true;
            }
            existingNums.add(nums[i]);
        }

        return false;
    }
}
