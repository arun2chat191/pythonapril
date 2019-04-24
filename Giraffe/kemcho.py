import re
print(re.sub('[ad]','*','abcde,abcdef,abcedf'))

print(re.sub('[abc]','*','abcdef,abcdef'))
