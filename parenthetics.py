"""Implementation of valid parenthetics string."""

from linked_list import LinkedList


def valid_parentheses(string):
    """Determine if string has proper parenthetics."""
    paren_list = [val for val in string if val in ('(', ')')]
    llist = LinkedList(paren_list[::-1])
    unclosed = 0
    while llist.head_node:
        value = llist.pop()
        if unclosed < 0:
            return -1
        elif value == '(':
            unclosed += 1
        else:
            unclosed -= 1
    if unclosed == 0:
        return 0
    elif unclosed > 0:
        return 1
    return -1
