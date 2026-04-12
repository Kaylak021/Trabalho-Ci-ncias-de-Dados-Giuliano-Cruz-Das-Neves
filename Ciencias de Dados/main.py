import pandas as pd
# -- Fonte do Dados --
tabela = pd.read_excel("default_of_credit_card_clients__courseware_version_1_21_19.xls")

# -- >> Total das Colunas << --
print(f"\nTotal de Colunas: {tabela.shape[1]}\n")

# -- >> Total das Linhas << --
print(f"Total de Linhas: {tabela.shape[0]}\n")

# -- >> Tipo de Dados << -- 
numericas = tabela.select_dtypes(include=["int64", "float64"])
categorias = tabela.select_dtypes(include=["str"])

# -- >> Frequencia das Colunas << --
for coluna in categorias.columns:
    print(f"Frequencia das Colunas: \n{coluna}:")
    print(tabela[coluna].value_counts())

print(f"\nNumericos:\n >{numericas.columns}\n")

print(f"\nCategorias:\n >{categorias.columns}\n")

# -- >> Aparencia dos dados << --
print(f"\nCabeçalho: >{tabela.head()}\n")

print(f"\nDescrissão: >{tabela.describe()}\n")

print(f"\nDados Faltantes:\n >{tabela.isnull().sum()}")