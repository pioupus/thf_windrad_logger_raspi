# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_logger.proto

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
  name='protobuf_logger.proto',
  package='enerlyzer',
  syntax='proto2',
  serialized_pb=_b('\n\x15protobuf_logger.proto\x12\tenerlyzer\"\xc1\x05\n\x07\x64\x61taset\x12\x13\n\x0blogger_time\x18\x1d \x02(\x02\x12\x16\n\x0e\x63urrent_l1_avg\x18\x01 \x02(\x02\x12\x16\n\x0e\x63urrent_l2_avg\x18\x02 \x02(\x02\x12\x16\n\x0e\x63urrent_l3_avg\x18\x03 \x02(\x02\x12\x17\n\x0fvoltage_l21_avg\x18\x04 \x02(\x02\x12\x17\n\x0fvoltage_l32_avg\x18\x05 \x02(\x02\x12\x17\n\x0fvoltage_l13_avg\x18\x06 \x02(\x02\x12\x16\n\x0e\x63urrent_l1_eff\x18\x07 \x02(\x02\x12\x16\n\x0e\x63urrent_l2_eff\x18\x08 \x02(\x02\x12\x16\n\x0e\x63urrent_l3_eff\x18\t \x02(\x02\x12\x17\n\x0fvoltage_l21_eff\x18\n \x02(\x02\x12\x17\n\x0fvoltage_l32_eff\x18\x0b \x02(\x02\x12\x17\n\x0fvoltage_l13_eff\x18\x0c \x02(\x02\x12\x16\n\x0e\x63urrent_l1_max\x18\r \x02(\x02\x12\x16\n\x0e\x63urrent_l2_max\x18\x0e \x02(\x02\x12\x16\n\x0e\x63urrent_l3_max\x18\x0f \x02(\x02\x12\x17\n\x0fvoltage_l21_max\x18\x10 \x02(\x02\x12\x17\n\x0fvoltage_l32_max\x18\x11 \x02(\x02\x12\x17\n\x0fvoltage_l13_max\x18\x12 \x02(\x02\x12\x16\n\x0etemperature_l1\x18\x13 \x02(\x02\x12\x16\n\x0etemperature_l2\x18\x14 \x02(\x02\x12\x16\n\x0etemperature_l3\x18\x15 \x02(\x02\x12\x13\n\x0bvoltage_aux\x18\x16 \x02(\x02\x12\x14\n\x0c\x66requency_Hz\x18\x17 \x02(\x02\x12\r\n\x05power\x18\x18 \x02(\x02\x12\x1f\n\x17\x65xternal_current_sensor\x18\x19 \x02(\x02\x12\x16\n\x0esupply_voltage\x18\x1a \x02(\x02\x12\x17\n\x0f\x63pu_temperature\x18\x1b \x02(\x02\x12\x14\n\x0c\x63oin_cell_mv\x18\x1c \x02(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DATASET = _descriptor.Descriptor(
  name='dataset',
  full_name='enerlyzer.dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logger_time', full_name='enerlyzer.dataset.logger_time', index=0,
      number=29, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l1_avg', full_name='enerlyzer.dataset.current_l1_avg', index=1,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l2_avg', full_name='enerlyzer.dataset.current_l2_avg', index=2,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l3_avg', full_name='enerlyzer.dataset.current_l3_avg', index=3,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l21_avg', full_name='enerlyzer.dataset.voltage_l21_avg', index=4,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l32_avg', full_name='enerlyzer.dataset.voltage_l32_avg', index=5,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l13_avg', full_name='enerlyzer.dataset.voltage_l13_avg', index=6,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l1_eff', full_name='enerlyzer.dataset.current_l1_eff', index=7,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l2_eff', full_name='enerlyzer.dataset.current_l2_eff', index=8,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l3_eff', full_name='enerlyzer.dataset.current_l3_eff', index=9,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l21_eff', full_name='enerlyzer.dataset.voltage_l21_eff', index=10,
      number=10, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l32_eff', full_name='enerlyzer.dataset.voltage_l32_eff', index=11,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l13_eff', full_name='enerlyzer.dataset.voltage_l13_eff', index=12,
      number=12, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l1_max', full_name='enerlyzer.dataset.current_l1_max', index=13,
      number=13, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l2_max', full_name='enerlyzer.dataset.current_l2_max', index=14,
      number=14, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_l3_max', full_name='enerlyzer.dataset.current_l3_max', index=15,
      number=15, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l21_max', full_name='enerlyzer.dataset.voltage_l21_max', index=16,
      number=16, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l32_max', full_name='enerlyzer.dataset.voltage_l32_max', index=17,
      number=17, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_l13_max', full_name='enerlyzer.dataset.voltage_l13_max', index=18,
      number=18, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_l1', full_name='enerlyzer.dataset.temperature_l1', index=19,
      number=19, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_l2', full_name='enerlyzer.dataset.temperature_l2', index=20,
      number=20, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_l3', full_name='enerlyzer.dataset.temperature_l3', index=21,
      number=21, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage_aux', full_name='enerlyzer.dataset.voltage_aux', index=22,
      number=22, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency_Hz', full_name='enerlyzer.dataset.frequency_Hz', index=23,
      number=23, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='enerlyzer.dataset.power', index=24,
      number=24, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_current_sensor', full_name='enerlyzer.dataset.external_current_sensor', index=25,
      number=25, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supply_voltage', full_name='enerlyzer.dataset.supply_voltage', index=26,
      number=26, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_temperature', full_name='enerlyzer.dataset.cpu_temperature', index=27,
      number=27, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coin_cell_mv', full_name='enerlyzer.dataset.coin_cell_mv', index=28,
      number=28, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=742,
)

DESCRIPTOR.message_types_by_name['dataset'] = _DATASET

dataset = _reflection.GeneratedProtocolMessageType('dataset', (_message.Message,), dict(
  DESCRIPTOR = _DATASET,
  __module__ = 'protobuf_logger_pb2'
  # @@protoc_insertion_point(class_scope:enerlyzer.dataset)
  ))
_sym_db.RegisterMessage(dataset)


# @@protoc_insertion_point(module_scope)