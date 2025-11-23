Overview
--------

The Directed Inputs Class library provides a robust and flexible interface for managing inputs from various sources in Python applications. It simplifies the process of working with inputs from environment variables, stdin, and predefined dictionaries, while offering advanced features such as input freezing, thawing, and decoding from multiple formats.

Key Features
------------

- **Environment Variable Integration**: Automatically integrates environment variables into your inputs, allowing for seamless configuration management.
- **Scoped Environment Loading**: Filter environment variables by prefix and optionally strip the prefix so consumer keys stay clean.
- **Stdin Input Handling**: Supports reading and merging inputs from stdin, with options to override default behaviors.
- **Input Freezing and Thawing**: Freeze inputs to prevent further modifications and thaw them when needed, ensuring consistent input management.
- **Advanced Decoding Utilities**: Decode inputs from Base64, JSON, and YAML formats with built-in error handling and customization options.
- **Type Conversion**: Convert inputs to boolean or integer types, with robust error handling for invalid inputs.
- **Deep Input Merging**: Merge new payloads into existing state without overwriting nested structures.

Usage Examples
--------------

Below are some examples demonstrating how to use the Directed Inputs Class library:

### Initializing the Class with Environment Variables

.. code-block:: python

    from directed_inputs_class import DirectedInputsClass

    dic = DirectedInputsClass()
    print(dic.inputs.get("MY_ENV_VAR"))  # Accessing an environment variable

### Reading Inputs from Stdin

.. code-block:: python

    import sys
    from directed_inputs_class import DirectedInputsClass

    sys.stdin.write('{"stdin_key": "stdin_value"}')
    dic = DirectedInputsClass(from_stdin=True)
    print(dic.inputs.get("stdin_key"))  # Output: stdin_value

### Freezing and Thawing Inputs

.. code-block:: python

    from directed_inputs_class import DirectedInputsClass

    dic = DirectedInputsClass(inputs={"key1": "value1"})
    frozen = dic.freeze_inputs()
    print(frozen)  # Outputs: {'key1': 'value1'}

    thawed = dic.thaw_inputs()
    print(thawed)  # Outputs: {'key1': 'value1'}

### Merging Additional Inputs

.. code-block:: python

    from directed_inputs_class import DirectedInputsClass

    dic = DirectedInputsClass(inputs={"feature_flags": {"existing": True}})
    dic.merge_inputs({"feature_flags": {"new": True}})

    print(dic.inputs)
    # Outputs: {'feature_flags': {'existing': True, 'new': True}}

### Decoding Base64 Inputs

.. code-block:: python

    from directed_inputs_class import DirectedInputsClass

    encoded_value = "eyJuYW1lIjogIkpvaG4ifQ=="  # Base64 encoded JSON {"name": "John"}
    dic = DirectedInputsClass(inputs={"base64_key": encoded_value})
    decoded = dic.decode_input("base64_key", decode_from_base64=True)
    print(decoded)  # Output: {'name': 'John'}

### Boolean and Integer Conversion

.. code-block:: python

    from directed_inputs_class import DirectedInputsClass

    dic = DirectedInputsClass(inputs={"bool_key": "true", "int_key": "42"})
    bool_value = dic.get_input("bool_key", is_bool=True)
    int_value = dic.get_input("int_key", is_integer=True)
    print(bool_value)  # Output: True
    print(int_value)   # Output: 42
