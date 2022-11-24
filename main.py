# Задание 4.1
# Используя подготовленную строку nat, получить новую строку, в которой в имени интерфейса вместо FastEthernet написано GigabitEthernet. Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.


nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat=nat.replace('FastEthernet', 'GigabitEthernet')
print(nat)

# Задание 4.2
# Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

mac = "AAAA:BBBB:CCCC"

mac=mac.replace(':', '.')
print(mac)
