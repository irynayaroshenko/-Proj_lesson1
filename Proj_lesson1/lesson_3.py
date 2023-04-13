a = 'hello'
a = 'H' + a[1:]
print(a)
if a.isprintable():
    print('yes')

# Different options for str formatting
name = 'Ira'
print('Hello, %s! Nice to meet you.' % name)
print(f'Hello, {name}! Nice to meet you.')
print('Hello, {0}! Nice to meet you.'.format(name))
print('Hello, {name}! Nice to meet you.'.format(name=name))
print('Hello, ' + name + '! Nice to meer you.')
