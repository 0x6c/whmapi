WHMApi python module
====================

Simple to use python module to perform WHM operations directly from python code.

Use cases:

* Test cPanel hooks modules
* Write automation
* Create test users
* Check accounts and domains
* and so on...

-------------
Example usage
-------------

To list all local cPanel users:

.. code:: python

    # List local cPanel user accounts.
    from whmapi import APIClient

    client = APIClient()
    local_users = client.call('listaccts')


To use function with paramaeters:

.. code:: python

    # Find particular user.
    from whmapi import APIClient

    client = APIClient()
    sample_user = client.call(
        function='listaccts',
        req_params={'searchtype': 'user',
                    'search': 'example'})

Sample output:

.. code:: json

	{  
	   "data":{  
	      "acct":[  
	         {  
	            "maxaddons":"*unknown*",
	            "ip":"0.0.0.0",
	            "min_defer_fail_to_trigger_protection":"20",
	            "legacy_backup":1,
	            "diskused":"10M",
	            "maxftp":"5",
	            "startdate":"08 Jun 19 17:05",
	            "max_defer_fail_percentage":"50",
	            "disklimit":"150000M",
	            "is_locked":0,
	            "suspendtime":0,
	            "email":"simple@example.com",
	            "domain":"example.com",
	            "unix_startdate":1213866345,
	            "user":"example",
	            "plan":"Sample - Hosting",
	            "shell":"/usr/local/cpanel/bin/noshell",
	            "maxpop":"100",
	            "backup":0,
	            "theme":"awesometheme",
	            "owner":"austghost",
	            "max_email_per_hour":"500",
	            "ipv6":[  
	
	            ],
	            "suspendreason":"not suspended",
	            "maxlst":"*unknown*",
	            "suspended":0,
	            "maxsql":"10",
	            "maxparked":"5",
	            "partition":"home5",
	            "maxsub":"unlimited"
	         }
	      ]
	   },
	   "metadata":{  
	      "version":1,
	      "reason":"OK",
	      "result":1,
	      "command":"accountsummary"
	   }
	} 

==============
Usefull linlks
==============

`WHMApi1 documentation <https://documentation.cpanel.net/display/SDK/Guide+to+WHM+API+1>`_
