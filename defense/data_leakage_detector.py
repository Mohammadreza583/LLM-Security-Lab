def detect_data_leakage(prompt):

    patterns = [

        "api key",
        "api keys",
        "password",
        "credentials",
        "database credentials",
        "private data",
        "user data",
        "secret",
        "confidential information"

    ]

    prompt = prompt.lower()

    for pattern in patterns:
        if pattern in prompt:
            return True

    return False