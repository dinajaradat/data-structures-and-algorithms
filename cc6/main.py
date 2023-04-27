from cc6.linked_list import LinkedList

if __name__=="__main__":
    LL= LinkedList()

    LL.append("a")
    LL.append("b")
    LL.append("c")

    print(LL)

    LL.insert_before("b","d")

    print(LL)


    LL.insert_after("b","m")
    
    print(LL)