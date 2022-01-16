# Capital Greenspaces Project
## Capital Greenspaces Project, Recreation Team 6, University of Edinburgh 2021-2022

## About    
The [website](https://www.geos.ed.ac.uk/dev/ARQI) is developed by Victoria Song, Attila Lukacs, Yixue Wang and Dorina Mosneanu in partial fulfilment of the TIGIS course (2021-22) at The University of Edinburgh.

## Navigating the Repository

In this repository, you can gain access to the code used in the creation of the website including HTML, CSS, JS and Python files. 

The website is created using [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/), a Python-based micro-web framework, and deployed using [Gunicorn](https://gunicorn.org/#deployment), a Python WSGI HTTP Server for UNIX. This was achieved by setting up a port on a UNIX server and binding the webapp to it via Gunicorn.

The website and the repository are organised in a Python module package. The main directory contains [main.py](main.py) which imports all app routes and instanciates the webapp, plus all Python files for the webmap and the query webpage. Within this are the sub-directories: [static](static) and [templates](templates) containing all 'decorative files' (CSS, JS, images and webmap data), and HTML files, respectively.

The website documentation is made available [here](Group_6_Documentation.pdf).

## Cloning Our Repository
To use the webapp for your research purposes:
1. Clone github repository to local computer
2. Download Python 3.10
3. Install required dependencies with the following command: "pip install Flask"
4. Navigate to app folder
5. From command line, type: "python3 main.py"
6. Open web browser to "localhost:8000"

NB: Repurpose of code required due to the use of relative paths and restrictive access to certain dependencies e.g. Oracle RDBMS


## Accessing the Website
To access the website, [click here](https://www.geos.ed.ac.uk/dev/ARQI). The website supports both viewing on desktop and mobile devices. For optimised viewing, please refer to the desktop version.

## Support
If you require help using the Python module package for your research, please direct emails to s1729202@ed.ac.uk. If you encounter an issue with the code, you can add the issue to the [issues list](https://github.com/attilacodes/Capital-Greenspaces-Project/issues).

## Further Resources
For additional information on the technologies used in the creation of the web app, please refer to:

Flask - https://flask.palletsprojects.com/en/2.0.x/

Gunicorn - https://gunicorn.org/

Folium - https://python-visualization.github.io/folium/

W3Schools HTML Tutorials - https://www.w3schools.com/html/default.asp
