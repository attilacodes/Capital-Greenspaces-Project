#!/usr/bin/env python3
import cx_Oracle
from flask import Flask, Blueprint, render_template, request
import cgi
import os
from markupsafe import Markup


query = Blueprint('query', __name__)


   
@query.route("/data", methods=['POST', 'GET'])
def index():
                """ Pass HTML form elements to Python script for processing. Once passed, a connection to Oracle RDBMS is created and unique data is retrieved and displayed.
                Parameters
                ----------
                conn = establishes connection to the Oracle RDBMS using username and password
                html = list containing all greenspace names from conn.cursor
                result = list holding a variety of data from conn.cursor depending on the items passed from HTML form



                Returns
                -------
                query = filtered rows of information from retrieved data (from Oracle) in tuple format and subsequently rendered onto the query_download HTML file
                greenspaces = all data defined by 'html' variable and rendered onto the query_download HTML file

                """
                
                with open("../../nada",'r') as pwf:
                                pw = pwf.read().strip()
                conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
                c = conn.cursor()
                c.execute("SELECT GREENSPACE_NAME FROM s2236682.GREENSPACE WHERE s2236682.GREENSPACE.GREENSPACE_ID > 0 ORDER BY s2236682.GREENSPACE.GREENSPACE_NAME")        
                html = []
                #loop through each retrieved greenspace name and get rid of non-required characters
                for row in c.fetchall():
                                html.extend(row)
                conn.close()
                return render_template('query_download.html', greenspaces = html)


@query.route("/submitted", methods=['POST'])

