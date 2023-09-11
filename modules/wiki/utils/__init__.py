import traceback

from core.builtins import Bot
from core.component import module
from modules.wiki.utils.dbutils import WikiTargetInfo, Audit
from modules.wiki.utils.wikilib import WikiLib, WhatAreUDoingError, PageInfo, InvalidWikiError, QueryInfo
from .ab import ab
from .ab_qq import ab_qq
from .newbie import newbie
from .rc import rc
from .rc_qq import rc_qq

rc_ = module('rc', desc='{wiki.help.rc.desc}', developers=['OasisAkari'])


@rc_.handle()
async def rc_loader(msg: Bot.MessageSession):
    start_wiki = WikiTargetInfo(msg).get_start_wiki()
    if start_wiki is None:
        return await msg.finish(msg.locale.t('wiki.message.not_set'))
    legacy = True
    if msg.Feature.forward and msg.target.target_from == 'QQ|Group':
        try:
            nodelist = await rc_qq(start_wiki)
            await msg.fake_forward_msg(nodelist)
            legacy = False
        except Exception:
            traceback.print_exc()
            await msg.send_message(msg.locale.t('wiki.message.rollback'))
            legacy = True
    if legacy:
        res = await rc(msg, start_wiki)
        await msg.finish(res)


a = module('ab', desc='{wiki.help.ab.desc}', developers=['OasisAkari'])


@a.handle()
async def ab_loader(msg: Bot.MessageSession):
    start_wiki = WikiTargetInfo(msg).get_start_wiki()
    if start_wiki is None:
        return await msg.finish(msg.locale.t('wiki.message.not_set'))
    legacy = True
    if msg.Feature.forward and msg.target.target_from == 'QQ|Group':
        try:
            nodelist = await ab_qq(start_wiki)
            await msg.fake_forward_msg(nodelist)
            legacy = False
        except Exception:
            traceback.print_exc()
            await msg.send_message(msg.locale.t('wiki.message.rollback'))
            legacy = True
    if legacy:
        res = await ab(msg, start_wiki)
        await msg.finish(res)


n = module('newbie', desc='{wiki.help.newbie.desc}', developers=['OasisAkari'])


@n.handle()
async def newbie_loader(msg: Bot.MessageSession):
    start_wiki = WikiTargetInfo(msg).get_start_wiki()
    if start_wiki is None:
        return await msg.finish(msg.locale.t('wiki.message.not_set'))
    res = await newbie(msg, start_wiki)
    await msg.finish(res)
