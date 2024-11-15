import java.util.ArrayList;
import java.util.Collections;

public class problem404 {

    public int maxRoomsRequired(int[][] classTimes) {
        ArrayList<Integer> startTimes = new ArrayList<>();
        ArrayList<Integer> endTimes = new ArrayList<>();
        for (int[] classInstance : classTimes) {
            startTimes.add(classInstance[0]);
            endTimes.add(classInstance[1]);
        }
        Collections.sort(startTimes);
        Collections.sort(endTimes);
        int numActiveRooms = 0;
        int maxActiveRooms = 0;
        int currentStartTimeIndex = 0;
        int currentEndTimeIndex = 0;

        while (currentStartTimeIndex < startTimes.size()) {
            if (startTimes.get(currentStartTimeIndex) < endTimes.get(currentEndTimeIndex)) {
                numActiveRooms++;
                maxActiveRooms = Math.max(numActiveRooms, maxActiveRooms);
                currentStartTimeIndex++;
            } else {
                numActiveRooms--;
                currentEndTimeIndex++;
            }
        }
        return maxActiveRooms;
    }
    
}
