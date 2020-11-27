from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from ignore import AmazonAnswers, save_userData, read_userData
import ast

if __name__ == "__main__":
    user_agent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
    options = Options()
    options.add_argument(f'user-agent={user_agent}')
    d = webdriver.Chrome('.\driver\chromedriver.exe', options=options)
    d.set_window_size(480, 900)
    d.get('https://www.amazon.in/s?k=quiz&ref=nb_sb_noss')
    time.sleep(1)
    d.find_element_by_xpath("//span[contains(text(),'FunZone')]").click()
    time.sleep(1)
    all_contests = d.find_elements_by_xpath("//a[contains(@href,'game')]")
    """for i in all_contests:
        print(i.get_attribute('aria-label'))"""
    # d.find_element_by_xpath(f"(//a[contains(@href,'game')])[{int(input('Enter quiz name : '))}]").click()
    d.find_element_by_xpath(f"(//a[contains(@href,'game')])[1]").click()
    time.sleep(1)


    def login():
        email_r_phone = ''
        pwd1 = ''
        # print('Login Process', '\n', '-' * 20)
        if d.find_element_by_xpath("//input[contains(@type,'email')]").is_displayed():
            if len(read_userData()) != 2:
                print('!OneTime Login is required')
                print("!Login Credentials Can Be Saved in userDetails.txt")
                
                email_r_phone = input("Enter Email or phone (country code required) : ")
            else:
                email_r_phone = read_userData()[0]
            d.find_element_by_xpath("//input[contains(@type,'email')]").send_keys(email_r_phone)
        if d.find_element_by_xpath("//input[contains(@type,'password')]").is_displayed():  # login amazon
            # print('login needed', '\n', '-' * 20)
            # print('Bypassing..login')
            if len(read_userData()) != 2:
                pwd1 = input('Enter Your Password : ')
            else:
                pwd1 = read_userData()[1]
            d.find_element_by_xpath("//input[contains(@type,'password')]").send_keys(pwd1)
            d.find_element_by_xpath("(//input[contains(@type,'submit')])[1]").click()
            time.sleep(2)
        print('login completed.. ')
        save_userData([email_r_phone, pwd1])


    try:
        login()
    except:
        pass
    time.sleep(1)
    try:
        if d.find_element_by_xpath("//input[contains(@type,'password')]").is_displayed():  # login amazon
            login()
    except:
        pass
    time.sleep(1)
    try:
        # start quiz
        d.find_element_by_xpath("//input[contains(@aria-labelledby,'start')]").click()
    except:
        pass
    # initialise amazon answers
    amz = AmazonAnswers()


    def try1():
        amz.source1()
        if not len(amz.answers) > 1:
            amz.source2()


    try:
        try1()
    except:
        amz.source2()
        try1()

    # storing value
    answers = amz.answers
    print("Quiz answers : ", answers)
    time.sleep(1)

    try:
        if d.find_element_by_xpath("//a[contains(text(),'Play more games')]").is_displayed():
            print('Congratulations! You Already Completed Quiz')
        else:
            # all options of all questions
            amazon_options = d.find_elements_by_xpath("//div[contains(@id,'option-')]")
            try:
                for i in answers:
                    for j in amazon_options:
                        if i in j.text:
                            j.click()
                            time.sleep(8)
                        else:
                            pass
                print('Congratulations!')
            except:
                pass

    except:
        pass
