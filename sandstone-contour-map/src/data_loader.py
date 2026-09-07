import pandas as pd
import re


def load_excel(file):
    df = pd.read_excel(file)

    required_columns = [
        "No Sumur",
        "Koordinat",
        "Top",
        "Bottom"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            "Kolom berikut tidak ditemukan: "
            + ", ".join(missing_columns)
        )

    coordinates = df["Koordinat"].astype(str)

    def parse_coordinate(value):
        value = value.replace(" ", "")

        numbers = re.findall(
            r"-?\d+(?:\.\d+)?",
            value
        )

        if len(numbers) < 2:
            raise ValueError(
                f"Format koordinat tidak valid: {value}"
            )

        return float(numbers[0]), float(numbers[1])

    parsed = coordinates.apply(parse_coordinate)

    df["X"] = parsed.apply(lambda value: value[0])
    df["Y"] = parsed.apply(lambda value: value[1])

    df["Top"] = pd.to_numeric(
        df["Top"],
        errors="coerce"
    )

    df["Bottom"] = pd.to_numeric(
        df["Bottom"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["X", "Y", "Top", "Bottom"]
    )

    df["Thickness"] = (
        df["Top"] - df["Bottom"]
    ).abs()

    return df