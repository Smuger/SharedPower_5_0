# import functionality
from FUNC.f_db import f_db
from FUNC.f_rental import f_rental

class f_products():
    tool_list = []
    rental = f_rental()

    # list all tools of a user handler
    def list_all(self, userid):
        db = f_db()
        return db.gettool("userid", userid)

    # search by type of a product handler
    def search_by_type(self, typeof):
        db = f_db()
        return db.gettool("typeof", typeof)

    # search by product name handler
    def search_by_name(self, name):
        db = f_db()
        return db.gettool("name", name)

    # add product handler
    def add_tool(self, userid, name, price, type, photolist, condition, description, deliveryprices):
        db = f_db()
        db.createtool(userid, name, price, type, photolist, condition, description, deliveryprices)

    # pass tool by id handler
    def gettoolbyid(self, toolid):
        db = f_db()
        self.tool_list = db.gettool("id", toolid)
        # return simngle object
        return self.tool_list[0]
