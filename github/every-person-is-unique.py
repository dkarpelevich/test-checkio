from datetime import datetime


class Person:
    today_date = [2018, 1, 1]

    def __init__(self,
                 first_name,
                 last_name,
                 birth_date,
                 job,
                 working_years: float,
                 salary,
                 country,
                 city,
                 gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        birth_date = self.birth_date.split('.')
        age = datetime(Person.today_date[0], Person.today_date[1], Person.today_date[2]) - \
            datetime(int(birth_date[2]), int(birth_date[1]), int(birth_date[0]))
        return age.days // 365

    def work(self):
        if self.gender == 'male':
            return 'He is a {}'.format(self.job)
        elif self.gender == 'female':
            return 'She is a {}'.format(self.job)
        else:
            return 'Is a {}'.format(self.job)

    def money(self):
        salary = round(self.working_years * self.salary * 12)
        return '{:,}'.format(salary).replace(',', ' ')

    def home(self):
        return 'Lives in {}, {}'.format(self.city, self.country)


if __name__ == '__main__':
    person1 = Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
    print(person1.age())
