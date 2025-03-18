from dagster import Definitions, load_assets_from_modules

from dagster_scripts import assets  # noqa: TID252

all_assets = load_assets_from_modules([assets])

import dagster as dg

defs = dg.Definitions(
  assets=all_assets,
  resources={},
)