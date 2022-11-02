import os

if __name__ == '__main__':
    print('######DJANGO TESTS######')
    os.system('python3 test/run_django_tests.py')
    print('######            ######')
    print('######OTHER TESTS######')
    os.system('python3 -m unittest')
    print('######            ######')