from copy import deepcopy
import numpy as np
import plotly.graph_objs as go
from plotly.tools import make_subplots

def configure_plotly_browser_state():
    import IPython
    display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
            },
          });
        </script>
        '''))
    
def convex_j(w):
    return w ** 2

def convex_djdw(w):
    return 2 * w

def nonconvex_j(w):
    return np.sin(w*3) + w**2 + 1

def nonconvex_djdw(w):
    return 3*np.cos(w*3) + 2*w

def build_fig(func, lr, w0=2, n_steps=10):
    w = np.linspace(-2, 2, 100)

    if func == 'Convex':
        j = convex_j
        djdw = convex_djdw
    else:
        j = nonconvex_j
        djdw = nonconvex_djdw

    delta = lr * djdw(w0)

    traces = [go.Scatter(x=w, y=j(w), mode='lines', line={'color': 'black'}, showlegend=False)]
    
    template_traces = [go.Scatter(x=[w0], y=[j(w0)], marker={'color': 'black'}, name='w before'),
             go.Scatter(x=[w0-delta], y=[j(w0-delta)], marker={'color': 'red'}, name='w after'),
             go.Scatter(x=[w0-delta, w0-delta], y=[j(w0), j(w0-delta)], showlegend=False, mode='lines', line={'color': 'gray', 'dash': 'dot'}),
             go.Scatter(x=[w0, w0-delta], y=[j(w0-delta), j(w0-delta)], showlegend=False, mode='lines', line={'color': 'gray', 'dash': 'dot'}),
             go.Scatter(x=[w0, w0-delta], y=[j(w0), j(w0-delta)], showlegend=False, mode='lines', line={'color': 'red', 'width': 2, 'dash': 'dash'}),
             go.Scatter(x=[w0, w0-delta], y=[j(w0), j(w0)], mode='lines', line={'color': 'red'}, name='update'),
             go.Scatter(x=[w0, w0], y=[j(w0), j(w0-delta)], mode='lines', line={'color': 'gray'}, name='loss change')]
    
    data = deepcopy(template_traces)
    
    traces.extend(data)
    
    for i in range(n_steps):
        w0, j0 = data[1].x[0], data[1].y[0]
        data = deepcopy(template_traces)

        delta = lr * djdw(w0)
        w1 = w0-delta
        j1 = j(w1)
        data[0].x = [w0]
        data[0].y = [j0]
        data[1].x = [w1]
        data[1].y = [j1]
        data[2].x = [w1, w1]
        data[2].y = [j0, j1]
        data[3].x = [w0, w1]
        data[3].y = [j1, j1]
        data[4].x = [w0, w1]
        data[4].y = [j0, j1]
        data[5].x = [w0, w1]
        data[5].y = [j0, j0]
        data[6].x = [w0, w0]
        data[6].y = [j0, j1]
        for k in range(7):
            data[k].visible = False
        traces.extend(data)
        
    steps = []
    for i in range(n_steps):
        step = dict(
            method = 'restyle',
            args = ['visible', [True] + [False] * ((n_steps + 1) * 7)],
        )
        for j in range(i * 7 + 1, i * 7 + 8):
            step['args'][1][j] = True
        steps.append(step)
        
    sliders = [dict(
        active = 0,
        currentvalue = {'prefix': 'Update: '},
        pad = {'t': 50},
        steps = steps
    )]

    fig = go.Figure(traces, layout={'title': 'Gradient Descent - Learning Rate = {:.2f}'.format(lr),
                                    'width': 600, 'height': 600, 
                                    'xaxis': {'zeroline': False, 'title': 'Feature (w)', 'range': [-2.1, 2.1]},
                                    'yaxis': {'title': 'Loss', 'range': [-.1, 6]},
                                    'sliders': sliders})
    return fig