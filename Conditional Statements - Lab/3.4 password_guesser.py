DB_PASSWORD_ID_USER = 's3cr3t!P@ssw0rd'

password = input()

if password == DB_PASSWORD_ID_USER:
    print('Welcome')
else:
    print('Wrong password!')