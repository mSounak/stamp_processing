# Changelog

## [Unreleased] - 2024-12-XX

### Changed
- **BREAKING**: Package name changed from `stamp_processing` to `better_stamp_processing`
- **BREAKING**: Updated minimum Python version requirement from 3.7 to 3.8
- Updated all dependencies to modern versions:
  - PyTorch: 1.8.1 → ≥2.0.0
  - Torchvision: 0.9.1 → ≥0.15.0
  - FastAI: 2.3.1 → ≥2.7.0
  - Pillow: ≤8.2.0 → ≥10.0.0
  - OpenCV: ≥4.1.2.30 → ≥4.8.0
  - PyYAML: 5.4.1 → ≥6.0
  - NumPy: ≥1.20 → ≥1.21.0
  - gdown: (no version) → ≥4.7.1
- Updated build system requirements in pyproject.toml
- Added setuptools≥65.0.0 as explicit dependency for pkg_resources
- Enhanced package description and documentation
- Updated repository URLs to reflect new ownership

### Fixed
- Fixed syntax error in setup.py (missing comma after Pillow dependency)
- Fixed wrong package name in __init__.py version detection
- Fixed double equals bug in version fallback
- Updated Python version consistency across all configuration files
- Enhanced package classifiers for better PyPI categorization
- Improved mypy configuration with additional ignored modules

### Added
- Created requirements.txt for development dependencies
- Added comprehensive development tools (pytest, black, isort, etc.)
- Enhanced flake8 configuration with better exclusions
- Added more detailed mypy configuration options
- Added GitHub Actions workflows for automated testing and publishing
- Enhanced .gitignore with comprehensive exclusions
- Added usage examples in README

### Security
- Updated all dependencies to address known security vulnerabilities in older versions

## Installation

```bash
# Old package (deprecated)
pip install stamp_processing

# New package (recommended)
pip install better_stamp_processing
``` 