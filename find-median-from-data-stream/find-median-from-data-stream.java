class MedianFinder {
    
    PriorityQueue<Integer> lo;
    PriorityQueue<Integer> hi;

    /** initialize your data structure here. */
    public MedianFinder() {
        this.lo = new PriorityQueue<>((i1, i2) -> Integer.compare(i2, i1)); // max heap
        this.hi = new PriorityQueue<>(); // min heap
    }
    
    public void addNum(int num) {
        if (lo.isEmpty()) {
            lo.add(num);
            System.out.println("Add to lo");
            return;
        }
        
        if (hi.isEmpty() || num < hi.peek()) {
            lo.add(num);
            System.out.println("Add to lo");
        } else {
            hi.add(num);
            System.out.println("Add to hi");
        }
        
        if (lo.size() > hi.size() + 1) {
            int mid = lo.poll();
            hi.add(mid);
            System.out.println("Move from lo to hi");
        }
        
        if (hi.size() > lo.size()) {
            int mid = hi.poll();
            lo.add(mid);
            System.out.println("Move from hi to lo");
        }
    }
    
    public double findMedian() {
        if (lo.size() == hi.size()) {
            System.out.println("Take average of lo and hi");
            return (double)(lo.peek() + hi.peek()) / 2;
        } else {
            System.out.println("Take from lo");
            return lo.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */