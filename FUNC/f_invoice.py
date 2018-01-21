# import functionality
from FUNC.f_db import f_db

class f_invoice:
    db = f_db()

    # invoice for user handler
    def get_invoices(self, userid):
        return self.db.getinvoices(userid)

    # get specific inovice handler
    def get_invoce(self, invoiceid):
        return self.db.getinvoice(invoiceid)

    # add new invoice handler
    def add_invoce(self, userid, itemlist, summaryprice, ownerid, photolist):
        return str(self.db.addinvoice(userid, itemlist, summaryprice, ownerid, photolist))

    # get invoices for
    def get_retlated_invoices(self, userid):
        return self.db.getrelatedinvoces(userid)