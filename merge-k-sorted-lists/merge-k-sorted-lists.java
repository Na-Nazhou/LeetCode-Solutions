/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((l1, l2) -> Integer.compare(l1.val, l2.val));
        
        for (ListNode l : lists) {
            if (l != null) {
                pq.add(l);
            }
        }
        
        ListNode dummyHead = new ListNode();
        ListNode prev = dummyHead;
        
        while (!pq.isEmpty()) {
            ListNode l = pq.poll();
            prev.next = new ListNode(l.val);
            prev = prev.next;
            
            if (l.next != null) {
                pq.add(l.next);
            }
        }
        
        return dummyHead.next;
    }
}