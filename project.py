import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("I:/Era/E.documents/cse303_PC/project303/LoanData_Preprocessed_v1.1.csv")

counts= df['default'].value_counts()

percen= df['default'].value_counts(normalize=True)*100

print("Counts:\n", counts)
print("\nRatios:\n", percen)

for col in df.columns:
    if df[col].dtypes == 'float':
        average = df[col].mean()
        std_dev = df[col].std()
        variance = df[col].var()
        median = df[col].median()
        
        print(col)
        print(f"Average (Mean): {average}")
        print(f"Standard Deviation {std_dev}")
        print(f"Variance: {variance}")
        print(f"Median: {median}")
    else:
        
        frequency= df[col].value_counts()
        percentage= ratios= df[col].value_counts(normalize=True)*100
        
        print(col)
        print(f"Frequency: {frequency}")
        print(f"Percentage: {percentage}")

for col in df.columns:
    plt.figure(figsize=(7, 6))
    
    if df[col].dtype in ['float64']:
        if df[col].nunique() > 20:
            sns.histplot(df[col], kde=True)
            plt.title(f"{col} Distribution (Histogram)")
            plt.xlabel(col)
            plt.ylabel("Frequency")
        else:
            sns.countplot(x=col, data=df)
            plt.title(f"{col} Distribution (Bar Chart)")
            plt.xlabel(col)
            plt.ylabel("Count")
    
    else:
        sns.countplot(x=col, data=df)
        plt.title(f"{col} Distribution (Bar Chart)")
        plt.xlabel(col)
        plt.ylabel("Count")
    
    # Customize the layout and show the plot
    plt.tight_layout()
    plt.show()
df_sorted = df.sort_values('income')

plt.figure(figsize=(10, 8))

#Plot Income vs Age (first plot)
plt.subplot(2, 1, 1)
sns.lineplot(x='age', y='income', data=df_sorted)
plt.title('Income vs Age')
plt.xlabel('Age')
plt.ylabel('Income (in thousands)')
plt.tight_layout()
plt.show()

ed_counts = df['ed'].value_counts()

# Create the pie chart
plt.figure(figsize=(5, 5))
plt.pie(ed_counts, labels=ed_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)

# Add title
plt.title('Education Level Distribution')

# Show the chart
plt.show()


corr_matrix = df.corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='RdBu', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

print(df.isnull().sum())
print(df[df.isnull().any(axis=1)])

df['age'] = df['age'].fillna(df['age'].mean())
df['income'] = df['income'].fillna(df['income'].mean())
df['ed'] = df['ed'].fillna(df['ed'].mode()[0])