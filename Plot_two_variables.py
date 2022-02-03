#DataCamp Introduction to Data Visualization with Matplotlib
#Chapter2 - Plotting Time Series
import pandas as pd
import matplotlib.pyplot as plt
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x,y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)
climate_change = pd.read_csv('/home/mukul/PycharmProjects/DataCamp/climate_change.csv', parse_dates=['date'], index_col='date')
fig, ax = plt.subplots()
plot_timeseries(ax, climate_change.index, climate_change['co2'], 'blue', 'Time (years)','CO2 levels')
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', 'Time (years)', 'Relative temperature (Celsius)')

#ax.plot(climate_change.index, climate_change['co2'], color='blue')
#ax2 = ax.twinx()
#ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')
plt.show()