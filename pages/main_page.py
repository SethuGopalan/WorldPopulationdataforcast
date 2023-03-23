import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
import dash_labs as dl
from dash_labs.plugins.pages import register_page
import itertools,functools,collections
from plotly.subplots import make_subplots
import os,sys
from matplotlib import pyplot as plt
df = pd.read_csv("Data\population_total.csv")
# Year=df.drop(df.columns[0])
data = df['country']
# Year=df.pop(df.columns[0])
Year = df[['1799','1800','1801','1802','1803','1804','1805','1806','1807','1808','1809','1810','1811','1812','1813','1814','1815','1816','1817','1818','1819','1820','1821','1822','1823','1824','1825','1826','1827','1828','1829','1830','1831','1832','1833','1834','1835','1836','1837','1838','1839','1840','1841','1842','1843','1844','1845','1846','1847','1848','1849','1850','1851','1852','1853','1854','1855','1856','1857','1858','1859','1860','1861','1862','1863','1864','1865','1866','1867',	
                         '1868','1869','1870','1871','1872','1873','1874','1875','1876','1877','1878','1879','1880','1881','1882','1883','1884','1885','1886','1887','1888','1889','1890','1891','1892','1893','1894','1895','1896','1897','1898','1899','1900','1901','1902','1903','1904','1905','1906','1907','1908','1909','1910','1911',
                        '1912','1913','1914','1915','1916','1917','1918','1919','1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939','1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989',
                        '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018',
                        '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2044','2045','2046','2047','2048',	'2049',	'2050',	'2051',	'2052',	'2053',	'2054',	'2055',	'2056',	'2057',	'2058',	'2059',	'2060',	'2061',	'2062',	'2063',	'2064',	'2065',	'2066',	'2067',	'2068',	'2069',	'2070',	'2071',	'2072',	'2073',	'2074',	'2075',	'2076',	'2077',	'2078',	'2079',	'2080',	'2081',	'2082',	'2083',	'2084',	'2085',	'2086',	'2087',	'2088',	'2089',	'2090',	'2091',	'2092',	'2093',	'2094',	'2095',	'2096',	'2097',	'2098',	'2099']]
# # Year = year_df.set_axis([1799,1800,1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,	
# #                          1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,
# #                         1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
# #                         1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
# #                          2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], axis='columns')
# Y_Year=Year.dropna()
# All_data=pd.concat([data, Year])


# files = os.listdir(path)



load_figure_template("sketchy")

register_page(__name__, path="/")
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

            html.H1("Wold Population data forcast", style={
                'color': 'white', 'fontSize': 24, 'font-family': 'Sans-serif'}),
            #  html.H6("________________________________________________")


        ], width={'size': 12, 'offset': 4 }),
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

               html.H6("Select the Country In alphabetic Order"),

               dcc.Dropdown(id="cont_ID", 
                            options=[{'label': x, 'value': x}
                                      for x in (df['country'])],
                            
                            value = ["Australia","China","United States"],
                            multi=True


                             ),

            ])

        ], width={'size': 6, 'offset': 0}),

        dbc.Col([

            html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),


            html.Div([  
                

                html.H6("Select Year"),
                
                
                dcc.Dropdown(id="Year_ID", 
                            options=[{'label': str(i), 'value':str(i)}
                                      for i in Year],
                             value = "1976",
                            # # multi=True
 

                             ),



            ])

        ], width={'size': 2, 'offset': 0}),

        

        dbc.Col([
        html.Br(),
        html.Br(),
        html.Div([
       
        dbc.NavItem(dbc.Button('Click here to find agewise population',style={
                'color': 'white', 'fontSize': 16, 'font-family': 'cursive'},href="pages\data_Statistics.py")),
    
    
        ])
    
        ]),
        

        dbc.Col([

            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),
            # html.Br(),

         html.Div([
            
            html.Br(),
            dcc.RadioItems(id="rado_id",options = [{"label":"ScatterPlot",
                                                       "value":"ScatterPlot",},
                                                       {"label":"BarPlot",
                
                                                       "value":"BarPlot",},
                                                      {"label":"PiePlot",
                
                                                       "value":"PiePlot"},{"label":"LineChart","value":"LineChart"}],value="ScatterPlot"),

               

                dcc.Graph(id="graph"),
                # dcc.Graph(id="graph1"),
                
                html.Br(),
                html.Br(),
               
                

            ])

        ], width={'size': 6, 'offset': 0}),

        dbc.Col([
        html.Br(),
        html.Br(),
    
        html.Div([
        
    
        html.Div(id="sel_id",style={"margin-left": "30px"}),
        
        
         
    
        ]),

        

        html.Div([
        
        
        html.Br(),

        
    
        html.Div(id="Mess_id",style={"margin-left": "36px"}),
        # html.Div(id="Mess1_id",style={"margin-left": "36px",'fontSize': 30,"height": "200px",  'width': '45%','align' :'left'}),
        # html.Div(id="Mess2_id",style={"margin-left": "36px",'fontSize': 30,"height": "200px",  'width': '45%','align' :'left'}),
        # html.Div(id="Mess3_id",style={"margin-left": "36px",'fontSize': 30,"height": "200px",  'width': '45%','align' :'left'})
        
    
         
    
        
       
        ])
       
        ],width={'size': 4, 'offset': 0}),
        
        
       

       

        ])



]),



       
# p--------------------------------------------------------------------------------------------------------------(fisrt app)
# p--------------------------------------------------------------------------------------------------------------(start second app)


