import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from defense.security_pipeline import security_pipeline


def call_api(prompt, options, context):
    
    result = security_pipeline(prompt)

    if result["status"] == "blocked":
        return {
            "output": f"BLOCKED: {result['reason']}"
        }

    return {
        "output": result["response"]
    }