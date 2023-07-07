import random
import time
import vk_api


def authorization():
    vk_session = vk_api.VkApi('номер телефона', 'пароль')
    vk_session.auth()
    vk_ses = vk_session.get_api()
    return vk_ses


def post(vk):
    for random_public in public:
        try:
            vk.wall.post(owner_id=random_public, message=random.choice(messages), attachments=random.choice(images))
        except vk_api.exceptions.Captcha:
            pass
    print('POSTED')
    time.sleep(20)


def save_group(group):
    f = open('groups.txt', 'a')
    f.write(group)
    f.close()


def take_groups():
    groups = []
    with open('groups.txt') as f:
        for line in f:
            groups.append(line.replace('\n', ''))
    return groups


images = ['photo308197981_457240485', 'photo308197981_457240484', 'photo308197981_457240483', 'photo308197981_457240481', 'photo308197981_457240480']
messages = [
'💞Беседка💞\n'
'🌿Поддерживаем любые вкусы.🌿\n'
'👋Правил особо нет.\n'
'😘Ссылочка в закрепе на стене 😘\n',

'🐬🧩🌥• 🐬🧩🌩•🐬🧩🌥• 🐬🧩🌩•🐬🧩🌥• 🐬\n'
'-ˏˋ ☁ ˊˎ- -ˏˋ ☁ ˊˎ- -ˏˋ ☁ ˊˎ-\n'
'ссылка на беседу находится в закрепе на стене\n'
'-ˏˋ ☁ ˊˎ- -ˏˋ ☁ ˊˎ- -ˏˋ ☁ ˊˎ-\n'
'🐬🧩🌥• 🐬🧩🌩•🐬🧩🌥• 🐬🧩🌩•🐬🧩🌥• 🐬\n',

'🖤🐾ССЫЛКА НА НАШУ БЕСЕДКУ В ЗАКРЕПЕ🐾✦🖤🍇\n'
'Тебя приветствует беседа с дружелюбными собеседниками🍀\n'
'💥Ищем собеседников для долгого общения💥'
]

vkk = authorization()
command = True
while command != 0:
    public = take_groups()
    command = int(input('1 - сделать пост (проверка)\n'
    '2 - запустить бота (напишите сколько кругов бот будет спамить)\n'
    '3 - добавить группу для спама\n'
    '0 - end\n'
    'Команда:'))
    if command == 1:
        post(vkk)
    if command == 2:
        loop = int(input('\nКруги:'))
        for i in range(loop):
            post(vkk)
            time.sleep(240)
    if command == 3:
        group_ = str(input('\nГруппа:'))
        save_group(group_)