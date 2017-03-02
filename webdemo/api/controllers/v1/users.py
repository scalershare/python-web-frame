#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pecan import rest
from wsme import types as wtypes
import logging
from webdemo.api import expose
logger = logging.getLogger(__name__)


class User(wtypes.Base):
    name = wtypes.text
    age = int


class Users(wtypes.Base):
    users = [User]


class UsersController(rest.RestController):

    '''
       None 表示这个方法没有返回值
       status_code 表示这个API的响应状态码是201
       test eg:
       curl -X POST http://localhost:8080/v1/users -H "Content-Type: application/json" -d '{"name": "Cook", "age": 50}' -v

    '''
    @expose.expose(None, body=User, status_code=201)
    def post(self, user):
        print user

    @expose.expose(Users)
    def get(self):
        logger.info("v1 UsersController Get Method is called ...")
        user_info_list = [
            {
                'name': 'Alice',
                'age': 30,
            },
            {
                'name': 'Bob',
                'age': 40,
            }
        ]
        users_list = [User(**user_info) for user_info in user_info_list]
        return Users(users=users_list)
