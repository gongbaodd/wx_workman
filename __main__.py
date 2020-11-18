from wxpy import *

bot = Bot('bot.pkl', console_qr=True)


def invite(user):
    '''
    定义邀请用户的方法
    '''
    group = bot.groups().search('Ⓙ🅙即刻大连群')
    group[0].add_members(user, use_invitation=True)


@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    '''
    处理加好友信息
    '''
    user = msg.card.accept()
    invite(user)
