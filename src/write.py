import csv
import logging
from pathlib import Path
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(pathname)s - %(message)s")
logger = logging.getLogger(__name__)
cwd = Path.cwd()
reports_dir_path = cwd.parent / "reports"


def write_holidays_to_report(params: Dict, fieldnames: List[str], processed: List[Dict]):
    """
    Write holidays report to a CSV file.
    :param params: Parameters.
    :param fieldnames: Headers.
    :param processed: List of holiday rows.
    """
    reports_dir_path.mkdir(exist_ok=True)
    filename = reports_dir_path / f"{params['country']}_holidays_({params['year']})_report.csv"
    with open(filename, "w", encoding="UTF-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed)
    logger.info(f"Wrote report to `{filename}`.")
