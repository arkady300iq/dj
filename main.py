import setup

from myapp.models import Role, User

admin_role = Role.objects.create(name="admin")
user_role = Role.objects.create(name="user")


'''
user1 = User.objects.create(name = "Ivan", email = "ivan@gmail.com", role = admin_role)
user2 = User.objects.create(name = "Max",email = "max@gmai.com", role = user_role)
user3 = User.objects.create(name = "Igor", email = "igor@gmail.com", role = admin_role)
'''
#Добавил вывод информации про пользователей
'''
users = User.objects.all()
for user in users:
    print (f"Name:{user.name}, Email: {user.email}, Role: {user.role}")
'''
#Добавил обновление информации про пользователя
'''users_to_update = User.objects.get(id=13)а
users_to_update.name = "Arkady"
users_to_update.email = "arkady@gmail.com"
users_to_update.role = user_role
users_to_update.save()
'''

#Добавил добавление нового юзера
new_name = input("Введіть ім'я нового користувача: ")
new_email = input("Введіть електронну пошту нового користувача: ")
    
print("Список доступних ролей:")
roles = Role.objects.all()
for role in roles:
    print(f"{role.id}: {role.name}")
    
role_id = input("Введіть роль нового користувача: ")
role = Role.objects.get(pk=role_id)

new_user = User.objects.create(name=new_name, email=new_email, role=role)
print(f"Створено нового користувача: {new_user}")


'''not_need = User.objects.get(id=11)
not_need.delete()'''