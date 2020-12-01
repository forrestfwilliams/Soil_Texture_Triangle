# import plotly.express as px
import plotly.graph_objects as go

# df = px.data.election()
# fig = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron")
# fig.show()

lines = [
         [0,55,45], [28,27,45],[None,None,None],
         [15,40,45], [60,40, 0],[None,None,None],
         [40,60, 0], [40,40,20],[None,None,None],
         [40,40,20], [52,27,20],[None,None,None],
         [28,27,45], [73,27, 0],[None,None,None],
         [50,27,23], [50, 0,50],[None,None,None],
         [80,12, 8], [88,12, 0],[None,None,None],
         [80,12, 8], [80, 0,20],[None,None,None],
         [40, 8,52], [50, 8,42],[None,None,None],
         [40, 8,52], [28,20,52],[None,None,None],
         [28,20,52], [28,27,45],[None,None,None],
         [28,20,52], [ 0,20,80],[None,None,None],
         [ 0,15,85], [30, 0,70],[None,None,None],
         [ 0,10,90], [14, 0,86],[None,None,None],
         [ 0,35,65], [20,35,45]
         ]
c = [x[0]/100 if x[0] != None else None for x in lines]
a = [x[1]/100 if x[1] != None else None for x in lines]
b = [x[2]/100 if x[2] != None else None for x in lines]


def makeAxis(title, tickangle):
    return {
      'title': title,
      'titlefont': { 'size': 20 },
      'tickangle': tickangle,
      'tickfont': { 'size': 15 },
      'tickcolor': 'rgba(0,0,0,0)',
      'ticklen': 5,
      'showline': True,
      'showgrid': True
    }
    
fig = go.Figure(go.Scatterternary(a=a, b=b, c=c, mode='lines', line_width=2, line_color='black'))
fig.update_layout(template='plotly_white',ternary={
        'sum': 100,
        'aaxis': makeAxis('Clay', 0),
        'baxis': makeAxis('<br>Sand', 45),
        'caxis': makeAxis('<br>Silt', -45)
    })
fig.show()