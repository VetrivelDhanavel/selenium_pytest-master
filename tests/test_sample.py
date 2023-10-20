from automation.pages.home_page import AlphaPage

def test_alpha_page(driver):
    # Instantiate the AlphaPage class

    alpha_page = AlphaPage(driver)

    # Open Alpha page
    alpha_page.open()

