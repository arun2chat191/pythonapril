def hello_func(greeting,name='You'):
    return '{},{}'.format(greeting,name)

#print(hello_func('Hi',name='corey'))

def student_info(*args,**kwargs):

    print(args)
    print(kwargs)
student_info('Math',name='John',age=22)