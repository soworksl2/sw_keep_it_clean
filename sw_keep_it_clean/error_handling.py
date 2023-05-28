from typing import NoReturn


def exit_with_error(error_message: str = '') -> NoReturn:
    output_message = 'ERROR: '

    if len(error_message) <= 0:
        output_message += 'something went wrong'
    else:
        output_message += error_message

    exit(-1)
