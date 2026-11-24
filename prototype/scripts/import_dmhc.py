
import csv
import os
import sys
from collections import Counter
from pathlib import Path

import django

# Locate the project and CSV file.
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "dmhc_imr.csv"

sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_project.settings")
django.setup()

from django.db import transaction
from draft_analysis.models import DMHCDecision


def import_data():
    required_columns = [
        "ReferenceID",
        "ReportYear",
        "TreatmentCategory",
        "Type",
        "Determination",
    ]

    total = 0
    imported = 0
    missing = 0
    duplicates = 0
    invalid_years = 0
    normalized_categories = 0

    seen_ids = set()
    determinations = Counter()
    categories = Counter()
    batch = []

    # Track possible treatment category inconsistencies.
    category_names_seen = {}
    possible_variations = set()

    # Allow long text in unused CSV columns such as Findings.
    csv.field_size_limit(10_000_000)

    with open(CSV_FILE, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        missing_columns = set(required_columns) - set(reader.fieldnames or [])
        if missing_columns:
            raise ValueError(f"Missing CSV columns: {missing_columns}")

        with transaction.atomic():
            # Make repeated imports reproducible without duplicate records.
            DMHCDecision.objects.all().delete()

            for row in reader:
                total += 1

                values = {
                    column: (row.get(column) or "").strip()
                    for column in required_columns
                }

                if not all(values.values()):
                    missing += 1
                    continue

                # Standardize known treatment category names.
                original_category = values["TreatmentCategory"]

                if original_category.lower() == "gen surg proc":
                    values["TreatmentCategory"] = "Gen Surg Proc"

                if original_category.lower() in ["dme", "durable med equip"]:
                    values["TreatmentCategory"] = "Durable Med Equip"

                try:
                    year = int(values["ReportYear"])
                except ValueError:
                    invalid_years += 1
                    continue

                reference_id = values["ReferenceID"]

                if reference_id in seen_ids:
                    duplicates += 1
                    continue

                seen_ids.add(reference_id)

                if original_category != values["TreatmentCategory"]:
                    normalized_categories += 1

                # Check for possible category spelling or spacing variations.
                category_name = values["TreatmentCategory"]
                cleaned_category = " ".join(category_name.split())

                if category_name != cleaned_category:
                    possible_variations.add(
                        f"Extra spaces: {category_name}"
                    )

                category_key = cleaned_category.lower()

                if category_key in category_names_seen:
                    if category_names_seen[category_key] != category_name:
                        possible_variations.add(
                            f"Different labels: {category_names_seen[category_key]} / {category_name}"
                        )
                else:
                    category_names_seen[category_key] = category_name

                batch.append(DMHCDecision(
                    reference_id=reference_id,
                    report_year=year,
                    treatment_category=values["TreatmentCategory"],
                    review_type=values["Type"],
                    determination=values["Determination"],
                ))

                determinations[values["Determination"]] += 1
                categories[values["TreatmentCategory"]] += 1
                imported += 1

                if len(batch) >= 1000:
                    DMHCDecision.objects.bulk_create(batch)
                    batch.clear()

            if batch:
                DMHCDecision.objects.bulk_create(batch)

    print("\nDMHC IMPORT RESULTS")
    print(f"CSV rows examined: {total}")
    print(f"Records imported: {imported}")
    print(f"Skipped - missing values: {missing}")
    print(f"Skipped - duplicate reference IDs: {duplicates}")
    print(f"Skipped - invalid years: {invalid_years}")
    print(f"Treatment category labels normalized: {normalized_categories}")
    print(f"Distinct treatment categories: {len(categories)}")
    print(f"Determination values: {dict(determinations)}")
    print(f"Top treatment categories: {categories.most_common(10)}")

    print("\nPOSSIBLE TREATMENT CATEGORY INCONSISTENCIES")

    if possible_variations:
        for variation in sorted(possible_variations):
            print(variation)
    else:
        print("No additional capitalization or spacing inconsistencies found.")


if __name__ == "__main__":
    import_data()
