import traceback
from datetime import datetime, timezone

from config import Config
from core.builtins import Plain
from core.logger import Logger
from core.queue import JobQueue
from core.scheduler import Scheduler, IntervalTrigger
from core.utils.html2text import html2text
from core.utils.http import get_url

identifys = []
headers = {'cookie': 'csrf_token=woshixiaoke', 'x-csrf-token': 'woshixiaoke'}


@Scheduler.scheduled_job(IntervalTrigger(seconds=60 if not Config('slower_schedule') else 180))
async def check_crowdin():
    first = not identifys
    url = f"https://crowdin.com/backend/project_actions/activity_stream?date_from=&date_to=&user_id=0&project_id=3579&language_id=0&type=0&translation_id=0&after_build=0&before_build=0&request=1"
    try:
        get_json: dict = await get_url(url, 200, attempt=1, headers=headers,
                                       fmt='json')
        Logger.info(get_json)
        if get_json:
            if 'error' in get_json:
                raise Exception(get_json['msg'])
            for act in get_json['activity']:
                m = html2text(act["message"])
                if act['count'] == 1:
                    identify = f'{act["user_id"]}{str(act['timestamp'])}{m}'
                    if not first and identify not in identifys:
                        await JobQueue.trigger_hook_all('mc_crowdin', message=[Plain(m).to_dict()])
                    identifys.append(identify)
                else:
                    detail_url = f"https://crowdin.com/backend/project_actions/activity_stream_details?request_type=project&type={
                        act["type"]}&timestamp={
                        act["timestamp"]}&offset=0&user_id={
                        act["user_id"]}&project_id={
                        act["project_id"]}&language_id=0&after_build=0&before_build=0"
                    get_detail_json: dict = await get_url(detail_url, 200, attempt=1, headers=headers,
                                                          fmt='json')
                    if get_detail_json:
                        for detail_num in get_detail_json['activity']:
                            identify_ = []
                            for detail in get_detail_json['activity'][detail_num]:
                                identify = f'{detail["title"]}: {html2text(detail["content"])}'
                                identify_.append(identify)
                            identify = "\n".join(identify_)
                            if not first and identify not in identifys:
                                await JobQueue.trigger_hook_all('mc_crowdin', message=[Plain(m + '\n' + identify).to_dict()])
                            identifys.append(identify)
    except Exception:
        if Config('debug'):
            Logger.error(traceback.format_exc())