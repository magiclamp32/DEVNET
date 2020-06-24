userinput = input('Type your line : ')
newfile = open('/Users/lam/Documents/GitHub/DEVNET/PRNE/newfile','r+')
# newfile.writelines(userinput)
#for printout in newfile:
#    print(printout)
# userinput = input('Type your line: ')
print(userinput, newfile)
# for printout in newfile:
#    print(printout)

newfile.close()