public class problem422 {

    public static void main(String[] args) {

        Node leftLeftChild = new Node(null, null, 4);
        Node leftChild = new Node(leftLeftChild, null, 5);
        Node rightChild = new Node(null, null, 5);
        Node rootNode = new Node(null, rightChild, 1);
        Node rootNode2 = new Node(leftChild, null, 2);

        Node merged = mergeTrees(rootNode, rootNode2);
        System.out.println(merged.getValue());
        System.out.println(merged.getLeft().getLeft().getValue());

    }

    public Node mergeTrees(Node tree1, Node tree2) {
        if (tree1 == null) {
            return tree2;
        } else if (tree2 == null) {
            return tree1;
        }
        return new Node(mergeTrees(tree1.getLeft(), tree2.getLeft()),
            mergeTrees(tree1.getRight(), tree2.getRight()),  
            tree1.getValue() + tree2.getValue());
    }


    public class Node {
        private Node left;
        private Node right;
        private int value;

        public Node(Node leftNode, Node rightNode, int value) {
            this.left = leftNode;
            this.right = rightNode;
            this.value = value;
        }

        public Node getLeft() {
            return this.left;
        }

        public Node getRight() {
            return this.right;
        }

        public void setLeft(Node leftNode) {
            this.left = leftNode;
        }

        public void setRight(Node rightNode) {
            this.right = rightNode;
        }

        public int getValue() {
            return this.value;
        }

        public void setValue(int value) {
            this.value = value;
        }
    }

    
}
