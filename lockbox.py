#!/usr/bin/python3

import os
import sys

def decrypt(file):
   os.system('gpg {} >/dev/null 2>&1'.format(file))   

def encrypt(file):
   os.system('gpg -c --yes {} >/dev/null 2>&1'.format(file))

def main(): 

   if (len(sys.argv) < 2):
      sys.exit()
 
   option = sys.argv[1]

   if (option == "-r"):
      
      if (len(sys.argv) != 4):
         sys.exit()
		
      decrypt('data.gpg')
      try:
         data = open('data', 'r')
      except:
         print('Could not open data')
         sys.exit()
		
      target = sys.argv[2]
      info = sys.argv[3]

      while 1:
         line = data.readline()
         if not line:
            print('Info for {} not found'.format(target))
            break

         line = line.split()
         if (line[0] == target):
            found = False
            for i in range(1,len(line),2):
               if (line[i] == info):
                  print(line[i+1])
                  found = True
                  break
            if (not found):
               print('{} for {} not found'.format(info,target))
            break
            
   elif (option == "-a"):
	   
      if (len(sys.argv) != 3):
         print('Wrong number of arguments')
         sys.exit()
	      
      decrypt('data.gpg')
      try:
	      data = open('data', 'r')
      except:
         print('Could not open data')
         sys.exit()
	   
      target = sys.argv[2]
	   
      while 1:
         line = data.readline()
         if not line:
            print('Info for {} not found'.format(target))
            break
         line = line.split()
         if (line[0] == target):
            print(line)
            break
		  
   elif (option == "-w"):
   
      if (len(sys.argv) != 5):
         print('Wrong number of arguments')
         sys.exit()
         
      decrypt('data.gpg')
      try:
         data = open('data', 'r')
      except:
         print('Could not open data')
         sys.exit()   

      target = sys.argv[2]
      info = sys.argv[3]
      value = sys.argv[4]

      temp = open('temp', 'w')

      found = False
      
      while 1:
         line = data.readline()
         if not line:
            break	
         line = line.split()
         if (line[0] == target):
            print(target, end=" ", file=temp)
            for i in range(1,len(line),2):
               print(line[i], end=" ",file=temp)
               if (line[i] == info):
                  if (i == len(line)-2):
                     print(value,temp)
                  else:
                     print(value,end=" ",file=temp)
                     found = True
               else:
                  if (found and i == len(line)-2):
                     print(line[i+1],file=temp)
                  else:
                     print(line[i+1],end=" ",file=temp)
                
            if (not found):
               print(info,end=" ", file=temp)
               print(value,file=temp)
               found = True   
         else:
            print(line, file=temp)
      
      if (not found):
         print(target, end=" ", file=temp)
         print(info, end=" ", file=temp)
         print(value, file=temp)

      temp.close()
      os.system('mv temp data')
      encrypt('data')
      
   else:
      print('Invalid Option: {}'.format(option))

   os.system('rm data')
   
if __name__ == "__main__":
    main()

