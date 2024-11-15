public class problem394 {

    public class Node {
        private int value;
        private Node right;
        private Node left;

        public int getValue() {
            return this.value;
        }

        public Node getRight() {
            return this.right;
        }

        public Node getLeft() {
            return this.left;
        }
    }

    public boolean findSumPath(Node currentNode, int target) {
        if (currentNode == null) {
            return false;
        }
        if (currentNode.getLeft() == null && currentNode.getRight() == null) {
            return target == currentNode.getValue();
        }
        return findSumPath(currentNode.getLeft(), target - currentNode.getValue()) 
        || findSumPath(currentNode.getRight(), target - currentNode.getValue());
    }

}