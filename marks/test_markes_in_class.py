import pytest
user_type = "normal"

@pytest.mark.skipif(user_type  == "normal", reason = "Test applicable for admin role only")
class TestAdminTest:
    def test_sign_in(self):
        assert 20 == 18

    def test_config_menu(self):
        assert 10 == 4


class TestAllUserTest:
    def test_home_page(self):
        assert 50 == 50
