from dagster import Definitions, load_assets_from_modules

#from dgproj import assets  # noqa: TID252
from ingestion.system_01 import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)