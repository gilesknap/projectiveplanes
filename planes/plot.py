from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, output_file, show
import math


# p.multi_line(
#     [[1, 3, 2], [3, 4, 6, 6]],
#     [[2, 1, 4], [4, 7, 8, 5]],
#     color=["firebrick", "navy"],
#     alpha=[0.8, 0.3],
#     line_width=4,
# )


def plot_cards(order: int):
    count = order ** 2 - order + 1
    lines = order - 1

    step = 2 * math.pi / lines
    length = 9
    start = 1

    output_file("/tmp/cards.html")
    p = figure(plot_width=900, plot_height=900, x_range=(-10, 10), y_range=(-10, 10))
    p.dot()

    x = [0.0]
    y = [0.0]
    for line in range(order):
        for symbol in range(lines):
            newy = math.cos(step * line) * (start + symbol * length / lines)
            newx = math.sin(step * line) * (start + symbol * length / lines)
            x.append(newx)
            y.append(newy)
    labels = [str(i) for i in range(count)]
    data = {"x": x, "y": y, "labels": labels}
    source = ColumnDataSource(data=data)
    p.diamond('x', 'y', size=10, source=source)

    show(p)


plot_cards(4)
