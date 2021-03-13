import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data_migracion_MX.csv')
print(df.head())

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode = 'ISO-3',
    lon=df['origen_lon'],
    lat=df['origen_lat'],
    text=df['origen'],
    mode='markers',
    marker=dict(
        size=2,
        color='rgba(0, 182, 255, 0.6)',
        line=dict(
            width=3,
            color='rgba(0, 182, 255, 0.6)'
        )
)))

ruta_migratoria = []



for i in range(len(df)):
    # ancho_linea = float(df['poblacion_total'][i]) / float(df['poblacion_total'].max()) + 1
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'ISO-3',
            lon = [df['origen_lon'][i], df['destino_lon'][i]],
            lat = [df['origen_lat'][i], df['destino_lat'][i]],
            mode = 'lines',
            line = dict(width = 2, color = 'black'),
            opacity = float(df['poblacion_total'][i]) / float(df['poblacion_total'].max()),
        )
    )

fig.update_layout(
    title_text = 'Población por entidad federativa actual y lugar de nacimiento',
    showlegend = False,
    geo = dict(
        scope = 'north america',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgba(206, 222, 220, 0.5)',
        countrycolor = 'rgba(92, 214, 199, 0.5)',
    ),
)

fig.show()
