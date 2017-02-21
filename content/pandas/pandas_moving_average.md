Title: Moving Averages In Pandas
Slug: pandas_moving_average
Summary: Moving Averages In Pandas
Date: 2016-05-01 12:00
Category: pandas
Tags: Data Wrangling
Authors: Samira Ouaaz



### Import modules


```python
import pandas as pd
```

### Create a dataframe 


```python
data = {'score': [1,1,1,2,2,2,3,3,3]}
df = pd.DataFrame(data)
df
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 1</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 2</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 2</td>
    </tr>
    <tr>
      <th>5</th>
      <td> 2</td>
    </tr>
    <tr>
      <th>6</th>
      <td> 3</td>
    </tr>
    <tr>
      <th>7</th>
      <td> 3</td>
    </tr>
    <tr>
      <th>8</th>
      <td> 3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculate the moving average. That is, take
# the first two values, average them, 
# then drop the first and add the third, etc.
pd.rolling_mean(df, 2)
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 1.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td> 2.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td> 2.5</td>
    </tr>
    <tr>
      <th>7</th>
      <td> 3.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td> 3.0</td>
    </tr>
  </tbody>
</table>
</div>


