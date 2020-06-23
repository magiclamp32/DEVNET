#Read in the device informationfile = open('dev-01-info',')
file = open('/Users/lam/Documents/GitHub/DEVNET/PRNE/dev-01-info.txt','r')
# Read in the device information one line at a time
name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

# print out the information
print('device name: ',name)
print ('ip address: ',ip_address)
print ('OS type: ',os_type)
print ('username: ',username)
print ('password: ',password)

