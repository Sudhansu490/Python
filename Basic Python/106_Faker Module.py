# sometimes we have required fake data for database testing purpose.faker module gives more realstic fake data.
# In faker module we have to import Faker() class.If we have to use Faker class then first we create the object of Faker() class.
from faker import Faker
# object creation
fk=Faker()

# print(fk.name())
# print(fk.email())
# print(fk.address())
# print(fk.country())
# print(fk.first_name())
# print(fk.last_name())
# print(fk.url())
# print(fk.text())
# print(fk.am_pm())
# print(fk.boolean())
# print(fk.credit_card_number())
# print(fk.color())
# print(fk.color_name())
# print(fk.company())
# print(fk.company_email())
# print(fk.cryptocurrency())
# print(fk.currency())
# print(fk.date())
# print(fk.file_extension())
# print(fk.date_of_birth())
# print(fk.domain_name())
# print(fk.zipcode())
# print(fk.csv())  # CSV=Comma Separated Value
# print(fk.json())   # dictionary type of data
# print(fk.ipv4_private())  # Generate IP Address
# print(fk.language_name())
# print(fk.month_name())
# print(fk.password())
# print(fk.random_letters())
# print(fk.profile())  # here everytime job is changing

# to show same output for multiple times we have to use seed function
# Faker.seed(1)
# print(fk.profile())

# to generate the things in Hindi Language
# fk=Faker('hi-IN')
# print(fk.name())
# print(fk.address())

# We can also use other languages of different countries.
# fk=Faker('it-IT')  # Generate Italian Names
# print(fk.name())