import plotly.express as px
import pandas as pd


df = pd.read_csv('estado_x_migracion.csv')

fig = px.scatter_geo(df, lat='lat',
                     lon='lon',
                     color='poblacion',
                     color_continuous_scale='Peach',
                     hover_name='poblacion',
                     size='total_inmigracion',
                     projection='azimuthal equal area',
                     scope='north america',
                     center=dict(lat=19.419444, lon=-99.145556),
                     title="Cantidad de inmigrantes",
                     size_max=40
                     )
fig.show()
