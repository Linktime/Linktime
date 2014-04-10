# -*- coding:utf-8 -*-
import StringIO
import qrcode
from activity.models import ActivityTicket
import base64

def get_qrcode(activity_ticket):
    owner = activity_ticket.owner
    type = activity_ticket.type
    activity = type.activity

    base_str = base64.b64encode(("%s|%s|%s"%(owner.username,activity.name,type.type)).encode("utf-8"))
    encode = "begin{%s}end\n"%base_str
    encode = encode + u"拥有者:%s,活动名:%s,票类型:%s"%(owner.username,activity.name,type.type)

    q = qrcode.main.QRCode()

    q.add_data(encode)

    q.make()
    i = q.make_image()
    f = StringIO.StringIO()
    i.save(f)
    f.seek(0)
    img = f.read()
    f.close()
    return img