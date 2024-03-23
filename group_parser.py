# understand the structure of a group given
from typing import Callable

# A group will be determined by a list and a function that returns elements of the list
def parse_group(items: list[any], operation: Callable[[any, any], any]):
    """This figures out stuff about a group
    
    For now, I probably just want to determine if the set is a group
    
    The operation is closed
    """
    # Do I want to include an "is_abelian" flag?

    if not is_group(items, operation):
        print("Not a group")
        return
    
    print("This is a group!")
    # I probably want to do something here such as find subgroups.



    return

def is_group(items: list[any], operation: Callable[[any, any], any]) -> bool:
    """Let's determine if this is a group!"""


    # Determine that operation is closed
    if not is_closed(items, operation):
        return False
    
    # Determine that identity exists
    if not has_identity(items, operation):
        return False

    # Determine if associative
    if not is_associative(items, operation):
        return False

    return True


def has_identity(items: list[any], operation: Callable[[any, any], any]) -> bool:
    """Determine if identity exists"""
    for id_candidate in items:
        if all([item == operation(item, id_candidate) for item in items]):
            # This is the identity!
            # We probably want to do something to check for dupes
            return True
    return False

def is_associative(items: list[any], operation: Callable[[any, any], any]) -> bool:
    """Determine if associative"""
    # TODO: Come back to make this better
    for item1 in items:
        for item2 in items:
            o12 = operation(item1, item2)
            for item3 in items:
                if operation(item1, operation(item2, item3)) != operation(o12, item3):
                    return False
    return True

def is_closed(items: list[any], operation: Callable[[any, any], any]) -> bool:
    """Determine if operation is closed on items"""
    # TODO: Make this better. This is a slow implementation. I think I can improve this
    for item1 in items:
        for item2 in items:
            if operation(item1, item2) not in items:
                # Oh no!
                print("Not closed!")
                return False
    return True
