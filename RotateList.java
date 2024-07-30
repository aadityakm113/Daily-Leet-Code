// https://leetcode.com/problems/rotate-list/
public class RotateList {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null||head.next==null||k==0)
            return head;
        
        int l=1;
        ListNode temp = head; 
        while(temp.next!=null){
            temp=temp.next;
            l++;
        }
        temp.next=head;
        k=k%l; //when length of list is smaller than k
        int rotate = l-k;
        int i=1;
        temp=head;
        while(i<rotate){
            temp=temp.next;
            i++;
        }
        head=temp.next;
        temp.next=null;
        return head;
    }
}
