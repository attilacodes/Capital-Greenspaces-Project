# Capital Greenspaces Project
## Capital Greenspaces Project, Recreation Team 6, University of Edinburgh 2021-2022

## About
The website is developed by Victoria Song, Attila Lukacs, Yixue Wang and Dorina Mosneanu in partial fulfilment of the TIGIS course (2021-22) at The University of Edinburgh.

## Navigating the Repo

In this repository, you can gain access to the code used in the creation of the website including HTML, CSS, JS and Python files. 

The website is created using [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/), a Python-based micro-web framework, and deployed using [Gunicorn](https://gunicorn.org/#deployment), a Python WSGI HTTP Server for UNIX.This was achieved by setting up a port on a UNIX server and binding the webapp to it.

In line with any Flask webapp, this repostitory is organised in a Python module package. The main directory contains the Python files for the webmap and the query webpage, as well as the necessary files required to initiate the webapp and provide extensions to. Within this are the sub-directories: [static](static) and [templates](templates) containing all 'decorative files' (CSS, JS, images and webmap data), and HTML files, respectively.

The website documentation is made avaiable [here](Group_6_Documentation.pdf)

## Forking Our Repo

To use some of our code, simply fork this repo. Note: repurpose of code required for some files due to restricted access to the server aside from the owner e.g. to the Oracle DB.


## Access the Website
To access the website, [click here.](https://www.geos.ed.ac.uk/dev/ARQI). The website supports both viewing in desktop and mobile devices. For best view of the webmap, please refer to the desktop version.

## Support
If you require help using the Python module package for your research, please direct emails to (s1729202@ed.ac.uk). If you encounter an issue with the code, you can add the issue to the [issues list](https://github.com/attilacodes/Capital-Greenspaces-Project/issues).

## Further Resources
For additional information on the technologies used in the creation of the web app, please refer to:

Flask - https://flask.palletsprojects.com/en/2.0.x/

Gunicorn - https://gunicorn.org/

Folium - https://python-visualization.github.io/folium/

W3Schools HTML Tutorials - https://www.w3schools.com/html/default.asp




