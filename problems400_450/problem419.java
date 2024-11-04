import java.util.ArrayList;
import java.util.List;

public class problem419 {

    public static void main(String[] args) {
        // System.out.println(stepsToOne(10, 0, Integer.MAX_VALUE));


        System.out.println(findFactors(10));
        System.out.println(findFactors(100));
    }


    public static int stepsToOne(int startingNumber, int stepsTaken, int currMinPath) {
        if (startingNumber == 1) {
            return 1;
        }
        List<Integer> potentialPaths = findFactors(startingNumber);
        potentialPaths.add(startingNumber - 1);
        System.out.println("Potential paths from: " + startingNumber + " to evaluate: " + potentialPaths);

        int tmpMinPath = Integer.MAX_VALUE;
        for (Integer i : potentialPaths) {
            int minSteps = stepsToOne(i, stepsTaken + 1, currMinPath) + stepsTaken;
            System.out.println("Evaluating i: " + i + " with min steps: " + minSteps);
            if (minSteps < tmpMinPath) {
                tmpMinPath = minSteps;
            }
        }

        if (tmpMinPath < currMinPath) {
            return tmpMinPath;
        } else {
            return currMinPath;
        }
    }

    public static List<Integer> findFactors(int number) {
        List<Integer> factors = new ArrayList<>();
        int i = 2;
        while (i < Math.floor(Math.sqrt(number))) {
            if (number % i == 0) {
                factors.add(number/i);
            }
            i++;
        }
        return factors;
    }

}