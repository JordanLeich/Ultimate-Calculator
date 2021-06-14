import colors


def validate_float(data):
    try:
        float(data)
        return True
    except ValueError:
        return False


def validate_operator(data):
    operator_options = [
        "+", "-", "*", "/", "**", "=",
        "add", "subtract", "multiply", "times",
        "power", "divide", "division", "equals"]

    if data in operator_options:
        return True

    return False


def validate_yes_no(data):
    accepted = ["yes", "y", "no", "n"]
    return True if data.lower() in accepted else False


# To remove the ugly while True and to make user input validation easier
def repeat_input(sentence, error, flag):
    flags = {
        "float": validate_float,
        "operator": validate_operator,
        "yes_no": validate_yes_no
    }

    while True:
        inputs = input(sentence)  # sentence is what the input text is
        if flags[flag](inputs):  # flag is what kind of validation it will use
            return inputs

        print(colors.red + error, colors.reset)  # error is what error it will print when the validation fails
