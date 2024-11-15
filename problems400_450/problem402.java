import java.util.ArrayList;
import java.util.Arrays;

public class problem402 {

    public static void main(String[] args) {
        System.out.println(findStrobogrammaticNumbers(3));
    }


    public static ArrayList<String> findStrobogrammaticNumbers(int numDigits) {
        if (numDigits == 0) {
            return new ArrayList<>();
        } else if (numDigits == 1) {
            return new ArrayList<String>(Arrays.asList("0", "1", "8"));
        }

        int n = 2;
        String[] rotatableNums = {"0", "1", "6", "8", "9"};
        String[] validMiddleNums = {"0", "1", "8"};
        ArrayList<String> strobNums = new ArrayList<>();
        strobNums.addAll(Arrays.asList(rotatableNums));
        strobNums.remove("0");
        ArrayList<String> newVals = new ArrayList<>();

        while (n <= numDigits/2) {
            for (int i = 0; i < strobNums.size(); i++) {
                for (int j = 0; j < rotatableNums.length; j++) {
                    newVals.add(strobNums.get(i) + rotatableNums[j]);
                }
            }
            strobNums.clear();
            strobNums.addAll(newVals);
            newVals.clear();
            n++;
        }

        for (int i = 0; i < strobNums.size(); i++) {
            String secondHalf = createStrobSecondHalf(strobNums.get(i));
            if (numDigits % 2 == 1) {
                for (String middleDigit : validMiddleNums) {
                    newVals.add(strobNums.get(i) + middleDigit + secondHalf);
                }
            } else {
                newVals.add(strobNums.get(i) + secondHalf);
            }
        }

        return newVals;
    }

    // Passing in the first half of a string we want to return the second half
    private static String createStrobSecondHalf(String currentString) {
        String secondHalfString = "";
        char[] currentNumCharArray = currentString.toCharArray();
        for (int i = currentNumCharArray.length - 1; i > -1; i--) {
            if (currentNumCharArray[i] == '0') {
                secondHalfString += '0';
            } else if (currentNumCharArray[i] == '1') {
                secondHalfString += '1';
            } else if (currentNumCharArray[i] == '6') {
                secondHalfString += '9';
            } else if (currentNumCharArray[i] == '8') {
                secondHalfString += '8';
            } else if (currentNumCharArray[i] == '9') {
                secondHalfString += '6';
            }
        }
        return secondHalfString;
    }
    
}
