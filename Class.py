class OccupationalHealthandEngineering:
       count = 0
       def __init__(self, name, sex, city, gdp):
              self.nameandSurname = name
              self.sex = sex
              self.city = city
              self.gdp = gdp
              OccupationalHealthandEngineering.count += 1
       
       def get_name(self):
              print(f'The name and surname is {self.nameandSurname}')
       
       def get_sex(self):
              print(f'Sex is {self.sex}')
       
       def get_city(self):
              print(f'The city {self.nameandSurname} lives is: {self.city}')
       
       def get_gdp(self):
              print(f'And the gdp is: {self.gdp}')

       def get_info(self):
              print('Full student informations')
              yield self.nameandSurname
              yield self.sex
              yield self.city
              yield self.gdp
              # we can use another simple way like below but personally i like yield function.
              # print(f'Full info\nname: {self.nameandSurname}\nsex: {self.sex}\ncity: {self.city}\ngdp: {self.gdp}')

       def get_count(self):
              return(OccupationalHealthandEngineering.count)


arash = OccupationalHealthandEngineering('Arash Hatami', 'Male', 'Shiraz', '17.51')
meisam = OccupationalHealthandEngineering('Meisam Karimi', 'Male', 'Tehran', '15.91')
mina = OccupationalHealthandEngineering('Mina Amiri', 'Female', 'Abadan', '17.91')
sepideh = OccupationalHealthandEngineering('Sepideh Zanjani', 'Female', 'Semnan', '16.91')
names = [arash, meisam, mina, sepideh]

# make 2 for loops to reach the info of all students just by adding names not name.get_info() separately.
counter = 0
for name in names:
       name.get_info()
       counter += 1
       print('-------------------------------------------')
       print(f'Number {counter}')
       for info in name.get_info():
              print(info)


print('-------------------------------------------')
# get the numbers of the students 2 ways, first one from class(line 8) and the other one from object(line 41).
print(f'Number of students is {OccupationalHealthandEngineering.count}')
# print(f'Number of students is {counter}')
