import time

from FUNC.f_db import f_db


class f_invoice:
    db = f_db()

    # get invoices
    def get_invoices(self, userid):
        return self.db.getinvoices(userid)

    # get details of invoice
    def get_invoce(self, invoiceid):
        return self.db.getinvoice(invoiceid)

    # add invoice
    def add_invoce(self, userid, itemlist, summaryprice, ownerid, photolist):
        return str(self.db.addinvoice(userid, itemlist, summaryprice, ownerid, photolist))

    # get invoice of owner of tool
    def get_retlated_invoices(self, userid):
        return self.db.getrelatedinvoces(userid)