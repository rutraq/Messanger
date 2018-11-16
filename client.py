import vk_api
from easygui import passwordbox

vk_session = vk_api.VkApi("+375293332133", passwordbox(msg="Enter password"))
vk_session.auth()
vk = vk_session.get_api()

info_for_messages = vk.messages.getLongPollServer(need_pts=1)
while True:
    updates = vk.messages.getLongPollHistory(ts=info_for_messages['ts'], pts=info_for_messages['pts'])
    if len(updates['messages']['items']) > 0:
        for msg in range(len(updates['messages']['items'])):
            vk.messages.markAsRead(peer_id=updates['messages']['items'][msg]['peer_id'])
            if len(updates['profiles']) == 1:
                print(updates['profiles'][0]['first_name'] + " " + updates['profiles'][0]['last_name'] + ":")
                print(updates['messages']['items'][msg]['text'])
            elif len(updates['profiles']) == 2:
                print(updates['profiles'][1]['first_name'] + " " + updates['profiles'][1]['last_name'] + ":")
                print(updates['messages']['items'][msg]['text'])
        info_for_messages = vk.messages.getLongPollServer(need_pts=1)
        print("read")
