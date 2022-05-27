import inspect
from functools import wraps

import allure

from const import RespCode


def checkpoint(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        parameters = inspect.signature(func).parameters
        arguments = list(parameters.keys())
        payload = {
            parameter.name: parameter.default
            for _, parameter in parameters.items()
            if parameter.default is not inspect._empty and parameter.name != "self"
        }
        if arguments[0] == "self":
            arguments.pop(0)
            args_ = args[1:]
        else:
            args_ = None
        if args_:
            for index, val in enumerate(args_):
                arg_name = arguments[index]
                payload[arg_name] = val
        payload.update(kwargs)

        func_name = func.__name__

        expect = payload.get("expect", None)
        actual = payload.get("actual", None)

        if "response" in func_name:
            expect = {"code": RespCode.SUCCESS}
            actual = payload.get("resp")

        tmp = func_name.split("_")

        if expect is None:
            expect = " ".join(tmp[1:])

        msg = "[Expect]: {ex}\n[Actual]: {ac}".format(ex=expect, ac=actual)
        # print(func_name)
        # print(msg)
        with allure.step('checkpoint: \n'):
            allure.attach(msg, func_name)
        func(*args, **kwargs)

    return wrapped
