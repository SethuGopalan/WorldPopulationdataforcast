
import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go

from dash_labs.plugins.pages import register_page
from bokeh.models import HoverTool

# import data 

# from data import data_File

# data_14=data_File.pop_0_14

df = pd.read_csv("Data\population_aged_0_14_years_both_sexes_percent.csv").dropna()
data = df['country'].dropna()
year_df = df[['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
                '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']]
Year = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
                         2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], axis='columns')

# ----------------------------------------------------------------------------------------------------------------------------------------------(gae14 data end)

df_15 = pd.read_csv("Data\population_aged_15_19_years_both_sexes_percent.csv").dropna()
data_15 = df_15['country'].dropna()
year_df_15 = df_15[['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
                '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']]

Year_15 = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
                         2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], axis='columns')
# ----------------------------------------------------------------------------------------------------------------------------------------(seccond 15 age completed)
df_20 = pd.read_csv("Data\population_aged_20_39_years_both_sexes_percent.csv").dropna()
data_20 = df_15['country'].dropna()
year_df_20 = df_15[['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
                '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']]

Year_20 = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
                         2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], axis='columns')
# -------------------------------------------------------------------------------------------------------------------------------------------(age 20 data end)
df_40 = pd.read_csv("Data\population_aged_40_59_years_both_sexes_percent.csv").dropna()
data_40 = df_15['country'].dropna()
year_df_40 = df_15[['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
                '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']]

Year_40 = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
                         2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], axis='columns')

# Year_15 = year_df_15

# data_lake = [[country, Year]]

data_list=["age_0_14","age_15_19","age_20_39","age_30_59","age_60plus","age_65plus","age_70plus"]

load_figure_template("sketchy")

register_page(__name__)
# app = dash.Dash(__name__,plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.SOLAR])


layout = html.Div([ 
#     [navbar, dl.plugins.page_container],
#     fluid=True,

dbc.Row([

        dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            html.H1("World age wise Population data forcast", style={
                'color': 'LightGoldenrodYellow', 'fontSize': 34, 'font-family': 'Sans-serif',}),
            #  html.H6("________________________________________________")
             


        ], width={'size': 12, 'offset': 4 }),
    ]),
    dbc.Row([

        dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            
            #  html.H6("________________________________________________")
             html.P(" Young Population 0 to 14 year old", style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'}),


        ], width={'size': 3, 'offset': 0 }),
         dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            
            #  html.H6("________________________________________________")
             html.P(" Young Population 15 to 19 year old", style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'}),


        ], width={'size': 3, 'offset': 0 }),
         dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            
            #  html.H6("________________________________________________")
             html.P(" Young Population 20 to 39 year old", style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'}),


        ], width={'size': 3, 'offset': 0 }),
         dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            
            #  html.H6("________________________________________________")
             html.P(" Young Population 40 to 59 year old", style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'}),


        ], width={'size': 3, 'offset': 0 }),
    ]),
    # ---------------------------------------------------------------------------------------------------------------------------------------("here page satrt")

 
# ---------------------------------------------------------------------------------------------------------------------------------------------------(page end)
   
