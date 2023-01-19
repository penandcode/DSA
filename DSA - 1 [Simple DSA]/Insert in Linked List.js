// https://www.crio.do/learn/PSDS/ME_PE_SIMPLE_DS_IMPLEMENTATION_NEW/ME_PE_SIMPLE_DS_IMPLEMENTATION_NEW_MODULE_LINKEDLISTINSERT/assessment/

const ListNode = require('../crio/javascript/ds/ListNode/ListNode');

/*
Definition for ListNode
class ListNode {
    constructor(val){
		this.val = val;
		this.next = null;
	}
}

Use new ListNode(data) to create new node
*/

class LinkedList{
	constructor(){
		this.head = null;
		this.tail = null;
	}
	insertAtBeginning(data) {
    var new_node = new ListNode(data);
 
    new_node.next = this.head;
 
    this.head = new_node;
    }
    insertAtEnd(data) {
    var new_node = new ListNode(data);
 
    if (this.head == null)
    {
        this.head = new_node;
        return;
    }
 
    new_node.next = null;
 
    var last = this.head;
    while (last.next != null)
        last = last.next;
    last.next = new_node;
    return;
    }

}

module.exports = LinkedList;
