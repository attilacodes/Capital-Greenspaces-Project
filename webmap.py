from flask import Blueprint, render_template
import folium
import os
import pandas as pd
import geopandas as gpd
from folium import plugins
import numpy as np
from folium.plugins import MarkerCluster
from folium.plugins import MeasureControl
from folium.plugins import HeatMap
import branca.colormap as cm

webmap = Blueprint('webmap', __name__)

@webmap.route('/webmap')
def web_map():
    """ Creating a base map with a set location. 
    
    Parameters
    ----------
    map = creates the map

    """
    map = folium.Map(location=[55.9306,-3.2337], tiles='openstreetmap',zoom_start=12)

    folium.TileLayer('openstreetmap').add_to(map)
    folium.TileLayer('Stamen Terrain').add_to(map)
    folium.TileLayer('CartoDB Positron').add_to(map)
    folium.TileLayer('CartoDB Dark_Matter').add_to(map)

    

    tooltip='Click here for more info'



###Importing the geojson file for the index, SIMD  and the greenspaces    

    arqi = os.path.join('recreation/static', 'Arqi2.geojson')  #index geojson file
    
    greenspaces = os.path.join('recreation/static', 'greenspaces.geojson')  #greenspaces geojson file

    SIMD = os.path.join('recreation/static', 'EdinburghSIMD.geojson') #SIMD geojson

    df_points = (os.path.join('recreation/static', 'access.csv')) # access points data

    df = (os.path.join('recreation/static', 'arqi_layer2.csv'))   #index csv file

    df_simd = (os.path.join('recreation/static', 'EdinburghSIMD.csv')) #SIMD csv file

###Reading the ARQI layer with pandas###
    arqi_data = pd.read_csv(df)

###Loading the greenspaces cvs file###
    df2 = (os.path.join('recreation/static', 'greenspaces_arqi.csv'))
    
###Reading the greenspaces layer with pandas###
    greenspaces_data = pd.read_csv(df2)

###Reading the access points csv with pandas###
    df_acc = pd.read_csv(df_points)

###Reading the access points csv with pandas###
    df_simd_data = pd.read_csv(df_simd)

#Hover over feature part 1
    style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
###########

    ARQImap = folium.Choropleth(
        name = 'ARQI - Edinburgh',
        geo_data = arqi,
        data = arqi_data,
        columns = ['DataZone', 'Quintile'],
        key_on = 'feature.properties.DataZone',
        fill_color = 'OrRd_r',
        fill_opacity = 0.7,
        line_opacity = 1,
        legend_name = 'ARQI 1-5 (Quintile 1 = Most Environmentally Deprived)',
        smooth_factor = 0,
        highlight=highlight_function,
        ).add_to(map)

#remove legend from layer
    
    for key in ARQImap._children:
        if key.startswith('color_map'):
            del (ARQImap._children[key])
    ARQImap.add_to(map)
    
    ARQImap.geojson.add_child(folium.features.GeoJsonTooltip(fields=['DZName','DataZone','Quintile'],
        aliases=['Datazone Name: ','Datazone ID: ','ARQI Quintile: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))

#add custom legend to layer
    
    step = cm.StepColormap(['#b30000', '#e34a33', '#fc8d59', '#fdcc8a','#fef0d9'],
    vmin = 1, vmax = 6,
    index = [1, 2, 3, 4, 5], caption='ARQI (Quintile 1 = Most Environmentally Deprived)')

    step.add_to(map)
    
    
###########

    GSmap = folium.Choropleth(
        name = 'Greenspaces - Edinburgh',
        geo_data = greenspaces,
        data = greenspaces_data,
        columns = ['NAME', 'qual_score'],
        key_on = 'feature.properties.NAME',
        fill_color = 'Greens',
        fill_opacity = 0.7,
        show=False,
        highlight=highlight_function,
        line_opacity = 1,
        legend_name = 'Greenspaces Quality Score 1-5',
        smooth_factor = 0
        ).add_to(map)

    #remove legend from layer
    
    for key in GSmap._children:
        if key.startswith('color_map'):
            del (GSmap._children[key])
    GSmap.add_to(map)
    
    GSmap.geojson.add_child(folium.features.GeoJsonTooltip(fields=['NAME','qual_score'],
        aliases=['Greenspace Name: ','Quality Score: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))

#add custom legend to layer
    
    step = cm.StepColormap(['#e5f5e0', '#a1d99b', '#a1d99b', '#31a354', '#31a354'],
    vmin = 0, vmax = 5,
    index = [0, 1.67, 1.68, 3.33, 3.34, 5], caption='Greenspaces Score')

    step.add_to(map)

    SIMDmap = folium.Choropleth(
        name = 'SIMD',
        geo_data = SIMD,
        data = df_simd_data,
        columns = ['DataZone', 'Quintilev2'],
        key_on = 'feature.properties.DataZone',
        fill_color = 'Blues_r',
        fill_opacity = 0.7,
        show=False,
        highlight=highlight_function,
        style=style_function,
        line_opacity = 1,
        legend_name = 'Scottish Index of Multiple Deprivation (Quintile 1 = Most Socially Deprived)',
        smooth_factor = 0,
        ).add_to(map)

#remove legend from layer
    
    for key in SIMDmap._children:
        if key.startswith('color_map'):
            del (SIMDmap._children[key])
    SIMDmap.add_to(map)
    
    SIMDmap.geojson.add_child(folium.features.GeoJsonTooltip(fields=['DZName','DataZone', 'Quintilev2'],
        aliases=['Datazone Name: ','Datazone ID: ', 'SIMD Quintile: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")))

#add custom legend to layer
    
    step = cm.StepColormap(['#08519c', '#3182bd', '#6baed6', '#bdd7e7', '#eff3ff'],
    vmin = 1, vmax = 6,
    index = [1, 2, 3, 4, 5], caption='Scottish Index of Multiple Deprivation (Quintile 1 = Most Socially Deprived)')

    step.add_to(map)
    
    
###Inset map###

    minimap = plugins.MiniMap(toggle_display=True).add_to(map)
#    map.add_child(minimap)
   

### Marker Cluster Map  ###

#Make list for lat and long
    lat = df_acc.xcoord_cen.tolist()
    long = df_acc.ycoord_cen.tolist()

    locations = list(zip(long, lat))

# create a folium marker cluster
    marker_cluster = MarkerCluster(locations, name = 'Greenspace Access Points', show=False)

# add marker cluster map
    marker_cluster.add_to(map)

# add tooltip
    tooltip = "Click to see greenspace name!"
# Here I add pop ups for each point and add it to the cluster.
    for index, row in df_acc.iterrows():
        popup = folium.Popup(row['NAME'], parse_html = True)
        folium.Marker([df_acc['ycoord_cen'].iloc[index], df_acc['xcoord_cen'].iloc[index]], popup=popup, tooltip = tooltip).add_to(marker_cluster)

###Measure tool to the top right
    map.add_child(MeasureControl()) #adds a measurement widget on top of the layer menu

### Heatmap ###

    HeatMap(locations, name = 'Heatmap of Access Points', show=False).add_to(map) #here I use the same coordinate list to plot the points

    folium.LayerControl().add_to(map)

    

    map.save('recreation/templates/map.html')

    
    
    return render_template('webmap.html', map = map)
#    return render_template('map.html')
