import pandas as pd
import plotly.express as px
import requests
import plotly.io as pio

json_data = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json'
regiones_mx = requests.get(json_data).json()

df = pd.read_csv('estado_x_migracion.csv')

fig = px.choropleth(
    df,
    geojson=regiones_mx,
    locations='poblacion',
    featureidkey='properties.name',
    color='total_inmigracion',
    color_continuous_scale='Peach'
)

fig.update_geos(fitbounds='locations')

fig.update_layout(
    title_text = 'Inmigración por Estado',
    title_x=0.5,
    annotations = [dict(
        x=0.55,
        y=-0.1,
        xref='paper',
        yref='paper',
        text='Fuente: Censo de población y vivienda 2020, <a href="https://www.inegi.org.mx/contenidos/programas/ccpv/2020/tabulados/cpv2020_b_eum_04_migracion.xlsx", target="_blank">sección migración.</a>',
        showarrow=False
    )]
)

pio.write_html(fig, file='migracion_por_estado.html', auto_open=True)

fig.show()
