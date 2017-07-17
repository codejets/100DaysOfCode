import datetime
import os

LOG = 'README.md'
DAY_ZERO = datetime.datetime(2017, 7, 18)
NUM_DAYS = 100
NUM_WIDTH = 3
TABLE_HEADER = '''## Progress Log

| Day | Date | Created | Task |
| --- | --- | --- | --- |
'''
LOG_HEADER = '''
# #100DaysOfCode Challenge
'''
DAY = '| {0} | {1} | [LINK]({0}) | Task Description |\n'


def gen_days():
    '''Generate day range 001...100'''
    for day in range(1, NUM_DAYS + 1):
        yield str(day).zfill(NUM_WIDTH)


def get_date(day):
    '''Get date by offsetting nth day from day 0'''
    date = DAY_ZERO + datetime.timedelta(int(day))
    return date.strftime('%b %d, %Y')


def create_log():
    '''Create progress log file with markdown table '''
    with open(LOG, 'w') as f:
        f.write(LOG_HEADER)
        f.write(TABLE_HEADER)
        for d in gen_days():
            date = get_date(d)
            f.write(DAY.format(d, date))


if __name__ == '__main__':
    if os.path.isfile(LOG):
        print('Logfile already created')
    else:
        print('Creating logfile')
        create_log()

    # dirs = [d for d in gen_days() if not os.path.isdir(d)]
    # if not dirs:
    #     print('All 100 days directories already created')
    # else:
    #     print('Creating missing day directories')
    #     for d in dirs:
    #         os.makedirs(d)
