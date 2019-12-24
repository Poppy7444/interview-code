package interview;

import java.util.ArrayList;
import java.util.List;

/*
 * 数据结构编程
 * 编写一个单链表，要求包含以下方法：插入头节点，删除头结点，在任意位置插入新节点， 在任意位置删除节点。打印所有节点信息，根据位置查找节点
 */
class MyLinkedList {

    private Node start = null;
    private Node tail = null;
    private int length =0;

    static class Node{
        public Node(Node prev,Node next,Object value){
            this.prev = prev;
            this.next = next;
            this.value = value;
        }
        private Node prev;
        private Node next;
        private Object value;
    }

    /*插入头节点*/
    public boolean addHead(Object o){

        if(start==null){
            start = new Node(null,null,o);
        }else{
            start = new Node(null,start,o);
        }
        length++;
        return true;
    }

    /*在任意位置插入新节点*/
    public boolean add(Object o) {
        Node newNode = new Node(tail, null, o);
        if (start == null) {
            start = newNode;
        }
        if (tail != null) {
            tail.next = newNode;
        }
        tail = newNode;
        length++;
        return true;
    }

    public boolean add(int index,Object o) {
        Node curr = start;
        for(int i=0;i<index-1;i++){
            curr = curr.next;
        }

        Node newNode = new Node(curr,curr.next,o); // 新节点 prev 是 Node(index-1)个
        curr.next = newNode; //老的插入节点的next 改为新节点
        curr.next.prev = newNode; //老的下一个节点的prev 改成新节点
        length++;
        return true;
    }

    /*删除头结点*/
    public boolean deleteHead(){
        start = start.next;
        length--;
        return true;
    }
    /*在任意位置删除节点*/
    public boolean delete(int index){
        Node curr = start;
        Node temp = null;
        for(int i=0;i<=index;i++){
            if(i==index-1){
                temp = curr;
            }
            curr = curr.next;
        }
        temp.next = curr;
        if(curr!=null) { //如果删除节点是尾部节点，不需要重置后续节点的prev
            curr.prev = temp;
        }
        length--;
        return true;
    }

    public Object get(int index){
        Node curr = start;
        for(int i=0;i<index;i++){
            curr = curr.next;
        }
        return curr.value;
    }

    /*打印所有节点信息*/
    @Override
    public String toString() {
        List<String> strList = new ArrayList<>();
        for(int i=0;i<length;i++){
            Object curr = get(i);
            strList.add(curr.toString());
        }
        return String.join("->",strList);
    }

    public static void main(String[] args) {
        MyLinkedList mll = new MyLinkedList();
        mll.add("1");
        mll.add("2");
        mll.addHead("5");
        mll.add(1,"10");
        mll.add(3,"11");
        mll.deleteHead();
        mll.delete(3);
        System.out.println(mll);
    }
}