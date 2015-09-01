# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='raw_data.proto',
  package='evarilos',
  serialized_pb='\n\x0eraw_data.proto\x12\x08\x65varilos\"\x9b\x02\n\x0cRawRFReading\x12\x11\n\tsender_id\x18\x01 \x01(\t\x12\x14\n\x0csender_bssid\x18\x02 \x02(\t\x12\x0f\n\x07\x63hannel\x18\x03 \x02(\t\x12\x0c\n\x04rssi\x18\x04 \x02(\x05\x12\x15\n\rtimestamp_utc\x18\x05 \x01(\x03\x12\x0e\n\x06run_nr\x18\x06 \x02(\x05\x12:\n\x11receiver_location\x18\x07 \x02(\x0b\x32\x1f.evarilos.RawRFReading.Location\x1a`\n\x08Location\x12\x14\n\x0c\x63oordinate_x\x18\x01 \x02(\x01\x12\x14\n\x0c\x63oordinate_y\x18\x02 \x02(\x01\x12\x14\n\x0c\x63oordinate_z\x18\x03 \x01(\x01\x12\x12\n\nroom_label\x18\x04 \x01(\t\"\xb5\x01\n\x16RawRFReadingCollection\x12/\n\x0fraw_measurement\x18\x01 \x03(\x0b\x32\x16.evarilos.RawRFReading\x12\x13\n\x0bmeas_number\x18\x02 \x02(\x05\x12\x0f\n\x07\x64\x61ta_id\x18\x03 \x02(\t\x12\x0b\n\x03_id\x18\x04 \x01(\x0c\x12\x1b\n\x13timestamp_utc_start\x18\x05 \x01(\x03\x12\x1a\n\x12timestamp_utc_stop\x18\x06 \x01(\x03')




_RAWRFREADING_LOCATION = descriptor.Descriptor(
  name='Location',
  full_name='evarilos.RawRFReading.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='coordinate_x', full_name='evarilos.RawRFReading.Location.coordinate_x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coordinate_y', full_name='evarilos.RawRFReading.Location.coordinate_y', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coordinate_z', full_name='evarilos.RawRFReading.Location.coordinate_z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='room_label', full_name='evarilos.RawRFReading.Location.room_label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=216,
  serialized_end=312,
)

_RAWRFREADING = descriptor.Descriptor(
  name='RawRFReading',
  full_name='evarilos.RawRFReading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sender_id', full_name='evarilos.RawRFReading.sender_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender_bssid', full_name='evarilos.RawRFReading.sender_bssid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='channel', full_name='evarilos.RawRFReading.channel', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rssi', full_name='evarilos.RawRFReading.rssi', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp_utc', full_name='evarilos.RawRFReading.timestamp_utc', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='run_nr', full_name='evarilos.RawRFReading.run_nr', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='receiver_location', full_name='evarilos.RawRFReading.receiver_location', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RAWRFREADING_LOCATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=29,
  serialized_end=312,
)


_RAWRFREADINGCOLLECTION = descriptor.Descriptor(
  name='RawRFReadingCollection',
  full_name='evarilos.RawRFReadingCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='raw_measurement', full_name='evarilos.RawRFReadingCollection.raw_measurement', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='meas_number', full_name='evarilos.RawRFReadingCollection.meas_number', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_id', full_name='evarilos.RawRFReadingCollection.data_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='_id', full_name='evarilos.RawRFReadingCollection._id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp_utc_start', full_name='evarilos.RawRFReadingCollection.timestamp_utc_start', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp_utc_stop', full_name='evarilos.RawRFReadingCollection.timestamp_utc_stop', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  extension_ranges=[],
  serialized_start=315,
  serialized_end=496,
)

_RAWRFREADING_LOCATION.containing_type = _RAWRFREADING;
_RAWRFREADING.fields_by_name['receiver_location'].message_type = _RAWRFREADING_LOCATION
_RAWRFREADINGCOLLECTION.fields_by_name['raw_measurement'].message_type = _RAWRFREADING
DESCRIPTOR.message_types_by_name['RawRFReading'] = _RAWRFREADING
DESCRIPTOR.message_types_by_name['RawRFReadingCollection'] = _RAWRFREADINGCOLLECTION

class RawRFReading(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Location(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _RAWRFREADING_LOCATION
    
    # @@protoc_insertion_point(class_scope:evarilos.RawRFReading.Location)
  DESCRIPTOR = _RAWRFREADING
  
  # @@protoc_insertion_point(class_scope:evarilos.RawRFReading)

class RawRFReadingCollection(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RAWRFREADINGCOLLECTION
  
  # @@protoc_insertion_point(class_scope:evarilos.RawRFReadingCollection)

# @@protoc_insertion_point(module_scope)