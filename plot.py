import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig = []
ax = []


def draw_plt(sort_alg, states_to_draw):
	# Setting title, labels, etc.
	plt.ion()
	index = np.arange(states_to_draw.size)
	
	global fig
	global ax

	fig = plt.figure()
	ax = fig.gca()
	fig.show()
	ax.bar(index, states_to_draw)
	ax.set(title= sort_alg, ylabel='# Number', xlabel='Position')

	
def redraw_plt(states, x, y, col):
	global fig
	global ax

	plt.cla()
	index = np.arange(states.size)
	ax.bar(index, states, color= 'blue')
	ax.patches[x].set_color(col)
	ax.patches[y].set_color(col)
	fig.canvas.draw()
	plt.pause(0.005)


