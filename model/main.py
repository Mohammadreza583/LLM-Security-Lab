import sys
from model_loader import ask_model


if __name__ == "__main__":

    prompt = sys.argv[1]

    response = ask_model(prompt)

    print(response)