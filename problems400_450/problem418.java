import java.util.Arrays;

public class problem418 {
    
    public static void main(String[] args) {
        testPeakAndValleyPattern();
        testLargerFollowedBySmaller();
        testDescendingPattern();
        testPlateauAfterIncrease();
        testSingleElement();
        testEmptyArray();
        
        System.out.println("All tests passed.");
    }

    private static void testPeakAndValleyPattern() {
        int[] linesOfCode = {5, 10, 5, 10, 5};
        int[] expected = {1, 2, 1, 2, 1};
        assert java.util.Arrays.equals(expected, determineBonus(linesOfCode)) 
            : "Test failed: Peak and Valley Pattern";
    }

    private static void testLargerFollowedBySmaller() {
        int[] linesOfCode = {1, 2, 3, 4, 1};
        int[] expected = {1, 2, 3, 4, 1};
        assert java.util.Arrays.equals(expected, determineBonus(linesOfCode)) 
            : "Test failed: Larger Followed by Smaller";
    }

    private static void testDescendingPattern() {
        int[] linesOfCode = {5, 4, 3, 2, 1};
        int[] expected = {5, 4, 3, 2, 1};
        assert java.util.Arrays.equals(expected, determineBonus(linesOfCode)) 
            : "Test failed: Descending Pattern";
    }

    private static void testPlateauAfterIncrease() {
        int[] linesOfCode = {1, 2, 2, 3, 2};
        int[] expected = {1, 2, 1, 2, 1};
        assert java.util.Arrays.equals(expected, determineBonus(linesOfCode)) 
            : "Test failed: Plateau After Increase";
    }

    private static void testSingleElement() {
        int[] linesOfCode = {100};
        int[] expected = {1};
        assert java.util.Arrays.equals(expected, determineBonus(linesOfCode)) 
            : "Test failed: Single Element";
    }

    private static void testEmptyArray() {
        int[] linesOfCode = {};
        int[] expected = {};
        assert java.util.Arrays.equals(expected, determineBonus(linesOfCode)) 
            : "Test failed: Empty Array";
    }


    public static int[] determineBonus(int[] linesOfCode) {
        if (linesOfCode.length == 0) {
            return new int[0];
        }

        int[] bonuses = new int[linesOfCode.length];
        for (int i = 0; i < bonuses.length; i++) {
            bonuses[i] = 1;
        }

        for (int i = 1; i < bonuses.length; i++) {
            if (linesOfCode[i] > linesOfCode[i-1]) {
                bonuses[i] = bonuses[i-1] + 1;
            }
        }

        for (int i = bonuses.length - 1; i > 0; i--) {
            if (linesOfCode[i - 1] > linesOfCode[i]) {
                if (bonuses[i - 1] <= bonuses[i]) {
                    bonuses[i - 1] = bonuses[i] + 1;
                }
            }
        }

        return bonuses;
    }

}
