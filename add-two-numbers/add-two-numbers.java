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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbers(l1, l2, 0);
    }
    
    private ListNode addTwoNumbers(ListNode l1, ListNode l2, int carry) {
        if (l1 == null & l2 == null & carry == 0) {
            return null;
        }
        
        int first = l1 != null ? l1.val : 0;
        int second = l2 != null ? l2.val : 0;
        int sum = first + second + carry;
        
        ListNode head = new ListNode(sum % 10);
        ListNode nextFirst = l1 != null ? l1.next : null;
        ListNode nextSecond = l2 != null ? l2.next : null;
        
        head.next = addTwoNumbers(nextFirst, nextSecond, sum / 10);
        return head;
    }
}