from core.builtins import Url, Bot
from core.dirty_check import check
from modules.wiki.utils.time import strptime2ts
from modules.wiki.utils.wikilib import WikiLib


async def rc(msg: Bot.MessageSession, wiki_url):
    wiki = WikiLib(wiki_url)
    query = await wiki.get_json(action='query', list='recentchanges',
                                rcprop='title|user|timestamp|loginfo|comment|sizes',
                                rclimit=10,
                                rctype='edit|new|log',
                                _no_login=not msg.options.get("use_bot_account", False))
    pageurl = wiki.wiki_info.articlepath.replace('$1', 'Special:RecentChanges')
    d = []
    for x in query['query']['recentchanges']:
        if 'title' in x:
            if x['type'] in ['edit', 'new']:
                count = x['newlen'] - x['oldlen']
                if count > 0:
                    count = f'+{str(count)}'
                else:
                    count = str(count)
                d.append(
                    f"•{msg.ts2strftime(strptime2ts(x['timestamp']), iso=True, timezone=False)} - {x['title']} .. ({count}) .. {x['user']}")
                if x['comment']:
                    comment = msg.locale.t('message.brackets', msg=x['comment'])
                    d.append(comment)
            if x['type'] == 'log':
                if x['logtype'] == x['logaction'] or x['logaction'] == '*':
                    log = msg.locale.t(f"wiki.message.rc.action.{x['logtype']}", user=user, title=title)
                else:
                    log = msg.locale.t(f"wiki.message.rc.action.{x['logtype']}.{x['logaction']}", user=user, title=title)
                if log.find("{") != -1 and log.find("}") != -1:
                    log = f"{user} {x['logtype']} {x['logaction']} {title}"
                d.append(f"•{msg.ts2strftime(strptime2ts(x['timestamp']), iso=True, timezone=False)} - {log}")
                params = x['logparams']
                if 'suppressredirect' in params:
                    d.append(msg.locale.t('wiki.message.rc.params.suppress_redirect'))
                if 'duration' in params:
                    d.append(msg.locale.t('wiki.message.rc.params.duration') + params['duration'])
                if 'flags' in params:
                    d.append(', '.join(params['flags']))
                if 'tag' in params:
                    d.append(msg.locale.t('wiki.message.rc.params.tag') + params['tag'])
                if 'target_title' in params:
                    d.append(msg.locale.t('wiki.message.rc.params.target_title') + params['target_title'])
                if x['comment']:
                    comment = msg.locale.t('message.brackets', msg=x['comment'])
                    d.append(comment)
    y = await check(*d)
    y = '\n'.join(z['content'] for z in y)
    if y.find("<吃掉了>") != -1 or y.find("<全部吃掉了>") != -1:
        y = y.replace("<吃掉了>", msg.locale.t("check.redacted"))
        y = y.replace("<全部吃掉了>", msg.locale.t("check.redacted.all"))
        return f'{str(Url(pageurl))}\n{y}\n{msg.locale.t("message.collapse", amount="10")}\n{msg.locale.t("wiki.message.utils.redacted")}'
    else:
        return f'{str(Url(pageurl))}\n{y}\n{msg.locale.t("message.collapse", amount="10")}'
