from code.pom.pages.login_page import Login
from code.pom.pages.dashboard_page import Dashboard
import allure
user = {
    "username": "contact+atb5x@thetestingacademy.com",
    "password": "ATBx@1234"
}



class TestLogin:
    @allure.title("TC#1 - vwo Login testcase")
    def test_valid_login(self, page):
        login_page = Login(page)
        dashboard_page = Dashboard(page)
        login_page.navigate()
        login_page.submit_login_form(user)
        username_text = dashboard_page.get_logged_in_username()
        assert username_text == "Dashboard"
        
    
