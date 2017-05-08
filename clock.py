from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import smtplib

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print('This job is run every hour.')
    r = request.get('https://in.bookmyshow.com/buytickets/cinepolis-manjeera-mall-hyderabad/cinema-hyd-CPMH-MT/20170512')
    if r.url != 'https://in.bookmyshow.com/buytickets/cinepolis-manjeera-mall-hyderabad/cinema-hyd-CPMH-MT/20170512':
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('testinguser2495@gmail.com', '24952495')
        server.sendmail('Chandan Singh', 'chandan2495@gmail.com', 'Tickets Available in cinepolis for friday')
        # server.sendmail('Chandan Singh', 'anchitnema12@gmail.com', 'Tickets Available in cinepolis for friday')

sched.start()
