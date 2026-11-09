import csv
import subprocess
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "dmhc_imr.csv"

DOWNLOAD_URL = (
    "https://data.chhs.ca.gov/dataset/"
    "b79b3447-4c10-4ae6-84e2-1076f83bb24e/resource/"
    "3340c5d7-4054-4d03-90e0-5f44290ed095/download/"
    "independent-medical-review-imr-determinations-trends.csv"
)


def download_data():
    if CSV_FILE.exists():
        print("DMHC CSV already exists. Download skipped.")
        return

    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = CSV_FILE.with_suffix(".csv.part")

    print("Downloading the official DMHC CSV...")

    try:
        subprocess.run(
            [
                "curl",
                "--fail",
                "--location",
                "--retry", "2",
                "--output", str(temporary_file),
                DOWNLOAD_URL,
            ],
            check=True,
        )

        with temporary_file.open(
            "r", encoding="utf-8-sig", newline=""
        ) as file:
            columns = next(csv.reader(file), [])

        required = {
            "ReferenceID",
            "ReportYear",
            "TreatmentCategory",
            "Type",
            "Determination",
        }

        if not required.issubset(columns):
            raise ValueError(
                "Downloaded file is not the expected DMHC CSV."
            )

        temporary_file.replace(CSV_FILE)
        print("Download complete:", CSV_FILE)

    except Exception:
        temporary_file.unlink(missing_ok=True)
        raise


if __name__ == "__main__":
    download_data()