import subprocess

if __name__ == '__main__':
    print('######DJANGO TESTS######')
    subprocess.call(['python', 'test/run_django_tests.py'])
    print('######            ######')
    print('######OTHER TESTS######')
    subprocess.call(['python', '-m', 'unittest'])
    print('######            ######')