movies_df['Year'].plot(kind='hist', title='Rating');
movies_df.plot(kind='scatter', x='Metascore', y='Year', title='Year vs Metascore');
metascore = movies_df['Metascore']
metascore_mean = metascore.mean()
metascore_mean