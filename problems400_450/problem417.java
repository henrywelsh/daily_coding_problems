import java.util.LinkedList;
import java.util.Objects;

public class problem417 {

    public static void main(String[] args) {
        LinkedList<Integer> sampleList = new LinkedList<>();

        sampleList.add(3);
        sampleList.add(4);
        sampleList.add(-7);
        sampleList.add(5);
        sampleList.add(-6);
        sampleList.add(6);

        removeZeroSum(sampleList);
    }


    public static void removeZeroSum(LinkedList<Integer> currentList) {
        for (int i = 0; i < currentList.size(); i++) {
            int sum = currentList.get(i);
            for (int j = i + 1; j < currentList.size(); j++) {
                sum += currentList.get(j);
                if (sum == 0) {
                    System.out.println("Found 0 sum between indexes: (" + i + ", " + j + ")");
                    for (int k = j; k >= i; k--) {
                        System.out.println("Removing index: " + k);
                        currentList.remove(k);
                        System.out.println(currentList);
                    }
                    break;
                }
            }
        }
        System.out.println(currentList);
    }

}