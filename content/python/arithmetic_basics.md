Title: Arithmetic Basics
Slug: arithmetic_basics
Summary: Arithmetic Basics
Date: 2016-05-01 12:00
Category: Python
Tags: Basics
Authors: Samira Ouaaz

### Create some simulated variables


```python
x = 6
y = 9
```

### x plus y


```python
print(x + y)
```

    15


### x minus y


```python
print(x - y)
```

    -3


### x times y


```python
print(x * y)
```

    54


### the remainder of x divided by y


```python
print(x % y)
```

    6


### x divided by y


```python
print(x / y)
```

    0.6666666666666666


### x divided by y (floor) (i.e. the quotient)


```python
print(x // y)
```

    0


### x raised to the y power


```python
print(x ** y)
```

    10077696


### x plus y, then divide by x


```python
print((x + y) / x)
```

    2.5


## Classics vs. floor division. This varies between 2.x and 3.x.

### Classic divison of 3 by 5


```python
print(3 / 5)
```

    0.6


### Floor divison of 3 by 5. This means it truncates any remainder down the its "floor"


```python
print(3 // 5)
```

    0
