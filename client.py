import json

import grpc
from news import news_pb2 as pb2, news_pb2_grpc as pb2_grpc


def client_run():
    f = open('resources/application.json', encoding='UTF-8')
    settings = json.load(f)
    f.close()
    address = f"{settings['grpc']['server']['ip']}:{settings['grpc']['server']['port']}"

    conn = grpc.insecure_channel(address)
    client = pb2_grpc.NewsServiceStub(channel=conn)
    response = client.hello(pb2.StringRequest(name='dawn'))
    print(response.result)


if __name__ == '__main__':
    client_run()
