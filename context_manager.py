class Resource:
    def __init__(self, name):
        print('Resource create {}'.format(name))
        self.name = name

    def get_name(self):
        return self.name

    def close(self):
        print("Прекращение работы!")


class ContextResource:
    def __init__(self, name):
        self.resource = Resource(name)

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resource.close()


with ContextResource('Worker') as r:
    print(r.get_name())
