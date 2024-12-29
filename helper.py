import pandas as pd


def header_manipulation(df: pd.DataFrame):
    """Modifies the column headers of a DataFrame.

    This function converts all column names to lowercase and replaces 
    spaces with underscores to ensure uniform and clean column naming.

    :param df (pd.DataFrame): The input DataFrame whose column headers need modification.

    :return: pd.Index, the modified column headers as a pandas Index object.

    >>> header_manipulation("salary_df")
    ['job_title', 'location', 'size', 'industry', 'seniority']
    """
    # put all columns into lowercase, replace spaces with underscores
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df.columns


def check_unique_values(dataframe: pd.DataFrame):
    """display the unique values in a DataFrame.

    This function displays the unique values in categorical columns
    and columns with less than 10 unique values

    :param dataframe: a python pandas dataframe.

    :return: unique values in the dataframe

    >>> check_unique_values(salary_prediction_dataframe)
    Unique values in 'spark' column: False, True
    """

    # Iterate over each column in the DataFrame
    column_list = []

    index = 0
    for column in dataframe.columns:
        if dataframe[column].dtype == 'object' or len(dataframe[column].unique()) < 10:
            unique_values = dataframe[column].unique()
            unique_values_str = [str(value) for value in unique_values]
            print(
                f"Unique values in '{column}' column: {', '.join(unique_values_str)}")
            column_list.append(index)
            index += 1

    # return column_list
