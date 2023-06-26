import asyncio
from flask import Flask, request, redirect
from flask_restful import Resource, Api, reqparse
import pymongo

app = Flask(__name__)
api = Api(app)
cluster = pymongo.MongoClient("mongodb://localhost:27017")
db = cluster["luaZXC"]
collection = db['users']
block_ip = []


class LuaServer(Resource):
    def __init__(self):
        with open(r"lua path", "r") as file:
            self.read = file.read()

    def post(self):
        data = reqparse.RequestParser()
        data.add_argument("name", type=str)
        data.add_argument("uuid", type=str)
        data.add_argument("password", type=str)
        data.add_argument("processor", type=str)
        data.add_argument("video-card", type=str)
        data.add_argument("ip", type=str)
        args = data.parse_args()
        for i in args.values():
            if (i is None) or (type(i) is not str):
                return "HWID FAIL1"
        user = collection.find_one({"name": args['name']})
        if user is not None:
            if "password" in user:
                del user["_id"]
                good = 0
                for k, v in user.items():
                    if args[k] == v:
                        good += 1
                if good >= 5:
                    pass
                else:
                    return "HWID FAIL2"
            else:
                collection.update_one({"name": args['name']}, {"$set": {"uuid": args["uuid"], "password": args["password"], "processor": args["processor"], "video-card": args["video-card"]}})
            return self.read
        else:
            return "HWID FAIL3 "


api.add_resource(LuaServer, '/api')
if __name__ == '__main__':
    app.run(debug=False)