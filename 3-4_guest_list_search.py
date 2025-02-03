guests = ['kurt cobain', 'nicola tesla', 'willem dafoe']

print("{}, you're formally invited to my dinner party.".format(guests[0]))

print("{}, you're formally invited to my dinner party.". format(guests[1]))

print("{}, you're formally invited to my dinner party.".format(guests[2]))

#3 additional guests
guests.append('porter robinson')
guests.append('george miller')
guests.append('akira yamaoka')

#add one guest at start and middle of list 
guests.insert(0, 'kunimitsu takahashi')
guests.insert(4, 'sean bowie')

#add one guest to the end of the list
#(redundant since I used .append for the 3 extra guests but that doesn't really matter)
guests.append('benjamin lasky')

#the invitations before sorting
print("Before sorting:")
for guest in guests:
    print("{}, you're formally invited to my dinner party.".format(guest))

#sorting
guests.sort()

#Print invitations after sorting
print("\nAfter sorting:")
for guest in guests:
    print("{}, you're formally invited to my dinner party.".format(guest))

#Print call about bigger guest list
print("\nMore people will be invited since I found a bigger dinner table.")