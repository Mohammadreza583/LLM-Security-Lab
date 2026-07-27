from defense.prompt_injection_detector import detect_prompt_injection
from defense.jailbreak_detector import detect_jailbreak
from defense.data_leakage_detector import detect_data_leakage


def input_guard(prompt):

    if detect_prompt_injection(prompt):
        return {
            "blocked": True,
            "reason": "Prompt Injection detected"
        }


    if detect_jailbreak(prompt):
        return {
            "blocked": True,
            "reason": "Jailbreak detected"
        }


    if detect_data_leakage(prompt):
        return {
            "blocked": True,
            "reason": "Data Leakage attempt detected"
        }


    return {
        "blocked": False,
        "reason": "Safe input"
    }