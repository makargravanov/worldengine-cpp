# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: World.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='World.proto',
  package='World',
  serialized_pb='\n\x0bWorld.proto\x12\x05World\"\xb2\x0b\n\x05World\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05width\x18\x02 \x02(\x05\x12\x0e\n\x06height\x18\x03 \x02(\x05\x12\x30\n\rheightMapData\x18\x04 \x02(\x0b\x32\x19.World.World.DoubleMatrix\x12\x17\n\x0fheightMapTh_sea\x18\x05 \x02(\x01\x12\x19\n\x11heightMapTh_plain\x18\x06 \x02(\x01\x12\x18\n\x10heightMapTh_hill\x18\x07 \x02(\x01\x12*\n\x06plates\x18\x1e \x02(\x0b\x32\x1a.World.World.IntegerMatrix\x12)\n\x05ocean\x18\x08 \x02(\x0b\x32\x1a.World.World.BooleanMatrix\x12,\n\tsea_depth\x18\x1d \x02(\x0b\x32\x19.World.World.DoubleMatrix\x12)\n\x05\x62iome\x18\t \x01(\x0b\x32\x1a.World.World.IntegerMatrix\x12\x38\n\x08humidity\x18\n \x01(\x0b\x32&.World.World.DoubleMatrixWithQuantiles\x12-\n\nirrigation\x18\x0b \x01(\x0b\x32\x19.World.World.DoubleMatrix\x12\x33\n\x10permeabilityData\x18\x0c \x01(\x0b\x32\x19.World.World.DoubleMatrix\x12\x18\n\x10permeability_low\x18\r \x01(\x01\x12\x18\n\x10permeability_med\x18\x0e \x01(\x01\x12/\n\x0cwatermapData\x18\x0f \x01(\x0b\x32\x19.World.World.DoubleMatrix\x12\x16\n\x0ewatermap_creek\x18\x10 \x01(\x01\x12\x16\n\x0ewatermap_river\x18\x11 \x01(\x01\x12\x1a\n\x12watermap_mainriver\x18\x12 \x01(\x01\x12\x34\n\x11precipitationData\x18\x13 \x01(\x0b\x32\x19.World.World.DoubleMatrix\x12\x19\n\x11precipitation_low\x18\x14 \x01(\x01\x12\x19\n\x11precipitation_med\x18\x15 \x01(\x01\x12\x32\n\x0ftemperatureData\x18\x16 \x01(\x0b\x32\x19.World.World.DoubleMatrix\x12\x19\n\x11temperature_polar\x18\x17 \x01(\x01\x12\x1a\n\x12temperature_alpine\x18\x18 \x01(\x01\x12\x1a\n\x12temperature_boreal\x18\x19 \x01(\x01\x12\x18\n\x10temperature_cool\x18\x1a \x01(\x01\x12\x18\n\x10temperature_warm\x18\x1b \x01(\x01\x12\x1f\n\x17temperature_subtropical\x18\x1c \x01(\x01\x1a\x1a\n\tDoubleRow\x12\r\n\x05\x63\x65lls\x18\x01 \x03(\x01\x1a\x1b\n\nBooleanRow\x12\r\n\x05\x63\x65lls\x18\x01 \x03(\x08\x1a\x1b\n\nIntegerRow\x12\r\n\x05\x63\x65lls\x18\x01 \x03(\x05\x1a\x18\n\x07\x42yteRow\x12\r\n\x05\x63\x65lls\x18\x01 \x03(\x05\x1a\x34\n\x0c\x44oubleMatrix\x12$\n\x04rows\x18\x01 \x03(\x0b\x32\x16.World.World.DoubleRow\x1a\x36\n\rBooleanMatrix\x12%\n\x04rows\x18\x01 \x03(\x0b\x32\x17.World.World.BooleanRow\x1a\x36\n\rIntegerMatrix\x12%\n\x04rows\x18\x01 \x03(\x0b\x32\x17.World.World.IntegerRow\x1a,\n\x0e\x44oubleQuantile\x12\x0b\n\x03key\x18\x01 \x02(\x05\x12\r\n\x05value\x18\x02 \x02(\x01\x1aq\n\x19\x44oubleMatrixWithQuantiles\x12.\n\tquantiles\x18\x01 \x03(\x0b\x32\x1b.World.World.DoubleQuantile\x12$\n\x04rows\x18\x02 \x03(\x0b\x32\x16.World.World.DoubleRow')




