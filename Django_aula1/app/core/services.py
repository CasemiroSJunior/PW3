import requests
import datetime

def verifyHoliday(holiday, fakedate=None):
    response = False
    dado = requests.get(f'https://api.invertexto.com/v1/holidays/{datetime.date.today().year}?token=18656|xbl7c8uQE3A0ScfNydAx86ciAe4sEovF')
    searched_holiday={}
    for data in dado.json():
        if data['name'] == holiday:
            searched_holiday = data

    if searched_holiday['name'] == holiday:
        if fakedate is None:
            fakedate = datetime.date.today().strftime('%Y-%m-%d')
        else:
            fakedate = fakedate
        if searched_holiday['date'] == fakedate:
            response = True
    return response