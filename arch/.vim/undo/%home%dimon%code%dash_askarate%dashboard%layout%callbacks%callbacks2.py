Vim�UnDo� 2|@�������n�/9pQ�*�Ĥ�t�   c                                  d�܁    _�                             ����                                                                                                                                                                                                                                                                                                                                                             d��d    �                   5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             d���    �               U@app.callback(Output("tabs-example-content", "children"), Input("app-tabs", "value"))5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d���    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       d��Q    �      b       �             5�_�                            ����                                                                                                                                                                                                                                                                                                                            c          h          V       d��[   	 �         h    �         h    5�_�                            ����                                                                                                                                                                                                                                                                                                                                       
           V        d��n   
 �          d    �         d    �              
   from dashboard.index import app   (from dashboard.layout.tab_1 import tab_1   (from dashboard.layout.tab_2 import tab_2   +from dash.dependencies import Input, Output   	import os   import glob   ;from dash import Dash, dcc, html, dash_table, Input, Output   import pandas as pd   'import dash_bootstrap_components as dbc   !import plotly.graph_objects as go5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             d��+    �         k    5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             d��,    �         l       �         l    5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             d��,    �         l    5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             d��.    �         l    5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             d��/    �         l    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��2    �         l    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��3     �         l    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��7    �   m               �       n       �               l   from dashboard.index import app   import pandas as pd   ;from dash import Dash, dcc, html, dash_table, Input, Output   (from dashboard.layout.tab_1 import tab_1   (from dashboard.layout.tab_2 import tab_2   +from dashboard.index import sportsmen_frame   'import dash_bootstrap_components as dbc   !import plotly.graph_objects as go       %def chart_count_region(year, region):       region_count = (           sportsmen_frame.loc[   >            sportsmen_frame["Год"].astype(int).isin([year])   9            & (sportsmen_frame["Регион"] == region)   	        ]   "        .groupby(["Регион"])           .size()   3        .to_frame(name="Виды программ")           .reset_index()       )       data = sportsmen_frame.loc[   :        sportsmen_frame["Год"].astype(int).isin([year])   5        & (sportsmen_frame["Регион"] == region)       ][   	        [               "пол",               "Фамилия",               "Имя",               "Отчество",   (            "Дата рождения",   "            "Полных лет",               "Регион",   	        ]       ]       rr = data.drop_duplicates()   e    region_rr = rr.groupby(["Регион"]).size().to_frame(name="Участники").reset_index()   V    region_rr["Виды программ"] = region_count["Виды программ"]   2    region_rr.reset_index(drop=True, inplace=True)       region_rr.index += 1   ^    return region_rr["Участники"].sum(), region_rr["Виды программ"].sum()           @app.callback(   %    Output("region_chart", "figure"),   8    Output("table_histogram_region_output", "children"),   $    Input("region-filter", "value"),   )   def view_chart(region):       results = []       for _ in range(2015, 2023):           i = []   ,        x, y = chart_count_region(_, region)           i.extend([_, x, y])           results.append(i)   h    dff = pd.DataFrame(results, columns=["Год", "Спортсмены", "Виды программ"])       fig = go.Figure()       fig.add_scatter(           x=dff["Год"],   +        y=dff["Виды программ"],   )        name="Виды программ",   U        hovertemplate="Год=%{x}<br>Виды программ=%{y}<extra></extra>",       )       fig.add_scatter(           x=dff["Год"],   &        y=dff["Спортсмены"],   $        name="Спортсмены",   P        hovertemplate="Год=%{x}<br>Спортсмены=%{y}<extra></extra>",       )   !    fig.layout.yaxis.title = None   p    fig.layout.title = f"Количество участников Чемпионата России - {region}"           tables_region = html.Div(   	        [   E            dbc.Label(f"Чемпионат России - {region}"),   !            dash_table.DataTable(   ,                data=dff.to_dict("records"),   J                columns=[{"name": col, "id": col} for col in dff.columns],                   style_cell={   (                    "textAlign": "left",   )                    "overflow": "hidden",   /                    "textOverflow": "ellipsis",   "                    "maxWidth": 0,                   },   J                style_data={"color": "black", "backgroundColor": "white"},   (                style_data_conditional=[                       {   3                        "if": {"row_index": "odd"},   5                        "backgroundColor": "#E5ECF6",                       }                   ],                   style_header={   1                    "backgroundColor": "#eb6864",   %                    "color": "white",   )                    "fontWeight": "bold",   +                    "whiteSpace": "normal",                   },               ),   	        ]       )       return fig, tables_region           V@app.callback(Output("tabs2-example-content", "children"), Input("app-tabs", "value"))   def callback2(tab):       if tab == "tab-1":           return tab_1       elif tab == "tab-2":           return tab_25�_�                    h        ����                                                                                                                                                                                                                                                                                                                            h          m          V       d��w    �   l   n                  return tab_2�   k   m              elif tab == "tab-2":�   j   l                  return tab_1�   i   k              if tab == "tab-1":�   h   j          def callback2(tab):�   g   i          V@app.callback(Output("tabs2-example-content", "children"), Input("app-tabs", "value"))5�_�                    h        ����                                                                                                                                                                                                                                                                                                                            h           m           V        d�؝    �   g   h          X# @app.callback(Output("tabs2-example-content", "children"), Input("app-tabs", "value"))   # def callback2(tab):   #     if tab == "tab-1":   #         return tab_1   #     elif tab == "tab-2":   #         return tab_25�_�                    g        ����                                                                                                                                                                                                                                                                                                                            h           h           V        d�؝    �   f   g           5�_�                    f        ����                                                                                                                                                                                                                                                                                                                            g           g           V        d�؞    �   e               �       f       �               f   from dashboard.index import app   import pandas as pd   ;from dash import Dash, dcc, html, dash_table, Input, Output   (from dashboard.layout.tab_1 import tab_1   (from dashboard.layout.tab_2 import tab_2   +from dashboard.index import sportsmen_frame   'import dash_bootstrap_components as dbc   !import plotly.graph_objects as go           %def chart_count_region(year, region):       region_count = (           sportsmen_frame.loc[   >            sportsmen_frame["Год"].astype(int).isin([year])   9            & (sportsmen_frame["Регион"] == region)   	        ]   "        .groupby(["Регион"])           .size()   3        .to_frame(name="Виды программ")           .reset_index()       )       data = sportsmen_frame.loc[   :        sportsmen_frame["Год"].astype(int).isin([year])   5        & (sportsmen_frame["Регион"] == region)       ][   	        [               "пол",               "Фамилия",               "Имя",               "Отчество",   (            "Дата рождения",   "            "Полных лет",               "Регион",   	        ]       ]       rr = data.drop_duplicates()   e    region_rr = rr.groupby(["Регион"]).size().to_frame(name="Участники").reset_index()   V    region_rr["Виды программ"] = region_count["Виды программ"]   2    region_rr.reset_index(drop=True, inplace=True)       region_rr.index += 1   ^    return region_rr["Участники"].sum(), region_rr["Виды программ"].sum()           @app.callback(   %    Output("region_chart", "figure"),   8    Output("table_histogram_region_output", "children"),   $    Input("region-filter", "value"),   )   def view_chart(region):       results = []       for _ in range(2015, 2023):           i = []   ,        x, y = chart_count_region(_, region)           i.extend([_, x, y])           results.append(i)   h    dff = pd.DataFrame(results, columns=["Год", "Спортсмены", "Виды программ"])       fig = go.Figure()       fig.add_scatter(           x=dff["Год"],   +        y=dff["Виды программ"],   )        name="Виды программ",   U        hovertemplate="Год=%{x}<br>Виды программ=%{y}<extra></extra>",       )       fig.add_scatter(           x=dff["Год"],   &        y=dff["Спортсмены"],   $        name="Спортсмены",   P        hovertemplate="Год=%{x}<br>Спортсмены=%{y}<extra></extra>",       )   !    fig.layout.yaxis.title = None   p    fig.layout.title = f"Количество участников Чемпионата России - {region}"           tables_region = html.Div(   	        [   E            dbc.Label(f"Чемпионат России - {region}"),   !            dash_table.DataTable(   ,                data=dff.to_dict("records"),   J                columns=[{"name": col, "id": col} for col in dff.columns],                   style_cell={   (                    "textAlign": "left",   )                    "overflow": "hidden",   /                    "textOverflow": "ellipsis",   "                    "maxWidth": 0,                   },   J                style_data={"color": "black", "backgroundColor": "white"},   (                style_data_conditional=[                       {   3                        "if": {"row_index": "odd"},   5                        "backgroundColor": "#E5ECF6",                       }                   ],                   style_header={   1                    "backgroundColor": "#eb6864",   %                    "color": "white",   )                    "fontWeight": "bold",   +                    "whiteSpace": "normal",                   },               ),   	        ]       )       return fig, tables_region    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��w    �         e      ;from dash import Dash, dcc, html, dash_table, Input, Output5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��x     �         e      7from dash import , dcc, html, dash_table, Input, Output5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��x    �         e      6from dash import  dcc, html, dash_table, Input, Output5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��{     �         e      5from dash import dcc, html, dash_table, Input, Output5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��|     �         e      2from dash import , html, dash_table, Input, Output5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             d��|    �         e      1from dash import  html, dash_table, Input, Output5�_�                             ����                                                                                                                                                                                                                                                                                                                                                V       d�܀    �                (from dashboard.layout.tab_1 import tab_1   (from dashboard.layout.tab_2 import tab_25�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d��M    �              5��