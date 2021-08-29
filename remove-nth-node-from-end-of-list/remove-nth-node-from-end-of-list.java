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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode slowPtr = head;
        ListNode fastPtr = head;
        
        while (n > 0) {
            fastPtr = fastPtr.next;
            n--;
        }
        
        if (fastPtr == null) {
            return head.next;
        }
        
        while (fastPtr.next != null) {
            fastPtr = fastPtr.next;
            slowPtr = slowPtr.next;
        }
        
        slowPtr.next = slowPtr.next.next;
        
        return head;
    }
}