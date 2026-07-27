def detect_jailbreak(prompt):

    patterns = [
        "dan",
        "ignore all limitations",
        "remove your safety rules",
        "act as unrestricted ai",
        "no restrictions",
        "bypass safety"
    ]

    prompt = prompt.lower()

    for pattern in patterns:
        if pattern in prompt:
            return True

    return False