import linked_list

my_linked_list = linked_list.LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.append(4)
my_linked_list.append(5)

# my_linked_list.print_list()


def reverse_linked_list(ll):
    temp = ll.head
    ll.head = ll.tail
    ll.tail = temp
    before = None
    after = temp.next

    while before.next:
        after = temp.next
        temp.next = before
        before = temp
        temp = after

    temp.print_list()


reverse_linked_list(my_linked_list)
