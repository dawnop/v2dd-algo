import json
import time

import grpc
import image_pb2 as pb2
import image_pb2_grpc as pb2_grpc
from concurrent import futures
from PIL import Image
from io import BytesIO
from grpc_reflection.v1alpha import reflection


class ImageService(pb2_grpc.ImageServiceServicer):
    def hello(self, request, context):
        bytes_image = request.image
        bytes_stream = BytesIO(bytes_image)
        image = Image.open(bytes_stream)
        result = f'python grpc service: size of this image is {image.size})'
        return pb2.StringResponse(result=result)


MAX_MESSAGE_LENGTH = 256 * 1024 * 1024
SERVER_ADDRESS = 'localhost:9090'


def image_server_run():
    # create a grpc server and register it.
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4),
                              options=[('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
                                       ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH)])
    pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), grpc_server)
    service_name = (
        pb2.DESCRIPTOR.services_by_name['ImageService'].full_name,
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
    image_server_run()
