from core.builtins import Bot
from core.builtins import Image
from core.component import module
from database import BotDBUtil
from .dbutils import CytoidBindInfoManager
from .profile import cytoid_profile
from .rating import get_rating
from .utils import get_profile_name

cytoid = module('cytoid',
                developers=['OasisAkari'], alias='ctd')


@cytoid.handle('profile [<UserID>] {{cytoid.help.profile}}')
async def _(msg: Bot.MessageSession):
    if msg.parsed_msg['profile']:
        await cytoid_profile(msg)


@cytoid.handle('(b30|r30) [<UserID>] {{cytoid.help.b30}}')
async def _(msg: Bot.MessageSession):
    if 'b30' in msg.parsed_msg:
        query = 'b30'
    elif 'r30' in msg.parsed_msg:
        query = 'r30'
    else:
        raise
    pat = msg.parsed_msg.get('<UserID>', False)
    if pat:
        query_id = pat
    else:
        query_id = CytoidBindInfoManager(msg).get_bind_username()
        if query_id is None:
            await msg.finish(msg.locale.t('cytoid.message.user_unbound', prefix=msg.prefixes[0]))
    if query:
        if msg.target.target_from == 'TEST|Console':
            c = 0
        else:
            qc = BotDBUtil.CoolDown(msg, 'cytoid_rank')
            c = qc.check(150)
        if c == 0:
            img = await get_rating(query_id, query, msg)
            if 'path' in img:
                await msg.send_message([Image(path=img['path'])], allow_split_image=False)
            if 'text' in img:
                await msg.send_message(img['text'])
            if msg.target.target_from != 'TEST|Console':
                if img['status']:
                    qc.reset()
        else:
            await msg.finish(msg.locale.t('cytoid.message.b30.cooldown', time=int(c)))


@cytoid.handle('bind <username> {{cytoid.help.bind}}')
async def _(msg: Bot.MessageSession):
    code: str = msg.parsed_msg['<username>'].lower()
    getcode = await get_profile_name(code)
    if getcode:
        bind = CytoidBindInfoManager(msg).set_bind_info(username=getcode[0])
        if bind:
            if getcode[1]:
                m = f'{getcode[1]}({getcode[0]})'
            else:
                m = getcode[0]
            await msg.finish(msg.locale.t('cytoid.message.bind.success') + m)
    else:
        await msg.finish(msg.locale.t('cytoid.message.bind.failed'))


@cytoid.handle('unbind {{cytoid.help.unbind}}')
async def _(msg: Bot.MessageSession):
    unbind = CytoidBindInfoManager(msg).remove_bind_info()
    if unbind:
        await msg.finish(msg.locale.t('cytoid.message.unbind.success'))
