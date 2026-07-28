from defense.input_guard import input_guard
from defense.output_filter import filter_output
from defense.attack_classifier import AttackClassifier
from defense.risk_engine import RiskEngine
from model.model_loader import ask_model


classifier = AttackClassifier()
risk_engine = RiskEngine()


def security_pipeline(prompt):

    # مرحله 1: طبقه بندی حمله
    attack_result = classifier.classify(prompt)


    # مرحله 2: ارزیابی ریسک
    risk_result = risk_engine.calculate_risk(
        attack_result["attack_type"]
    )


    if risk_result["action"] == "block":

        return {
            "status": "blocked",
            "stage": "risk_engine",
            "reason": f'{attack_result["attack_type"]} detected',
            "risk": risk_result,
            "response": None
        }


    # مرحله 3: بررسی ورودی قدیمی
    input_check = input_guard(prompt)


    if input_check["blocked"]:

        return {
            "status": "blocked",
            "stage": "input",
            "reason": input_check["reason"],
            "response": None
        }


    # مرحله 4: اجرای مدل
    response = ask_model(prompt)


    # مرحله 5: بررسی خروجی
    output_check = filter_output(response)


    if output_check["blocked"]:

        return {
            "status": "blocked",
            "stage": "output",
            "reason": output_check["reason"],
            "response": None
        }


    return {
        "status": "allowed",
        "stage": "complete",
        "reason": "Passed security checks",
        "attack_analysis": attack_result,
        "risk_analysis": risk_result,
        "response": response
    }