from simplebst import Node
from simplebst.utils import insert_node
from simplebst.traversals import pre_order_nodes

tree = Node(50)
tree.get_left()
tree.get_right()
insert_node(tree, 17)
for value in [72, 12, 23, 54, 76, 9, 14, 19, 67]:
    insert_node(tree, value)
for node in pre_order_nodes(tree):
        print(node.get_value())
print("Numere gasite:")
for node in pre_order_nodes(tree):
    if node.get_value() > 23 and node.get_value() < 69:
        print(node.get_value())

    

    
        




        
        

        
    




        

    

	





	
