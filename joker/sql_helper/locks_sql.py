from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

jpvois1 = "joker/helpers/styles/Voic/تخوني ؟.ogg"
jpvois2 = "joker/helpers/styles/Voic/مستمرة الكلاوات.ogg"
jpvois3 = "joker/helpers/styles/Voic/احب العراق.ogg"
jpvois4 = "joker/helpers/styles/Voic/احبك .ogg"
jpvois5 = "joker/helpers/styles/Voic/اخت التنيج.ogg"
jpvois6 = "joker/helpers/styles/Voic/اذا اكمشك ماكو.ogg"
jpvois7 = "joker/helpers/styles/Voic/اسكت.ogg"
jpvois8 = "joker/helpers/styles/Voic/افتهمنا.ogg"
jpvois9 = "joker/helpers/styles/Voic/اكل خرة لك.ogg"
jpvois10 = "joker/helpers/styles/Voic/الة اخلي العراق امريكا.ogg"
jpvois11 = "joker/helpers/styles/Voic/الكعدة وياكم حلوة.ogg"
jpvois12 = "joker/helpers/styles/Voic/الكمر اني النجم اني.ogg"
jpvois13 = "joker/helpers/styles/Voic/اللهم لا شماتة.ogg"
jpvois14 = "joker/helpers/styles/Voic/انا ما اكدر بعد.ogg"
jpvois15 = "joker/helpers/styles/Voic/بقولك اي يا قلبي كسمك.ogg"
jpvois16 = "joker/helpers/styles/Voic/تف على شرفك.ogg"
jpvois17 = "joker/helpers/styles/Voic/شجلبت.ogg"
jpvois18 = "joker/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
jpvois19 = "joker/helpers/styles/Voic/صباح القنادر.ogg"
jpvois20 = "joker/helpers/styles/Voic/ضحكة فيطية.ogg"
jpvois21 = "joker/helpers/styles/Voic/طار القلب.ogg"
jpvois22 = "joker/helpers/styles/Voic/غطيلي واغطيلك.ogg"
jpvois23 = "joker/helpers/styles/Voic/في منتصف الجبهة.ogg"
jpvois24 = "joker/helpers/styles/Voic/لا تقتل المتعة .ogg"
jpvois25 = "joker/helpers/styles/Voic/لا لتغلط.ogg"
jpvois26 = "joker/helpers/styles/Voic/لا يمه لا محاجي.ogg"
jpvois27 = "joker/helpers/styles/Voic/لحد يحجي وياي.ogg"
jpvois28 = "joker/helpers/styles/Voic/ما ادري يعني.ogg"
jpvois29 = "joker/helpers/styles/Voic/منو انت لخاطر النجف.ogg"
jpvois30 = "joker/helpers/styles/Voic/مو صوجكم يا زبايل.ogg"
jpvois31 = "joker/helpers/styles/Voic/والله انت خوش تسولف.ogg"
jpvois32 = "joker/helpers/styles/Voic/يعععع.ogg"
jpvois33 = "joker/helpers/styles/Voic/زيج.ogg"
jpvois34 = "joker/helpers/styles/Voic/زيح2.ogg"
jpvois35 = "joker/helpers/styles/Voic/يعني مااعرف.ogg"
jpvois36 = "joker/helpers/styles/Voic/يامرحبا.ogg"
jpvois37 = "joker/helpers/styles/Voic/منو انتة.ogg"
jpvois38 = "joker/helpers/styles/Voic/ماتستحي.ogg"
jpvois39 = "joker/helpers/styles/Voic/كعدت الديوث.ogg"
jpvois40 = "joker/helpers/styles/Voic/عيب.ogg"
jpvois41 = "joker/helpers/styles/Voic/عنعانم.ogg"
jpvois42 = "joker/helpers/styles/Voic/طبك مرض.ogg"
jpvois43 = "joker/helpers/styles/Voic/سييي.ogg"
jpvois44 = "joker/helpers/styles/Voic/سبيدر مان.ogg"
jpvois45 = "joker/helpers/styles/Voic/خاف حرام.ogg"
jpvois46 = "joker/helpers/styles/Voic/تحيه لاختك.ogg"
jpvois47 = "joker/helpers/styles/Voic/امشي كحبة.ogg"
jpvois48 = "joker/helpers/styles/Voic/امداك.ogg"
jpvois49 = "joker/helpers/styles/Voic/الحس.ogg"
jpvois50 = "joker/helpers/styles/Voic/افتهمنا.ogg"
jpvois51 = "joker/helpers/styles/Voic/اطلع برا.ogg"
jpvois52 = "joker/helpers/styles/Voic/اخت التنيج.ogg"
jpvois53 = "joker/helpers/styles/Voic/اوني تشان.ogg"
jpvois54 = "joker/helpers/styles/Voic/اوني تشان2.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
