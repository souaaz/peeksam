Title: Display an image
Date: 2016-05-01 12:00  
Category: Jupyter 
Tags:  
Slug: ipython_display_image
Authors: Samira Ouaaz  
Summary: ipython_display_image


# View an image in iPython


## Display an image


```
# Load the ipython display and image module
from IPython.display import Image
from IPython.display import display
```


```
# display this image
display(Image(url='http://history.nasa.gov/ap11ann/kippsphotos/5903.jpg'))
```


<img src="http://history.nasa.gov/ap11ann/kippsphotos/5903.jpg"/>


## Display an svg


```
# Load the svg module
from IPython.display import SVG

# Display an svg
SVG(url='http://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg')
```




![svg](ipython_display_image_files/ipython_display_image_5_0.svg%2Bxml)




```

```
