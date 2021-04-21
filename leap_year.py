from loguru import logger


class LeapYear:
    def __init__(self, year, loggers):
        self.loggers = loggers
        self.year = year
        self.main()

    def main(self):
        self.loggers.info('Program started')
        self.check_div_by_4()
        self.loggers.info("Checked for the year's divisibility by 4.")
        self.check_div_by_100()
        self.loggers.info("Checked for the year's divisibility by 100")
        self.check_div_by_400()
        self.loggers.info("Checked for the year's divisibility by 400")
        self.check_leap_year()
        self.loggers.success('Program ended.')

    def check_div_by_4(self):
        if self.year % 4 == 0:
            return True
        else:
            return False

    def check_div_by_100(self):
        if self.year % 100 == 0:
            return True
        else:
            return False

    def check_div_by_400(self):
        if self.year % 400 == 0:
            return True
        else:
            return False

    def check_leap_year(self):
        div_by_4 = self.check_div_by_4()
        div_by_100 = self.check_div_by_100()
        div_by_400 = self.check_div_by_400()
        if div_by_4 and not div_by_100:
            print('leap')
            self.loggers.debug('The given year was clearly a leap year.')
        elif div_by_4 and div_by_100:
            self.loggers.info('The given year has reached the point of possibility of not being a leap year.')
            if div_by_400:
                print('leap')
                self.loggers.debug('After some checking it can be confirmed that the give year is a leap year.')
            else:
                print('not leap')
                self.loggers.debug('After some checking it can be confirmed that the give year is not a leap year.')
        else:
            print('not leap')
            self.loggers.debug('The given year is clearly not a leap year.')


if __name__ == '__main__':
    logger.add("my_log_file.log", rotation="10 MB")
    logs = logger
    var = True
    while var:
        year_to_check = int(input('Enter the year to check:\n'))
        leap_checker = LeapYear(year=year_to_check, loggers=logs)
