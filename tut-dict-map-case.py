# Use dictionary to achive switch case funtionallity in python.
from faker import Faker as F
from random import randint as rint
import pandas as pd, os

if not os.path.exists("files"):
    os.mkdir("files")

files = [
    "sample_file.csv",
    "sample_file.xlsx",
    "sample_file.json",
    "sample_file.parquet",
    "sample_file.csv.gz",
    "sample_file.json.gz",
    "sample_file.parquet.snappy",
    "sample_file.parquet.gzip",
]


def get_profile_info(entries: int):
    person = F()
    profiles = [person.profile() for _ in range(entries)]
    profiles_df = pd.DataFrame(profiles)
    return profiles_df


def write_file(df: pd.DataFrame, path: str, extention: str, compression: str = None):
    print()
    print(
        f"File path: {path} | Extention: {extention} | Compression type : {compression}"
    )

    result = pd.DataFrame()

    if compression == "gz":
        compression = "gzip"

    map_pandas_method = {
        "csv": (
            df.to_csv,
            {
                "path_or_buf": f"files/{path}",
                "index": False,
                "compression": compression,
            },
        ),
        "xlsx": (df.to_excel, {"excel_writer": f"files/{path}", "index": False}),
        "json": (
            df.to_json,
            {"path_or_buf": f"files/{path}", "compression": compression},
        ),
        "parquet": (
            df.to_parquet,
            {"path": f"files/{path}", "compression": compression},
        ),
    }
    function, params = map_pandas_method.get(extention)

    try:
        result = function(**params)
    except Exception as e:
        print(e)

    return path


def read_file(path: str, extention: str, compression: str = None):
    print()
    print(
        f"File path: {path} | Extention: {extention} | Compression type : {compression}"
    )

    map_pandas_method = {
        "csv": pd.read_csv,
        "xls": pd.read_excel,
        "xlsx": pd.read_excel,
        "json": pd.read_json,
        "parquet": pd.read_parquet,
    }
    function = map_pandas_method.get(extention)
    result = function(f"files/{path}")
    return result


for f in files:
    comp_or_ext, ext_or_fname = f.rsplit(".", 2)[::-1][:2]
    compressions = ["gz", "gzip", "snappy"]

    if comp_or_ext in compressions:
        compression = comp_or_ext
        extention = ext_or_fname
    else:
        compression = None
        extention = comp_or_ext

    try:
        print()
        df = get_profile_info(25)
        write = write_file(df, f, extention, compression)
        print(write)

        print()
        read = read_file(f, extention)
        print(read)

    except Exception as e:
        print(e)
