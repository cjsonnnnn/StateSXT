from functools import wraps
import logging
import sys

from .faker import FakerGenerator


class Wrapper:
    """Making use functools\wraps"""

    @classmethod
    def exception_handling_returns_None(cls, func):
        """
        to let a test case returns a None value instead of raises an exception/error
        """
        decoratorClassName = cls.__name__
        decoratorMethodName = sys._getframe().f_code.co_name

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.getLogger(f"root.{__name__}.{decoratorClassName}.{decoratorMethodName}").error(f"error:\n{str(e)}")
                return None

        return wrapper

    @classmethod
    def exception_handling_raises_error(cls, func):
        """
        to handle the error by tracking, but keeps raises the error
        """
        decoratorClassName = cls.__name__
        decoratorMethodName = sys._getframe().f_code.co_name

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.getLogger(f"root.{__name__}.{decoratorClassName}.{decoratorMethodName}").error(f"error:\n{str(e)}")
                raise Exception(str(e))

        return wrapper

    @classmethod
    def result_receiving(cls, func):
        """
        to track the result of test cases, so instead of directly raising error, it lets to write down the error first, e.g. email, report, and summary
        """
        decoratorClassName = cls.__name__
        decoratorMethodName = sys._getframe().f_code.co_name

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            funcName = str(func.__name__).replace("_", " ").title()
            try:
                isFail = False
                errorMessage = None
                try:
                    func(self, *args, **kwargs)
                    self.email.testResult[funcName].append("PASSED")
                except Exception as e:
                    if str(e).replace("'", "") != funcName:
                        logging.getLogger(f"root.{__name__}.{decoratorClassName}.{decoratorMethodName}").error(
                            f"class: {self.__class__.__name__}, method: {func.__name__}\n{str(e)}"
                        )
                        isFail = True
                    errorMessage = str(e)
                    self.email.testResult[funcName].append("FAILED")
            except:
                if not isFail:
                    self.email.testResult[funcName] = ["PASSED"]
                else:
                    self.email.testResult[funcName] = ["FAILED"]

            print(f"\n\nCurrent results:\n{self.email.testResult}")
            if isFail:
                raise Exception(f"There is an error in {funcName}: {errorMessage}")

        return wrapper

    @classmethod
    def unpagshe(cls, worksheetName, named_range, needExternalCheck=False):
        """
        to retrieve and unpack the data from gsheet
        """
        decoratorClassName = cls.__name__
        decoratorMethodName = sys._getframe().f_code.co_name

        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                data = self.gsheet.get_values_by_named_range(worksheetName, named_range)
                result = []
                isFail = False
                emptyFormats = [
                    "",
                    "-",
                    "<blank>",
                    "<empty>",
                    "blank",
                    "empty",
                    "inactive",
                    "uncheck",
                ]
                anyFormats = ["anything", "dc", "Any", "any"]
                for row in data:
                    # preprocess data
                    row = [None if (col in emptyFormats) else col for col in row]
                    row = [(FakerGenerator().generate_sentence() if (col in anyFormats) else col) for col in row]

                    try:
                        func(self, *row, *args, **kwargs)
                        result.append(["PASSED", "PASSED" if needExternalCheck else "", ""])
                        self.p.resetState()
                    except Exception as e:
                        logging.getLogger(f"root.{__name__}.{decoratorClassName}.{decoratorMethodName}").error(
                            f"class: {self.__class__.__name__}, method: {func.__name__}\n{str(e)}"
                        )
                        # raise Exception(str(e))
                        result.append(
                            [
                                "FAILED",
                                "FAILED" if needExternalCheck else "",
                                f"'{str(e)}'",
                            ]
                        )
                        if not isFail:
                            isFail = True

                try:
                    self.gsheet.scenarioResult[worksheetName][named_range] = result
                except:
                    self.gsheet.scenarioResult[worksheetName] = {named_range: result}
                if isFail:
                    raise Exception("an error occured")

            return wrapper

        return decorator

    """UNUSED"""

    # temp, still don't know how to move this to the utils.wrapper
    @classmethod
    def login_exeception_handling(cls, func):
        """to catch the error when login"""
        decoratorClassName = cls.__name__
        decoratorMethodName = sys._getframe().f_code.co_name

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)

            except Exception as e:
                logging.getLogger(f"root.{__name__}.{decoratorClassName}.{decoratorMethodName}").error(f"login error:\n{str(e)}")
                raise Exception(str(e))

        return wrapper

    @classmethod
    def role_checking(cls, func_role):
        """
        to check the role inputted (from command) before executing any testcase (not used/deprecated)
        """

        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.role == func_role:
                    func(self, *args, **kwargs)
                else:
                    print(f"Role doesn't match, skipping '{func.__name__}' execution")
                    return

            return wrapper

        return decorator
