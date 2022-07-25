from pymongo import MongoClient
import configuration

connection_params = configuration.connection_params

#connect to mongodb
mongoconnection = MongoClient(
    'mongodb://{user}:{password}@{host}:'
    '{port}/{namespace}?retryWrites=false'.format(**connection_params)
)


db = mongoconnection.iiotMiba

default_permissions = { "MSA": [ { "app_name": "Monitoring", "module": [ "Connection" ], "role": "read" } ] }
