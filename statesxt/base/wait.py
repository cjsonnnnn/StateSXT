from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from utils.wrapper import Wrapper


class MyBy:
    """
    Provides keys that each links to an 'By' object.
    The purpose is to have control to By objects name.

    For example:
    If we want to rename one of the keys, that can be done by renaming it just in here.
    Of course do not forget to use F2 before renaming it, so it applies to all references.
    """

    xpath = By.XPATH
    css = By.CSS_SELECTOR
    cname = By.CLASS_NAME
    id = By.ID
    link = By.LINK_TEXT
    plink = By.PARTIAL_LINK_TEXT
    name = By.NAME
    tag = By.TAG_NAME


class WaitDriver:
    """
    Provides explicit wait, i.e. will wait until either the element has found or exceed time limit.
    """

    def __init__(self, driver, duration: int) -> None:
        self.init_duration = duration
        self.wdw = WebDriverWait(driver, duration)

    @Wrapper.exception_handling_returns_None
    def an_element(self, by: MyBy, locator, custom_duration: float = 0) -> WebElement:
        if custom_duration > 0:
            self.wdw._timeout = custom_duration
        res = self.wdw.until(EC.presence_of_element_located((by, locator)))
        self.wdw._timeout = self.init_duration
        return res

    @Wrapper.exception_handling_returns_None
    def all_elements(self, by: MyBy, locator, custom_duration: float = 0) -> list[WebElement]:
        if custom_duration > 0:
            self.wdw._timeout = custom_duration
        res = self.wdw.until(EC.presence_of_all_elements_located((by, locator)))
        self.wdw._timeout = self.init_duration
        return res

    @Wrapper.exception_handling_returns_None
    def clickable(self, by: MyBy, locator, custom_duration: float = 0) -> WebElement:
        if custom_duration > 0:
            self.wdw._timeout = custom_duration
        res = self.wdw.until(EC.element_to_be_clickable((by, locator)))
        self.wdw._timeout = self.init_duration
        return res

    @Wrapper.exception_handling_returns_None
    def visible(self, by: MyBy, locator, custom_duration: float = 0) -> WebElement:
        if custom_duration > 0:
            self.wdw._timeout = custom_duration
        res = self.wdw.until(EC.visibility_of_element_located((by, locator)))
        self.wdw._timeout = self.init_duration
        return res

    @Wrapper.exception_handling_returns_None
    def invisible(self, by: MyBy, locator, custom_duration: float = 0) -> bool:
        if custom_duration > 0:
            self.wdw._timeout = custom_duration
        res = self.wdw.until(EC.invisibility_of_element_located((by, locator)))
        self.wdw._timeout = self.init_duration
        return res
