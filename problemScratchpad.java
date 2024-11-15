import java.util.HashMap;
import java.util.Map;

public class problemScratchpad {

    public static void main(String[] args) {
        int[] nums = {3, 2, 4};
        int[] results = twoSum(nums, 7);
        System.out.println("Index 0: " + results[0] + " Index 1: " + results[1]);
    }

    public static int[] twoSum(int[] nums, int target) {
        int[] r = new int[2];
        Map<Integer, Integer> foundNums = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (foundNums.containsKey(nums[i])) {
                r[0] = foundNums.get(nums[i]);
                r[1] = i;
                return r;
            } else {
                foundNums.put(target - nums[i], i);
            }
        }
        return r;
    }
}
