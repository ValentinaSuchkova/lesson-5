from selene import browser, by, have, command, be
import os


def test_qa_reg_form():

    browser.open('/')

    #User data
    browser.element('#firstName').should(be.blank).type("Tina")
    browser.element('#lastName').should(be.blank).type("Test")
    browser.element('#userEmail').should(be.blank).type("valentina.m.suchkova@gmail.com")
    browser.element('[value="Female"]').perform(command.js.click)
    browser.element('[value="Female"]')
    browser.element('#userNumber').should(be.blank).type("9161234567")

    #Date of birth selection
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(by.text("1994")).click()
    browser.element('.react-datepicker__month-select').click().element(by.text("September")).click()
    browser.element('.react-datepicker__week .react-datepicker__day--020').click()

    #Additional info
    browser.element('#subjectsInput').type("English").press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('666.jpg'))

    #Address
    browser.element('#currentAddress').should(be.blank).type('Random street, house 3')
    browser.element('#react-select-3-input').should(be.blank).type('NCR').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Delhi').press_enter()

    #Submit the application
    browser.element('#submit').click()

    #Modal window check
    browser.element('.table').should(have.text('Tina Test'))
    browser.element('.table').should(have.text('valentina.m.suchkova@gmail.com'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('valentina.m.suchkova@gmail.com'))
    browser.element('.table').should(have.text('9161234567'))
    browser.element('.table').should(have.text('20 September,1994'))
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Music'))
    browser.element('.table').should(have.text('666.jpg'))
    browser.element('.table').should(have.text('Random street, house 3'))
    browser.element('.table').should(have.text('NCR Delhi'))