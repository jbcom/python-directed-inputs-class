# CLAUDE.md - directed-inputs-class

This file provides guidance to Claude Code when working with the directed-inputs-class repository.

## Project Overview

**directed-inputs-class** is a Python library that provides flexible, transparent input handling for Python applications. It allows loading inputs from environment variables, stdin (JSON), or dictionaries and automatically injecting them into method arguments.

### Key Features
- Decorator-based API (`@directed_inputs`, `@input_config`)
- Automatic type coercion (bool, int, float, datetime, Path)
- Multi-source loading (environment variables, stdin JSON, dictionaries)
- Environment variable prefix filtering with optional stripping
- Base64, JSON, and YAML decoding
- Input freezing/thawing for immutable snapshots

## Project Structure

```
directed-inputs-class/
├── src/directed_inputs_class/
│   ├── __init__.py          # Package exports
│   ├── __main__.py          # DirectedInputsClass (legacy API)
│   ├── decorators.py        # @directed_inputs, @input_config decorators
│   └── py.typed             # PEP 561 type marker
├── tests/
│   ├── test_main.py         # Tests for DirectedInputsClass
│   └── test_decorators.py   # Tests for decorator API
├── docs/                    # Sphinx documentation
├── pyproject.toml           # Package configuration
└── CHANGELOG.md             # Release history
```

## Development Commands

```bash
# Install dependencies (including test and typing extras)
uv sync --extra tests --extra typing

# Run tests
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ --cov=src

# Lint and format
uvx ruff check src/ tests/
uvx ruff format src/ tests/

# Type checking
uv run mypy src/

# Build package
uv build
```

## Code Style

- **Formatter**: Ruff (Black-compatible, 88 char line length)
- **Type hints**: Required on all public functions
- **Docstrings**: Google style
- **Imports**: Use absolute imports (`from directed_inputs_class...`)
- **Future annotations**: Always include `from __future__ import annotations`

## Dependencies

### Core Dependencies
- `case-insensitive-dictionary>=0.2.1` - Case-insensitive dict for inputs
- `deepmerge>=1.1.1` - Deep merge for combining inputs
- `extended-data-types>=5.1.2` - Type coercion utilities (jbcom ecosystem)
- `PyYAML>=6.0` - YAML parsing

### Ecosystem Position
This package is part of the jbcom ecosystem:
- **Upstream**: `extended-data-types` (type conversion utilities)
- **Downstream**: `python-terraform-bridge` (uses decorator API for Terraform data sources)

## Versioning

This project uses **SemVer** (Semantic Versioning):
- Format: `MAJOR.MINOR.PATCH` (e.g., `1.2.0`)
- Releases are automated via GitHub Actions CI workflow
- Uses `python-semantic-release` for changelog and version management

## Architecture Notes

### Two APIs

1. **Decorator API (Recommended)**: Use `@directed_inputs` class decorator
   - Transparent, no inheritance required
   - Methods auto-populate parameters from inputs
   - Use `@input_config` for fine-grained parameter control

2. **Legacy API**: Inherit from `DirectedInputsClass`
   - Manual `get_input()` calls required
   - Maintained for backward compatibility

### Input Resolution Order

1. Explicit argument (always wins)
2. Stdin JSON (if `from_stdin=True`)
3. Environment variable (if `from_env=True`)
4. Default value

## Testing

- All tests use pytest
- Use `pytest.raises` for expected exceptions
- Use `monkeypatch` for environment variable manipulation
- Test both decorator and legacy APIs

## CI/CD

- **Build**: Uses `hynek/build-and-inspect-python-package@v2`
- **Test**: Python 3.9 and 3.13 matrix
- **Lint**: Ruff check and format verification
- **Release**: Automated on main branch push with conventional commits

## Common Tasks

### Adding a new input config option

1. Add field to `InputConfig` dataclass in `decorators.py`
2. Update `InputConfig.resolve()` method
3. Add corresponding parameter to `@input_config` decorator
4. Write tests in `test_decorators.py`

### Updating dependencies

```bash
# Update extended-data-types
uv add "extended-data-types>=5.1.2"

# Verify
uv run pytest tests/ -v
uv run mypy src/
```

## Important Notes

- This package uses absolute imports - always `from directed_inputs_class...`
- The `py.typed` marker indicates this is a PEP 561 typed package
- Environment variable names are case-insensitive (via CaseInsensitiveDict)
