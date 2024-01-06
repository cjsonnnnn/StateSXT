from . import Locator


class LoginLocator(Locator):
    """Login page locator class"""

    def __init__(self, base) -> None:
        super().__init__(base)
        self.setup()

    def setup(self) -> None:
        # usernames
        self.USERNAME_INPUTBOX = lambda loc="//input[@placeholder='Enter username' or @placeholder='ユーザ名を入力']": self.bd.wd.clickable(self.by.xpath, loc)
        self.JPN_USERNAME_LABEL = lambda loc="//label[contains(text(),'ユーザー名')]": self.bd.wd.an_element(self.by.xpath, loc)
        self.JPN_USERNAME_PLACEHOLDER = lambda loc="//input[@placeholder='ユーザ名を入力']": self.bd.wd.an_element(self.by.xpath, loc)
        self.ENG_USERNAME_LABEL = lambda loc="//label[contains(text(),'Username')]": self.bd.wd.an_element(self.by.xpath, loc)
        self.ENG_USERNAME_PLACEHOLDER = lambda loc="//input[@placeholder='Enter username']": self.bd.wd.an_element(self.by.xpath, loc)

        # passwords
        self.PASSWORD_INPUTBOX = lambda loc="//input[@id='userpassword']": self.bd.wd.clickable(self.by.xpath, loc)
        self.JPN_PASSWORD_LABEL = lambda loc="//label[contains(text(),'パスワード')]": self.bd.wd.an_element(self.by.xpath, loc)
        self.JPN_PASSWORD_PLACEHOLDER = lambda loc="//input[@placeholder='パスワードを入力']": self.bd.wd.an_element(self.by.xpath, loc)
        self.ENG_PASSWORD_LABEL = lambda loc="//label[contains(text(),'Password')]": self.bd.wd.an_element(self.by.xpath, loc)
        self.ENG_PASSWORD_PLACEHOLDER = lambda loc="//input[@placeholder='Enter password']": self.bd.wd.an_element(self.by.xpath, loc)

        # login buttons
        self.LOGIN_BUTTON = lambda loc="//button[@type='submit']": self.bd.wd.clickable(self.by.xpath, loc)
        self.JPN_LOGIN_BUTTON_LABEL = lambda loc="ログイン": loc
        self.ENG_LOGIN_BUTTON_LABEL = lambda loc="Login": loc

        # flags
        self.JPN_FLAG_BUTTON = lambda loc="//div[@class='d-flex justify-content-center']//label[1]": self.bd.wd.clickable(self.by.xpath, loc)
        self.ENG_FLAG_BUTTON = lambda loc="//div[@class='d-flex justify-content-center']//label[2]": self.bd.wd.clickable(self.by.xpath, loc)

        # alerts
        self.FAILED_LOGIN_ALERT = lambda loc="//div[@role='alert']": self.bd.wd.an_element(self.by.xpath, loc)
        self.JPN_ALERT_EMPTY_USERNAME = lambda loc="//div[contains(text(),'適切なユーザ名を入力してください')]": self.bd.wd.visible(self.by.xpath, loc)
        self.JPN_ALERT_EMPTY_PASSWORD = lambda loc="//div[contains(text(),'適切なパスワードを入力してください')]": self.bd.wd.visible(self.by.xpath, loc)
        self.ENG_ALERT_EMPTY_USERNAME = lambda loc="//div[contains(text(),'Please enter the username')]": self.bd.wd.visible(self.by.xpath, loc)
        self.ENG_ALERT_EMPTY_PASSWORD = lambda loc="//div[contains(text(),'Please enter the password')]": self.bd.wd.visible(self.by.xpath, loc)
        self.VALID_LOGIN_LOCATOR = lambda loc="/html[1]/body[1]/div[1]/div[2]/nav[1]/div[1]/div[1]/a[1]": self.bd.wd.visible(self.by.xpath, loc)
