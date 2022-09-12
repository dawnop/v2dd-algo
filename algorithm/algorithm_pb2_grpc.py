# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import algorithm_pb2 as algorithm__pb2


class AlgorithmServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.image = channel.unary_stream(
                '/algorithm.AlgorithmService/image',
                request_serializer=algorithm__pb2.ImageRequest.SerializeToString,
                response_deserializer=algorithm__pb2.ImageResponse.FromString,
                )
        self.video = channel.unary_stream(
                '/algorithm.AlgorithmService/video',
                request_serializer=algorithm__pb2.VideoRequest.SerializeToString,
                response_deserializer=algorithm__pb2.VideoResponse.FromString,
                )


class AlgorithmServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def image(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def video(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlgorithmServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'image': grpc.unary_stream_rpc_method_handler(
                    servicer.image,
                    request_deserializer=algorithm__pb2.ImageRequest.FromString,
                    response_serializer=algorithm__pb2.ImageResponse.SerializeToString,
            ),
            'video': grpc.unary_stream_rpc_method_handler(
                    servicer.video,
                    request_deserializer=algorithm__pb2.VideoRequest.FromString,
                    response_serializer=algorithm__pb2.VideoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'algorithm.AlgorithmService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AlgorithmService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def image(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/algorithm.AlgorithmService/image',
            algorithm__pb2.ImageRequest.SerializeToString,
            algorithm__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def video(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/algorithm.AlgorithmService/video',
            algorithm__pb2.VideoRequest.SerializeToString,
            algorithm__pb2.VideoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
