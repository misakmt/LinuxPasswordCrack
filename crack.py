#!/usr/bin/env python3

import crypt

#dict_file = raw_input("Enter file name of password dictionary: ")

#with open(dict_file) as fp:
 #   line = fp.readline()
  #  while line:
   #     password = (line.strip())
    #    print (password)
     #   line = fp.readline()

f = open("100000passwords.txt", "r")
for password in f.readlines():
    password = password.strip('\n')
    #print (password)

    h = open("etc_shadow", "r")
    for hashes in h.readlines():
        hashes = hashes.strip('\n')
        #print hashes
        hashType = (hashes[0:3])
        #print hashType
        salt = (hashes[3:11])
        #print salt
        
        #f = open("test.txt", "r")
        #for password in f.readlines():
         #   password = password.strip('\n')
          #  print (password)
        #line2 = f.read()
        #password = (line.strip())
        
        theHash = crypt.crypt(password, hashType + salt + '$')
        #print (theHash)
        
        if (hashes == theHash):
            print("Password found!")
            print("Password for: ", theHash)
            print(password)
            print

exit()
