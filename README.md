# Creating a web map using Python.

This project demonstrates creation of a web map using python. The map will have 2 layers.
1. Layer with pop-ups for city names in USA. For this, data/city.csv is used.
2. Layer with polygons drawn as each country's boundary and color code according to population. For this, data/polygons.json is used.
We will be able to control these layers (i.e. Switch on and off the layers as we need.)

The countries will be coloured as yellow if population <10000000 , green if 10000000<=population<=20000000 and red if population >20000000.

## Prerequisites
The python libraries folium and pandas are needed.

````
pip install folium

````
If it doesn't work, use

````
pip3 install folium

````

Similarly install pandas.

## Usage

1. Run the python file map.py. Use the commands below in any terminal.
```
python map.py

```
or if the python version is 3, use command.

```
python3 map.py

```
or you can also use any python IDE.

2. Now open the file webmap.html in any browser.

3. You can use the icon in the right hand top side to switch on and off layers.
