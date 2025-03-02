# Changelog

## [0.1.0] - 2025-03-02

### Summary
- Introduced support for ETH and SOL staking, as well as account-level settings.
- Reorganized API endpoints for the Account and Funding modules.
- Deprecated outdated savings API paths and updated loan API endpoints.
- Enhanced unit testing to improve overall code reliability.

### Added
- Support for ETH and SOL staking ([#3](https://github.com/parker1019/python-okx-ext/pull/3)).
- Account-level settings ([#4](https://github.com/parker1019/python-okx-ext/pull/4)).
- Implemented `black` formatting workflow to ensure consistent code style ([#7](https://github.com/parker1019/python-okx-ext/pull/7)).

### Changed
- Migrated from `setup.py` to `pyproject.toml` ([#2](https://github.com/parker1019/python-okx-ext/pull/2)).
- Enhanced unit tests for the `Account` module and improved resource management ([#9](https://github.com/parker1019/python-okx-ext/pull/9)).
- Improved unit tests for the `Funding` module ([#11](https://github.com/parker1019/python-okx-ext/pull/11)).

### Fixed
- Updated Loan API endpoints and reorganized related functionality ([#6](https://github.com/parker1019/python-okx-ext/pull/6)).
- Resolved missing `type` parameter in `deposit-history` API ([#5](https://github.com/parker1019/python-okx-ext/pull/5)).
- Corrected parameter issue in the `withdrawal lightning` function ([#11](https://github.com/parker1019/python-okx-ext/pull/11)).

**Full Changelog**: [View complete changes](https://github.com/parker1019/python-okx-ext/compare/v0.0.0...v0.1.0)

---

## [0.0.0] - 2025-02-28

### Summary
- This release serves as a continuation of `python-okx 0.3.5`, as the original project appears to be inactive.
- Retained all major functionalities from `python-okx 0.3.5`.

### Notes
- Future updates will focus on supporting all OKX API endpoints and ensuring long-term project maintenance.
