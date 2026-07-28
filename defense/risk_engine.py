class RiskEngine:

    RISK_LEVELS = {
        "safe": 0,
        "suspicious": 30,
        "jailbreak": 80,
        "prompt_injection": 85,
        "system_prompt_extraction": 90,
        "data_leakage": 95
    }

    def calculate_risk(self, attack_type):

        score = self.RISK_LEVELS.get(
            attack_type,
            0
        )

        if score >= 90:
            severity = "critical"

        elif score >= 70:
            severity = "high"

        elif score >= 30:
            severity = "medium"

        else:
            severity = "low"

        return {
            "attack_type": attack_type,
            "risk_score": score,
            "severity": severity,
            "action": "block" if score >= 70 else "allow"
        }


if __name__ == "__main__":

    engine = RiskEngine()

    test_attacks = [
        "safe",
        "jailbreak",
        "prompt_injection",
        "system_prompt_extraction",
        "data_leakage"
    ]

    for attack in test_attacks:
        result = engine.calculate_risk(attack)

        print("=" * 50)
        print(result)