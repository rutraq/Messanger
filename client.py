import vk_api
import psycopg2
from easygui import passwordbox, enterbox


check = 0
list_domain = []


def login():
    global vk
    vk_session = vk_api.VkApi(enterbox(msg="Enter telephone"), passwordbox(msg="Enter password"))
    vk_session.auth()
    vk = vk_session.get_api()


def get_friends():
    conn = psycopg2.connect("dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
    cur = conn.cursor()
    res = cur.execute("SELECT * FROM users")
    row = cur.fetchone()
    list_domain.append(row[1])
    for entry in cur:
        list_domain.append(entry[1])


def send_message(domain_for_sending):
    message = input("Enter your message: ")
    vk.messages.send(domain=domain_for_sending, message=message)


def get_message():
    info_for_messages = vk.messages.getLongPollServer(need_pts=1)
    while True:
        updates = vk.messages.getLongPollHistory(ts=info_for_messages['ts'], pts=info_for_messages['pts'], fields='domain')
        if len(updates['messages']['items']) > 0:
            for msg in range(len(updates['messages']['items'])):
                domain_vk = updates['profiles'][0]['domain']
                for domain in list_domain:
                    if domain == domain_vk:
                            vk.messages.markAsRead(peer_id=updates['messages']['items'][msg]['peer_id'])
                            if len(updates['profiles']) == 1:
                                print(updates['profiles'][0]['first_name'] + " " + updates['profiles'][0]['last_name'] + ":")
                                print(updates['messages']['items'][msg]['text'])
                            elif len(updates['profiles']) == 2:
                                print(updates['profiles'][1]['first_name'] + " " + updates['profiles'][1]['last_name'] + ":")
                                print(updates['messages']['items'][msg]['text'])
            info_for_messages = vk.messages.getLongPollServer(need_pts=1)
