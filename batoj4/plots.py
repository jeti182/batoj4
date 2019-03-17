from matplotlib.pylab import plt
import seaborn as sns

def plot_tojs(tojs, relative=False, plots_per_row=5, show=True):
	if not relative:
		grid = sns.FacetGrid(tojs, col="Subject", col_wrap=plots_per_row)
		grid.map(sns.pointplot, "SOA", "Probe_first_count", color=".3",  ci=None, linestyles=None)
	else:
		tmp = tojs
		tmp["Probe_first_frequency"] = tmp["Probe_first_count"]/tmp["Repetitions"]
		grid = sns.FacetGrid(tmp, col="Subject", col_wrap=plots_per_row)		
		grid.map(sns.pointplot, "SOA", "Probe_first_frequency", color=".3",  ci=None, linestyle="")
	if show:
		plt.show()
