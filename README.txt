
Smithery
--------

Collect and reformat data and metadata

Dependencies
------------

 * Python

Optional dependencies
---------------------

 * gdata-python-client (for Google Data APIs support)
 * 

Setup development environment
-----------------------------

    git clone git://github.com/bopen/smithery.git smithery
    cd smithery
    python bootstrap.py -d
    ./bin/buildout -nv

Test and examples
-----------------

    ./bin/test
    ./bin/smithery -c examples/csv.cfg

Update docs
-----------

     make -C docs/ html

Copyright statement
-------------------

Copyright (c) 2011 B-Open Solutions srl. All rights reserved.
Copyright (c) 2010-2011 Alessandro Amici. All rights reserved.

This software is subject to the provisions of the Zope Public License, 
Version 2.1 (ZPL). A copy of the ZPL should accompany this distribution. 
THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED 
WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS 
FOR A PARTICULAR PURPOSE.
