import pandas as pd

from app.pipeline.transform import concat_data_frames

# --- TESTE concat_data_frames ---

# Criando o primeiro DataFrame
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df1 = pd.DataFrame(data1)

# Criando o segundo DataFrame
data2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}
df2 = pd.DataFrame(data2)

dataframes_list = [df1, df2]


def testar_a_concatenacao_da_lista_de_dataframe():
    arrange = pd.concat(dataframes_list, ignore_index=True)
    act = concat_data_frames(dataframes_list)   # função que queremos testar
    assert arrange.equals(act)
