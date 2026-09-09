class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> existingSet = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (existingSet.contains(nums[i])) {
                return true;
            }
            existingSet.add(nums[i]);
        }
        return false;
    }
}
