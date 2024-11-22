import java.util.Comparator;
import java.util.PriorityQueue;

public class problem438 {
    
}

class HeapNode<T> {
    private int value;
    private T object;

    HeapNode(int value, T object) {
        this.value = value;
        this.object = object;
    }

    public int getValue() {
        return this.value;
    }

    public T getObject() {
        return this.object;
    }
}

class HeapStack<T> {
    private PriorityQueue<HeapNode<T>> pq;

    HeapStack() {
        Comparator<HeapNode<T>> comp = (o1 , o2) -> Integer.compare(o2.getValue(), o1.getValue());
        this.pq = new PriorityQueue<>(comp);
    }

    public void push(T object) {
        HeapNode<T> currMax = this.pq.peek();
        HeapNode<T> newMax;
        if (currMax == null) {
            newMax = new HeapNode<T>(1, object);
        }else {
            newMax = new HeapNode<T>(currMax.getValue() + 1, object);
        }
        this.pq.add(newMax);
    }

    public T pop() throws Exception {
        HeapNode<T> currTop = this.pq.poll();
        if (currTop == null) {
            throw new Exception("Unable to pop as the heap is empty");
        } else {
            return currTop.getObject();
        }
    }
}
