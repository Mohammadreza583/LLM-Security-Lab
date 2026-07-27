import re


def filter_output(response):

    sensitive_patterns = [

        r"api[_ -]?key",
        r"password",
        r"secret",
        r"token",
        r"sk-[a-zA-Z0-9]+",
        r"private[_ -]?key"

    ]


    for pattern in sensitive_patterns:

        if re.search(pattern, response, re.IGNORECASE):

            return {
                "blocked": True,
                "reason": "Sensitive information detected",
                "response": None
            }


    return {
        "blocked": False,
        "reason": "Output is safe",
        "response": response
    }