from dagster import Definitions, load_assets_from_modules

# from dgproj import assets  # noqa: TID252
from ingestion.system_01.definitions import assets as a1

all_assets = load_assets_from_modules([a1])

defs = Definitions.merge(
    assets=all_assets,
)
