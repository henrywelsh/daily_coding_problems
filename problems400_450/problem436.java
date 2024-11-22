public class problem436 {
    public static void main(String[] args) {
        
    }
}

class Node {
    private int value;
    private Node next;

    Node(int value, Node nextNode) {
        this.value = value;
        this.next = nextNode;
    }

    Node(int value) {
        this.value = value;
        this.next = null;
    }

    public Node getNext() {
        return this.next;
    }

    public int getValue() {
        return this.value;
    }
}

class Stack {
    private Node[] headNodes;
    
    Stack() {
        Node[] initHeadNodes = {null, null, null};
        this.headNodes = initHeadNodes;
    }

    public Integer pop(int stack_number) {
        Node headNode = this.headNodes[stack_number];
        if (headNode == null) return null;
        this.headNodes[stack_number] = headNode.getNext();
        return headNode.getValue();
    }

    public void push(int item, int stack_number) {
        Node currentHead = this.headNodes[stack_number];
        if (currentHead == null) {
            Node newHead = new Node(item);
            this.headNodes[stack_number] = newHead;
        } else {
            Node newHead = new Node(item, currentHead);
            this.headNodes[stack_number] = newHead;
        }
    }
}