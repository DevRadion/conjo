import datetime
import inspect

import colorama
from colorama import Fore, Style, Back

from config import Config
from logger.level import Level


class Logger(object):
    _config = None

    def __init__(self):
        colorama.init()

    @staticmethod
    def log(message: str, level: Level = Level.INFO):
        if message == "":
            return

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        caller_class = inspect.stack()[1].frame.f_locals.get("self").__class__.__name__
        caller_class = caller_class if caller_class != "NoneType" else inspect.stack()[1].frame.f_locals.get("__name__")
        level_format = Style.BRIGHT + f"[{level.value}]:" + Style.RESET_ALL
        log_format = f"{timestamp} | {caller_class} | {level_format} {message}"

        level_color = ''
        level_bg_color = ''
        if level == Level.VERBOSE:
            level_color = Fore.BLUE
            level_bg_color = Back.RESET
        elif level == Level.INFO:
            level_color = Fore.GREEN
            level_bg_color = Back.RESET
        elif level == Level.WARNING:
            level_color = Fore.YELLOW
            level_bg_color = Back.RESET
        elif level == Level.ERROR:
            level_color = Fore.RED
            level_bg_color = Back.RESET
        elif level == Level.CRITICAL:
            level_color = Fore.BLACK
            level_bg_color = Back.RED
        elif level == Level.TRACE:
            level_color = Fore.CYAN
            level_bg_color = Back.RESET

        if Level(Config.shared().log_level).id <= level.id:
            print(f"{level_bg_color}{level_color}{log_format}{Style.RESET_ALL}")
