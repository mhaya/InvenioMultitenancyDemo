..
    Copyright (C) 2019 CERN.

    My site is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

=========
 Multitenancy demo of Invenio3
=========

.. image:: https://img.shields.io/travis/my-site/my-site.svg
        :target: https://travis-ci.org/my-site/my-site

.. image:: https://img.shields.io/coveralls/my-site/my-site.svg
        :target: https://coveralls.io/r/my-site/my-site

.. image:: https://img.shields.io/github/license/my-site/my-site.svg
        :target: https://github.com/my-site/my-site/blob/master/LICENSE

This is multitenancy demo of Invenio3. 
This demo uses uWSGI emperor mode and Nginx virtual host and SEARCH_INDEX_PREFIX config.

How to use
==================

1. Set up demonstration environment. ::

        git clone https://github.com/mhaya/InvenioMultitenancyDemo.git
        cd InvenioMultitenancyDemo
        pipenv lock
        ./docker/build-images.sh
        docker-compose -f docker-compose.full.yml up -d
        ./docker/wait-for-services.sh --full
        docker-compose -f docker-compose.full.yml exec web-ui ./scripts/setup

2. Add following records in your hosts file. ::

        127.0.0.1 a.example.org
        127.0.0.1 b.example.org



3. Access https://a.example.org and https://b.example.org. 

4. Add example records into each instance. ::

        curl -k --header "Content-Type: application/json" \
        --request POST \
        --data '{"title":"Some title", "contributors": [{"name": "Doe, John"}]}' \
        https://a.example.org/api/records/?prettyprint=1



        curl -k --header "Content-Type: application/json" \
        --request POST \
        --data '{"title":"Some title2", "contributors": [{"name": "Doe, John"}]}' \
        https://b.example.org/api/records/?prettyprint=1


5. Check Added records on each instance.


