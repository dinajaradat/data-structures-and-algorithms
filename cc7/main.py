from linked_list import LinkedList

if __name__=="__main__":
    LL= LinkedList()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    # print(LL)

    # LL.insert_before(3 , 9)

    print(LL)


    # LL.insert_after("b","m")
    
    # print(LL)

    print(LL.kthFromEnd(3))
