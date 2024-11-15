import java.util.ArrayDeque;
import java.util.Queue;

import problem422.Node;

public class problem426 {
    
    public static void main(String[] args) {

    }

    public static int findLevelMinSum(Node rootNode) {
        if (rootNode == null) {
            return -1;
        }
        int minSum = rootNode.getValue();
        int minSumLvl = 0;
        int tmpMinSum = 0;
        int currentLevel = 1;
        Queue<Node> nodesAtLevel = new ArrayDeque<Node>();
        if (rootNode.getRight() != null) {
            nodesAtLevel.add(rootNode.getRight());
        }
        if (rootNode.getLeft() != null) {
            nodesAtLevel.add(rootNode.getLeft());
        }

        while (nodesAtLevel.size() != 0) {
            int lvlSize = nodesAtLevel.size();

            while (lvlSize > 0) {
                Node currNode = nodesAtLevel.poll();
                tmpMinSum += currNode.getValue();
                if (currNode.getRight() != null) {
                    nodesAtLevel.add(currNode.getRight());
                }
                if (currNode.getLeft() != null) {
                    nodesAtLevel.add(currNode.getLeft());
                }
                lvlSize--;
            }

            if (tmpMinSum < minSum) {
                minSum = tmpMinSum;
                minSumLvl = currentLevel;
            }
            tmpMinSum = 0;
            currentLevel ++;
        }
        return minSumLvl;
    }

}
