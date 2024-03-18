def generate_keystore(keys, path):
    """Generate a keystore with the given keys.

    Args:
        keys: A list of keys to generate.
        path: The path to the keystore file.
    """

    keystore = {}
    for key in keys:
        keystore[key] = generate_key()

    with open(path, 'w') as f:
        json.dump(keystore, f)

