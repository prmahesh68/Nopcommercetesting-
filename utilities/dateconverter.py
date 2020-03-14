import dateutils
import datetime
from datetime import date,datetime
import time
import dateutil.parser
class Date_spilt:

    def dateconverter(date1):
        date1 = str(date1)
        date1 = date1.split()[0]
        # date1= datetime.date(date1)
        # print (date1)
        # print (type(date1))
        return date1
    def dataconverter1(date2):
        return (date2.strftime('%m/%d/%Y'))







