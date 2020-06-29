import pexpect
ip_address = '10.11.99.47'
username = 'emergency-acct'
password = 'password'
session = pexpect.spawn('telnet ' + ip_address, timeout = 20)
result = session.expect(['Username:', pexpect.TIMEOUT])
if result != 0:
    print '---- FAILURE!  creating session for: ', ip_address
    exit()
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])
