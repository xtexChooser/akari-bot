import asyncio
import os
import sys
from datetime import datetime

import ujson as json

from core.builtins import Bot, PrivateAssets, ExecutionLockList, MessageTaskManager
from core.component import module
from core.logger import Logger
from core.utils.info import Info

upd = module('update', required_superuser=True, base=True)


@upd.command()
async def update_bot(msg: Bot.MessageSession):
    if True:
        ExecutionLockList.remove(msg)
        restart_time.append(datetime.now().timestamp())
        await wait_for_restart(msg)
        write_version_cache(msg)
        restart()

if Info.subprocess or True:
    rst = module('restart', required_superuser=True, base=True)

    def restart():
        sys.exit(233)

    def write_version_cache(msg: Bot.MessageSession):
        update = os.path.abspath(PrivateAssets.path + '/cache_restart_author')
        write_version = open(update, 'w')
        write_version.write(json.dumps({'From': msg.target.target_from, 'ID': msg.target.target_id}))
        write_version.close()

    restart_time = []

    async def wait_for_restart(msg: Bot.MessageSession):
        get = ExecutionLockList.get()
        if datetime.now().timestamp() - restart_time[0] < 60:
            if len(get) != 0:
                await msg.send_message(msg.locale.t("core.message.restart.wait", count=len(get)))
                await asyncio.sleep(10)
                return await wait_for_restart(msg)
            else:
                await msg.send_message(msg.locale.t("core.message.restart.restarting"))
                get_wait_list = MessageTaskManager.get()
                for x in get_wait_list:
                    for y in get_wait_list[x]:
                        for z in get_wait_list[x][y]:
                            if get_wait_list[x][y][z]['active']:
                                await z.send_message(z.locale.t("core.message.restart.prompt"))

        else:
            await msg.send_message(msg.locale.t("core.message.restart.timeout"))

    @rst.command()
    async def restart_bot(msg: Bot.MessageSession):
        if True:
            ExecutionLockList.remove(msg)
            restart_time.append(datetime.now().timestamp())
            await wait_for_restart(msg)
            write_version_cache(msg)
            restart()


if Info.subprocess or True:
    upds = module('update&restart', required_superuser=True, alias='u&r', base=True)

    @upds.command()
    async def update_and_restart_bot(msg: Bot.MessageSession):
        if True:
            ExecutionLockList.remove(msg)
            restart_time.append(datetime.now().timestamp())
            await wait_for_restart(msg)
            write_version_cache(msg)
            restart()


reexc = module('stop', required_superuser=True, base=True)


@reexc.command()
async def stop_bot(msg: Bot.MessageSession):
    if True:
        ExecutionLockList.remove(msg)
        restart_time.append(datetime.now().timestamp())
        await wait_for_restart(msg)
        write_version_cache(msg)
        sys.exit(234)


reexc = module('reexec', required_superuser=True, base=True)


@reexc.command()
async def reexec_bot(msg: Bot.MessageSession):
    if True:
        ExecutionLockList.remove(msg)
        restart_time.append(datetime.now().timestamp())
        await wait_for_restart(msg)
        write_version_cache(msg)
        sys.exit(235)
