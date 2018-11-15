import time
import vk_api


vk_session = vk_api.VkApi("+375293332133", "sTAl#1701")
vk_session.auth()
vk = vk_session.get_api()

info_for_messages = vk.messages.getLongPollServer(need_pts=1)
while True:
    updates = vk.messages.getLongPollHistory(ts=info_for_messages['ts'], pts=info_for_messages['pts'])
    print(len(updates['messages']['items']))
    print(updates)
    if len(updates['messages']['items']) > 0:
        for msg in range(len(updates['messages']['items'])):
            vk.messages.markAsRead(peer_id=updates['messages']['items'][msg]['peer_id'])
        print("read")