dbc.Row([

        dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([

               html.H6("Select the Country"),

               dcc.Dropdown(id="age14_cid",style={"width": "18rem","background-color": "Tan" }, 
                            options=[{'label': x, 'value': x}
                                      for x in data.unique()],
                            value = ["United States","Australia","China","India"],
                            multi=True


                             ),

            ])

        ], width={'size': 2, 'offset': 0}),
        dbc.Col([

            


            html.Div([
                html.Br(),
                html.Br(),

                html.H6("Select Year"),
                
                
                dcc.Dropdown(id="age14_yid",  style={"background-color": "LightSlateGray"},
                            options=[{'label': str(i), 'value':str(i)}
                                      for i in Year.columns],
                             value = "1980",
                            # # multi=True
 

                             ),



            ])

        ], width={'size': 1, 'offset': 0}),
         dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([

               html.H6("Select the Country"),

               dcc.Dropdown(id="age15_cid", style={"width": "18rem","background-color": "Tan" ,'color':'white',},
                            options=[{'label': x, 'value': x}
                                      for x in data_15.unique()],
                            value = ["United States","Australia","China","India"],
                            multi=True


                             ),

            ])

        ], width={'size': 2, 'offset': 0}),
       
         dbc.Col([

            


            html.Div([
                html.Br(),
                html.Br(),

                html.H6("Select Year"),
                
                
                dcc.Dropdown(id="age15_yid", style={"background-color": "LightSlateGray"},
                            options=[{'label': str(i), 'value':str(i)}
                                      for i in Year_15.columns],
                             value = "1990",
                            # # multi=True
 

                             ),



            ])

        ], width={'size': 1, 'offset': 0}),

         dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([

               html.H6("Select the Country"),

               dcc.Dropdown(id="age20_cid", style={"background-color": "Tan" },
                            options=[{'label': x, 'value': x}
                                      for x in data_20.unique()],
                            value = ["United States","Australia","China","India"],
                            multi=True


                             ),

            ])

        ], width={'size': 2, 'offset': 0}),
       
         dbc.Col([

            


            html.Div([
                html.Br(),
                html.Br(),

                html.H6("Select Year"),
                
                
                dcc.Dropdown(id="age20_yid", style={"background-color": "LightSlateGray"},
                            options=[{'label': str(i), 'value':str(i)}
                                      for i in Year_20.columns],
                             value = "2000",
                            # # multi=True
 

                             ),



            ])

        ], width={'size': 1, 'offset': 0}),
         dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([

               html.H6("Select the Country"),

               dcc.Dropdown(id="age40_cid", style={"width": "18rem","background-color": "Tan" },
                            options=[{'label': x, 'value': x}
                                      for x in data_40.unique()],
                            value = ["United States","Australia","China","India"],
                            multi=True


                             ),

            ])

        ], width={'size': 2, 'offset': 0}),
       
         dbc.Col([

            


            html.Div([
                html.Br(),
                html.Br(),

                html.H6("Select Year"),
                
                
                dcc.Dropdown(id="age40_yid", style={"background-color": "LightSlateGray"},
                            options=[{'label': str(i), 'value':str(i)}
                                      for i in Year_40.columns],
                             value = "2023",
                            # # multi=True
 

                             ),



            ])

        ], width={'size': 1, 'offset': 0}),
       
        dbc.Row([
        dbc.Col([

           

         html.Div([
            
            html.Br(),
            dcc.RadioItems(id="age14_rid",options = [{"label":"ScatterPlot",
                                                       "value":"ScatterPlot",},
                                                       {"label":"BarPlot",
                
                                                       "value":"BarPlot",},
                                                      {"label":"PiePlot",
                
                                                       "value":"PiePlot"},{"label":"LineChart","value":"LineChart"}],value="ScatterPlot"),

               

                dcc.Graph(id="graph1"),
                # dcc.Graph(id="graph1"),
                html.Br(),
                html.Div(id="age14_sid",style={"margin-left": "30px"})
                              
                

            ])

        ], width={'size': 3, 'offset': 0}),
        # dbc.Col([
    
        # html.Div([
        # html.Br(),
        # html.Br(),
        # html.Br(),
        # html.Br(),
    
        
    
         
    
        # ])
    
        # ],width={'size': 6, 'offset': 0}),

        dbc.Col([

           

         html.Div([
            
            html.Br(),
            dcc.RadioItems(id="age15_rid",options = [{"label":"BarPlot",
                
                                                       "value":"BarPlot",},
                                                      {"label":"ScatterPlot",
                                                       "value":"ScatterPlot",},
                                                       
                                                      {"label":"PiePlot",
                
                                                       "value":"PiePlot"},{"label":"LineChart","value":"LineChart"}],value="BarPlot"),

               

                dcc.Graph(id="graph2"),
                # dcc.Graph(id="graph1"),
                html.Br(),
                html.Div(id="age15_sid",style={"margin-left": "30px"})             
                

            ])

        ], width={'size': 3, 'offset': 0}),

        # dbc.Col([
    
        # html.Div([
        # html.Br(),
        # html.Br(),
        # html.Br(),
        # html.Br(),
    
       
    
         
    
        # ])
    
        # ],width={'size': 6, 'offset': 0}),

        dbc.Col([

           

         html.Div([
            
            html.Br(),
            dcc.RadioItems(id="age20_rid",options = [{"label":"ScatterPlot",
                                                       "value":"ScatterPlot",},
                                                       {"label":"BarPlot",
                
                                                       "value":"BarPlot",},
                                                      {"label":"PiePlot",
                
                                                       "value":"PiePlot"},{"label":"LineChart","value":"LineChart"}],value="PiePlot"),

               

                dcc.Graph(id="graph3"),
                # dcc.Graph(id="graph1"),
                html.Br(),
                 html.Div(id="age20_sid",style={"margin-left": "30px"})
                              
                

            ])

        ], width={'size': 3, 'offset': 0}),

        # dbc.Col([
    
        # html.Div([
        # html.Br(),
        # html.Br(),
        # html.Br(),
        # html.Br(),
    
       
    
         
    
        # ])
    
        # ],width={'size': 6, 'offset': 0}),

        dbc.Col([

           

         html.Div([
            
            html.Br(),
            dcc.RadioItems(id="age40_rid",options = [{"label":"ScatterPlot",
                                                       "value":"ScatterPlot",},
                                                       {"label":"BarPlot",
                
                                                       "value":"BarPlot",},
                                                      {"label":"PiePlot",
                
                                                       "value":"PiePlot"},{"label":"LineChart","value":"LineChart"}],value="LineChart"),

               

                dcc.Graph(id="graph4"),
                # dcc.Graph(id="graph1"),
                html.Br(),
                
                html.Div(id="age40_sid",style={"margin-left": "30px"})
                              
                

            ])

        ], width={'size': 3, 'offset': 0}),


        
        ]),

       

        

        # dbc.Col([
        
        # html.Div([
       
        # dbc.NavItem(dbc.Button('Click here to find agewise population',style={
        #         'color': 'white', 'fontSize': 16, 'font-family': 'cursive'},href="pages\data_Statistics.py")),
    
    
        # ])
    
        # ]),
        

        

        # dbc.Col([
    
        # html.Div([
        # html.Br(),
        # html.Br(),
        # html.Br(),
        # html.Br(),
    
        
    
         
    
        # ])
    
        # ],width={'size': 6, 'offset': 0})

        
       


])

])
       
