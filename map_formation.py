import folium
import pandas

def create_addressmap(df_adr):

    width, height = 1125, 500
    m = folium.Map(location=[40, -122], zoom_start=4,
                    tiles='OpenStreetMap', width=width, height=height)
    fg=folium.FeatureGroup(name="Address Map")
    for i, row in df_adr.iterrows():
       print(row["Latitude"])
       if pandas.isna(row["Latitude"])==False :
           fg.add_child(folium.Marker(location=[row["Latitude"],row["Longitude"]],popup="<strong> Address: </strong>"+row["Address"],icon=folium.Icon(color="green")))

    m.add_child(fg)
    map_html = m.get_root().render()
    return map_html
