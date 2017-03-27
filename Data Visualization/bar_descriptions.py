import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Python Projects"
chart.x_labels = ["httpie", "flask", "django"]

plot_dicts = [
    {"value": 28848, "label": "Description of httpie"},
    {"value": 26063, "label": "Description of flask"},
    {"value": 24612, "label": "Description of django"},

]

chart.add("", plot_dicts)
chart.render_to_file("bar_descriptions.svg")