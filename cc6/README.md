# linked-list-insertions

# Whiteboard Process
![img](./cc6.png)

# Approach & Efficiency
## 1-	Create a Node class with ( value attribute & next attribute initialized to None) 
## 2-	Create a LinkedList class with ( head attribute initialized to None)
## 3-	Create an append method in the LinkedList class that takes a value as an argument.
## 4-	Inside the append method --> create a new Node object with the value argument passed in.
## 5-	Check if the head of the LinkedList is None -->  set the new Node object as the head of the LinkedList.
## 6-	If the head of the LinkedList is not None --> traverse the list starting from the head and looking for the last node.
## 7-	When the last node is found, set its next attribute to the new Node object. 

## time --> O(n) because the method traverses the entire list to find the last node
## Space --> O(n) because each node in the list requires memory allocation for both the value and the next pointer



# Solution

## Given 9 , return 9 --> X
## Given (1, 2 , 3) ,6  , return 1 --> 2 --> 3 --> 6 --> X

