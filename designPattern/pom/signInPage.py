from ..utilities.gerenalMethods import GeneralMethods
from .homePage import Home

class SignIn(GeneralMethods):
    mySelector = "This is the selector"
    mySelector2 = "This is the selector2"

    def __init__(self):
        self.browser = "chrome"

    #Methods without arguments and action done within the method
    def click_on_signIn(self):
        print(f"button clicked: {SignIn.mySelector}")
        return Home()

    #Method which receives arguments
    def type_email(self, email):
        print(f"This is the {email}")

    #Using method from generalMehtods and local method
    def type_password(self, text):
        self.wait_for_element(SignIn.mySelector2)
        print(f"Ingresando el password: {text}")





