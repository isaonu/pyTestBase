import pytest

@pytest.mark.parametrize("enviro, user, password", [("qa", "test@mail.com", 123), ("prod", "testProd@mail.com", 123)])
class TestLogin:

    def test_signIn(self, enviro, user, password):
        if(enviro == "qa"):
            print("qa credentials user: ", user, "password: ", password)
            assert True
        else:
            print("prod credentials user: ", user, "password: ", password)
            assert True

    def test_home_page(self, enviro, user, password):
        if(enviro == "qa"):
            print("User is in the correct position on qa: ", user)
            print("Password for Qa is shown", password)
            assert True
        else:
            print("user is in the correct position in prod ", user)
            print("Password for prod is hidden", password)
            assert True

    #If we run the method like this it will fail, we must use all the parameters we are sending in the parametrize line
    # def test_home_page(self, enviro, user):
    #     if (enviro == "qa"):
    #         print("User is in the correct position on qa: ", user)
    #         assert True
    #     else:
    #         print("user is in the correct position in prod ", user)
    #         assert True