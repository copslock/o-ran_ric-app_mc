# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sgnb_release_confirm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import x2ap_common_types_pb2 as x2ap__common__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sgnb_release_confirm.proto',
  package='streaming_protobufs',
  syntax='proto3',
  serialized_options=_b('Z1gerrit.o-ran-sc.org/r/ric-plt/streaming-protobufs'),
  serialized_pb=_b('\n\x1asgnb_release_confirm.proto\x12\x13streaming_protobufs\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17x2ap_common_types.proto\"V\n\x12SgNBReleaseConfirm\x12@\n\x0bprotocolIEs\x18\x01 \x01(\x0b\x32+.streaming_protobufs.SgNBReleaseConfirm_IEs\"\xce\x02\n\x16SgNBReleaseConfirm_IEs\x12\x1a\n\x12id_MeNB_UE_X2AP_ID\x18\x01 \x01(\r\x12\x1a\n\x12id_SgNB_UE_X2AP_ID\x18\x02 \x01(\r\x12h\n&id_E_RABs_ToBeReleased_SgNBRelConfList\x18\x03 \x01(\x0b\x32\x38.streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConfList\x12N\n\x19id_CriticalityDiagnostics\x18\x04 \x01(\x0b\x32+.streaming_protobufs.CriticalityDiagnostics\x12\x42\n\x1cid_MeNB_UE_X2AP_ID_Extension\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"\x91\x01\n#E_RABs_ToBeReleased_SgNBRelConfList\x12j\n\'id_E_RABs_ToBeReleased_SgNBRelConf_Item\x18\x01 \x03(\x0b\x32\x39.streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item\"\xc9\x03\n$E_RABs_ToBeReleased_SgNBRelConf_Item\x12\x10\n\x08\x65_RAB_ID\x18\x01 \x01(\r\x12U\n\x1b\x65n_DC_ResourceConfiguration\x18\x02 \x01(\x0b\x32\x30.streaming_protobufs.EN_DC_ResourceConfiguration\x12_\n\x0fsgNBPDCPpresent\x18\x03 \x01(\x0b\x32\x44.streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresentH\x00\x12\x65\n\x12SgNBPDCPnotpresent\x18\x04 \x01(\x0b\x32G.streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentH\x00\x12V\n\riE_Extensions\x18\x05 \x03(\x0b\x32?.streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEsB\x18\n\x16resource_configuration\",\n*E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs\"\xbd\x01\n/E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent\x12\x44\n\x14uL_GTPtunnelEndpoint\x18\x01 \x01(\x0b\x32&.streaming_protobufs.GTPtunnelEndpoint\x12\x44\n\x14\x64L_GTPtunnelEndpoint\x18\x02 \x01(\x0b\x32&.streaming_protobufs.GTPtunnelEndpoint\"\x9a\x01\n2E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent\x12\x64\n\riE_Extensions\x18\x01 \x03(\x0b\x32M.streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs\":\n8E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEsB3Z1gerrit.o-ran-sc.org/r/ric-plt/streaming-protobufsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,x2ap__common__types__pb2.DESCRIPTOR,])




_SGNBRELEASECONFIRM = _descriptor.Descriptor(
  name='SgNBReleaseConfirm',
  full_name='streaming_protobufs.SgNBReleaseConfirm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocolIEs', full_name='streaming_protobufs.SgNBReleaseConfirm.protocolIEs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=108,
  serialized_end=194,
)


_SGNBRELEASECONFIRM_IES = _descriptor.Descriptor(
  name='SgNBReleaseConfirm_IEs',
  full_name='streaming_protobufs.SgNBReleaseConfirm_IEs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_MeNB_UE_X2AP_ID', full_name='streaming_protobufs.SgNBReleaseConfirm_IEs.id_MeNB_UE_X2AP_ID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_SgNB_UE_X2AP_ID', full_name='streaming_protobufs.SgNBReleaseConfirm_IEs.id_SgNB_UE_X2AP_ID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_E_RABs_ToBeReleased_SgNBRelConfList', full_name='streaming_protobufs.SgNBReleaseConfirm_IEs.id_E_RABs_ToBeReleased_SgNBRelConfList', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_CriticalityDiagnostics', full_name='streaming_protobufs.SgNBReleaseConfirm_IEs.id_CriticalityDiagnostics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_MeNB_UE_X2AP_ID_Extension', full_name='streaming_protobufs.SgNBReleaseConfirm_IEs.id_MeNB_UE_X2AP_ID_Extension', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=197,
  serialized_end=531,
)


_E_RABS_TOBERELEASED_SGNBRELCONFLIST = _descriptor.Descriptor(
  name='E_RABs_ToBeReleased_SgNBRelConfList',
  full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConfList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_E_RABs_ToBeReleased_SgNBRelConf_Item', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConfList.id_E_RABs_ToBeReleased_SgNBRelConf_Item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=534,
  serialized_end=679,
)


_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM = _descriptor.Descriptor(
  name='E_RABs_ToBeReleased_SgNBRelConf_Item',
  full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='e_RAB_ID', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item.e_RAB_ID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='en_DC_ResourceConfiguration', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item.en_DC_ResourceConfiguration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sgNBPDCPpresent', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item.sgNBPDCPpresent', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SgNBPDCPnotpresent', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item.SgNBPDCPnotpresent', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iE_Extensions', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item.iE_Extensions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
    _descriptor.OneofDescriptor(
      name='resource_configuration', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item.resource_configuration',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=682,
  serialized_end=1139,
)


_E_RABS_TOBERELEASED_SGNBRELCONF_ITEMEXTIES = _descriptor.Descriptor(
  name='E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs',
  full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1141,
  serialized_end=1185,
)


_E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPPRESENT = _descriptor.Descriptor(
  name='E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent',
  full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uL_GTPtunnelEndpoint', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent.uL_GTPtunnelEndpoint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dL_GTPtunnelEndpoint', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent.dL_GTPtunnelEndpoint', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1188,
  serialized_end=1377,
)


_E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENT = _descriptor.Descriptor(
  name='E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent',
  full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iE_Extensions', full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent.iE_Extensions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1380,
  serialized_end=1534,
)


_E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENTEXTIES = _descriptor.Descriptor(
  name='E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs',
  full_name='streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1536,
  serialized_end=1594,
)

_SGNBRELEASECONFIRM.fields_by_name['protocolIEs'].message_type = _SGNBRELEASECONFIRM_IES
_SGNBRELEASECONFIRM_IES.fields_by_name['id_E_RABs_ToBeReleased_SgNBRelConfList'].message_type = _E_RABS_TOBERELEASED_SGNBRELCONFLIST
_SGNBRELEASECONFIRM_IES.fields_by_name['id_CriticalityDiagnostics'].message_type = x2ap__common__types__pb2._CRITICALITYDIAGNOSTICS
_SGNBRELEASECONFIRM_IES.fields_by_name['id_MeNB_UE_X2AP_ID_Extension'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_E_RABS_TOBERELEASED_SGNBRELCONFLIST.fields_by_name['id_E_RABs_ToBeReleased_SgNBRelConf_Item'].message_type = _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['en_DC_ResourceConfiguration'].message_type = x2ap__common__types__pb2._EN_DC_RESOURCECONFIGURATION
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['sgNBPDCPpresent'].message_type = _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPPRESENT
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['SgNBPDCPnotpresent'].message_type = _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENT
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['iE_Extensions'].message_type = _E_RABS_TOBERELEASED_SGNBRELCONF_ITEMEXTIES
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.oneofs_by_name['resource_configuration'].fields.append(
  _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['sgNBPDCPpresent'])
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['sgNBPDCPpresent'].containing_oneof = _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.oneofs_by_name['resource_configuration']
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.oneofs_by_name['resource_configuration'].fields.append(
  _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['SgNBPDCPnotpresent'])
_E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.fields_by_name['SgNBPDCPnotpresent'].containing_oneof = _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM.oneofs_by_name['resource_configuration']
_E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPPRESENT.fields_by_name['uL_GTPtunnelEndpoint'].message_type = x2ap__common__types__pb2._GTPTUNNELENDPOINT
_E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPPRESENT.fields_by_name['dL_GTPtunnelEndpoint'].message_type = x2ap__common__types__pb2._GTPTUNNELENDPOINT
_E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENT.fields_by_name['iE_Extensions'].message_type = _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENTEXTIES
DESCRIPTOR.message_types_by_name['SgNBReleaseConfirm'] = _SGNBRELEASECONFIRM
DESCRIPTOR.message_types_by_name['SgNBReleaseConfirm_IEs'] = _SGNBRELEASECONFIRM_IES
DESCRIPTOR.message_types_by_name['E_RABs_ToBeReleased_SgNBRelConfList'] = _E_RABS_TOBERELEASED_SGNBRELCONFLIST
DESCRIPTOR.message_types_by_name['E_RABs_ToBeReleased_SgNBRelConf_Item'] = _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM
DESCRIPTOR.message_types_by_name['E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs'] = _E_RABS_TOBERELEASED_SGNBRELCONF_ITEMEXTIES
DESCRIPTOR.message_types_by_name['E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent'] = _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPPRESENT
DESCRIPTOR.message_types_by_name['E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent'] = _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENT
DESCRIPTOR.message_types_by_name['E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs'] = _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENTEXTIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SgNBReleaseConfirm = _reflection.GeneratedProtocolMessageType('SgNBReleaseConfirm', (_message.Message,), {
  'DESCRIPTOR' : _SGNBRELEASECONFIRM,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.SgNBReleaseConfirm)
  })
_sym_db.RegisterMessage(SgNBReleaseConfirm)

SgNBReleaseConfirm_IEs = _reflection.GeneratedProtocolMessageType('SgNBReleaseConfirm_IEs', (_message.Message,), {
  'DESCRIPTOR' : _SGNBRELEASECONFIRM_IES,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.SgNBReleaseConfirm_IEs)
  })
_sym_db.RegisterMessage(SgNBReleaseConfirm_IEs)

E_RABs_ToBeReleased_SgNBRelConfList = _reflection.GeneratedProtocolMessageType('E_RABs_ToBeReleased_SgNBRelConfList', (_message.Message,), {
  'DESCRIPTOR' : _E_RABS_TOBERELEASED_SGNBRELCONFLIST,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConfList)
  })
