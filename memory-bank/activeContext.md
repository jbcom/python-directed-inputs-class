# Active Context

## directed-inputs-class

Python decorator library for CLI argument and configuration management.

### Features
- Decorator-based CLI argument definition
- Configuration file support
- Environment variable integration
- Type validation

### Package Status
- **Version**: 1.1.0
- **Registry**: PyPI
- **Python**: 3.9+
- **Dependencies**: extended-data-types (>=5.1.2), lifecyclelogging

### Development
```bash
uv sync --extra tests
uv run pytest tests/ -v
uvx ruff check src/ tests/
uvx ruff format src/ tests/
```

---
*Last updated: 2025-12-24*
