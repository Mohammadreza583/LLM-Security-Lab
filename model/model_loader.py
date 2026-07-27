from transformers import pipeline


model_name = "gpt2"


generator = pipeline(
    "text-generation",
    model=model_name
)


def ask_model(prompt):

    result = generator(
        prompt,
        max_new_tokens=100
    )

    return result[0]["generated_text"]
