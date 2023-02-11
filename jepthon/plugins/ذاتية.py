from jepthon import jepiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
from jepthon import *

@jepiq.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية|حفظ)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    lMl10l = await event.get_reply_message()
    pic = await lMl10l.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @Jepthon
- Dev: @lMl10l
  """,
    )
    await event.delete()

@jepiq.on(admin_cmd(pattern="الذاتية تشغيل"))
async def reda(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "**حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "reda")
        await edit_delete(event, "**تم تفعيل حفظ الذاتيات بنجاح**")
 
@jepiq.on(admin_cmd(pattern="الذاتية تعطيل"))
async def Reda_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**تم تعطيل حفظت الذاتيات بنجاح**")
    else:
        await edit_delete(event, "**انت لم تفعل حفظ الذاتيات لتعطيلها !**")


@jepiq.ar_cmd(incoming=True)
async def reda(event):
    if gvarstatus ("savepicforme"):
        if event.is_private:
            if event.media and event.media_unread:
                pic = await event.download_media()
                await bot.send_file(
                "me",
                pic,
                caption=f"""
                - تـم حفظ الصـورة بنجـاح ✓ 
                - غير مبري الذمه اذا استخدمت الامر للابتزاز
                - CH: @Jepthon
                - Dev: @rd0r0
                """,
                )
                os.remove(pic)
