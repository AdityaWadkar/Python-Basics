from __future__ import print_function

# 1. Capitalize #
print('*'*10 + ' 1. Capitalize only First letter' + '*'*10)
my_str = input("Enter an string: ")
print(my_str.capitalize())
print('\n')

# 2. Lower #
print('*'*10 + ' 2. Lower ' + '*'*10)
my_str = input("Enter an string in Capital letters: ")
print(my_str.lower())
print('\n')

# 3. Upper #
print('*'*10 + ' 3. Upper ' + '*'*10)
my_str = input("Enter an string in small letters: ")
print(my_str.upper())
print('\n')

# 4. Is digit #
print('*'*10 + ' 4. Is digit ' + '*'*10)
my_str = input("Enter an string: ")
print(my_str.isdigit())
print('\n')
my_str = input("Enter an number: ")
print(my_str.isdigit())
print('\n')

# 5. Startswith #
print('*'*10 + ' 5. Startswith ' + '*'*10)
ip_addr = input("Enter an IP address: ")
print(ip_addr.startswith( '192' ))
print('\n')
ip_addr = input("Enter an IP address stratswith 192. : ")
print(ip_addr.startswith( '192' ))
print('\n')
