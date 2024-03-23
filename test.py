import group_parser as gp



def z4_test():
    print("Doing test for Z4")
    items = [0, 1, 2, 3]
    operation = lambda x, y: (x + y)%4

    gp.parse_group(items, operation)

def mul_z4_test():
    print("Doing test for group isom to Z4")
    items = [1, 3, 7, 9]
    operation = lambda x, y: (x*y)%10

    gp.parse_group(items, operation)

def do_tests():
    z4_test()
    mul_z4_test()


do_tests()