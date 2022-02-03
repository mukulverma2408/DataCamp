#DataCamp Introduction to Data Visualization with Matplotlib
#Chapter2 - Plotting Time Series
import pandas as pd
import matplotlib.pyplot as plt
climate_change = pd.read_csv('/home/mukul/PycharmProjects/DataCamp/climate_change.csv', parse_dates=['date'], index_col='date')
#climate_change['date'] = climate_change['date'].astype('datetime64[ns]')
#print(climate_change.info())
#climate_change.set_index('date', inplace=True)
#print(climate_change.index)
#print(climate_change.head())
#fig, ax = plt.subplots()
#ax.plot(climate_change.index, climate_change['relative_temp'], color='g')
#ax.set_xlabel("Time")
#ax.set_ylabel("Relative temperature (Celsius)")
#plt.show()
fig, ax = plt.subplots()
seventies = climate_change["1970-01-01":"1979-12-31"]
ax.plot(seventies.index, seventies['co2'])
plt.show()