_WORLD_DOUBLEROW = _descriptor.Descriptor(
  name='DoubleRow',
  full_name='World.World.DoubleRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='World.World.DoubleRow.cells', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1044,
  serialized_end=1070,
)

_WORLD_BOOLEANROW = _descriptor.Descriptor(
  name='BooleanRow',
  full_name='World.World.BooleanRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='World.World.BooleanRow.cells', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1072,
  serialized_end=1099,
)

_WORLD_INTEGERROW = _descriptor.Descriptor(
  name='IntegerRow',
  full_name='World.World.IntegerRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='World.World.IntegerRow.cells', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1101,
  serialized_end=1128,
)

_WORLD_BYTEROW = _descriptor.Descriptor(
  name='ByteRow',
  full_name='World.World.ByteRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='World.World.ByteRow.cells', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1130,
  serialized_end=1154,
)

_WORLD_DOUBLEMATRIX = _descriptor.Descriptor(
  name='DoubleMatrix',
  full_name='World.World.DoubleMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='World.World.DoubleMatrix.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1156,
  serialized_end=1208,
)

_WORLD_BOOLEANMATRIX = _descriptor.Descriptor(
  name='BooleanMatrix',
  full_name='World.World.BooleanMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='World.World.BooleanMatrix.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1210,
  serialized_end=1264,
)

_WORLD_INTEGERMATRIX = _descriptor.Descriptor(
  name='IntegerMatrix',
  full_name='World.World.IntegerMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='World.World.IntegerMatrix.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1266,
  serialized_end=1320,
)

_WORLD_DOUBLEQUANTILE = _descriptor.Descriptor(
  name='DoubleQuantile',
  full_name='World.World.DoubleQuantile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='World.World.DoubleQuantile.key', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='World.World.DoubleQuantile.value', index=1,
      number=2, type=1, cpp_type=5, label=2,
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
  serialized_start=1322,
  serialized_end=1366,
)

_WORLD_DOUBLEMATRIXWITHQUANTILES = _descriptor.Descriptor(
  name='DoubleMatrixWithQuantiles',
  full_name='World.World.DoubleMatrixWithQuantiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quantiles', full_name='World.World.DoubleMatrixWithQuantiles.quantiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='World.World.DoubleMatrixWithQuantiles.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1368,
  serialized_end=1481,
)

_WORLD = _descriptor.Descriptor(
  name='World',
  full_name='World.World',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='World.World.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='World.World.width', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='World.World.height', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heightMapData', full_name='World.World.heightMapData', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heightMapTh_sea', full_name='World.World.heightMapTh_sea', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heightMapTh_plain', full_name='World.World.heightMapTh_plain', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heightMapTh_hill', full_name='World.World.heightMapTh_hill', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plates', full_name='World.World.plates', index=7,
      number=30, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ocean', full_name='World.World.ocean', index=8,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sea_depth', full_name='World.World.sea_depth', index=9,
      number=29, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biome', full_name='World.World.biome', index=10,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='World.World.humidity', index=11,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='irrigation', full_name='World.World.irrigation', index=12,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permeabilityData', full_name='World.World.permeabilityData', index=13,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permeability_low', full_name='World.World.permeability_low', index=14,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permeability_med', full_name='World.World.permeability_med', index=15,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watermapData', full_name='World.World.watermapData', index=16,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watermap_creek', full_name='World.World.watermap_creek', index=17,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watermap_river', full_name='World.World.watermap_river', index=18,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watermap_mainriver', full_name='World.World.watermap_mainriver', index=19,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precipitationData', full_name='World.World.precipitationData', index=20,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precipitation_low', full_name='World.World.precipitation_low', index=21,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precipitation_med', full_name='World.World.precipitation_med', index=22,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperatureData', full_name='World.World.temperatureData', index=23,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_polar', full_name='World.World.temperature_polar', index=24,
      number=23, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_alpine', full_name='World.World.temperature_alpine', index=25,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_boreal', full_name='World.World.temperature_boreal', index=26,
      number=25, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_cool', full_name='World.World.temperature_cool', index=27,
      number=26, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_warm', full_name='World.World.temperature_warm', index=28,
      number=27, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature_subtropical', full_name='World.World.temperature_subtropical', index=29,
      number=28, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WORLD_DOUBLEROW, _WORLD_BOOLEANROW, _WORLD_INTEGERROW, _WORLD_BYTEROW, _WORLD_DOUBLEMATRIX, _WORLD_BOOLEANMATRIX, _WORLD_INTEGERMATRIX, _WORLD_DOUBLEQUANTILE, _WORLD_DOUBLEMATRIXWITHQUANTILES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=1481,
)

