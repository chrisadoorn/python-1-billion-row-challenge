import dask.dataframe as dd
from datetime import datetime
start = datetime.now()

df = (
    dd.read_parquet("data/measurements.parquet")
        .groupby("station_name")
        .agg(["min", "mean", "max"])
        .compute()
)

df.columns = df.columns.get_level_values(level=1)
df = df.reset_index()
df.columns = ["station_name", "min_measurement", "mean_measurement", "max_measurement"]
df = df.sort_values("station_name")

print("{", end="")
for row in df.itertuples(index=False):
    print(
        f"{row.station_name}={row.min_measurement:.1f}/{row.mean_measurement:.1f}/{row.max_measurement:.1f}",
        end=", "
    )
print("\b\b} ")

eind = datetime.now()
duur = eind - start
print('verwerking duurde ' + str(duur))
