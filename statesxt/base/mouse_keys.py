from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from typing import Callable
from typing import Union
import time


class MouseKeysDriver:
    """
    Provides Mouse and Keys capabilities.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.ac = ActionChains(driver)
        self.__driver = driver

    def hovering(
        self,
        element: Union[WebElement, Callable[[], WebElement]],
        isHover: bool = True,
        onFocus: bool = False,
    ) -> None:
        if isHover:
            if isinstance(element, Callable):
                element = element()
            if onFocus:
                self.scrolling(element)
            self.ac.move_to_element(element).perform()
            self.ac.reset_actions()

    def scrolling(
        self,
        element: Union[WebElement, Callable[[], WebElement]] = None,
        isScroll: bool = True,
        steps: int = None,
        block: str = "center",
        sleep: float = 0.75,
    ) -> None:
        """
        'block', defines vertical alignment.
        - 'start',
        - 'center' (default),
        - 'end',
        - 'nearest'.
        """

        if isScroll:
            if element:
                if isinstance(element, Callable):
                    element = element()
                if steps:
                    print(f"steps: {steps}")
                    self.ac.scroll_by_amount(0, steps).pause(sleep).perform()
                    self.__driver.execute_script("arguments[0].scrollIntoView();", element)
                else:
                    self.__driver.execute_script(
                        "arguments[0].scrollIntoView({block: '" + block + "'});",
                        element,
                    )
                    time.sleep(sleep)
            else:
                self.ac.scroll_by_amount(0, steps).pause(sleep).perform()
                self.ac.reset_actions()

    def clicking(
        self,
        element: Union[WebElement, Callable[[], WebElement]],
        isClick: bool = True,
        sleep: float = 0.36,
        steps: int = None,
        block: str = "center",
    ) -> None:
        if isClick:
            if isinstance(element, Callable):
                element = element()
            if sleep >= 0.36:
                self.scrolling(element=element, steps=steps, block=block, sleep=sleep)
            element.click()

    def pressing_keys(self, options: str) -> None:  # temp: has an unknown error
        keys = {
            "esc": Keys.ESCAPE,
            "enter": Keys.ENTER,
        }
        self.ac.send_keys(keys[options]).perform()
        self.ac.reset_actions()

    def zooming(self, zoom_percentage: float, sleep: int = 1) -> None:
        """
        Zooms in and out the screen.

        Args:
            - zoom_percentage (float), is the percentage of the screen wanted to be
        """
        self.__driver.execute_script(f"document.body.style.zoom = '{zoom_percentage/100}';")
        time.sleep(sleep)

    def paginating(
        self,
        target_row: list[str],
        func_get_paginations: Callable[[], list[WebElement]],
        func_check_rows: Callable[[list[str]], bool],
        direction: str = "backward",
        tobeFound: bool = True,
        sleep: float = 0,
    ):
        def get_list_of_pagination_numbers():
            raw_pns = func_get_paginations()
            pns = []
            titles = []
            for pn in raw_pns:
                title = pn.get_attribute("title")
                if title in [
                    "previous page",
                    "next page",
                    "first page",
                    "last page",
                ]:
                    pns.append(pn)
                    titles.append(title)
            return [pns, titles]

        def click_page_number(title: str, pns: list[WebElement], titles: list[str]):
            """
            - clicks the title page and updates the pagination numbers, and their titles
            - title is whether 'previous page','next page','first page', or 'last page'
            """

            pn = pns[titles.index(title)]
            self.scrolling(element=pn)
            pn.click()
            return get_list_of_pagination_numbers()

        pns, titles = get_list_of_pagination_numbers()
        if direction == "backward":
            # go to the last page
            if "last page" in titles:
                pns, titles = click_page_number(title="last page", pns=pns, titles=titles)
            else:
                # backwarding (without checking)
                while "next page" in titles:
                    pns, titles = click_page_number(title="next page", pns=pns, titles=titles)

        # checking while also backwarding
        occur = 0
        while occur < 1:
            # check whether or not the condition is ready to stop
            if ("previous page" not in titles) if (direction == "backward") else ("next page" not in titles):  # when in page item-1
                occur += 1
            # check current page's rows
            time.sleep(sleep)
            if func_check_rows(target_row):
                return True if tobeFound else False
            # forwarding / backwarding (depends on the direction)
            if occur != 1:
                pns, titles = (
                    click_page_number(title="previous page", pns=pns, titles=titles) if (direction == "backward") else click_page_number(title="next page", pns=pns, titles=titles)
                )
        return False if tobeFound else True