@callback(Output("graph", "figure"),
        
               Output("sel_id","children"),
               Output("Mess_id","children"),
            #    Output("Mess1_id","children"),
            #    Output("Mess2_id","children"),
            #    Output("Mess3_id","children"),
               [Input('cont_ID', "value"),
               Input("Year_ID","value"),
               Input("rado_id","value")])

def cont_value(Con_data,Yr_data,Rad_data):

    
    # dff=[data.isin(Con_data)]
    
    dff=df.loc[df['country'].isin(Con_data)& [i for i in Year if i==Yr_data]]

    # todayMPCon=df.groupby[df['country'].agg & Year["2023"]:[max,min]] 

    # dff=df.loc[df['country'].isin(Con_data)& (Year==Yr_data)]

    # dff =[df['country'].isin(Con_data) & (Year==Yr_data[1])]
    # dff=dff[Year==Yr_data]
    # dff=df.loc[(Year == Yr_data) & df['country'].isin(Con_data)]
    

    def flag_return():
   
        flag_file="assets\Flag_name"
        new_flag=[]
        # file_flag=os.listdir(flag_file)
        for i in os.listdir(flag_file):
           for x in Con_data:
                   if i==x + ".png":
                                               
                        new_flag.append(i)
                        
                
        return (str(new_flag)[1:-1].replace("'", ""))
        
               
    flag=flag_return()
                    
                   
        
    if Rad_data == "ScatterPlot":
    
       fig = px.scatter(dff, x=Con_data,y=Yr_data,color=Yr_data,symbol=Con_data,labels={'x':"Country"})
       fig.update_traces(marker_size=15)
    #    fig.update_xaxes(categoryorder="min ascending")
    #    fig.update_yaxes(categoryorder="min ascending")
    
    if Rad_data =="BarPlot":
             
         fig=px.bar(dff,x=Con_data,y=Yr_data,color=Con_data,height=400,barmode='group',text=Yr_data,text_auto=True,labels={'x':"Country"},pattern_shape_sequence=[".", "x", "+"])
         
         fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        #  fig.update_xaxes(categoryorder="trace",categoryarray="array")
        #  fig.update_yaxes(categoryorder="trace" )
    

    if Rad_data== "PiePlot":

        fig=px.bar_polar(dff,r=Yr_data,theta=Con_data,color=Con_data,template="plotly_dark", color_continuous_scale=px.colors.sequential.Plasma)
        # fig.update_xaxes(categoryorder="trace")
        # fig.update_yaxes(categoryorder="trace")

    if Rad_data == "LineChart":
    
         fig = px.line(dff, x=Con_data,y=Yr_data,color=Con_data,symbol=Con_data, labels={'x':"Country"})
        #  fig = px.line(dff, x=df['country'],y=Year,color=df['country'],symbol=df['country'], labels={'x':"Country"})
         fig.update_traces(mode="markers + lines")
    
        
    

    
    # return fig ,html.Div([html.P("Selected Contires are {},Year is {}".format(str(Con_data)[1:-1].replace("'", ""),Yr_data,sep=", "))]),html.Div([html.P("Population Minis {},Population Max{} population mean{}".format(min(Con_data),max(Con_data),max(Con_data)))])
    
    return fig ,html.Div([html.P("Selected Contires are {},Year is {}".format(str(Con_data)[1:-1].replace("'", ""),Yr_data,sep=", "))]), html.Div([html.Img(srcSet=("assets/Flag_name/"f'{flag}'))])



# if __name__ == "__main__":
#     app.run_server(debug=True, port=8052
