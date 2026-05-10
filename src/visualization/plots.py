import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_choropleth(df: pd.DataFrame, metric: str):
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        locations="state",
        featureidkey="properties.ST_NM",
        color=metric,
        color_continuous_scale="Viridis"
    )
    
    fig.update_geos(
        visible=False,
        showsubunits=True,
        showcountries=True
    )
    
    return fig

def create_trend_chart(df: pd.DataFrame, x: str, y: str, title: str):
    fig = px.line(
        df,
        x=x,
        y=y,
        title=title
    )
    
    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y
    )
    
    return fig
