from datetime import datetime
from enum import Enum


class __LogType(str, Enum):
    INFO = "info"
    WARN = "warn"
    ERROR = "error"


class __Colors(str, Enum):
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    GRAY = '\033[0;2m'
    UNDER = '\033[0;4m'
    RESET = '\033[0m'


def __get_log_type(type: __LogType) -> str:
    type_formated = f"[{type}]"
    return {
        __LogType.INFO: green(type_formated),
        __LogType.WARN: yellow(type_formated),
        __LogType.ERROR: red(type_formated),
    }[type]


def __get_time() -> str:
    return datetime.now().strftime(f"{__Colors.GRAY}[%H:%M:%S]{__Colors.RESET}")


def __log_message(message: str, type: __LogType):
    print(f"{__get_time()} {__get_log_type(type)} {message}")


def info(message: str):
    __log_message(message=message, type=__LogType.INFO)


def warn(message: str):
    __log_message(message=message, type=__LogType.WARN)


def error(message: str):
    __log_message(message=message, type=__LogType.ERROR)


def under(message: str):
    return f"{__Colors.UNDER}{message}{__Colors.RESET}"


def green(message: str):
    return f"{__Colors.GREEN}{message}{__Colors.RESET}"


def yellow(message: str):
    return f"{__Colors.YELLOW}{message}{__Colors.RESET}"


def red(message: str):
    return f"{__Colors.RED}{message}{__Colors.RESET}"
