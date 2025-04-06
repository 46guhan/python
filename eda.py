 #exploratory data analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("hospital.csv")
print(data.describe())

numberical=["Procedure.Heart Attack.Cost","Procedure.Heart Failure.Cost","Procedure.Pneumonia.Cost","Procedure.Hip Knee.Cost"]

meanvalue=data[numberical].mean()
print(meanvalue)

medianvalue=data[numberical].median()
print(medianvalue)

sns.countplot(x="Facility.Type",data=data,palette="cividis")
plt.show()

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file (Replace 'supermarket.csv' with your actual file name)
df = pd.read_csv('supermarket.csv')


sns.countplot(x='Branch', data=df, palette='coolwarm')
plt.title('Number of Transactions by Branch')
plt.xlabel('Branch')
plt.ylabel('Count')
plt.show() """

""" 
1.viridis
2.plasma
3.inferno
4.magma
5.cividis

coolwarm
seismic
spectral
RDYlGn
RdBu
PiYD
PRGn
BrBg
""" 


"""
df['Payment'].value_counts().plot.pie(autopct='%1.1f%%', cmap='Reds', startangle=90)
plt.title('Payment Method Distribution')
plt.ylabel('')
plt.show()



sns.barplot(x=df['Product line'], y=df['Total'], palette='viridis')
plt.xticks(rotation=45)
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales ($)')
plt.show() """

""" df['Date'] = pd.to_datetime(df['Date'])  # Convert Date column to datetime format
sales_trend = df.groupby('Date')['Total'].sum()  # Group sales by date


plt.plot(sales_trend, marker='o', linestyle='-', color='b')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.grid()
plt.show() """

"""

df['Customer type'].value_counts().plot.pie(autopct='%1.1f%%', cmap='coolwarm', startangle=90)
plt.title('Customer Type Distribution')
plt.ylabel('')
plt.show()
"""
