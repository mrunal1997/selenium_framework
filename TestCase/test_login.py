import pytest
from time import sleep
from PageObject.LoginPage import Login
from PageObject.DashBoard_Practice import Dashboard
from PageObject.DashBoard_Contact import Contact
from Utilities.test_logs import LogClass
import configparser
parser = configparser.ConfigParser()
parser.read(filenames="Utilities/input.properties")
logger = LogClass().get_logger()

@pytest.mark.usefixtures("page")
class Test_login:

    @pytest.mark.parametrize("username, password, condition",
                             [("student", "Password123", "+ve"), ("stuent", "Password123", "-ve"),
                              ("student", "Password12", "-ve")])
    def test_login1(self, username, password, condition):
        self.logger = LogClass().get_logger()

        login = Login(self.driver)
        dashboard_p = Dashboard(self.driver)

        login.username(username)
        login.password(password)
        login.click_submit()
        sleep(2)
        if condition == "+ve":
            if "Logged In Successfully" in dashboard_p.login_msg():
                assert True
            else:
                assert False
        if condition == "-ve":
            if "Your username is invalid!" in login.invalid_msg():
                assert True

            elif "Your password is invalid!" in login.invalid_msg():
                assert True
            else:
                assert False, "Text not found"


    def test_login(self):
        self.logger = LogClass().get_logger()
        login = Login(self.driver)
        dashboard_p = Dashboard(self.driver)

        login.username(parser.get("credential", "username"))
        login.password(parser.get("credential", "password"))
        login.click_submit()
        sleep(2)
        dashboard_p.practicePage()
        self.logger.info("Practice page is open")
        dashboard_p.exceptionTest()
        self.logger.info("Clicked on exception label")
        sleep(2)
        dashboard_p.edit_text_btn()
        sleep(2)
        dashboard_p.save_btn()
        self.logger.info("Entered text get save successfully...!")
        sleep(2)
        dashboard_p.add_btn()
        sleep(2)
        if "Row 2 was added" in dashboard_p.status():
            self.logger.info("Entered text get added in list")
            assert True
        else:
            # self.logger.error("Text not found for addition...!!!!")
            assert False, "Text msg not found for addition...!!!"

        sleep(3)
        dashboard_p.remove_btn()
        if "Row 2 was removed" in dashboard_p.status():
            # sleep(5)
            self.logger.info("Added text get removed...!")
            assert True
        else:
            # self.logger.error("Text not found for remove...!!!!")
            assert False, "Text msg not found for remove...!!!"
        sleep(3)
        self.logger.info("Added row get removed again")
        sleep(3)
        dashboard_p.remove_btn()
        self.logger.info("Added row get removed 3rd time")

    def test_username(self):

        login = Login(self.driver)
        login.username("stuent")
        login.password("Password123")
        login.click_submit()
        sleep(5)
        if "Your username is invalid!" in login.invalid_msg():
            assert True
        else:
            assert False, "Text not found"

    def test_password(self):

        login = Login(self.driver)
        login.username("student")
        login.password("Password12")
        login.click_submit()
        sleep(3)
        if "Your password is invalid!" in login.invalid_msg():
            assert True
        else:
            assert False, "Text not found..!!!"

    def test_contact(self):
        login = Login(self.driver)
        dashboard_c = Contact(self.driver)
        login.username("student")
        login.password("Password123")
        login.click_submit()
        logger.info("Login successfully...!!!")
        sleep(3)
        dashboard_c.contactPage()
        dashboard_c.first_name(parser.get("Contact_details", "first_name"))
        dashboard_c.last_name(parser.get("Contact_details", "last_name"))
        dashboard_c.enter_email(parser.get("Contact_details", "emailID"))
        dashboard_c.enter_comment(parser.get("Contact_details", "comment"))
        sleep(3)
        dashboard_c.click_botCheckBox()
        sleep(2)
        dashboard_c.click_submit()
        sleep(2)
        if "Thanks for contacting us! We will be in touch with you shortly." in dashboard_c.thanks_msg():
            assert True
        else:
            assert False, "Something went wrong, successfully sent response message not found..!!!"

