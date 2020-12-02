/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int i = 0;
        ListNode slow = head;
        ListNode fast = head;
        while (i < n) {
            fast = fast.next;
            i++;
        }
        
        // Remove head
        if (fast == null) {
            return slow.next;
        }
        
        // Fast ptr is n steps ahead of slow ptr
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        
        // Remove next node of slow ptr
        slow.next = slow.next.next;
        
        return head;
    }
}
