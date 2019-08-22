# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/* /etc/nginx/conf.d/
COPY test.key /etc/ssl/private/test.key
COPY test.crt /etc/ssl/certs/test.crt
COPY a.key /etc/ssl/private/a.key
COPY a.crt /etc/ssl/certs/a.crt
COPY b.key /etc/ssl/private/b.key
COPY b.crt /etc/ssl/certs/b.crt

CMD ["/usr/sbin/nginx-debug", "-g", "daemon off;"]