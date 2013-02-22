#!/usr/bin/python3

import argparse
import sqlite3 as sqlite
import os
import sys

def decrypt(file):
	os.system('gpg {} >/dev/null 2>&1'.format(file))   

def encrypt(file):
	os.system('gpg -c --yes {} >/dev/null 2>&1'.format(file))

def main(): 

	# Set up the argument parser
	parser = argparse.ArgumentParser('lockbox.py')
	parser.add_argument('account', nargs='?', help='Retrieve the data associated with your account')
	parser.add_argument('-a', '--add', dest='add', nargs=3, metavar=('account', 'key', 'val'), help='Add data to your account')
	parser.add_argument('-r', '--remove', dest='remove', nargs=2, metavar=('account', 'key'), help='Remove data from your account')
	args = parser.parse_args()

	db = None
	modified = False

	try:
		# decrypt file if it exists
		decrypt('accounts.db.gpg')

		# connect to database
		db = sqlite.connect('accounts.db')
		cs = db.cursor()

		# read data
		account = args.account;
		if (account):
			print('[ ' + account + ' ]')
			try:
				rows = cs.execute('SELECT * FROM ' + account).fetchall()
				for row in rows:
					print(' : '.join(str(x) for x in row))
			except:
				print("Account information not found")

		# add data
		elif (args.add):
			acc = args.add[0]
			key = args.add[1]
			val = args.add[2]
			cs.execute('CREATE TABLE IF NOT EXISTS ' + acc + '(key TEXT PRIMARY KEY, val TEXT )')
			cs.execute('INSERT OR REPLACE INTO ' + acc + ' VALUES (\''+ key +'\',\''+val +'\')')
			modified = True

		# remove data
		elif (args.remove):
			acc = args.remove[0]
			key = args.remove[1]
			cs.execute('DELETE FROM ' + acc + ' WHERE key=\'' + key + '\'')
			modified = True

		# save changes
		db.commit()
		# re-encrypt the database
		if (modified):
			encrypt('accounts.db')


	# Handle db exception - OOPS
	except sqlite.Error as e:
		print("Error " + e.args[0])

	finally:
		if db:
			# close the db
			db.close()
			# remove unencypted db
			os.system('rm accounts.db')
			
main()