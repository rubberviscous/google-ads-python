# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/errors/time_zone_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/errors/time_zone_error.proto',
  package='google.ads.googleads.v3.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v3.errorsB\022TimeZoneErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V3.Errors\312\002\036Google\\Ads\\GoogleAds\\V3\\Errors\352\002\"Google::Ads::GoogleAds::V3::Errors'),
  serialized_pb=_b('\n:google/ads/googleads_v3/proto/errors/time_zone_error.proto\x12\x1egoogle.ads.googleads.v3.errors\x1a\x1cgoogle/api/annotations.proto\"Y\n\x11TimeZoneErrorEnum\"D\n\rTimeZoneError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11INVALID_TIME_ZONE\x10\x05\x42\xed\x01\n\"com.google.ads.googleads.v3.errorsB\x12TimeZoneErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V3.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V3\\Errors\xea\x02\"Google::Ads::GoogleAds::V3::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TIMEZONEERRORENUM_TIMEZONEERROR = _descriptor.EnumDescriptor(
  name='TimeZoneError',
  full_name='google.ads.googleads.v3.errors.TimeZoneErrorEnum.TimeZoneError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TIME_ZONE', index=2, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=145,
  serialized_end=213,
)
_sym_db.RegisterEnumDescriptor(_TIMEZONEERRORENUM_TIMEZONEERROR)


_TIMEZONEERRORENUM = _descriptor.Descriptor(
  name='TimeZoneErrorEnum',
  full_name='google.ads.googleads.v3.errors.TimeZoneErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TIMEZONEERRORENUM_TIMEZONEERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=213,
)

_TIMEZONEERRORENUM_TIMEZONEERROR.containing_type = _TIMEZONEERRORENUM
DESCRIPTOR.message_types_by_name['TimeZoneErrorEnum'] = _TIMEZONEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeZoneErrorEnum = _reflection.GeneratedProtocolMessageType('TimeZoneErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _TIMEZONEERRORENUM,
  __module__ = 'google.ads.googleads_v3.proto.errors.time_zone_error_pb2'
  ,
  __doc__ = """Container for enum describing possible time zone errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.errors.TimeZoneErrorEnum)
  ))
_sym_db.RegisterMessage(TimeZoneErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)