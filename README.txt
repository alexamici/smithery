
Smithery
--------

Collect and reformat data and metadata

Dependencies
------------

 * Python

Setup development environment
-----------------------------

    git clone git://github.com/alexamici/smithery.git smithery
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

Copyright (c) 2011 by B-Open Solutions srl. All rights reserved.
Copyright (c) 2010-2011 by Alessandro Amici. All rights reserved.
