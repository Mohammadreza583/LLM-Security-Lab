from defense.input_guard import input_guard
from defense.output_filter import filter_output
from model.model_loader import ask_model


def security_pipeline(prompt):

    # مرحله 1: بررسی ورودی
    input_check = input_guard(prompt)


    if input_check["blocked"]:

        return {
            "status": "blocked",
            "stage": "input",
            "reason": input_check["reason"],
            "response": None
        }


    # مرحله 2: اجرای مدل
    response = ask_model(prompt)


    # مرحله 3: بررسی خروجی
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
        "response": response
    }