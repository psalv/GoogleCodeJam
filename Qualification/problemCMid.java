import java.util.*;
import java.io.*;
import java.util.ArrayList;
import java.lang.Math;


class HasKey{
    private Integer key;
    int l;
    int r;

    public HasKey(Integer key, int l, int r) {
        this.key = key;
        this.l = l;
        this.r = r;
    }

    public int getKey(){
        return this.key;
    }


    public String toString(){
        return key.toString();
    }
}


class MinHeap<E extends HasKey> {

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
        if(heap.get(parent).getKey() > heap.get(i).getKey()){
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
        int smallest = heap.get(left).getKey() < heap.get(i).getKey() ? left : i;

        if(right <= size) {
            smallest = heap.get(right).getKey() < heap.get(smallest).getKey() ? right : smallest;
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



public class problemCMid {


    public static HasKey sol(int n, int k){

        MinHeap<HasKey> stalls = new MinHeap<>();
        stalls.insert(new HasKey(n + 1, 0, n+1));
        HasKey lowest = null;

        for(int i = 0; i < k; i++){

            lowest = stalls.extractMin();
            int mid = ((Double)(Math.floor((lowest.r + lowest.l) / 2))).intValue();
            int a = lowest.l - mid;
            int b = mid - lowest.r;
            stalls.insert(new HasKey(a, lowest.l, mid));
            stalls.insert(new HasKey(b, mid, lowest.r));
        }

        return lowest;
    }




    public static void main(String[] args) {

        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
        for (int i = 1; i <= t; ++i) {
            int n = in.nextInt();
            int k = in.nextInt();
            HasKey solution = sol(n, k);
            int mid = ((Double)(Math.floor((solution.r + solution.l) / 2))).intValue();
            System.out.println("Case #" + i + ": " + Math.max(solution.r - mid - 1, mid - solution.l - 1) + " " + Math.min(solution.r - mid - 1, mid - solution.l - 1));
        }
    }

}