from ..pom.signInPage import SignIn
from ..pom.homePage import Home

class TestMyPage:


    def test_one(self):
        sign_in = SignIn()
        sign_in.type_email("rober@mail.com")
        sign_in.type_password("myPassword")
        home = sign_in.click_on_signIn()
        assert home.get_title_text() == "This is the text __ of selector My title selector"

