from modules import colors


def validate_float(data):
    try:
        float(data)
        return True
    except ValueError:
        return False


def validate_int(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


def validate_str(data):
    try:
        str(data)
        return True
    except ValueError:
        return False


def validate_operator(data):
    operator_options = [
        "+", "-", "*", "/", "**", "=",
        "add", "subtract", "multiply", "times",
        "power", "divide", "division", "equals"]

    return data in operator_options


def validate_yes_no(data):
    accepted = ["yes", "y", "no", "n"]
    return data.lower() in accepted


# To remove the ugly while True and to make user input validation easier
def repeat_input(sentence, error, flag='', custom_validation=lambda _: True):
    flags = {
        "float": validate_float,
        "int": validate_int,
        "str": validate_str,
        "operator": validate_operator,
        "yes_no": validate_yes_no,
        '': lambda _: True
    }

    while True:
        inputs = input(sentence)
        if flags[flag](inputs) and custom_validation(inputs):  # flag is what kind of validation it will use
            return inputs

        print(colors.red + error, colors.reset)  # error is what error it will print when the validation fails
