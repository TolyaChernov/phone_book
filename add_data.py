from sqlalchemy.orm import sessionmaker
from models import *

# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Создаем объекты моделей
data_0 = User(name='John@emaol.com')
data_1 = Government(government='John@emaol.com')
data_2 = Department(department='John@emaol.com')
data_3 = Phone(phone='John@emaol.com')
data_4 = Email(email='John@emaol.com')

data_1.users.append(data_0)
data_2.users.append(data_0)
data_3.users.append(data_0)
data_4.users.append(data_0)

# Добавляем объекты в сессию
session.add(data_1)
session.add(data_2)
session.add(data_3)
session.add(data_4)

# Сохраняем изменения в базе данных
session.commit()