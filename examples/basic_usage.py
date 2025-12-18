#!/usr/bin/env python3
"""Basic usage example for DirectedInputsClass.

This example demonstrates the fundamental features of the legacy DirectedInputsClass API:
- Loading inputs from environment variables
- Providing default values
- Type conversion (boolean, integer, float)
- Input freezing and thawing

Run with:
    python -m examples.basic_usage
"""

from __future__ import annotations

import os

from directed_inputs_class import DirectedInputsClass


def main() -> None:
    """Demonstrate basic DirectedInputsClass usage."""
    # Set up some environment variables for demonstration
    os.environ["APP_DEBUG"] = "true"
    os.environ["APP_PORT"] = "8080"
    os.environ["APP_TIMEOUT"] = "30.5"
    os.environ["APP_NAME"] = "MyApplication"

    # Initialize with environment variables filtered by prefix
    inputs = DirectedInputsClass(
        from_environment=True,
        env_prefix="APP_",
        strip_env_prefix=True,
    )

    # Retrieve inputs with type conversion
    debug = inputs.get_input("DEBUG", is_bool=True)
    port = inputs.get_input("PORT", is_integer=True)
    timeout = inputs.get_input("TIMEOUT", is_float=True)
    name = inputs.get_input("NAME")

    print(f"Debug mode: {debug} (type: {type(debug).__name__})")
    print(f"Port: {port} (type: {type(port).__name__})")
    print(f"Timeout: {timeout} (type: {type(timeout).__name__})")
    print(f"App name: {name}")

    # Demonstrate default values
    log_level = inputs.get_input("LOG_LEVEL", default="INFO")
    print(f"Log level (with default): {log_level}")

    # Demonstrate freeze/thaw functionality
    print("\n--- Freezing inputs ---")
    frozen = inputs.freeze_inputs()
    print(f"Frozen inputs: {dict(frozen)}")
    print(f"Current inputs (should be empty): {dict(inputs.inputs)}")

    print("\n--- Thawing inputs ---")
    thawed = inputs.thaw_inputs()
    print(f"Thawed inputs: {dict(thawed)}")


if __name__ == "__main__":
    main()
