import random
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import (
    Bot,
    Message,
    MessageSegment,
)
from nonebot.permission import SUPERUSER
from .datasource import creat_eat_json
from nonebot_plugin_htmlrender import (
    md_to_pic
)
import io
from PIL import Image
from fuzzywuzzy import fuzz

eat_list = creat_eat_json()
eat = [k for k, v in eat_list.items()]

what_eat = on_command("今天吃什么", aliases={"今晚吃什么", "夜宵吃什么", "中午吃什么", "晚上吃什么", "午饭吃什么", "晚饭吃什么"}, priority=5)
how_to_cook = on_command("怎么做", priority=5)

@what_eat.handle()
async def _(bot: Bot, args: Message = CommandArg()):
    msg = f"建议吃 {random.choice(eat)}"
    await what_eat.finish(msg, at_sender=True)


@how_to_cook.handle()
async def _(bot: Bot, args: Message = CommandArg()):
    msg = args.extract_plain_text().strip()
    try:
        eat_list[msg]
        pic = await get_md_pic(msg)
        await how_to_cook.finish(MessageSegment.image(pic), at_sender=True)
    except KeyError:
        for k, v in eat_list.items():
            res = fuzz.ratio(msg, k)
            if res >= 85:
                pic = await get_md_pic(k)
                await how_to_cook.finish(MessageSegment.image(pic), at_sender=True)
            else:
                continue
        msg = f"不会做{msg}呢~"
        await how_to_cook.finish(msg, at_sender=True)
        
async def get_md_pic(name):
    data = eat_list[name]
    data_type = data['type']
    if data_type == 'dir':
        pic = await md_to_pic(md_path=data['path'] + "\\" + data['name'])

    else:
        pic = await md_to_pic(md_path=data['path'])

    a = Image.open(io.BytesIO(pic))
    a.save("md2pic.png", format="PNG")
    return pic

