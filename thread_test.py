import vk_api
from easygui import passwordbox

vk_session = vk_api.VkApi("+375293332133", passwordbox(msg="Enter password"))
vk_session.auth()
vk = vk_session.get_api()
id = "172058312"
history = vk.messages.getHistory(user_id=id, fields=['first_name'])
print(history)
history = history['items']
for i in range(len(history)):
    if history[i]['from_id'] == int(id):
        print("Женя Орлов: " + history[i]['text'])
    else:
        print("Артур: " + history[i]['text'])
