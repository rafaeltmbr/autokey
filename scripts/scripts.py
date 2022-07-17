from subprocess import check_call


def start():
    cmd = 'python3 -m autokey.autokey sample/motivacao.txt -m 3 -i 2'
    check_call(cmd.split(' '))
