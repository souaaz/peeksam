Title: Edit Tables    
Slug: edit_tables    
Summary: Edit tables in SQL.    
Date: 2017-01-16 12:00    
Category: SQL  
Tags: Basics  
Authors: Samira Ouaaz  

Note: This tutorial was written using [Catherine Devlin's SQL in Jupyter Notebooks library](https://github.com/catherinedevlin/ipython-sql). If you have not using a Jupyter Notebook, you can ignore the two lines of code below and any line containing `%%sql`. Furthermore, This tutorial uses SQLite's flavor of SQL, your version might have some differences in syntax.

For more, check out [Learning SQL](http://amzn.to/2jRriHj) by Alan Beaulieu.


```python
# Ignore
%load_ext sql
%sql sqlite://
%config SqlMagic.feedback = False
```

## Create Data


```python
%%sql

-- Create a table of criminals
CREATE TABLE criminals (pid, name, age, sex, city, minor);
INSERT INTO criminals VALUES (412, 'James Smith', 15, 'M', 'Santa Rosa', 1);
INSERT INTO criminals VALUES (901, 'Gordon Ado', 32, 'F', 'San Francisco', 0);
INSERT INTO criminals VALUES (512, 'Bill Byson', 21, 'M', 'Petaluma', 0);
```




    []



## View Table


```python
%%sql

--  Select all
SELECT *

-- From the criminals table
FROM criminals
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Santa Rosa</td>
        <td>1</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>0</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Petaluma</td>
        <td>0</td>
    </tr>
</table>



## Update One Row


```python
%%sql

-- Update the criminals table
UPDATE criminals

-- To say city: 'Palo Alto'
SET City='Palo Alto'

-- If the prisoner ID number is 412
WHERE pid=412;
```




    []



## Update Multiple Rows Using A Conditional


```python
%%sql

-- Update the criminals table
UPDATE criminals

-- To say minor: 'No'
SET minor = 'No'

-- If age is greater than 12
WHERE age > 12;
```




    []



## View Table Again


```python
%%sql

--  Select all
SELECT *

-- From the criminals table
FROM criminals
```




<table>
    <tr>
        <th>pid</th>
        <th>name</th>
        <th>age</th>
        <th>sex</th>
        <th>city</th>
        <th>minor</th>
    </tr>
    <tr>
        <td>412</td>
        <td>James Smith</td>
        <td>15</td>
        <td>M</td>
        <td>Palo Alto</td>
        <td>No</td>
    </tr>
    <tr>
        <td>901</td>
        <td>Gordon Ado</td>
        <td>32</td>
        <td>F</td>
        <td>San Francisco</td>
        <td>No</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Bill Byson</td>
        <td>21</td>
        <td>M</td>
        <td>Petaluma</td>
        <td>No</td>
    </tr>
</table>
