from bokeh.models import PrintfTickFormatter
from bokeh.plotting import figure, output_file, show

output_file("gridlines.html")

p = figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)

p.x_axis[0].formatter = PrintfTickFormatter(format="%4.1e")
p.y_axis[0].formatter = PrintfTickFormatter(format="%5.3f mu")

show(p)
