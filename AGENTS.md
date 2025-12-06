# Agent Instructions for directed-inputs-class

## Overview

Decorator library for CLI argument and configuration management.

## Before Starting

```bash
cat memory-bank/activeContext.md
```

## Development Commands

```bash
# Install dependencies
uv sync --extra tests

# Run tests
uv run pytest tests/ -v

# Lint
uvx ruff check src/ tests/
uvx ruff format src/ tests/

# Build
uv build
```

## Commit Messages

Use conventional commits:
- `feat(dic): new feature` → minor
- `fix(dic): bug fix` → patch

## Important Notes

- Use absolute imports (`from directed_inputs_class...`)
- Include `from __future__ import annotations`
- Depends on extended-data-types and lifecyclelogging
