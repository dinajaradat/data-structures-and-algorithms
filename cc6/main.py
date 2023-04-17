from linked_list import linked_list

if __name__=="__main__":
    LL= linked_list()

    LL.append("a")
    LL.append("b")
    LL.append("c")

    print(LL)

    LL.insert_before("b","d")

    print(LL)


    LL.insert_after("b","m")
    
    print(LL)