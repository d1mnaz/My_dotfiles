Vim�UnDo� �&V'sF��-i�J������zR�TYsRO   d       d                           d��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             d���    �                @from utils.constants import gdp_page_location, gcs_page_location5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d���    �                 5�_�                    @   @    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   ?   A   O      a                        "Общая статистика", href=gcs_page_location, active="exact"5�_�                    @   @    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   ?   A   O      P                        "Общая статистика", href=, active="exact"�   @   A   O    5�_�                    @   A    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   @   A   O    5�_�                    @   B    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���     �   @   A   O    5�_�                    D       ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   C   E   O      /                        href=gdp_page_location,5�_�      	              D       ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   C   E   O                              href=,�   D   E   O    5�_�      
           	   D       ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   D   E   O    5�_�   	              
   D       ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���   	 �   D   E   O    5�_�   
                 D   #    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���   
 �   D   E   O    5�_�                    D   $    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   D   E   O    5�_�                    D   &    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���     �   D   E   O    5�_�                    D   %    ����                                                                                                                                                                                                                                                                                                                            @   @       @   P       v   A    d���    �   M               �       N       �               O   'import dash_bootstrap_components as dbc   from dash import dcc, html           C# we use the Row and Col components to construct the sidebar header   M# it consists of a title, and a toggle, the latter is hidden on large screens   sidebar_header = dbc.Row(       [   4        dbc.Col(html.H2("", className="display-4")),           dbc.Col(               [                   html.Button(   G                    # use the Bootstrap navbar-toggler classes to style   ?                    html.Span(className="navbar-toggler-icon"),   /                    className="navbar-toggler",   @                    # the navbar-toggler classes don't set color                       style={   2                        "color": "rgba(0,0,0,.5)",   9                        "border-color": "rgba(0,0,0,.1)",                       },   '                    id="navbar-toggle",                   ),                   html.Button(   G                    # use the Bootstrap navbar-toggler classes to style   ?                    html.Span(className="navbar-toggler-icon"),   /                    className="navbar-toggler",   @                    # the navbar-toggler classes don't set color                       style={   2                        "color": "rgba(0,0,0,.5)",   9                        "border-color": "rgba(0,0,0,.1)",                       },   (                    id="sidebar-toggle",                   ),               ],   J            # the column containing the toggle will be only as wide as the   A            # toggle, resulting in the toggle being right aligned               width="auto",   7            # vertically align the toggle in the center               align="center",   
        ),       ]   )       sidebar = html.Div(       [           sidebar_header,   J        # we wrap the horizontal rule and short blurb in a div that can be   "        # hidden on a small screen           html.Div(               [                   html.Hr(),                   html.P(   x                    "Статистика Чемпионатов Росси по всестилевому каратэ",   %                    className="lead",                   ),               ],               id="blurb",   
        ),   H        # use the Collapse component to animate hiding / revealing links           dbc.Collapse(               dbc.Nav(                   [                        dbc.NavLink(   S                        "Общая статистика", href="/", active="exact"                       ),                        dbc.NavLink(   K                        "Статистика по дисциплинам",   (                        href="/archive",   '                        active="exact",                       ),                   ],                   vertical=True,                   pills=True,               ),               id="collapse",   
        ),       ],       id="sidebar",   )5�_�                            ����                                                                                                                                                                                                                                                                                                                            N   @       N   P       v   A    d��S    �         M    5�_�                            ����                                                                                                                                                                                                                                                                                                                            O   @       O   P       v   A    d��S     �         N    5�_�                    N        ����                                                                                                                                                                                                                                                                                                                            O   @       O   P       v   A    d���    �   N            �   N            5�_�                    O        ����                                                                                                                                                                                                                                                                                                                            c   @       c   P       v   A    d���    �   N   P   b    5�_�                    O        ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���     �   O   P   c    5�_�                           ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���    �         c      from dash import dcc, html5�_�                           ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���    �         c    5�_�                            ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���    �         c    5�_�                       "    ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���    �         c    5�_�                       $    ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���     �         c    5�_�                       #    ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d���    �   c               �       d       �               c   'import dash_bootstrap_components as dbc   $from dash import dcc, html, callback               C# we use the Row and Col components to construct the sidebar header   M# it consists of a title, and a toggle, the latter is hidden on large screens   sidebar_header = dbc.Row(       [   4        dbc.Col(html.H2("", className="display-4")),           dbc.Col(               [                   html.Button(   G                    # use the Bootstrap navbar-toggler classes to style   ?                    html.Span(className="navbar-toggler-icon"),   /                    className="navbar-toggler",   @                    # the navbar-toggler classes don't set color                       style={   2                        "color": "rgba(0,0,0,.5)",   9                        "border-color": "rgba(0,0,0,.1)",                       },   '                    id="navbar-toggle",                   ),                   html.Button(   G                    # use the Bootstrap navbar-toggler classes to style   ?                    html.Span(className="navbar-toggler-icon"),   /                    className="navbar-toggler",   @                    # the navbar-toggler classes don't set color                       style={   2                        "color": "rgba(0,0,0,.5)",   9                        "border-color": "rgba(0,0,0,.1)",                       },   (                    id="sidebar-toggle",                   ),               ],   J            # the column containing the toggle will be only as wide as the   A            # toggle, resulting in the toggle being right aligned               width="auto",   7            # vertically align the toggle in the center               align="center",   
        ),       ]   )       sidebar = html.Div(       [           sidebar_header,   J        # we wrap the horizontal rule and short blurb in a div that can be   "        # hidden on a small screen           html.Div(               [                   html.Hr(),                   html.P(   x                    "Статистика Чемпионатов Росси по всестилевому каратэ",   %                    className="lead",                   ),               ],               id="blurb",   
        ),   H        # use the Collapse component to animate hiding / revealing links           dbc.Collapse(               dbc.Nav(                   [   ]                    dbc.NavLink("Общая статистика", href="/", active="exact"),                        dbc.NavLink(   K                        "Статистика по дисциплинам",   (                        href="/archive",   '                        active="exact",                       ),                   ],                   vertical=True,                   pills=True,               ),               id="collapse",   
        ),       ],       id="sidebar",   )       
@callback(   #    Output("sidebar", "className"),   *    [Input("sidebar-toggle", "n_clicks")],   $    [State("sidebar", "className")],   )   #def toggle_classname(n, classname):       if n and classname == "":           return "collapsed"       return ""           
@callback(   "    Output("collapse", "is_open"),   )    [Input("navbar-toggle", "n_clicks")],   #    [State("collapse", "is_open")],   )    def toggle_collapse(n, is_open):   	    if n:           return not is_open       return is_open5�_�                        #    ����                                                                                                                                                                                                                                                                                                                            d   @       d   P       v   A    d��    �         c    �         c    5��