def dynamic_queries():
                """ Pass HTML form elements to Python script for processing. Once passed, a connection to Oracle RDBMS is created and unique data is retrieved and displayed. 
                
                Parameters
                ----------
                conn = establishes connection to the Oracle RDBMS using username and password
                html = list containing all greenspace names from conn.cursor

                Returns
                -------
                greenspaces = all data defined by 'html' variable and rendered on the query_download HTML file

                """
                
                #the same SQL query required to retain elements within drop-down menu (otherwise collapses after form is posted)
                with open("../../nada",'r') as pwf:
                                pw = pwf.read().strip()
                conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
                c = conn.cursor()
                c.execute("SELECT GREENSPACE_NAME FROM s2236682.GREENSPACE WHERE s2236682.GREENSPACE.GREENSPACE_ID > 0 ORDER BY s2236682.GREENSPACE.GREENSPACE_NAME")        
                html = []
                #loop through each retrieved greenspace name and get rid of non-required characters
                for row in c.fetchall():
                                html.extend(row)
                conn.close()

                #identify "POST" method then each of the three "services" offered then run dynamic queries connecting Oracle RDBMS
                if request.method == 'POST':
                                if request.form.get('service') == 'provisions':
                                                query = request.form.get("greenspace")
                                                with open("../../nada",'r') as pwf:
                                                                pw = pwf.read().strip()
                                                                conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
                                                                c = conn.cursor()
                                                                result = c.execute("SELECT s2236682.GREENSPACE.GREENSPACE_NAME, s2236682.AMENIT.BENCHES, s2236682.AMENIT.PLAY_AREA, s2236682.AMENIT.TOILETS, s2236682.AMENIT.BINS,s2236682.SAFET.CCTV, s2236682.SAFET.CRIME, s2236682.AESTHE.TREES, s2236682.AESTHE.CONSERVATION_AREA, s2236682.ACCESSI.CORE_PATHS FROM s2236682.GREENSPACE, s2236682.AMENIT, s2236682.AESTHE, s2236682.ACCESSI, s2236682.SAFET WHERE s2236682.GREENSPACE.GREENSPACE_ID = s2236682.AMENIT.GREENSPACE_ID AND s2236682.GREENSPACE.GREENSPACE_ID = s2236682.SAFET.GREENSPACE_ID AND s2236682.GREENSPACE.GREENSPACE_ID = s2236682.AESTHE.GREENSPACE_ID AND s2236682.GREENSPACE.GREENSPACE_ID = s2236682.ACCESSI.GREENSPACE_ID AND s2236682.GREENSPACE.GREENSPACE_NAME LIKE :query || '%'",{"query": str(query)}).fetchall()
                                                                query = ''
                                                                for row in result:
                                                                                query = Markup("<b><br>Greenspace name: </b>") + row[0] + Markup("</br>") + Markup("<b><br>Benches: </b>") + row[1] + Markup("</br>") + Markup("<b><br>Play area: </b>") +row[2] + Markup("</br>") + Markup("<b><br>Toilets: </b>") + row[3] + Markup("</br>") + Markup("<b><br>Bins: </b>") + row[4] + Markup("</br>") +  Markup("<b><br>CCTV Cameras: </b>") + row[5] + Markup("</br>") + Markup("<b><br>Presence of Crime: </b>") + row[6] + Markup("</br>") + Markup("<b><br>Trees: </b>") + row[7] + Markup("</br>") + Markup("<b><br>Conservation Area: </b>") + row[8] + Markup("</br>") + Markup("<b><br>Part of Core Paths Network: </b>") +row[9] + Markup("<br>")
                                                                conn.close()
                                elif request.form.get('service') == 'quality':
                                                query = request.form.get("greenspace")
                                                with open("../../nada",'r') as pwf:
                                                                pw = pwf.read().strip()
                                                                conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
                                                                c = conn.cursor()
                                                                #string interpolator for wildcard operator in SQL query
                                                                result = c.execute("SELECT s2236682.GREENSPACE.GREENSPACE_NAME, s2236682.QUALI.QUALITY_SCORE, s2236682.QUALI.GRADE FROM s2236682.GREENSPACE, s2236682.QUALI WHERE s2236682.GREENSPACE.GREENSPACE_ID = s2236682.QUALI.GREENSPACE_ID AND s2236682.GREENSPACE.GREENSPACE_NAME LIKE :query || '%'",{"query": str(query)}).fetchall()
                                                                query = Markup("<b><br>Greenspace name: </b>") + ('\n'.join([i[0] for i in result])) + Markup("</br>") + Markup("<br><b>Quality score: </b>") + ('\n'.join([i[1] for i in result])) + "/5" + Markup("</br>") + Markup("<br><b>Quality Grade: </b>") + ('\n'.join([i[2] for i in result])) + Markup("</br>")
                                                                conn.close()
                                elif request.form.get('service') == 'serviceAreas':
                                                query = request.form.get("greenspace")
                                                with open("../../nada",'r') as pwf:
                                                                pw = pwf.read().strip()
                                                                conn = cx_Oracle.connect(dsn="geoslearn", user="s2236682", password=pw)
                                                                c = conn.cursor()
                                                                #string interpolator for wildcard operator in SQL query then retrieve all results
                                                                result = c.execute("SELECT s2236682.DATAZ.DATAZONE_CODE, s2236682.DATAZ.DATAZONE_NAME FROM s2236682.GREENSPACE, s2236682.DATAZ WHERE s2236682.GREENSPACE.GREENSPACE_ID = s2236682.DATAZ.GREENSPACE_ID AND s2236682.GREENSPACE.GREENSPACE_NAME LIKE :query || '%'",{"query": str(query)}).fetchall()
                                                                #access each element within tuple getting rid of unneccessary characters in one go
                                                                #Markup adds html styling to the accessed elements
                                                                query = Markup("<b><br>Datazone codes: </b>") + (', '.join([i[0] for i in result])) + Markup("</br>") + Markup("<b><br>Datazone names: </b>") + (', '.join([i[1] for i in result])) + Markup("</br>")
                                                                                                
                                                                conn.close()
                             
                return render_template('query_download.html', query = query, greenspaces = html)


if __name__ == "__main__":
	app.run(debug=True)
