Vim�UnDo� ��4�a���p��K���)�2�iNͤ   4               x=[2015, 2023],   -                          e��   " _�                     
       ����                                                                                                                                                                                                                                                                                                                                                             d��@    �   
      @    �   
      @    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       d��M    �   
      A      /    sport_discipline = sorted(sport_discipline)�         A    5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                v       d��O    �   	   
              sport_programs.sort()5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       d��Y    �   C               �       D       �               @   !from src.utils.dataframe import (       man,   
    women,   )   !import plotly.graph_objects as go       def get_unique_programs(df):   C    cleanedlist = df["Вид программы"].unique().tolist()   K    sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]   -    sport_programs = sorted(sport_discipline)       return sport_programs       'programs_man = get_unique_programs(man)   +programs_women = get_unique_programs(women)       def get_fig(df):       fig = go.Figure()   C    cleanedlist = df["Вид программы"].unique().tolist()   K    sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]       sport_programs.sort()   "    for program in sport_programs:   ?        df_man = df[df["Вид программы"] == program]           fig.add_scatter(               x=df_man["Год"],   ;            y=df_man["Кол-во \nучастников"],               name=program,   T            hovertemplate="Год=%{x}<br>Участников=%{y}<extra></extra>",   !            mode="markers+lines",   	        )       fig.layout.title = (   s        f"Количество участников по видам программ - {', '.join(sport_programs)}"       )       return fig           def get_fig_bar(df):       fig = go.Figure()   C    cleanedlist = df["Вид программы"].unique().tolist()   K    sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]       sport_programs.sort()   "    for program in sport_programs:   ?        df_man = df[df["Вид программы"] == program]           fig.add_trace(               go.Bar(                   name=program,   #                x=df_man["Год"],   ?                y=df_man["Кол-во \nучастников"],                   text=program,   X                hovertemplate="Год=%{x}<br>Участников=%{y}<extra></extra>",               )   	        )       fig.layout.title = (   s        f"Количество участников по видам программ - {', '.join(sport_programs)}"       )       fig.add_trace(           go.Scatter(               x=[2015, 2023],               y=[8, 8],               mode="lines",   <            line=go.scatter.Line(color=" #58d68d", width=2),               showlegend=False,   	        )       )       return fig5�_�                           ����                                                                                                                                                                                                                                                                                                                                         +       v   +    d��h    �   
      C      -    sport_programs = sorted(sport_discipline)�         C    5�_�                    	   1    ����                                                                                                                                                                                                                                                                                                                                         )       v   +    d��|    �      
   C      C    cleanedlist = df["Вид программы"].unique().tolist()5�_�                    	   2    ����                                                                                                                                                                                                                                                                                                                                         )       v   +    d��|    �   	   
   C    5�_�      	              	   6    ����                                                                                                                                                                                                                                                                                                                                         )       v   +    d��~    �   	   
   C    5�_�      
           	   	   8    ����                                                                                                                                                                                                                                                                                                                                         )       v   +    d��   	 �   	   
   C    5�_�   	              
   	   9    ����                                                                                                                                                                                                                                                                                                                                         )       v   +    d���     �   	   
   C    5�_�   
                 
       ����                                                                                                                                                                                                                                                                                                                                         )       v   +    d���   
 �   	             K    sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]5�_�                           ����                                                                                                                                                                                                                                                                                                                                         )       v   )    d���    �   
      C      +    sport_programs = sorted(sport_programs)�         C    5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D          �         C    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D    5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D    5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D    5�_�                           ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �         D    5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                         &       v   )    d���    �   	   
          M    # sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
   &       v   )    d���    �   
                 print(sport_programs)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       d���    �                def get_unique_programs(df):   L    cleanedlist = df["Вид программы"].dropna().unique().tolist()   (    sport_programs = sorted(cleanedlist)       return sport_programs5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       d���    �         >    5�_�                           ����                                                                                                                                                                                                                                                                                                                            	          	          V       d���     �         ?    5�_�                            ����                                                                                                                                                                                                                                                                                                                            	          	          V       d���    �         ?       �         ?    5�_�                           ����                                                                                                                                                                                                                                                                                                                            	          	          V       d���    �   9               �       :       �               ?   !from src.utils.dataframe import (       man,   
    women,   get_unique_programs   )   !import plotly.graph_objects as go                   'programs_man = get_unique_programs(man)   +programs_women = get_unique_programs(women)           def get_fig(df):       fig = go.Figure()   C    cleanedlist = df["Вид программы"].unique().tolist()   K    sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]       sport_programs.sort()   "    for program in sport_programs:   ?        df_man = df[df["Вид программы"] == program]           fig.add_scatter(               x=df_man["Год"],   ;            y=df_man["Кол-во \nучастников"],               name=program,   T            hovertemplate="Год=%{x}<br>Участников=%{y}<extra></extra>",   !            mode="markers+lines",   	        )       fig.layout.title = (   s        f"Количество участников по видам программ - {', '.join(sport_programs)}"       )       return fig           def get_fig_bar(df):       fig = go.Figure()   C    cleanedlist = df["Вид программы"].unique().tolist()   K    sport_programs = [x for x in cleanedlist if str(x) != "nan" and "None"]       sport_programs.sort()   "    for program in sport_programs:   ?        df_man = df[df["Вид программы"] == program]           fig.add_trace(               go.Bar(                   name=program,   #                x=df_man["Год"],   ?                y=df_man["Кол-во \nучастников"],                   text=program,   X                hovertemplate="Год=%{x}<br>Участников=%{y}<extra></extra>",               )   	        )       fig.layout.title = (   s        f"Количество участников по видам программ - {', '.join(sport_programs)}"       )       fig.add_trace(           go.Scatter(               x=[2015, 2023],               y=[8, 8],               mode="lines",   <            line=go.scatter.Line(color=" #58d68d", width=2),               showlegend=False,   	        )       )       return fig5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d���    �                'programs_man = get_unique_programs(man)   +programs_women = get_unique_programs(women)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d���    �                 ?from src.utils.dataframe import man, women, get_unique_programs5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d���    �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d���     �                 5�_�                     -       ����                                                                                                                                                                                                                                                                                                                                                             e��   " �   ,   .   4                  x=[2015, 2023],5��