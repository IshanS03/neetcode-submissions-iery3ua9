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

        //using minHeap PriorityQueue from java 
        PriorityQueue<ListNode> pointers = new PriorityQueue<>((a, b) -> a.val - b.val);
        ListNode res = new ListNode(0);
        ListNode cur = res;
        //keep a tab on each node, store and remove from priority queue as needed

        for(int i = 0; i<lists.length; i++){
            if(lists[i] != null){
            pointers.add(lists[i]);
            }
        }

        //there exists some pointer that has not reached null
        while(!pointers.isEmpty()){
            ListNode polled = pointers.poll();
            cur.next = polled;
            cur = cur.next;
            if(polled.next != null){
                pointers.add(polled.next);
            }
        }
        return res.next;
    }
}
