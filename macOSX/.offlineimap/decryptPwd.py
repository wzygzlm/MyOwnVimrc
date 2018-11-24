import subprocess

def mailpasswd(account):
    path = "/Users/liumin/.mail-%s-passwd.gpg" % account
    return subprocess.check_output(["gpg", "--quiet", "--batch", "-d", path]).strip()
