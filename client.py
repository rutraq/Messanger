import vk_api
import requests

try:
    vk_session = vk_api.VkApi("+3452636", "+367345345")
    vk_session.auth()
    vk = vk_session.get_api()
except requests.exceptions.ConnectionError:
    print("sosat")
