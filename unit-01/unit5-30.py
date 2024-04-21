def square(x):
    return x*x

def square_list(items):
    if items == []:
        return []
    item = square_list(items[1:])
    return [square(items[0]), item]


def map(proc, items):
    if items == []:
        return []
    list_of_lists = [proc(items[0]), map(proc,items[1:])]

    return list_of_lists

#def square_tree(tree, factor):
#    if tree == []:
#        return
#        if tree == []:
#            return tree * factor


def scale_tree(tree, factor):
    print(type(tree))
    if tree == []:
        return []
    if isinstance(tree, int):
        print(tree)
        result = tree * factor
        return result
    else:
        return [ scale_tree(tree[0],factor), scale_tree(tree[1:],factor)]



def square_tree(tree):
    #print(type(tree))
    if tree == []:
        return []
    if isinstance(tree, int):
        #print(tree)
        result = square(tree)
        return result
    else:
        return [square_tree(tree[0]), square_tree(tree[1:])]


#def sca_tre(tree,factor):
#    (cond ((null? tree)nil)
#        ((not (pair? tree)) (* tree factor))


#    (else (cons (sca-tre(tree[0],factor) sca_tre(tree[1:]) factor))))

def square_tree2(tree, factor):
    map(lamb(sub_tree))



def main():
    print(square_tree([1,
                        [2,[3,4],5],
                        [6,7]]
                        ))
    


if __name__ == "__main__":
    main()