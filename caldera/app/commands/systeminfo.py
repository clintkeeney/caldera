from .command import CommandLine
from typing import List, Union, Callable, Tuple, Dict
from . import parsers


def systeminfo(args: List[str]=None) -> CommandLine:
    """
    Wrapper for the windows tool systeminfo.exe

    Args:
        args: The additional arguments for the command line

    Returns:
        The CommandLine
    """
    command_line = ["systeminfo.exe"]

    if args is not None:
        command_line += args

    return CommandLine(command_line)


def csv(remote_host: str=None, user_domain: str=None, user: str=None, password: str=None) \
        -> Tuple[CommandLine, Callable[[str], Dict]]:
    """Systeminfo.exe with CSV formatted output.


    Args:
        remote_host: (Optional) The host to get systeminfo about. If blank, the output will be for the local system.
        user: (Optional) Credentials for running systeminfo remotely.
        password: (Optional) Credentials for running systeminfo remotely.

    Returns:
        The CommandLine and a parser for the output of the command
    """
    args = ['/fo csv']

    if remote_host:
        args.append("/S " + remote_host)

        if user:
            args.append("/U " + ((user_domain + '\\' + user) if user_domain else user))

        if password:
            args.append("/p " + password)

    return systeminfo(args), parsers.systeminfo.csv_with_headers
