import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i):
	plt.cla()
	index = np.arange(states.size)
	plt.bar(index, states)
	plt.tight_layout()

	
def redraw_plt(states):
	plt.cla()
	index = np.arange(states.size)
	plt.bar(index, states)
	plt.tight_layout()

def plot_bar(states):
	index = np.arange(states.size)
	plt.bar(index, states)
	plt.show()