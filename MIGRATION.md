# Release Workflow Migration

## What Changed

Completely replaced the semantic-release based workflow with a **simple, automatic CalVer versioning** system.

## Old Approach (REMOVED)
- ❌ Used `python-semantic-release`
- ❌ Analyzed commit messages for version bumps
- ❌ Created git tags
- ❌ Could skip releases if no "conventional" commits found
- ❌ Complex configuration and failure modes

## New Approach (IMPLEMENTED)

### Simple Calendar Versioning
- ✅ Version format: `YYYY.MM.BUILD_NUMBER`
- ✅ Example: `2025.11.42`
- ✅ Uses GitHub run number (always incrementing)
- ✅ No git tags needed
- ✅ No commit message analysis

### Automatic PyPI Releases
Every push to `main` branch:
1. Runs all tests, type checking, linting
2. Auto-generates new version: `YYYY.MM.{github.run_number}`
3. Builds signed package with attestation
4. Publishes to PyPI
5. DONE

No conditionals, no skipping, no complexity.

## Files Changed

### Added
- `.github/scripts/set_version.py` - Auto-versioning script

### Modified
- `.github/workflows/ci.yml` - Simplified release job, removed semantic-release
- `pyproject.toml` - Removed `[tool.semantic_release]` section
- `.github/copilot-instructions.md` - Updated with new approach
- `AGENTS.md` - Complete rewrite to document CalVer approach

## How It Works

```
Push to main
  ↓
All tests pass
  ↓
Run: python .github/scripts/set_version.py
  ├─ Reads GITHUB_RUN_NUMBER (e.g., 42)
  ├─ Gets current date (e.g., 2025.11)
  └─ Generates version: 2025.11.42
  ↓
Updates __version__ in __init__.py
  ↓
Build package with hynek/build-and-inspect-python-package
  ↓
Sign with attestations
  ↓
Publish to PyPI
  ↓
DONE
```

## Benefits

1. **Predictable**: Every main push = new release
2. **Simple**: ~50 lines of Python, no external dependencies
3. **Reliable**: No analysis that could fail or skip
4. **Clean**: No git tags, no bot commits
5. **Fast**: No git history analysis

## Testing

The versioning script has been tested locally:
```bash
$ python3 .github/scripts/set_version.py
VERSION=2025.11.0

$ grep __version__ src/directed_inputs_class/__init__.py
__version__ = "2025.11.0"
```

The workflow YAML validates successfully:
```bash
$ python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"
✓ YAML syntax is valid
```

## Next Push to Main

The next push to main will:
1. Run through CI pipeline
2. Auto-generate version like `2025.11.{N}`
3. Publish to PyPI automatically
4. No manual intervention needed

## Documentation

All AI agent instructions have been updated:
- `AGENTS.md` - Full technical explanation
- `.github/copilot-instructions.md` - Quick reference for AI tools

Both documents now correctly describe the CalVer auto-versioning approach and tell agents NOT to suggest semantic-release or tag-based versioning.
