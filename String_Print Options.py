# Strings Examples #

from __future__ import print_function, unicode_literals

# 1 --- Repersentation of strings using  'single' and "Double" and ''' Triple ''' quotes #
my_str1 = 'whatever'
my_str2 = "something else"
my_str3 = '''This is a string
that spans
multiple lines
'''
print(f"{'*'*10} First Strings {'*'*10}")
print(my_str1)
print(f"{'*'*10} Second Strings {'*'*10}")
print(my_str2)
print(f"{'*'*10} Third Strings {'*'*10}")
print(my_str3)

# 2 --- Removing white spaces #
print(f"{'*'*10} 2. Removing white space {'*'*10}")
my_str = '      Whatever, somethings else\n\n\n'
print(my_str.strip())
print('\n')

# 3 --- Removing left side white spaces #
print(f"{'*'*10} 3. Removing white space on left {'*'*10}")
my_str = '      Whatever, somethings else\n\n'
print(my_str.lstrip())

# 4 --- Removing Right side white spaces #
print(f"{'*'*10} 4. Removing white space on Right {'*'*10}")
my_str = '      Whatever, somethings else\n\n'
print(my_str.rstrip())

# 5 --- Split #
print(f"{'*'*10} 5. Split 192.168.1.1 {'*'*10}")
ip_addr = '192.168.1.1'
print(ip_addr.split("."))
print('\n')

# 6 --- Split White space #
print(f"{'*'*10} 6. Split White space {'*'*10}")
sentence - 'This is some sentence with a bunch words in it'
print(sentence.split())
print('\n')
