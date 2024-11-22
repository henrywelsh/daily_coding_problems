import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class problem437 {

    public static void main(String[] args) {
        Set<Character> chSet = new HashSet<>();
        chSet.add('a');
        chSet.add('e');
        chSet.add('i');
        System.out.println(shortestSubString("figehaeci", chSet));
    }
 
    
    public static String shortestSubString(String original, Set<Character> contChar) {
        List<Integer> foundIndices = new ArrayList<>();
        Map<Character, Integer> charLastOccurence = new HashMap<>();
        char[] strChars = original.toCharArray();
        int minSize = strChars.length + 1;
        String retStr = null;
        for (int i = 0; i < strChars.length; i++) {
            if (contChar.contains(strChars[i])) {
                if (charLastOccurence.containsKey(strChars[i])) {
                    foundIndices.remove(charLastOccurence.get(strChars[i]));
                    foundIndices.add(i);
                } else {
                    foundIndices.add(i);
                }
                charLastOccurence.put(strChars[i], i);
                if (foundIndices.size() == contChar.size()) {
                    Collections.sort(foundIndices);
                    int subStrSize = foundIndices.get(foundIndices.size() - 1) - foundIndices.get(0);
                    if (subStrSize < minSize) {
                        minSize = subStrSize;
                        retStr = original.substring(foundIndices.get(0), foundIndices.get(foundIndices.size() - 1) + 1);
                    }
                }
            }
        }
    
        return retStr;
    }
}
