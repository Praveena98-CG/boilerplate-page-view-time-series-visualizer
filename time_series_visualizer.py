import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
lower_bound= df["value"].quantile(0.025)
upper_bound= df["value"].quantile(0.975)

df_clean= df[(df["value"]>=lower_bound) & (df["value"]<=upper_bound)]



def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots (figsize=(15,5))
    ax.plot (df_clean.index, df_clean['value'], color='red', linewidth=1)

    #title and labels

    ax.set_title ('Daily freecodecamp Forum Page Views')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_clean.copy()

    df_bar ['year']= df_bar.index.year
    df_bar['month']= df_bar.index.month

    df_grouped= df_bar.groupby(['year','month'])['value'].mean().unstack()
    fig= df_grouped.plot(kind= 'bar',figsize=(10,6)).figure


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)

    sns.box_plot (x='year', y= 'value', data= df_box, ax=axes[0])
    axes[0].set_title ("Year-wise Box plot (Trend)")
    axes[0].set_xlabel ("Year")
    axes[0].set_ylabel ("Page Views")

    sns.box_plot (x='year', y= 'value', data= df_box, order= month_order, ax=axes[1])
    axes[0].set_title ("Month-wise Box plot (Seasoanlity)")
    axes[0].set_xlabel ("Month")
    axes[0].set_ylabel ("Page Views")

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
