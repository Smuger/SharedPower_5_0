from Controllers.DataBase import DataBaseController
from Controllers.Rental import RentalController

from time import mktime
from datetime import datetime


class ToolController():
    tool_list = []
    rental = RentalController()

    # list all tools of user
    def list_all(self, userid):
        db = DataBaseController()

        return db.gettool("userid", userid)

    # search by type
    def search_by_type(self, typeof):
        db = DataBaseController()
        return db.gettool("typeof", typeof)

    # search by name
    def search_by_name(self, name):
        db = DataBaseController()
        return db.gettool("name", name)

    # add tool
    def add_tool(self, userid, name, price, type, photolist, condition, description, deliveryprices):
        db = DataBaseController()
        db.createtool(userid, name, price, type, photolist, condition, description, deliveryprices)

    # get details of tool by id
    def gettoolbyid(self, toolid):
        db = DataBaseController()
        self.tool_list = db.gettool("id", toolid)
        # return simngle object
        return self.tool_list[0]
