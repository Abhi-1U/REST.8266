import gc

def localtime():
    try:
        timezone_hour = 5
        timezone_min = 30
        days= {
            0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday",
            5:"Saturday",
            6:"Sunday"
        }
        months = {
            1:"January",
            2:"February",
            3:"March",
            4:"April",
            5:"May",
            6:"June",
            7:"July",
            8:"August",
            9:"September",
            10:"October",
            11:"November",
            12:"December"
        }
        import utime
        local_time_sec = utime.time() + timezone_hour * 3600+ timezone_min *60
        (year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime(local_time_sec)
        directory={'Year':year,'Month':months[month],'Day Of Month':mday,'Hour':hour,'Minute':minute,'Second':second,'WeekDay':days[weekday],'Year-Day':yearday,'TimeZone':'+5:30'}
        return directory
    except OSError as OSE:
        return {path:None}
    except Exception as e:
        print(e)
    finally:
        gc.collect()
