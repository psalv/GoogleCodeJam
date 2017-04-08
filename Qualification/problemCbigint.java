import java.util.*;
import java.io.*;
import java.util.ArrayList;
import java.lang.Math;
import java.math.BigInteger;


class HasKey2 {
    private BigInteger key;
    BigInteger l;
    BigInteger r;

    public HasKey2(BigInteger key, BigInteger l, BigInteger r) {
        this.key = key;
        this.l = l;
        this.r = r;
    }

    public BigInteger getKey(){
        return this.key;
    }

    public String toString(){
        return key.toString();
    }
}


class MinHeap<E extends HasKey2> {

    private ArrayList<E> heap = new ArrayList<>();

    public MinHeap(){
        // no initialization data.
    }

    // Takes O(nlgn) time.
    public MinHeap(E data[]){
        for(E i: data){
            insert(i);
        }
    }

    // Takes O(lgn) time.
    public void insert(E data){
        heap.add(data);
        buildMinHeapify(heap.size() - 1);
    }

    // Takes O(lgn) time since we can look at each parent until we reach the root.
    private void buildMinHeapify(int i){
        if(i == 0){
            return;
        }

        // Determining the parent.
        int adjust = i % 2 == 0 ? 1 : 0;
        int parent = (int)Math.floor(i/2.0) - adjust;

        // Since we assume that the current min heap maintains the min heap property,
        // we need only look at the parent.
        // If the new node is less than the parent, than it is also less than any of the children's parents.
        // We can therefore swap the parent and the new node.
        if(heap.get(parent).getKey().compareTo(heap.get(i).getKey()) == 1){
            E temp = heap.get(parent);
            heap.set(parent, heap.get(i));
            heap.set(i, temp);

            // We do this until we reach the root, or until our node is in the correct place (parent is smaller).
            buildMinHeapify(parent);
        }
    }

    // Takes O(lgn) time.
    private void minHeapify(int i){
        int left = 2*i + 1;
        int right = 2*i + 2;
        int size = heap.size() - 1;

        if(left > size){
            return;
        }

        // Need to determine the smallest element between i and it's two children
        int smallest = heap.get(left).getKey().compareTo(heap.get(i).getKey()) == -1 ? left : i;

        if(right <= size) {
            smallest = heap.get(right).getKey().compareTo(heap.get(smallest).getKey()) == -1 ? right : smallest;
        }

        // If the children are smaller we need to swap and recurse upwards.
        if(smallest != i){
            E temp = heap.get(smallest);
            heap.set(smallest, heap.get(i));
            heap.set(i, temp);

            minHeapify(smallest);
        }
    }

    // To extract the min it takes O(lgn) time since we need to min-heapify the root.
    public E extractMin(){
        int last = heap.size() - 1;

        // Swap with min with the end, remove the end, and min-heapify the root.
        E min = heap.get(0);
        heap.set(0, heap.get(last));
        heap.set(last, min);
        heap.remove(last);

        minHeapify(0);
        return min;
    }

    // Viewing the min takes O(1).
    public E getMin(){
        return heap.get(0);
    }

    public boolean isEmpty(){
        return heap.size() == 0;
    }

    public String toString(){
        return heap.toString();
    }

}



public class problemC {


    public static HasKey2 sol(BigInteger n, BigInteger k){

        MinHeap<HasKey2> stalls = new MinHeap<>();
        stalls.insert(new HasKey2(n.add(BigInteger.ONE), BigInteger.ZERO, n.add(BigInteger.ONE)));
        HasKey2 lowest = null;

        for(int i = 0; k.compareTo(BigInteger.valueOf(i)) == 1; i++){

            lowest = stalls.extractMin();
            BigInteger mid = (lowest.r.add(lowest.l)).divide(BigInteger.valueOf(2));
            BigInteger a = lowest.l.subtract(mid);
            BigInteger b = mid.subtract(lowest.r);
            stalls.insert(new HasKey2(a, lowest.l, mid));
            stalls.insert(new HasKey2(b, mid, lowest.r));

        }

        return lowest;
    }




    public static void main(String[] args) {

        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
        for (int i = 1; i <= t; ++i) {
            BigInteger n = in.nextBigInteger();
            BigInteger k = in.nextBigInteger();
            HasKey2 solution = sol(n, k);
            BigInteger mid = solution.r.add(solution.l).divide(BigInteger.valueOf(2));
            BigInteger a = solution.r.subtract(mid).subtract(BigInteger.ONE);
            BigInteger b = mid.subtract(solution.l).subtract(BigInteger.ONE);
            if(a.compareTo(b) == 1){
                System.out.println("Case #" + i + ": " + a.toString() + " " + b.toString());
            } else{
                System.out.println("Case #" + i + ": " + b.toString() + " " + a.toString());
            }

        }
    }

}
