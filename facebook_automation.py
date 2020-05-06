from selenium import webdriver
from time import sleep


class automateFacebook():

    def __init__(self, user_data_file, post, friend_name=None):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values.notifications': 2}
        chrome_options.add_experimental_option('prefs', prefs)
        self.browser = webdriver.Chrome(options=chrome_options,
                                        executable_path='C:\\Users\\simme\\PycharmProjects\\facebook_automation\\chrome_driver\\chromedriver.exe')
        self.browser.maximize_window()
        self.browser.get('https://www.facebook.com/')
        self._read_user_data(user_data_file)
        self._login()
        sleep(3)
        self._post_on_timeline(post)
        sleep(3)
        self._check_friend_requests()
        sleep(5)
        self._add_friend(friend_name)
        sleep(10)

    #  opens the external userData.txt and saves username and password
    def _read_user_data(self, user_data_file):
        with open(user_data_file, 'r+') as userData:
            self._username = userData.readline()
            self._username = self._username[12:-2]
            self._password = userData.readline()
            self._password = self._password[12:-1]

    def _login(self):
        self.browser.find_element_by_id('email').send_keys(self._username)
        self.browser.find_element_by_id('pass').send_keys(self._password)
        self.browser.find_element_by_id('loginbutton').click()

    def _post_on_timeline(self, post):
        self.browser.find_element_by_class_name('_3u16').click()
        sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div').send_keys(
            post)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/button').click()

    def _check_friend_requests(self):
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/a/div').click()
        sleep(5)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/a/div').click()

    def _add_friend(self, friend_name):
        self.browser.find_element_by_name('q').click()
        sleep(2)
        recent_search = self.browser.find_element_by_id('facebar_typeahead_view_list').text
        if friend_name not in recent_search:
            self.browser.find_element_by_name('q').send_keys(friend_name)
            self.browser.find_element_by_tag_name('button').click()
        else:
            self.browser.find_element_by_link_text(friend_name).click()
        sleep(3)
        self.browser.find_element_by_link_text(friend_name).click()
        sleep(2)
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/button[1]').click()