_sym_db.RegisterMessage(E_RABs_ToBeReleased_SgNBRelConfList)

E_RABs_ToBeReleased_SgNBRelConf_Item = _reflection.GeneratedProtocolMessageType('E_RABs_ToBeReleased_SgNBRelConf_Item', (_message.Message,), {
  'DESCRIPTOR' : _E_RABS_TOBERELEASED_SGNBRELCONF_ITEM,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_Item)
  })
_sym_db.RegisterMessage(E_RABs_ToBeReleased_SgNBRelConf_Item)

E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs = _reflection.GeneratedProtocolMessageType('E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs', (_message.Message,), {
  'DESCRIPTOR' : _E_RABS_TOBERELEASED_SGNBRELCONF_ITEMEXTIES,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs)
  })
_sym_db.RegisterMessage(E_RABs_ToBeReleased_SgNBRelConf_ItemExtIEs)

E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent = _reflection.GeneratedProtocolMessageType('E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent', (_message.Message,), {
  'DESCRIPTOR' : _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPPRESENT,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent)
  })
_sym_db.RegisterMessage(E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPpresent)

E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent = _reflection.GeneratedProtocolMessageType('E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent', (_message.Message,), {
  'DESCRIPTOR' : _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENT,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent)
  })
_sym_db.RegisterMessage(E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresent)

E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs = _reflection.GeneratedProtocolMessageType('E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs', (_message.Message,), {
  'DESCRIPTOR' : _E_RABS_TOBERELEASED_SGNBRELCONF_SGNBPDCPNOTPRESENTEXTIES,
  '__module__' : 'sgnb_release_confirm_pb2'
  # @@protoc_insertion_point(class_scope:streaming_protobufs.E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs)
  })
_sym_db.RegisterMessage(E_RABs_ToBeReleased_SgNBRelConf_SgNBPDCPnotpresentExtIEs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
