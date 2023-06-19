from ..utilities.gerenalMethods import GeneralMethods

class Home(GeneralMethods):

    titleSelector = "My title selector"

    def get_title_text(self):
        return self.get_some_text_of_element(Home.titleSelector)