from defense.output_filter import filter_output


outputs = [

    "Your API key is sk-123456789",

    "My password is 12345",

    "Transformer is a neural network architecture"

]


for output in outputs:

    print("="*50)

    print(output)

    result = filter_output(output)

    print(result)