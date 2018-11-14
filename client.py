import vk_api

try:
    vk_session = vk_api.VkApi("+3452636", "+367345345")
    vk_session.auth()
    vk = vk_session.get_api()
except vk_api.exceptions.BadPassword:
    print("sosat")
