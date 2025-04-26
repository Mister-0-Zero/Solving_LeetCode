import pandas as pd

def get_sample(df):
    df["is_no"] = (df["verdict"] == "No").astype(int)

    stats = df.groupby("banner_id").agg(
        total_count=("verdict", "count"),
        no_count=("is_no", "sum")
    ).reset_index()

    stats["no_ratio"] = stats["no_count"] / stats["total_count"]

    top_banners = stats.sort_values("no_ratio", ascending=False).head(100)

    return top_banners[["banner_id"]]


import sqlite3

conn = sqlite3.connect(r"data\moderation.db")

moderation = pd.read_sql_query("SELECT * FROM verdicts", conn)

res = get_sample(moderation)

print(res)