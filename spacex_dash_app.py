# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(
                                    id='site-dropdown',
                                options=[
                                    {'label': 'All Sites', 'value': 'ALL'},
                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                ],
                                value='ALL',
                                placeholder="Select a Launch Site here",
                                searchable=True 
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                # Function decorator to specify function input and output
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0',
                                                    2500: '2500',
                                                    5000: '5000',
                                                    7500: '7500',
                                                    10000: '10000',
                                                    },
                                                value=[min_payload, max_payload]),


                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
            Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
        names='Launch Site', #These are the names that get put into the Pie Chart
        title='Success Count for all launch sites')
        return fig
    else:
        # return the outcomes piechart for a selected site
        # I found this part tricky and had to look it up : https://www.coursera.org/learn/applied-data-science-capstone/discussions/forums/3RLFoOKZEeqQWwqIaxNuKw/threads/X-J-s2TpEe2BGA6-85lTCw
        # An even better explaination  : https://www.coursera.org/learn/applied-data-science-capstone/discussions/forums/3RLFoOKZEeqQWwqIaxNuKw/threads/bFVrSyDLEeywtQrBGtHwFQ

        filtered_df = spacex_df[spacex_df['Launch Site']== entered_site]
        filtered_df=filtered_df.groupby(['Launch Site','class']).size().reset_index(name='class count')
        # I'm not sure how people visualise the line above. How does the pie chart know how to group and plot only the 1s and not the 0s?
        # Okay after seeing the plot I kind of get it now it plots the successes and fails but how does the first if statement 
        # know that it should only plot the successes. This dash stuff is a bit tricky to get my head around.
        fig=px.pie(filtered_df,values='class count',names='class',title="Total Success Launches for site {}".format(entered_site))
        return fig


#https://github.com/AliciaSperatti/Pythoncourse/blob/main/spacex_dash_app.py
#https://github.com/monteirotb/doubts/blob/main/spacex_dash_app.py


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
    Input(component_id='payload-slider', component_property='value')])

def get_scatter_chart(entered_site, slider_range):
    low,high=slider_range

    masks = (spacex_df['Payload Mass (kg)']>low) & (spacex_df['Payload Mass (kg)']<high)
    filtered_df = spacex_df[masks]
    print('Hi')
    if entered_site == 'ALL':
        print('Hello')
        fig = px.scatter(filtered_df, 
        x='Payload Mass (kg)',
        y='class',
        color = 'Booster Version Category',
        title = 'Payload vs Launch Outcome for all sites:')
        return fig
    else : 
        print('Heya')
        filtered_df=spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title= f"Payload vs Launch Outcome for {entered_site}:")
        return fig




# Run the app
if __name__ == '__main__':
    app.run_server()
