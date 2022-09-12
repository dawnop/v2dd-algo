import time

import grpc
import algorithm_pb2 as pb2
import algorithm_pb2_grpc as pb2_grpc
from concurrent import futures
from PIL import Image
from io import BytesIO
from grpc_reflection.v1alpha import reflection
import cv2

MAX_MESSAGE_LENGTH = 256 * 1024 * 1024
SERVER_ADDRESS = 'localhost:9090'
UPLOAD_PATH = '~/workspace/upload/'


class AlgorithmService(pb2_grpc.AlgorithmServiceServicer):
    def image(self, request, context):
        bytes_image = request.image
        method = request.method
        bytes_stream = BytesIO(bytes_image)
        image = Image.open(bytes_stream)
        result = f'python grpc service: image info as follows: ' \
                 f'{image.format, image.mode, image.size}'
        yield pb2.ImageResponse(message="upload success", state=pb2.State.OK)
        time.sleep(10)
        yield pb2.ImageResponse(message=result, state=pb2.State.END)

    # def video(self, request, context):
    #     bytes_video = request.video
    #     method = request.method
    #     bytes_stream = BytesIO(bytes_video)
    #
    #     return pb2.VideoResponse(result=result)


def algorithm_server_run():
    # create a grpc server and register it.
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4),
                              options=[('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
                                       ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH)])
    pb2_grpc.add_AlgorithmServiceServicer_to_server(AlgorithmService(), grpc_server)
    service_name = (
        pb2.DESCRIPTOR.services_by_name['AlgorithmService'].full_name,
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
    algorithm_server_run()
