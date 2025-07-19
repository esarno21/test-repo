import pandas as pd
import dagster as dg

@dg.asset
def create_int_csv():
    ## Read data from the CSV
    df = pd.read_csv("data_files/testdb__user_test.csv")

    df.to_csv("data_files/processed_data_int.csv", index=False)
    return "Intermediate file created"


@dg.asset(deps=["create_int_csv"])
def create_final_csv():
    ## Read data from the CSV
    df = pd.read_csv("data_files/processed_data_int.csv")

    ## Save processed data
    df.to_csv("data_files/processed_data_final.csv", index=False)
    return "Data loaded successfully"

## Tell Dagster about the assets that make up the pipeline by
## passing it to the Definitions object
## This allows Dagster to manage the assets' execution and dependencies
defs = dg.Definitions(assets=[create_int_csv, create_final_csv])