# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/debug/debugger_event_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/debug/debugger_event_metadata.proto',
  package='third_party.tensorflow.core.debug',
  syntax='proto3',
  serialized_pb=_b('\n3tensorflow/core/debug/debugger_event_metadata.proto\x12!third_party.tensorflow.core.debug\"e\n\x15\x44\x65\x62uggerEventMetadata\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x13\n\x0boutput_slot\x18\x02 \x01(\x05\x12\x12\n\nnum_chunks\x18\x03 \x01(\x05\x12\x13\n\x0b\x63hunk_index\x18\x04 \x01(\x05\x62\x06proto3')
)




_DEBUGGEREVENTMETADATA = _descriptor.Descriptor(
  name='DebuggerEventMetadata',
  full_name='third_party.tensorflow.core.debug.DebuggerEventMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='third_party.tensorflow.core.debug.DebuggerEventMetadata.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_slot', full_name='third_party.tensorflow.core.debug.DebuggerEventMetadata.output_slot', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_chunks', full_name='third_party.tensorflow.core.debug.DebuggerEventMetadata.num_chunks', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunk_index', full_name='third_party.tensorflow.core.debug.DebuggerEventMetadata.chunk_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['DebuggerEventMetadata'] = _DEBUGGEREVENTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DebuggerEventMetadata = _reflection.GeneratedProtocolMessageType('DebuggerEventMetadata', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGGEREVENTMETADATA,
  __module__ = 'tensorflow.core.debug.debugger_event_metadata_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.core.debug.DebuggerEventMetadata)
  ))
_sym_db.RegisterMessage(DebuggerEventMetadata)


# @@protoc_insertion_point(module_scope)