import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class problem386 {

    public static void main(String[] args) {
        System.out.println(sortStringByFreq("tweet"));
    }

    // public static String sortStringByFreq(String orgStr) {
    //     char[] strChars = orgStr.toCharArray();
    //     Map<Character, Integer> charFreq = new HashMap<Character, Integer>();
    //     for (char ch : strChars) {
    //         if (charFreq.containsKey(ch)) { 
    //             charFreq.put(ch, charFreq.get(ch) + 1); 
    //         } else {
    //             charFreq.put(ch, 1);
    //         }
    //     }

    //     List<Map.Entry<Character, Integer>> list = new ArrayList<Map.Entry<Character, Integer>>(charFreq.entrySet());
    //     Collections.sort(list, new Comparator<Map.Entry<Character, Integer>>() {
    //         public int compare(Map.Entry<Character, Integer> o1, Map.Entry<Character, Integer> o2) {
    //             return o2.getValue().compareTo(o1.getValue());
    //         }
    //     });

    //     int i = 0;
    //     int n = 0;
    //     while (i < strChars.length) {
    //         int freq = list.get(n).getValue();
    //         while (freq > 0) {
    //             strChars[i] = list.get(n).getKey();
    //             freq--;
    //             i++;
    //         }
    //         n++;
    //     }
    //     return new String(strChars);
    // }

    public static String sortStringByFreq(String orgString) {
        char[] chArr = orgString.toCharArray();
        Map<Character, Integer> chFreq = new HashMap<>();
        for (char ch : chArr) {
            if (chFreq.containsKey(ch)) chFreq.put(ch, chFreq.get(ch) + 1);
            else chFreq.put(ch, 1);
        }
        Comparator<Map.Entry<Character, Integer>> comparator = new Comparator<Map.Entry<Character,Integer>>() {
            @Override
            public int compare(Map.Entry<Character, Integer> o1, Map.Entry<Character, Integer> o2) {
                return Integer.compare(o2.getValue(), o1.getValue());
            }
        };

        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(comparator);
        pq.addAll(chFreq.entrySet());
        StringBuilder response = new StringBuilder();
        while (!pq.isEmpty()) {
            Map.Entry<Character, Integer> e = pq.poll();
            int freq = e.getValue();
            while (freq > 0) {
                response.append(e.getKey());
                freq--;
            }
        }
        return response.toString();
    }
}
