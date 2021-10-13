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

	
def redraw_plt(states, sort_alg, x = None, y = None, z = None, col = None, col2 = None):
	global fig
	global ax

	plt.cla()
	index = np.arange(states.size)
	ax.set(title= sort_alg, ylabel='# Number', xlabel='Position')
	ax.bar(index, states, color= 'gray')

	if x is not None:
		ax.patches[x].set_color(col)
	if y is not None:
		ax.patches[y].set_color(col)
	if z is not None:
		ax.patches[z].set_color(col2)
	fig.canvas.draw()
	plt.pause(0.05)

def show():
	plt.show()


