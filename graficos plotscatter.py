import matplotlib.pyplot as plt
import pandas as pd
from google.colab import files
import io
import pandas as pd

data = files.upload()

plt.style.use('ggplot')
df = pd.read_csv('tesla22.csv')
x = df['Data']
y = df['Fechamento']

plt.figure (figsize=(26,8))
plt.title('Ações da Tesla Motors')
plt.xlabel('Dados de 2022', fontsize=18)
plt.ylabel('Valor da ação', fontsize=16)
plt.plot(x, y)
plt.scatter(x, y)


plt.show()