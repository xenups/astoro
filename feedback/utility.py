from datetime import datetime

import jdatetime


class DateConvert:
    @staticmethod
    def jalali_to_georgian(jalali_date):
        date_time_obj = datetime.strptime(jalali_date, '%Y-%m-%d').date()
        converted_time = jdatetime.date.togregorian(date_time_obj)
        return str(converted_time)

    @staticmethod
    def georgian_to_jalali(georgian_date):
        date_time_obj = datetime.strptime(georgian_date, '%Y-%m-%d').date()
        converted_time = jdatetime.date.fromgregorian(date=date_time_obj)
        return str(converted_time)
