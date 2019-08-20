# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Blueprint used for loading templates.

The sole purpose of this blueprint is to ensure that Invenio can find the
templates and static files located in the folders of the same names next to
this file.
"""

from __future__ import absolute_import, print_function

from flask import Blueprint

import os
from invenio_app.factory import instance_path, static_folder
from flask import current_app as flask_current_app


blueprint = Blueprint(
    'my_site',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route('/env')
def hello():
    L = []
    L.append("<h1>os.environ.items()</h1>")
    for k, v in os.environ.items():
        L.append("{key} : {value}".format(key=k, value=v))

    
    L.append("<h1>invenio_app()</h1>")
    L.append("instance_path:"+instance_path)
    L.append("static_folder:"+static_folder)

    L.append("<h1>flask_current_app</h1>")
    for k, v in flask_current_app.config.items():
        L.append("{key} : {value}".format(key=k, value=v))

    return "</br>".join(L)
