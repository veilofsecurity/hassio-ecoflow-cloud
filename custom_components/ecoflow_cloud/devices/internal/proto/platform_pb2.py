# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: platform.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eplatform.proto\"i\n\nEnergyItem\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x17\n\nwatth_type\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\r\n\x05watth\x18\x03 \x03(\rB\x0c\n\n_timestampB\r\n\x0b_watth_type\"n\n\x11\x45nergyTotalReport\x12\x16\n\twatth_seq\x18\x01 \x01(\rH\x00\x88\x01\x01\x12$\n\nwatth_item\x18\x02 \x01(\x0b\x32\x0b.EnergyItemH\x01\x88\x01\x01\x42\x0c\n\n_watth_seqB\r\n\x0b_watth_item\"_\n\x16\x42\x61tchEnergyTotalReport\x12\x16\n\twatth_seq\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x1f\n\nwatth_item\x18\x02 \x03(\x0b\x32\x0b.EnergyItemB\x0c\n\n_watth_seq\"\x84\x01\n\x14\x45nergyTotalReportAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x16\n\twatth_seq\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x17\n\nwatth_type\x18\x03 \x01(\rH\x02\x88\x01\x01\x42\t\n\x07_resultB\x0c\n\n_watth_seqB\r\n\x0b_watth_type\"\x91\x01\n\x0f\x45ventRecordItem\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x13\n\x06sys_ms\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x15\n\x08\x65vent_no\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x14\n\x0c\x65vent_detail\x18\x04 \x03(\x02\x42\x0c\n\n_timestampB\t\n\x07_sys_msB\x0b\n\t_event_no\"\x85\x01\n\x11\x45ventRecordReport\x12\x16\n\tevent_ver\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x16\n\tevent_seq\x18\x02 \x01(\rH\x01\x88\x01\x01\x12$\n\nevent_item\x18\x03 \x03(\x0b\x32\x10.EventRecordItemB\x0c\n\n_event_verB\x0c\n\n_event_seq\"\x8a\x01\n\x12\x45ventInfoReportAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x16\n\tevent_seq\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x1b\n\x0e\x65vent_item_num\x18\x03 \x01(\rH\x02\x88\x01\x01\x42\t\n\x07_resultB\x0c\n\n_event_seqB\x11\n\x0f_event_item_num\",\n\x0eProductNameSet\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"3\n\x11ProductNameSetAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x42\t\n\x07_result\"\x10\n\x0eProductNameGet\"/\n\x11ProductNameGetAck\x12\x11\n\x04name\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\x0c\n\nRTCTimeGet\"Y\n\rRTCTimeGetAck\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x15\n\x08timezone\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_timestampB\x0b\n\t_timezone\"V\n\nRTCTimeSet\x12\x16\n\ttimestamp\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x15\n\x08timezone\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_timestampB\x0b\n\t_timezone\"/\n\rRTCTimeSetAck\x12\x13\n\x06result\x18\x01 \x01(\rH\x00\x88\x01\x01\x42\t\n\x07_result\"T\n\x14\x63ountry_town_message\x12\x14\n\x07\x63ountry\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04town\x18\x02 \x01(\rH\x01\x88\x01\x01\x42\n\n\x08_countryB\x07\n\x05_town*N\n\tPlCmdSets\x12\x14\n\x10PL_NONE_CMD_SETS\x10\x00\x12\x15\n\x11PL_BASIC_CMD_SETS\x10\x01\x12\x14\n\x0fPL_EXT_CMD_SETS\x10\xfe\x01*F\n\x07PlCmdId\x12\x12\n\x0ePL_CMD_ID_NONE\x10\x00\x12\x12\n\x0ePL_CMD_ID_XLOG\x10\x10\x12\x13\n\x0fPL_CMD_ID_WATTH\x10 b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'platform_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLCMDSETS._serialized_start=1388
  _PLCMDSETS._serialized_end=1466
  _PLCMDID._serialized_start=1468
  _PLCMDID._serialized_end=1538
  _ENERGYITEM._serialized_start=18
  _ENERGYITEM._serialized_end=123
  _ENERGYTOTALREPORT._serialized_start=125
  _ENERGYTOTALREPORT._serialized_end=235
  _BATCHENERGYTOTALREPORT._serialized_start=237
  _BATCHENERGYTOTALREPORT._serialized_end=332
  _ENERGYTOTALREPORTACK._serialized_start=335
  _ENERGYTOTALREPORTACK._serialized_end=467
  _EVENTRECORDITEM._serialized_start=470
  _EVENTRECORDITEM._serialized_end=615
  _EVENTRECORDREPORT._serialized_start=618
  _EVENTRECORDREPORT._serialized_end=751
  _EVENTINFOREPORTACK._serialized_start=754
  _EVENTINFOREPORTACK._serialized_end=892
  _PRODUCTNAMESET._serialized_start=894
  _PRODUCTNAMESET._serialized_end=938
  _PRODUCTNAMESETACK._serialized_start=940
  _PRODUCTNAMESETACK._serialized_end=991
  _PRODUCTNAMEGET._serialized_start=993
  _PRODUCTNAMEGET._serialized_end=1009
  _PRODUCTNAMEGETACK._serialized_start=1011
  _PRODUCTNAMEGETACK._serialized_end=1058
  _RTCTIMEGET._serialized_start=1060
  _RTCTIMEGET._serialized_end=1072
  _RTCTIMEGETACK._serialized_start=1074
  _RTCTIMEGETACK._serialized_end=1163
  _RTCTIMESET._serialized_start=1165
  _RTCTIMESET._serialized_end=1251
  _RTCTIMESETACK._serialized_start=1253
  _RTCTIMESETACK._serialized_end=1300
  _COUNTRY_TOWN_MESSAGE._serialized_start=1302
  _COUNTRY_TOWN_MESSAGE._serialized_end=1386
# @@protoc_insertion_point(module_scope)
