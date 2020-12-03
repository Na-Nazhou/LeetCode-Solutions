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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        int i = 1;
        ListNode prev = null;
        ListNode curr = head;
        while (i < m) {
            prev = curr;
            curr = curr.next;
            i++;
        }
        
        ListNode tempPrev = prev;
        ListNode tempCurr = curr;
        while (i < n + 1) {
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            i++;
        }
        
        if (tempPrev != null) {
            tempPrev.next = prev;
        }
        tempCurr.next = curr;
        
        if (m != 1) {
            return head;
        } else {
            return prev;
        }
    }
}
