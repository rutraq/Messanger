import vk_api

vk_session = vk_api.VkApi(token='209295912aeab32b85fe25c0fdcd843fe8cb5fd7901186b44804c702d5c883faf31863f9ba3329999d964')
vk_session.auth()
vk = vk_session.get_api()