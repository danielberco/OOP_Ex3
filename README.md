# OOP_Ex3 - Weighted Directed Graph 
## Intro 
In this project , we implented an interface of a weighted directed graph in `python` by using our Ex2 which we crated the same interface, but on `java`. 
The interface is contains the following classes :


Interface | Class                   
------------ | -------------                    
GraphInterface | DiGraph
GraphAlgoInterface | GraphAlgo

* Each vertex in the graph is represneted by the class `NodeD` 

* DiGraph is implements `GraphInterface` and by using some more methods.

* GraphAlgo is implements `GraphAlgoInterface`, this class is adjusting the graph structure for some 
  methods for comparison between the libary `NetworkX` and our previous java libary.
  This class have several methods that finds the shortest path, by using Dijkstra's algorithem, and     checking the SCC between connected components algorithem.
  
  
  * add picture of graph
  
  
  _________________________________
  

## Graph's libaries comarpisons :
We comapred our interface with NetorkX libry and our previous java libary.
