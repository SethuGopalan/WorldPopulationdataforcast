import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

import plotly.express as px
from plotly.offline import plot


df = pd.read_csv("Data\population_total.csv")
data = df['country']
year_df = df[['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
                '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']]
Year = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
                         2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], axis='columns')

# data_lake = [[country, Year]]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])


app.layout = dbc.Container([

    dbc.Row([

        dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            html.H1("Wold Population data forcast", style={
                'color': 'white', 'fontSize': 24, 'font-family': 'Sans-serif'}),
            #  html.H6("________________________________________________")


        ], width={'size': 12, 'offset': 4 }),


        dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([

                html.H6("Select the Country"),

                dcc.Dropdown(id="cont_ID", style={'color': 'black', 'background': 'white', },
                             options=[{'label': x, 'value': x}
                                      for x in df["country"]],
                             value = ["United States","Australia","China","India"],
                             multi=True


                             ),


            ])

        ], width={'size': 3, 'offset': 0}),

        dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([

                html.H6("Select Year"),
                
                
                dcc.Dropdown(id="Year_ID", style={'color': 'black', 'background': 'white', },
                             options=[{'label': str(i), 'value':str(i)}
                                      for i in Year.columns],
                            value = "1976",
                            # multi=True
 

                             ),


            ])

        ], width={'size': 3, 'offset': 0}),

    ]),

    dbc.Row([

        dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),

            html.Div([

                html.H6("Year population data visualization "),
                html.Br(),
                dcc.RadioItems(id="rado_id",options = [{"label":"ScatterPlot",
                                                       "value":"ScatterPlot",},
                                                       {"label":"BarPlot",
                
                                                       "value":"BarPlot",},
                                                      {"label":"BoxPlot",
                
                                                       "value":"BoxPlot"}],value="ScatterPlot"),

               

                dcc.Graph(id="graph"),
                # dcc.Graph(id="graph1"),
                
                html.Br(),
                html.Br(),
                html.Div(id="sel_id")
                

            ])

        ], width={'size': 6, 'offset': 0}),

        dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),



            html.Div([

                html.H6("Contries Population Age carogories"),
                dcc.Dropdown(id="yon_ID"),
                html.Br(),

            ]),

        ], width={'size': 3, 'offset': 2}),


    ])

])


@app.callback(Output("graph", "figure"), Output("sel_id","children"),Input('cont_ID', "value"),Input("Year_ID","value"),Input("rado_id","value"))

def cont_value(Con_data,Yr_data,Rad_data):

    
    dff=df[df['country'].isin(Con_data)]

    if Rad_data == "ScatterPlot":
       fig = px.scatter(dff, x=Con_data,y=Yr_data,color=Con_data,labels={'x':"Country"})
       fig.update_traces(marker_size=15)
    # fig.update_layout(scattermode="group")

    if Rad_data =="BarPlot":
             
       fig=px.bar(dff,x=Con_data,y=Yr_data,color=Con_data,labels={'x':"Country"})

    if Rad_data== "BoxPlot":

        fig=px.box(dff,x=Con_data,y=Yr_data,color=Yr_data,labels={'x':"Country"})
        # fig.update_traces(orientation='h')
    
    return fig ,html.Div([html.P("Selected contires are {},Year is {}".format(str(Con_data),Yr_data))])
    
    
    
         
        
        



if __name__ == "__main__":
    app.run_server(debug=True, port=8052)
