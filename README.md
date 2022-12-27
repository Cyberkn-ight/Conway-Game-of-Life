# Conway-Game-of-Life
A simple implementation of Conway's Game of Life in Python, running in your terminal!

To run this code, save it to a file and then run it with the following command, replacing size with the desired size of the grid, num_cells with the number of initial live cells, and x1,y1, x2,y2, and so on with the starting positions of the cells:
```python filename.py size num_cells x1,y1 x2,y2 ...```

Here are the command for a few structures on a 20*20 grid :
Glider
```python filename.py 20 5 0,1 1,2 2,0 2,1 2,2```
Boat
```python filename.py 20 5 1,1 2,1 1,2 3,3 2,3```
Snake
```python filename.py 20 4 0,0 1,0 2,0 3,0 4,0```
Beehive
```python filename.py 20 6 1,1 2,1 3,2 1,3 3,3 2,4```

Here are the command for a few larger structures, the minimum grid size recommended is 50*50 :
Pulsar
```python filename.py 50 72 2,3 3,2 3,3 3,4 4,2 4,3 4,4 6,2 6,3 6,4 7,2 7,3 7,4 9,3 10,2 10,3 10,4 11,2 11,3 11,4 13,2 13,3 13,4 16,3 17,2 17,3 17,4 18,2 18,3 18,4 20,2 20,3 20,4 21,2 21,3 21,4 23,3 24,2 24,3 24,4 25,2 25,3 25,4 27,2 27,3 27,4 28,2 28,3 28,4 30,3 31,2 31,3 31,4 32,2 32,3 32,4 34,2 34,3 34,4 35,2 35,3 35,4 37,2 37,3 37,4 38,2 38,3 38,4 40,3```
