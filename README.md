# Praznici

A small chained automation script that fetches Bulgarian public holidays for the current year from the [Calendarific API]([https://calendarific.com/](https://calendarific.com/api/v2/holidays)) and exports them to a CSV file.

## What it does

1. **Fetch** — Calls the Calendarific API to retrieve Bulgarian holidays for the current year.
2. **Process** — Parses the raw JSON response and normalizes it into a clean, consistent format (e.g., date, name, type).
3. **Write** — Saves the processed data to a CSV file for easy viewing or downstream use.

## Prerequisites

- Python 3.x
- A Calendarific API key ([get one here](https://calendarific.com/signup))

## Setup

**Clone the repository:**

```bash
git clone https://github.com/ham1d-sys/praznici
cd praznici
```

**(Optional but recommended) Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

**Install requirements:**

```bash
pip install -r requirements.txt
```

**Set your API key as an environment variable:**

```bash
copy .env.example .env
```

Add your Calendarific API key from the Calendarific dashboard to the .env file.

## Usage

```bash
python src/holidays.py
```

This generates a file (e.g., `BG_holidays_(<year>)_report.csv`) in 'praznici/reports' containing the current year's holidays.

## Output format

| Name                                                              | Description | ISO | Primary type | Additional type(s) |
|-------------------------------------------------------------------|---|---|---|---|
| New Year's Day                                                    | New Year's Day is the first day of the year, or January 1, in the Gregorian calendar. | 2026-01-01 | National holiday | |
| New Year Holiday                                                  | New Year Holiday is a national holiday in Bulgaria | 2026-01-02 | National holiday | |
| Day of Remembrance and Respect to Victims of the Communist Regime | Day of Remembrance and Respect to Victims of the Communist Regime is an observance in Bulgaria | 2026-02-01 | Observance | |

## Testing

```bash
pytest
```