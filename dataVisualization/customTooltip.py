import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

style  = LS("#333366", base_style=LCS)
chart = pygal.Bar(x_lable_rotation=45, style=style, show_legend=False)

chart.x_labels = ['a', 'b', 'c']

plotDicts = [
    {'value': 1000, 'label': 'a'},
    {'value': 2000, 'label': 'c'},
    {'value': 3000, 'label': 'b'}
    ]

chart.add("", plotDicts)
chart.render_to_file("tets.svg")








