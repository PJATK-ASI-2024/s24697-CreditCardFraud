# Importowanie potrzebnych bibliotek
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sweetviz as sv

data = pd.read_csv('./data/data.csv')

print(data.info())
print(data.describe())
print(data.head())

missing_values = data.isnull().sum()
print("Brakujące wartości:\n", missing_values)

f_count = data[data["fraud"] == 1]["fraud"].count()
nf_count = data[data["fraud"] == 0]["fraud"].count()

plt.pie([f_count,nf_count],labels=['Fraud','Not Fraud'],autopct='%1.1f%%', colors = ['#FF8888', '#8888FF'] )
plt.savefig("graph/piechart")


num_cols = ['distance_from_home', 'distance_from_last_transaction', 'ratio_to_median_purchase_price']
data[num_cols].hist(bins=20, figsize=(15, 10))


plt.suptitle('Histogramy zmiennych numerycznych')
plt.savefig("graph/histogram")

plt.figure(figsize=(15, 8))
for i, col in enumerate(num_cols, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(y=data[col])
    plt.title(f'Wykres pudełkowy dla {col}')
plt.tight_layout()
plt.savefig("graph/boxplot")

plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Macierz korelacji')
plt.savefig("graph/heatmap")

report = sv.analyze(data, target_feat='fraud')
report.show_html("./docs/index.html")


