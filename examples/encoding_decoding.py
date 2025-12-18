#!/usr/bin/env python3
"""Encoding and decoding example for directed-inputs-class.

This example demonstrates input decoding capabilities:
- JSON decoding
- YAML decoding
- Base64 decoding
- Combined Base64 + JSON/YAML decoding

Run with:
    python -m examples.encoding_decoding
"""

from __future__ import annotations

import base64

from directed_inputs_class import DirectedInputsClass


def main() -> None:
    """Demonstrate encoding/decoding features."""
    # Prepare encoded test data
    json_data = '{"database": "postgres", "port": 5432}'
    yaml_data = "server:\n  host: localhost\n  port: 8080"
    base64_json = base64.b64encode(json_data.encode()).decode()
    base64_yaml = base64.b64encode(yaml_data.encode()).decode()

    inputs = DirectedInputsClass(
        inputs={
            "json_config": json_data,
            "yaml_config": yaml_data,
            "base64_json_config": base64_json,
            "base64_yaml_config": base64_yaml,
            "plain_text": "Hello, World!",
        },
        from_environment=False,
    )

    # JSON decoding
    print("=== JSON Decoding ===")
    json_result = inputs.decode_input("json_config", decode_from_json=True)
    print(f"JSON decoded: {json_result}")

    # YAML decoding
    print("\n=== YAML Decoding ===")
    yaml_result = inputs.decode_input("yaml_config", decode_from_yaml=True)
    print(f"YAML decoded: {yaml_result}")

    # Base64 + JSON decoding
    print("\n=== Base64 + JSON Decoding ===")
    b64_json_result = inputs.decode_input(
        "base64_json_config",
        decode_from_base64=True,
        decode_from_json=True,
    )
    print(f"Base64+JSON decoded: {b64_json_result}")

    # Base64 + YAML decoding
    print("\n=== Base64 + YAML Decoding ===")
    b64_yaml_result = inputs.decode_input(
        "base64_yaml_config",
        decode_from_base64=True,
        decode_from_yaml=True,
    )
    print(f"Base64+YAML decoded: {b64_yaml_result}")

    # Plain text (no decoding)
    print("\n=== Plain Text (No Decoding) ===")
    plain = inputs.get_input("plain_text")
    print(f"Plain text: {plain}")

    # Missing input with default
    print("\n=== Missing Input with Default ===")
    missing = inputs.decode_input(
        "nonexistent",
        default={"fallback": True},
        decode_from_json=True,
    )
    print(f"Missing (with default): {missing}")


if __name__ == "__main__":
    main()
