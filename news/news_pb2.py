# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: news.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nnews.proto\x12\x04news\"\x1d\n\rStringRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x0eStringResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2C\n\x0bNewsService\x12\x34\n\x05hello\x12\x13.news.StringRequest\x1a\x14.news.StringResponse\"\x00\x62\x06proto3')



_STRINGREQUEST = DESCRIPTOR.message_types_by_name['StringRequest']
_STRINGRESPONSE = DESCRIPTOR.message_types_by_name['StringResponse']
StringRequest = _reflection.GeneratedProtocolMessageType('StringRequest', (_message.Message,), {
  'DESCRIPTOR' : _STRINGREQUEST,
  '__module__' : 'news_pb2'
  # @@protoc_insertion_point(class_scope:news.StringRequest)
  })
_sym_db.RegisterMessage(StringRequest)

StringResponse = _reflection.GeneratedProtocolMessageType('StringResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRINGRESPONSE,
  '__module__' : 'news_pb2'
  # @@protoc_insertion_point(class_scope:news.StringResponse)
  })
_sym_db.RegisterMessage(StringResponse)

_NEWSSERVICE = DESCRIPTOR.services_by_name['NewsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STRINGREQUEST._serialized_start=20
  _STRINGREQUEST._serialized_end=49
  _STRINGRESPONSE._serialized_start=51
  _STRINGRESPONSE._serialized_end=83
  _NEWSSERVICE._serialized_start=85
  _NEWSSERVICE._serialized_end=152
# @@protoc_insertion_point(module_scope)