# p--------------------------------------------------------------------------------------------------------------(fisrt app)
# p--------------------------------------------------------------------------------------------------------------(start second app)


@callback(Output("graph1", "figure"),
               Output("age14_sid","children"),
               Input('age14_cid', "value"),
               Input("age14_yid","value"),
               Input("age14_rid","value"))

def cont_value(Con_data,Yr_data,Rad_data):

    
    # dff=[data.isin(Con_data)]
    
    dff=df[(df['country'].isin(Con_data))] 
    

    if Rad_data == "ScatterPlot":
    
       fig = px.scatter(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data,trendline="ols", trendline_options=dict(log_x=True),labels={'x':"Country"})
       fig.update_traces(marker_size=15,mode="markers+lines")
    

    if Rad_data =="BarPlot":
             
         fig=px.bar(dff,x=Con_data,y=Yr_data,color=Con_data,height=400,barmode='group',text=Yr_data,text_auto='.2s',labels={'x':"Country"},pattern_shape_sequence=[".", "x", "+"])
         
         fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    
    

    if Rad_data== "PiePlot":

        fig=px.bar_polar(dff,r=Yr_data,theta=Con_data,color=Con_data,template="plotly_dark", color_continuous_scale=px.colors.sequential.Plasma)

    if Rad_data == "LineChart":
    
         fig = px.line(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data, labels={'x':"Country"})
        #  fig = px.line(dff, x=df['country'],y=Year,color=df['country'],symbol=df['country'], labels={'x':"Country"})
         fig.update_traces(mode="markers + lines")
    
        
        
    
    return fig ,html.Div([html.P("Selected Contires are {},Year is {}".format(str(Con_data)[1:-1].replace("'", ""),Yr_data,sep=", ",),style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'})]),
    # ---------------------------------------------------------------------------------------------------------------------------------------------------(end fist callback)

@callback(Output("graph2", "figure"),
        Output("age15_sid","children"),
        Input('age15_cid', "value"),
        Input("age15_yid","value"),
        Input("age15_rid","value"))

def cont_value(Con_data,Yr_data,Rad_data):

    
    # dff=[data.isin(Con_data)]
    
    dff=df_15[(df_15['country'].isin(Con_data))] 
    

    if Rad_data == "ScatterPlot":
    
       fig = px.scatter(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data,trendline="ols", trendline_options=dict(log_x=True),labels={'x':"Country"})
       fig.update_traces(marker_size=15,mode="markers+lines")
    

    if Rad_data =="BarPlot":
             
         fig=px.bar(dff,x=Con_data,y=Yr_data,color=Con_data,height=400,barmode='group',text=Yr_data,text_auto='.2s',labels={'x':"Country"},pattern_shape_sequence=[".", "x", "+"])
         
         fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    
    

    if Rad_data== "PiePlot":

        fig=px.bar_polar(dff,r=Yr_data,theta=Con_data,color=Con_data,template="plotly_dark", color_continuous_scale=px.colors.sequential.Plasma)

    if Rad_data == "LineChart":
    
         fig = px.line(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data, labels={'x':"Country"})
        #  fig = px.line(dff, x=df['country'],y=Year,color=df['country'],symbol=df['country'], labels={'x':"Country"})
         fig.update_traces(mode="markers + lines")
    
        
        
    
    return fig ,html.Div([html.P("Selected Contires are {},Year is {}".format(str(Con_data)[1:-1].replace("'", ""),Yr_data,sep=", "),style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'})]),
# --------------------------------------------------------------------------------------------------------------------------------------(seccond callback finish)

@callback(Output("graph3", "figure"),
        Output("age20_sid","children"),
        Input('age20_cid', "value"),
        Input("age20_yid","value"),
        Input("age20_rid","value"))

def cont_value(Con_data,Yr_data,Rad_data):

    
    # dff=[data.isin(Con_data)]
    
    dff=df_20[(df_20['country'].isin(Con_data))] 
    

    if Rad_data == "ScatterPlot":
    
       fig = px.scatter(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data,trendline="ols", trendline_options=dict(log_x=True),labels={'x':"Country"})
       fig.update_traces(marker_size=15,mode="markers+lines")
    

    if Rad_data =="BarPlot":
             
         fig=px.bar(dff,x=Con_data,y=Yr_data,color=Con_data,height=400,barmode='group',text=Yr_data,text_auto='.2s',labels={'x':"Country"},pattern_shape_sequence=[".", "x", "+"])
         
         fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    
    

    if Rad_data== "PiePlot":

        fig=px.bar_polar(dff,r=Yr_data,theta=Con_data,color=Con_data,template="plotly_dark", color_continuous_scale=px.colors.sequential.Plasma)

    if Rad_data == "LineChart":
    
         fig = px.line(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data, labels={'x':"Country"})
        #  fig = px.line(dff, x=df['country'],y=Year,color=df['country'],symbol=df['country'], labels={'x':"Country"})
         fig.update_traces(mode="markers + lines")
    
        
        
    
    return fig ,html.Div([html.P("Selected Contires are {},Year is {}".format(str(Con_data)[1:-1].replace("'", ""),Yr_data,sep=", "),style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'})]),
# --------------------------------------------------------------------------------------------------------------------------------------(3rd callback end)
@callback(Output("graph4", "figure"),
        Output("age40_sid","children"),
        Input('age40_cid', "value"),
        Input("age40_yid","value"),
        Input("age40_rid","value"))

def cont_value(Con_data,Yr_data,Rad_data):

    
    # dff=[data.isin(Con_data)]
    
    dff=df_40[(df_20['country'].isin(Con_data))] 
    

    if Rad_data == "ScatterPlot":
    
       fig = px.scatter(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data,trendline="ols", trendline_options=dict(log_x=True),labels={'x':"Country"})
       fig.update_traces(marker_size=15,mode="markers+lines")
    

    if Rad_data =="BarPlot":
             
         fig=px.bar(dff,x=Con_data,y=Yr_data,color=Con_data,height=400,barmode='group',text=Yr_data,text_auto='.2s',labels={'x':"Country"},pattern_shape_sequence=[".", "x", "+"])
         
         fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    
    

    if Rad_data== "PiePlot":

        fig=px.bar_polar(dff,r=Yr_data,theta=Con_data,color=Con_data,template="plotly_dark", color_continuous_scale=px.colors.sequential.Plasma)

    if Rad_data == "LineChart":
    
         fig = px.line(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data, labels={'x':"Country"})
        #  fig = px.line(dff, x=df['country'],y=Year,color=df['country'],symbol=df['country'], labels={'x':"Country"})
         fig.update_traces(mode="markers + lines")
    
        
        
    
    return fig ,html.Div([html.P("Selected Contires are {},Year is {}".format(str(Con_data)[1:-1].replace("'", ""),Yr_data,sep=", "),style={
                'color': 'LightGoldenrodYellow', 'fontSize': 16, 'font-family': 'Sans-serif'})]),