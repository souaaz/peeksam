Title: Assignment Operators
Slug: assignment_operators
Summary: Assignment Operators
Date: 2016-05-01 12:00
Category: Python
Tags: Basics
Authors: Samira Ouaaz

### Create some variables


```python
a = 2
b = 1
c = 0
d = 3
```

### Assigns values from right side to left side


```python
c = a + b
c
```




    3



### Add right to the left and assign the result to left (c = a + c)


```python
c += a
c
```




    5



### Subtract right from the left and assign the result to left (c = a - c)


```python
c -= a
c
```




    3



### Multiply right with the left and assign the result to left (c = a * c)


```python
c *= a
c
```




    6



### Divide left with the right and assign the result to left (c = c / a)


```python
c /= a
c
```




    3.0



### Takes modulus using two operands and assign the result to left (a = d % a)


```python
d %= a
d
```




    1



### Exponential (power) calculation on operators and assign value to the left (d = d ^ a)


```python
d **= a
d
```




    1



### Floor division on operators and assign value to the left (d = d // a)


```python
d //= a
d
```




    0
