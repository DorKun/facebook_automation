import facebook_automation


def main():
    post = str(input('Please insert your chosen post: '))
    facebook_automation.automateFacebook('userData.txt', post, 'Florian Leberfinger')


if __name__ == '__main__':
    main()
