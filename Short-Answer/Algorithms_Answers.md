#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

If this code runs just once it is fine. There is no mention of either iteration or recursion. 
There is only one line of simple code after the while loop and there are only two variables. I would say it is either Constant O(1) or Logarithmic O(log n)

b)

A main source of inefficiency here is the for loop. The conditional while statement slows things down but only marginally. 
I would say this is Polynomial O(n^c)


c)

This is Exponential O(c^n)

## Exercise II


The floor determines if the egg is broken. 

Function is called throw(f).
"f" is the floor number.
An if statement would determine whether the egg gets broken or not. 

If the variable f is higher than the floor where eggs get broken, the return statement states that the egg will get broken if thrown from here. 

If the variable f is lower than the floor that the egg is thrown from, the return states that the egg is safe. 


This algorithm's time complexity is Logarithmic O(log n) although it isn't very efficient as it has be called for each egg that is thrown. 