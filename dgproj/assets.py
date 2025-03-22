import pandas as pd
import dagster as dg

@dg.asset
def processed_data():
    ## Read data from the CSV
    df = pd.read_csv("data_files/testdb__user_test.csv")

    ## Save processed data
    df.to_csv("data_files/processed_data.csv", index=False)
    return "Data loaded successfully"

## Tell Dagster about the assets that make up the pipeline by
## passing it to the Definitions object
## This allows Dagster to manage the assets' execution and dependencies
defs = dg.Definitions(assets=[processed_data])