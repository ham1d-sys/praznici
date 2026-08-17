# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.0.3] - 2026-08-17

### Added

- Added exception handling for potentially malformed response JSON.

### Changed

- Ensured that only `holidays.py` calls `logging.basicConfig()`.
- Removed retry-handled status codes from the `try-except` block in `fetch_holidays()` in `holidays.py`.

### Fixed

- Changed report saving to use a path relative to the script's location instead of the current working directory, preventing reports from potentially being saved outside `praznici/`.


## [1.0.2] - 2026-08-16

### Added

- `pytest.ini`

## [1.0.1] - 2026-08-16

### Added

- `LICENSE`

## [1.0.0] - 2026-08-16

### Added

- `README`

## [0.1.1] - 2026-08-14

### Added

- Tests.

### Changed

- Refactored the codebase into multiple modules.
- Save generated reports to a dedicated reports folder instead of the current working directory.
- Raise HTTPError.

## [0.1.0] - 2026-08-13

### Added

- Fetch 🇧🇬 holidays for the current year, clean fetched data and write to a CSV file.
- Retry on failed fetches