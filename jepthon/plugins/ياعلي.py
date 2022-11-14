from jepthon import jepiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import asyncio
from ..core.managers import edit_delete, edit_or_reply

@jepiq.ar_cmd(pattern="اشتراك")
async def reda(event):
    ty = event.text
    ty = ty.replace(".اشتراك", "")
    ty = ty.replace(" ", "")
    if len (ty) < 2:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري كروب او خاص**")
    if ty == "كروب":
        if not event.is_group:
            return await edit_delete("**استعمل الأمر في الجروب المراد تفعيل الاشتراك الاجباري به**")
        if event.is_group:
            if gvarstatus ("subgroup") == event.chat_id:
                return await edit_delete(event, "**الاشتراك الاجباري مفعل لهذا الكروب**")
            if gvarstatus("subgroup"):
                return await edit_or_reply(event, "**الاشتراك الاجباري مفعل لكروب اخر قم بالغائه لتفعيله في كروب اخر**")
            addgvar("subgroup", f"{event.chat_id}")
            return await edit_or_reply(event, "**تم تفعيل الاشتراك الاجباري لهذه المجموعة**")
    if ty == "خاص":
        if gvarstatus ("subprivate"):
            return await edit_delete(event, "**الاشتراك الاجباري للخاص مفعل**")
        if not gvarstatus ("subprivate"):
            addgvar ("subprivate", True)
            await edit_or_reply(event, "**تم تفعيل الاشتراك الاجباري للخاص**")
    if ty not in ["خاص", "كروب"]:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري كروب او خاص**")
@jepiq.ar_cmd(pattern="ايقاف")
async def reda (event):
    cc = event.text.replace(".الغاء", "")
    cc = cc.replace(" ", "")
    if len (cc) < 2:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري لإلغائه**")
    if cc == "كروب":
        if not gvarstatus ("subgroup"):
            return await edit_delete("**لم تفعل الاشتراك الاجباري للكروب لإلغائه**")
        if gvarstatus ("subgroup"):
            delgvar ("subgroup")
            return await edit_delete(event, "**تم الغاء الاشتراك الاجباري للكروب بنجاح**")
    if cc == "خاص":
        if not gvarstatus ("subprivate"):
            return await edit_delete(event, "** الاشتراك الاجباري للخاص غير مفعل لإلغائه **")
        if gvarstatus ("subprivate"):
            delgvar ("subprivate")
            return await edit_delete(event, "**تم إلغاء الاشتراك الاجباري للخاص**")
    if cc not in ["خاص", "كروب"]:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري لإلغائه**")

@jepiq.ar_cmd(incoming=True)
async def reda(event):
    if gvarstatus ("subprivate"):
        if event.is_private:
            await jepiq.send_message(event.chat_id, "**شبيك يغبي**")
