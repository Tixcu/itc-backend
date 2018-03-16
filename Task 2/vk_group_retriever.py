import os

import vk_api


def auth():#Dirty because vk always generating different keys. Dunno if i can fix this.
    login = '8' + os.environ.get('VK_LOG')
    password = os.environ.get('VK_PASS')
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk


def main():
    ses = auth()
    print(ses.users.getSubscriptions())

    
if __name__ == '__main__':
    main()

