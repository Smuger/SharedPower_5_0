from FUNC.f_db import f_db
from FUNC.f_rental import f_rental

from time import mktime
from datetime import datetime


class f_products():
    tool_list = []
    rental = f_rental()

    # list all tools of user
    def list_all(self, userid):
        db = f_db()

        return db.gettool("userid", userid)

    # search by type
    def search_by_type(self, typeof):
        db = f_db()
        return db.gettool("typeof", typeof)

    # search by name
    def search_by_name(self, name):
        db = f_db()
        return db.gettool("name", name)

    # add tool
    def add_tool(self, userid, name, price, type, photolist, condition, description, deliveryprices):
        db = f_db()
        db.createtool(userid, name, price, type, photolist, condition, description, deliveryprices)

    # get details of tool by id
    def gettoolbyid(self, toolid):
        db = f_db()
        self.tool_list = db.gettool("id", toolid)
        # return simngle object
        return self.tool_list[0]
