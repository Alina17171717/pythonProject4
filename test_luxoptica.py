from time import sleep
from selene import have, be
from selene.support.shared import browser

def test_luxoptica():
      browser.open('https://luxoptica.ua/')
      browser.all('.header-fast-click li')[3].click()
      browser.element('[name="email"]').type('melnichukdenisss@gmail.com').press_tab()
      browser.element('[name = "password"]').type('qweasdzxc')
      sleep(10)
      browser.element('#sign-in-form > div > div:nth-child(4) > button').click()
      browser.element('.js-show-search').click()
      browser.element('.show-hide-menu-in').click()
      browser.element('[href="/ua/sunglasses/"]').click()
      browser.element('[href="/ua/sunglasses/guess-gu00069-08b-63/"]').click()
      browser.element('.brod-buy-bt').click()
      sleep(5)
      browser.element('#successModal > div > div > button').click()
      browser.element('[href = "/ua/cart/"]').click()
      sleep(10)
      browser.all('.header-fast-click li')[2].click()
      browser.element('.bask-item-del').click()
      sleep(5)
      browser.quit()

def test_incorrect_password():
      browser.open('https://luxoptica.ua/')
      browser.all('.header-fast-click li')[3].click()
      browser.element('[name="email"]').type('melnichukdenisss@gmail.com').press_tab()
      browser.element('[name = "password"]').type('')
      sleep(5)
      browser.element('#sign-in-form > div > div:nth-child(4) > button').click()
      sleep(5)
      browser.element('.help-block-password.error-mess').should(have.text('Поле обязательно для заполнения'))
      browser.quit()


