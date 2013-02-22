# LockBox #

Password protected storage for your account information.

## Requirements ##

Python 3.2
SQLite3
GNU Privacy Guard (GPG)

## How-To ##

	./lockbox.py account [-a account key val] [-r account key]		
	-a --add [ account key val ]	
		Add new key with value val to your account
	-r --remove [ account key ]
		Remove key from account

## License ##

	LockBox - secure password storage

	Copyright (C) 2013  Kevin Pyc

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.