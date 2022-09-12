import json
import time

import grpc
import news_pb2 as pb2
import news_pb2_grpc as pb2_grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection


class NewsService(pb2_grpc.NewsServiceServicer):
    def hello(self, request, context):
        name = request.name
        result = f'python grpc service: name is {name}'
        return pb2.StringResponse(result=result)

SERVER_ADDRESS = 'localhost:9090'

def news_server_run():
    # create a grpc server and register it.
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    pb2_grpc.add_NewsServiceServicer_to_server(NewsService(), grpc_server)
    service_name = (
        pb2.DESCRIPTOR.services_by_name['NewsService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_name, grpc_server)
    # assign ip and port, start the server.
    grpc_server.add_insecure_port(SERVER_ADDRESS)
    grpc_server.start()
    print(f'server start at {SERVER_ADDRESS}')
    # keep the python program alive, else it will run once and shut down.
    grpc_server.wait_for_termination()


if __name__ == '__main__':
    news_server_run()
