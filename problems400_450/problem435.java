import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

class Node {
    private Integer value;
    private Node leftNode;
    private Node rightNode;

    Node(int value) {
        this.value = value;
    }

    public Integer getValue() {
        return this.value;
    }
    public void setValue(Integer value) {
        this.value = value;
    }

    public Node getLeftNode() {
        return this.leftNode;
    }
    public void setLeftNode(Node node) {
        this.leftNode = node;
    }

    public Node getRightNode() {
        return this.rightNode;
    }
    public void setRightNode(Node node) {
        this.rightNode = node;
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Node that)) {
            return false;
        }
        return Objects.equals(getValue(), that.getValue()) 
            && Objects.equals(getLeftNode(), that.getLeftNode()) 
            && Objects.equals(getRightNode(), that.getRightNode());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getValue(), getLeftNode(), getRightNode());
    }

}


public class problem435 {

    public static void main(String[] args) throws Exception {

        Node[] preOrd = {new Node(3), new Node(9), new Node(20), new Node(15), new Node(7)};
        Node[] inOrd = {new Node(9), new Node(3), new Node(15), new Node(20), new Node(7)};

        Node root = reconstructTree(preOrd, inOrd);

        // Print the tree (example: in-order traversal)
        printInOrder(root);
    }

    private static void printInOrder(Node node) {
        if (node == null) return;
        printInOrder(node.getLeftNode());
        System.out.print(node.getValue() + " ");
        printInOrder(node.getRightNode());
    }

    public static Node reconstructTree(Node[] preOrd, Node[] inOrd) throws Exception {
        if (preOrd.length != inOrd.length) throw new Exception();

        Map<Node, Integer> inOrdIndices = new HashMap<>();
        for (int i = 0; i < inOrd.length; i++) {
            inOrdIndices.put(inOrd[i], i);
        }

        return reconstructTreeHelper(preOrd, inOrdIndices, 0, preOrd.length - 1, 0, inOrd.length - 1);
    }

    public static Node reconstructTreeHelper(Node[] preOrd, Map<Node, Integer> inOrdIndices, int preOrdStart, int preOrdEnd, int inOrdStart, int inOrdEnd) throws Exception {
        if (preOrdStart > preOrdEnd || inOrdStart > inOrdEnd) return null;

        Node rootNode = preOrd[preOrdStart];
        int splitIndex = inOrdIndices.get(rootNode);

        int leftSubTreeSize = splitIndex - inOrdStart;

        rootNode.setLeftNode(reconstructTreeHelper(preOrd, inOrdIndices, preOrdStart + 1, preOrdStart + leftSubTreeSize, inOrdStart, splitIndex - 1));
        rootNode.setRightNode(reconstructTreeHelper(preOrd, inOrdIndices, preOrdStart + leftSubTreeSize + 1, preOrdEnd, splitIndex + 1, inOrdEnd));
        return rootNode;
    }

}
