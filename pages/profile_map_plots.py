from django.http import JsonResponse
from django.template.loader import render_to_string
from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from env_data.models import continuous_profile, cycle_metadata, discrete_profile
from .plot_helpers import add_bottom_trace, add_top_trace, var_translation

def update_profile_plot(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the selections
        profiles = request.GET.getlist("profiles[]", None)
        bot_var = request.GET.get("bot_var", None)
        top_var = request.GET.get("top_var", None)
        cont = request.GET.get("cont", None) == 'true'
        dis = request.GET.get("dis", None) == 'true'
        fig = go.Figure()
        
        for profile in profiles:

            #Hover data
            hov = pd.DataFrame()
            hov['float_profile'] = list(continuous_profile.objects.filter(PROFILE_ID=profile).all().values_list('PROFILE_ID', flat=True))
            hov['profile'] = hov['float_profile'].str.split('.').str[1]
            hov['float'] = hov['float_profile'].str.split('.').str[0]
            hov_data = hov.values.tolist()
            wmo = profile.split(".")[0]

            #Continuous data
            if cont and (bot_var != "NITRATE"):
                #Continuous data queries and convert to list
                PRES = continuous_profile.objects.filter(PROFILE_ID=profile).all().values_list('PRES', flat=True)
                bot = continuous_profile.objects.filter(PROFILE_ID=profile).all().values_list(bot_var, flat=True)

                #Convert lists to arrays
                bot_data = np.array(bot)
                y_data = np.array(PRES)*-1

                add_bottom_trace(fig, bot_data, y_data, hov_data, wmo)

            #Top axis continuous plotting
            if cont and top_var and (top_var != "NITRATE"):
                top = continuous_profile.objects.filter(PROFILE_ID=profile).all().values_list(top_var, flat=True)
                top_data = np.array(top)

                add_top_trace(fig, top_data, y_data, top_var, hov_data, wmo)

            #discrete data
            if dis:
                #Discrete data queries and convert to list
                PRES = discrete_profile.objects.filter(PROFILE_ID=profile).all().values_list('PRES', flat=True)
                bot = discrete_profile.objects.filter(PROFILE_ID=profile).all().values_list(bot_var, flat=True)

                #Convert lists to arrays
                bot_data = np.array(bot)
                y_data = np.array(PRES)*-1

                add_bottom_trace(fig, bot_data, y_data, hov_data, wmo, mode="markers")

                #Top axis discrete plotting
                if top_var:
                    top = discrete_profile.objects.filter(PROFILE_ID=profile).all().values_list(top_var, flat=True)
                    top_data = np.array(top)
                    add_top_trace(fig, top_data, y_data, top_var, hov_data, wmo, mode="markers")          
            
            # Formatting
            fig.update_layout(
                template = "ggplot2",
                xaxis = dict(
                    title=var_translation[bot_var],
                    showline=True,
                    linewidth=1,
                    linecolor="#000000",
                    mirror=True
                ),
                yaxis = dict(
                    title=var_translation["PRES"],
                    showline=True,
                    linewidth=1,
                    linecolor="#000000",
                    mirror=True
                ),
                font = {"size":12},
                height=800,
                width=1000,
                showlegend=False,
                margin={'t': 0, 'l':0,'r':0,'b':0},
                #yaxis_range=[-2000,0],
            )

        #Metadata for table
        table_context = cycle_metadata.objects.filter(PROFILE_ID__in=profiles).all()
        meta_table = render_to_string('partials/plot_table.html', context = {'metadatas':table_context}, request = request)

        plot_div = plot(fig,output_type='div', include_plotlyjs=False, config= {'displaylogo': False, 
            'modeBarButtonsToRemove':['lasso2d', 'select2d','resetScale2d']})

        return JsonResponse({'plot_div': plot_div, 'meta_table':meta_table}, status = 200)

    return JsonResponse({}, status = 400)

def update_map(request):
    
    if request.is_ajax and request.method == "GET":
        # get the selections
        deployments = request.GET.getlist("deployments[]", None)

        fig = go.Figure(go.Scattergeo())

        for d in deployments:
            lat = list(cycle_metadata.objects.filter(DEPLOYMENT__PLATFORM_NUMBER=d).order_by('-GpsFixDate').all().values_list('GpsLat', flat=True))
            lon = list(cycle_metadata.objects.filter(DEPLOYMENT__PLATFORM_NUMBER=d).order_by('-GpsFixDate').all().values_list('GpsLong', flat=True))
            profile_id = list(cycle_metadata.objects.filter(DEPLOYMENT__PLATFORM_NUMBER=d).order_by('-GpsFixDate').all().values_list('PROFILE_ID', flat=True))
            time_start_p = pd.Series(cycle_metadata.objects.filter(DEPLOYMENT__PLATFORM_NUMBER=d).order_by(
                '-GpsFixDate').all().values_list('TimeStartTelemetry', flat=True))
            time_start_p_human = time_start_p.dt.strftime('%Y-%m-%d %H:%M')
            time_start_p_human = time_start_p_human.replace(np.nan, '')
            #Hover data
            hov_data = np.stack((profile_id, time_start_p_human, lat, lon),axis = -1)

            fig.add_trace(go.Scattermapbox(
                mode = "lines",
                lon = lon,
                lat = lat,
                marker = {'size': 10},
                name = d,
                customdata = hov_data,
                hovertemplate ='Profile: %{customdata[0]}<br>Profile Start: %{customdata[1]}<br>Lat: %{customdata[2]}<br>Long: %{customdata[3]}',
                showlegend=False
            ))

        fig.update_layout(
            margin ={'l':0,'t':0,'b':0,'r':0},
            height=900,
            autosize=True,
            hovermode='closest',
            mapbox = {
                'style': "mapbox://styles/randerson5726/cklttcu382rbf17ljhunibjse",
                'accesstoken':'pk.eyJ1IjoicmFuZGVyc29uNTcyNiIsImEiOiJjanl5b2E0NTUxMGR5M25vN2xha2E4aHI1In0.xXUPHJrf_Shr6JX6u5X5cg',
                'center': {'lon': -36, 'lat': 39},
                'zoom': 3.5
            },
        )

        map_div = plot(fig,output_type='div', include_plotlyjs=False, config= {'displaylogo': False, 
            'modeBarButtonsToRemove':['lasso2d', 'select2d','resetScale2d']})

        return JsonResponse({'map_div': map_div }, status = 200)

    return JsonResponse({}, status = 400)
