import pandas as pd

DATA_PARAMETER_FILE = 'data_parameter.csv'


def update_parameters():
    df = pd.read_csv(DATA_PARAMETER_FILE)

    weights = df.values[:, 0: 785]
    return weights

