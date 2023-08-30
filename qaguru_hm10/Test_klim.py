from qaguru_hm10.Person import Person
from qaguru_hm10.Profession import Profession
from qaguru_hm10.Company import Company


developer = Profession(name="Developer", salary=7000)

cleaner = Profession(name="Cleaner", salary=100)

sasha = Person(name='Sasha', lastname="Ivolgin", profession=developer, stage=11)
vitya = Person(name='Vitya', lastname='Simonov', profession=cleaner, stage=3)

employers = [sasha, vitya]
workers = [developer, cleaner]

hostel = Company(workers)

kompas = Company(employers)


# hostel.print_workers_names()

kompas.print_workers_names()



#
# распечатать значения фонда оплаты труда
# функция которая поднимет зарплату всем на 10%