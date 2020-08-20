import plotly.graph_objects as go
import plotly.io as pio

mapbox_access_token = "pk.eyJ1IjoibWVlcGVycyIsImEiOiJja2UwNTE4cmYyOWE1MnhtY2lrd3NkY3oyIn0.y6jfb44p5jpJflTxLhXZ2g"

fig = go.Figure(go.Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=14
        ),
        text=['Montreal'],
    ))

fig.update_layout(
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5
    )
)
print("hopefully")
fig.write_image("maps/fig1.png")
fig.show()
