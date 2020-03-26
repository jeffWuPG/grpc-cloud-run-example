# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\"_\n\x0f\x42inaryOperation\x12\x15\n\rfirst_operand\x18\x01 \x01(\x02\x12\x16\n\x0esecond_operand\x18\x02 \x01(\x02\x12\x1d\n\toperation\x18\x03 \x01(\x0e\x32\n.Operation\"#\n\x11\x43\x61lculationResult\x12\x0e\n\x06result\x18\x01 \x01(\x02*\"\n\tOperation\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\x0c\n\x08SUBTRACT\x10\x01\x32?\n\nCalculator\x12\x31\n\tCalculate\x12\x10.BinaryOperation\x1a\x12.CalculationResultb\x06proto3'
)

_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTRACT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_OPERATION)

Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
ADD = 0
SUBTRACT = 1



_BINARYOPERATION = _descriptor.Descriptor(
  name='BinaryOperation',
  full_name='BinaryOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_operand', full_name='BinaryOperation.first_operand', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_operand', full_name='BinaryOperation.second_operand', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='BinaryOperation.operation', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=115,
)


_CALCULATIONRESULT = _descriptor.Descriptor(
  name='CalculationResult',
  full_name='CalculationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CalculationResult.result', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=152,
)

_BINARYOPERATION.fields_by_name['operation'].enum_type = _OPERATION
DESCRIPTOR.message_types_by_name['BinaryOperation'] = _BINARYOPERATION
DESCRIPTOR.message_types_by_name['CalculationResult'] = _CALCULATIONRESULT
DESCRIPTOR.enum_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BinaryOperation = _reflection.GeneratedProtocolMessageType('BinaryOperation', (_message.Message,), {
  'DESCRIPTOR' : _BINARYOPERATION,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:BinaryOperation)
  })
_sym_db.RegisterMessage(BinaryOperation)

CalculationResult = _reflection.GeneratedProtocolMessageType('CalculationResult', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATIONRESULT,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalculationResult)
  })
_sym_db.RegisterMessage(CalculationResult)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=190,
  serialized_end=253,
  methods=[
  _descriptor.MethodDescriptor(
    name='Calculate',
    full_name='Calculator.Calculate',
    index=0,
    containing_service=None,
    input_type=_BINARYOPERATION,
    output_type=_CALCULATIONRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
