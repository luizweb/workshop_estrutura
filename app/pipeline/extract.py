import os # bibliotecas para manipular arquivos e pastas 
import glob # biblioteca para listar arquivos

import pandas as pd
from typing import List




path = 'data/input'

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    '''
    função para ler os arquivos excel da pasta data/input
    e retornar uma lista de dataframes

    args: input_path (str): data/input

    return: lista de dataframes
    '''
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
