import json

class JsonSerializer(object):

    @classmethod
    def SerializeObject(self, data):

        if isinstance(data,dict):
            s = json.dumps(data)
        else:
            s = json.dumps(data.__dict__)

        return s

    @classmethod
    def DeserializeJson(self, json_string, object_to_serialize):
        object_to_serialize.__dict__ = json.loads(str(json_string))
        return object_to_serialize

