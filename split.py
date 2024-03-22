class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def split_list_with_pointers(head):
    if not head or not head.next:
        return head, None
    slow_pointer = head
    fast_pointer = head.next
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    second_half = slow_pointer.next
    slow_pointer.next = None  
    return head, second_half

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

# Example usage
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a linked list from the given list
head = ListNode(given_list[0])
current = head
for value in given_list[1:]:
    current.next = ListNode(value)
    current = current.next

# Split the linked list using fast and slow pointers
first_half, second_half = split_list_with_pointers(head)

# Print the two halves
print("First Half:")
print_linked_list(first_half)

print("\nSecond Half:")
print_linked_list(second_half)
def calculate_sum(head):
    total = 0
    current = head
    while current:
        total += current.value
        current = current.next
    return total
sum_first_half = calculate_sum(first_half)
sum_second_half = calculate_sum(second_half)

print("First half sum:", sum_first_half)
print("Second half sum:", sum_second_half)
