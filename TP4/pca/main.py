from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------- Procesamiento ---------

# Obtenemos los datos

df = pd.read_csv('../in/contaminacion.csv', encoding='utf-8', sep=';')
sitios = list(df["Sitios"])

columns = [
    'Tem_agua', 'Tem_aire','OD', 'pH', 'colif_totales_ufc_100ml', 'escher_coli_ufc_100ml', 'enteroc_ufc_100ml',
    'Nitrato_mg_l', 'NH4_mg_l', 'P_total_l_mg_l', 'Fosf_ortofos_mg_l', 'DBO_mg_l', 'DQO_mg_l', 'Turbiedad_NTU',
    'Cr_total_mg_l', 'Cd_total_mg_l', 'Clorofila_a_ug_l', 'Microcistina_a_ug_l'
]
df = df[columns]

# Los estandarizamos

df = StandardScaler().fit_transform(df.values)

# Realizamos PCA

pca = PCA()
fitted_df = pca.fit_transform(df)
components = (pca.components_ / (pca.components_.max() - pca.components_.min())).round(decimals=2)

print(components[0])

# --------- Graficos ---------

columns_readable = [
    'Temp. agua', 'Temp. aire','OD', 'pH', 'Bact. Coliformes', 'Bact. Escherichia', 'Enterobacteria',
    'Nitrato', 'NH4', 'Potasio', 'Fosforo', 'DBO', 'DQO', 'Turbiedad',
    'Cromo', 'Cadmio', 'Clorofila', 'Microcistina'
]

def variance_plot():
    plt.plot(range(1,len(pca.components_)+1), pca.explained_variance_ratio_)
    plt.ylabel("Ratio de varianza")
    plt.xlabel("Componente")
    plt.show()

    plt.plot(range(1,len(pca.components_)+1), np.cumsum(pca.explained_variance_ratio_))
    plt.ylabel("Ratio de varianza acumulada")
    plt.xlabel("Componente")
    plt.show()

def first_comp_weights_barplot():
    idx = np.argsort(components[0])
    values_sorted = np.array(components[0])[idx]
    labels_sorted = np.array(columns_readable)[idx]

    plt.barh(y=labels_sorted, width=values_sorted)
    plt.title("Peso de la primer componente")
    plt.show()


idx   = np.argsort(fitted_df[:,0])
values_sorted = np.array(fitted_df[:,0])[idx]
labels_sorted = np.array([s[:20] for s in sitios])[idx]

plt.barh(y=labels_sorted, width=values_sorted)
plt.title("Valor de la primer componente")
plt.show()