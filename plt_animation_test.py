import matplotlib.pyplot as plt
import numpy

hl, = plt.plot([], [])
ax = plt.gca()
plt.ion()
plt.show()

def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data[0]))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data[1]))
    ax.relim()
    ax.autoscale_view(True, True, True)
    plt.draw()
