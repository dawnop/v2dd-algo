# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algorithm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61lgorithm.proto\x12\talgorithm\"9\n\x0cImageRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05image\x18\x02 \x01(\x0c\x12\x0e\n\x06method\x18\x03 \x01(\t\"A\n\rImageResponse\x12\x1f\n\x05state\x18\x01 \x01(\x0e\x32\x10.algorithm.State\x12\x0f\n\x07message\x18\x02 \x01(\t\"9\n\x0cVideoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05video\x18\x02 \x01(\x0c\x12\x0e\n\x06method\x18\x03 \x01(\t\"A\n\rVideoResponse\x12\x1f\n\x05state\x18\x01 \x01(\x0e\x32\x10.algorithm.State\x12\x0f\n\x07message\x18\x02 \x01(\t*!\n\x05State\x12\x07\n\x03\x45RR\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x32\x92\x01\n\x10\x41lgorithmService\x12>\n\x05image\x12\x17.algorithm.ImageRequest\x1a\x18.algorithm.ImageResponse\"\x00\x30\x01\x12>\n\x05video\x12\x17.algorithm.VideoRequest\x1a\x18.algorithm.VideoResponse\"\x00\x30\x01\x62\x06proto3')

_STATE = DESCRIPTOR.enum_types_by_name['State']
State = enum_type_wrapper.EnumTypeWrapper(_STATE)
ERR = 0
OK = 1
END = 2


_IMAGEREQUEST = DESCRIPTOR.message_types_by_name['ImageRequest']
_IMAGERESPONSE = DESCRIPTOR.message_types_by_name['ImageResponse']
_VIDEOREQUEST = DESCRIPTOR.message_types_by_name['VideoRequest']
_VIDEORESPONSE = DESCRIPTOR.message_types_by_name['VideoResponse']
ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'algorithm_pb2'
  # @@protoc_insertion_point(class_scope:algorithm.ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)

ImageResponse = _reflection.GeneratedProtocolMessageType('ImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGERESPONSE,
  '__module__' : 'algorithm_pb2'
  # @@protoc_insertion_point(class_scope:algorithm.ImageResponse)
  })
_sym_db.RegisterMessage(ImageResponse)

VideoRequest = _reflection.GeneratedProtocolMessageType('VideoRequest', (_message.Message,), {
  'DESCRIPTOR' : _VIDEOREQUEST,
  '__module__' : 'algorithm_pb2'
  # @@protoc_insertion_point(class_scope:algorithm.VideoRequest)
  })
_sym_db.RegisterMessage(VideoRequest)

VideoResponse = _reflection.GeneratedProtocolMessageType('VideoResponse', (_message.Message,), {
  'DESCRIPTOR' : _VIDEORESPONSE,
  '__module__' : 'algorithm_pb2'
  # @@protoc_insertion_point(class_scope:algorithm.VideoResponse)
  })
_sym_db.RegisterMessage(VideoResponse)

_ALGORITHMSERVICE = DESCRIPTOR.services_by_name['AlgorithmService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATE._serialized_start=282
  _STATE._serialized_end=315
  _IMAGEREQUEST._serialized_start=30
  _IMAGEREQUEST._serialized_end=87
  _IMAGERESPONSE._serialized_start=89
  _IMAGERESPONSE._serialized_end=154
  _VIDEOREQUEST._serialized_start=156
  _VIDEOREQUEST._serialized_end=213
  _VIDEORESPONSE._serialized_start=215
  _VIDEORESPONSE._serialized_end=280
  _ALGORITHMSERVICE._serialized_start=318
  _ALGORITHMSERVICE._serialized_end=464
# @@protoc_insertion_point(module_scope)
