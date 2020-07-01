import os
import pexpect

currentdir = pexpect.spawn(pwd)
result = currentdir.expect(expect.EOF)
currentdir_output = currentdir.before
print(currentdir_output)

icmp = pexpect.spawn('ping -c 5 www.yahoo.com')
result = icmp.expect(pexpect.EOF)
icmp_output = icmp.before
print(icmp_output)
