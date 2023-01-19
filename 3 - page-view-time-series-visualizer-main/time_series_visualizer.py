import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')
# Clean data
df= df.loc[(df['value']>df['value'].quantile(q=0.025)) & (df['value']<df['value'].quantile(q=0.975))]

def draw_line_plot():
    df.index = pd.to_datetime(df.index)
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 7))
    ax = plt.plot(df.index, df['value'], color='orange')
    plt.xlabel("Date")  # add X-axis label
    plt.ylabel("Page Views")  # add Y-axis label
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")  # add title


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df.copy(deep=True)
    df_bar.reset_index(inplace=True)
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month
    df_bar = df_bar.groupby(["year","month"])['value'].mean().reset_index().sort_values(by=['year','month'])
    df_bar = df_bar.set_index('year')
    df_bar = df_bar.pivot_table(values = "value", index=df_bar.index, columns="month", aggfunc='first').reset_index()
    
    df_bar = df_bar.set_index('year')
    df_bar.columns = ['January','February','March','April','May','June','July','August','September','October','November','December']
    df_bar= df_bar.fillna(0)

          
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 10))
    
    bar = df_bar.plot(kind='bar', rot=0, ax=ax)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title='Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18, 10))
    axes[0].set_title('Year-wise Box Plot (Trend)')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    

     
    axes[0]=sns.boxplot(ax=axes[0], x = 'Year', y = 'value', data = df_box)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    m_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    axes[1]=sns.boxplot(ax=axes[1], x = 'Month', y = 'value', data = df_box, order=m_order)

    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