_WORLD_DOUBLEROW.containing_type = _WORLD;
_WORLD_BOOLEANROW.containing_type = _WORLD;
_WORLD_INTEGERROW.containing_type = _WORLD;
_WORLD_BYTEROW.containing_type = _WORLD;
_WORLD_DOUBLEMATRIX.fields_by_name['rows'].message_type = _WORLD_DOUBLEROW
_WORLD_DOUBLEMATRIX.containing_type = _WORLD;
_WORLD_BOOLEANMATRIX.fields_by_name['rows'].message_type = _WORLD_BOOLEANROW
_WORLD_BOOLEANMATRIX.containing_type = _WORLD;
_WORLD_INTEGERMATRIX.fields_by_name['rows'].message_type = _WORLD_INTEGERROW
_WORLD_INTEGERMATRIX.containing_type = _WORLD;
_WORLD_DOUBLEQUANTILE.containing_type = _WORLD;
_WORLD_DOUBLEMATRIXWITHQUANTILES.fields_by_name['quantiles'].message_type = _WORLD_DOUBLEQUANTILE
_WORLD_DOUBLEMATRIXWITHQUANTILES.fields_by_name['rows'].message_type = _WORLD_DOUBLEROW
_WORLD_DOUBLEMATRIXWITHQUANTILES.containing_type = _WORLD;
_WORLD.fields_by_name['heightMapData'].message_type = _WORLD_DOUBLEMATRIX
_WORLD.fields_by_name['plates'].message_type = _WORLD_INTEGERMATRIX
_WORLD.fields_by_name['ocean'].message_type = _WORLD_BOOLEANMATRIX
_WORLD.fields_by_name['sea_depth'].message_type = _WORLD_DOUBLEMATRIX
_WORLD.fields_by_name['biome'].message_type = _WORLD_INTEGERMATRIX
_WORLD.fields_by_name['humidity'].message_type = _WORLD_DOUBLEMATRIXWITHQUANTILES
_WORLD.fields_by_name['irrigation'].message_type = _WORLD_DOUBLEMATRIX
_WORLD.fields_by_name['permeabilityData'].message_type = _WORLD_DOUBLEMATRIX
_WORLD.fields_by_name['watermapData'].message_type = _WORLD_DOUBLEMATRIX
_WORLD.fields_by_name['precipitationData'].message_type = _WORLD_DOUBLEMATRIX
_WORLD.fields_by_name['temperatureData'].message_type = _WORLD_DOUBLEMATRIX
DESCRIPTOR.message_types_by_name['World'] = _WORLD

class World(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class DoubleRow(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_DOUBLEROW

    # @@protoc_insertion_point(class_scope:World.World.DoubleRow)

  class BooleanRow(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_BOOLEANROW

    # @@protoc_insertion_point(class_scope:World.World.BooleanRow)

  class IntegerRow(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_INTEGERROW

    # @@protoc_insertion_point(class_scope:World.World.IntegerRow)

  class ByteRow(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_BYTEROW

    # @@protoc_insertion_point(class_scope:World.World.ByteRow)

  class DoubleMatrix(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_DOUBLEMATRIX

    # @@protoc_insertion_point(class_scope:World.World.DoubleMatrix)

  class BooleanMatrix(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_BOOLEANMATRIX

    # @@protoc_insertion_point(class_scope:World.World.BooleanMatrix)

  class IntegerMatrix(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_INTEGERMATRIX

    # @@protoc_insertion_point(class_scope:World.World.IntegerMatrix)

  class DoubleQuantile(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_DOUBLEQUANTILE

    # @@protoc_insertion_point(class_scope:World.World.DoubleQuantile)

  class DoubleMatrixWithQuantiles(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _WORLD_DOUBLEMATRIXWITHQUANTILES

    # @@protoc_insertion_point(class_scope:World.World.DoubleMatrixWithQuantiles)
  DESCRIPTOR = _WORLD

  # @@protoc_insertion_point(class_scope:World.World)


# @@protoc_insertion_point(module_scope)
