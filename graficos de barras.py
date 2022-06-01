import matplotlib.pyplot as plt
import pandas as pd
from google.colab import files
import io
import pandas as pd

data = files.upload()

plt.style.use('ggplot')
df = pd.read_csv('tesla1a.csv')
x = df['Data']
y = df['Fechamento']

plt.figure (figsize=(10,5))
plt.title('Ações da Tesla Motors')
plt.xlabel('Dados dos Últimos 12 Meses', fontsize=18)
plt.ylabel('Valor da ação', fontsize=16)
plt.bar(x, y)

plt.show() 
