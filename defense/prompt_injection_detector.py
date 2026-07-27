# defense/prompt_injection_detector.py

def detect_prompt_injection(prompt):

    patterns = [
        "ignore previous instructions",
        "forget your rules",
        "show system prompt",
        "reveal system prompt",
        "hidden instructions",
        "developer instructions"
    ]

    prompt = prompt.lower()

    for pattern in patterns:
        if pattern in prompt:
            return True

    return False