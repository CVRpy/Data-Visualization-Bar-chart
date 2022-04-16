

import plotly.graph_objects as go


years = ["Output1.1", "Output1.2", "Output1.3", "Output1.4", "Output2.1", "Output2.2",
         "Output2.3", "Output3.1", "Output3.2", "Output3.3", "Outcome1", "Outcome2", "Outcome3", "Impact"]

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                     y=[100, 100, 100, 100, 100, 100, 100,
                         100, 100, 85, 60, 100, 92, 100],
                     name='Target',
                     marker_color='rgb(150, 93, 12)'
                     ))
fig.add_trace(go.Bar(x=years,
                     y=[50, 100, 100, 85, 50, 50, 68,
                         100, 10, 50, 40, 55, 50, 50],
                     name='Progress (Actual Data)',
                     marker_color='rgb(244, 120, 50)'
                     ))

fig.update_layout(
    title='MEAL CHART TRACKING',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Percentage',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.5,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,  # gap between bars of adjacent location coordinates.
    bargroupgap=0.1  # gap between bars of the same location coordinate.
)
fig.show()
