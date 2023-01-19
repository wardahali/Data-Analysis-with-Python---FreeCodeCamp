import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df =  pd.read_csv("medical_examination.csv")

# Add 'overweight' column
BMI=df['weight']/(df['height'].div(100)**2)
over_weight=[]
for values in BMI:
  if(values>25):
   over_weight.append(1)   
  
  if(values<=25):
   over_weight.append(0)   
print(over_weight)
df['overweight']=over_weight

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'].replace([1,2,3],[0,1,1] , inplace = True)
df['gluc'].replace([1,2,3],[0,1,1], inplace = True)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active', 'alco' , 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of
    # each feature. You will have to rename one of the columns for the catplot
    # to work correctly.
    df_cat = df_cat.value_counts().reset_index(name="total")

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        order=['active', 'alco' , 'cholesterol', 'gluc', 'overweight', 'smoke'],
    )
    
    fig.set_ylabels("total")
    fig.set_xlabels("variable")
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig("catplot.png") # Don't save to file
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
     # Clean the data
    df_heat = df.loc[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    # with sns.axes_style("white"):
    fig, ax = plt.subplots(figsize=(15, 10))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, vmax=1, square=True, fmt=".1f", annot=True)

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    # Don't save to file
    return fig
