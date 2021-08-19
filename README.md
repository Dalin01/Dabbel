# Dabbel Assessment

#### Technology and Libraries
Tech: Python
Libraries: datetime, random, csv, math, unittest, re and json

#### Questions:
##### Computational complexity for the match prediction algo
Assuming m is number of rows in reading list
Assuming n is number of sensors/cols

Time complexity = O(m) * O(n) =  O(m^2) (worst case, if m = n)
Time complexity = O(m) * O(1) =  O(m) (best case, if n=1)

So the time complexity is quadratic (worst senario) or linear at best. 


#### Why I choose the data structure
#### input - nested list
I choose this because I needed my items to be ordered, changeable and the possibility
to allow duplicates. Also, it comes with very useful methods like length, pop and append. 
I needed to data structure to loop through sequentially, and since I did not have to perform a 
loopup, list was a good option.