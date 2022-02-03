#DataCamp Introduction to Data Visualization with Matplotlib
#Chapter2 - Plotting Annotation
import pandas as pd
import matplotlib.pyplot as plt
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x,y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)
climate_change = pd.read_csv('/home/mukul/PycharmProjects/DataCamp/climate_change.csv', parse_dates=['date'], index_col='date')
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)', 'CO2 levels')
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'r', 'Time (years)', 'Relative temperature (Celsius)')
ax2.annotate('>1 degree',
             xy=(pd.Timestamp('2015-10-06'), 1),
             xytext=(pd.Timestamp('2008-10-06'), -0.2),
             arrowprops={"arrowstyle":"->", "color": "gray"})
plt.show()