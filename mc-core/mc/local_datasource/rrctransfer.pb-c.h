/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: rrctransfer.proto */

#ifndef PROTOBUF_C_rrctransfer_2eproto__INCLUDED
#define PROTOBUF_C_rrctransfer_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003002 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif

#include "google/protobuf/wrappers.pb-c.h"
#include "rrc_general_message_types.pb-c.h"

typedef struct _StreamingProtobufs__UENRMeasurementExtIEs StreamingProtobufs__UENRMeasurementExtIEs;
typedef struct _StreamingProtobufs__UENRMeasurement StreamingProtobufs__UENRMeasurement;
typedef struct _StreamingProtobufs__SplitSRBExtIEs StreamingProtobufs__SplitSRBExtIEs;
typedef struct _StreamingProtobufs__DeliveryStatusExtIEs StreamingProtobufs__DeliveryStatusExtIEs;
typedef struct _StreamingProtobufs__DeliveryStatus StreamingProtobufs__DeliveryStatus;
typedef struct _StreamingProtobufs__SplitSRB StreamingProtobufs__SplitSRB;
typedef struct _StreamingProtobufs__RRCTransferIEs StreamingProtobufs__RRCTransferIEs;
typedef struct _StreamingProtobufs__RRCTransfer StreamingProtobufs__RRCTransfer;


/* --- enums --- */

typedef enum _StreamingProtobufs__SplitSRB__SRBType {
  STREAMING_PROTOBUFS__SPLIT_SRB__SRBTYPE__protobuf_unspecified = 0,
  STREAMING_PROTOBUFS__SPLIT_SRB__SRBTYPE__srb1 = 1,
  STREAMING_PROTOBUFS__SPLIT_SRB__SRBTYPE__srb2 = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(STREAMING_PROTOBUFS__SPLIT_SRB__SRBTYPE)
} StreamingProtobufs__SplitSRB__SRBType;

/* --- messages --- */

struct  _StreamingProtobufs__UENRMeasurementExtIEs
{
  ProtobufCMessage base;
};
#define STREAMING_PROTOBUFS__UENRMEASUREMENT__EXT_IES__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__uenrmeasurement__ext_ies__descriptor) \
     }


struct  _StreamingProtobufs__UENRMeasurement
{
  ProtobufCMessage base;
  StreamingProtobufs__RRCContainer *uenrmeasurements;
  size_t n_ie_extensions;
  StreamingProtobufs__UENRMeasurementExtIEs **ie_extensions;
};
#define STREAMING_PROTOBUFS__UENRMEASUREMENT__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__uenrmeasurement__descriptor) \
    , NULL, 0,NULL }


struct  _StreamingProtobufs__SplitSRBExtIEs
{
  ProtobufCMessage base;
};
#define STREAMING_PROTOBUFS__SPLIT_SRB__EXT_IES__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__split_srb__ext_ies__descriptor) \
     }


struct  _StreamingProtobufs__DeliveryStatusExtIEs
{
  ProtobufCMessage base;
};
#define STREAMING_PROTOBUFS__DELIVERY_STATUS__EXT_IES__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__delivery_status__ext_ies__descriptor) \
     }


struct  _StreamingProtobufs__DeliveryStatus
{
  ProtobufCMessage base;
  uint32_t highestsuccessdeliveredpdcpsn;
  size_t n_ie_extensions;
  StreamingProtobufs__DeliveryStatusExtIEs **ie_extensions;
};
#define STREAMING_PROTOBUFS__DELIVERY_STATUS__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__delivery_status__descriptor) \
    , 0, 0,NULL }


struct  _StreamingProtobufs__SplitSRB
{
  ProtobufCMessage base;
  /*
   *UNNECESSARILY LONG - CANNOT COMPLETE 36.331 RRCContainer -
   *ALSO SPLIT SRB IS NOT SUPPORTED IN NOKIA gNB. THIS WILL BE A HEAVILY
   *UNNECESSARY EXERCISE TO DO PROTOBUF SPEC. FOR THE TIME BEING, IT IS
   *OK TO USE 38.331
   */
  StreamingProtobufs__RRCContainer *rrccontainer;
  StreamingProtobufs__SplitSRB__SRBType srbtype;
  StreamingProtobufs__DeliveryStatus *deliverystatus;
  size_t n_ie_extensions;
  StreamingProtobufs__SplitSRBExtIEs **ie_extensions;
};
#define STREAMING_PROTOBUFS__SPLIT_SRB__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__split_srb__descriptor) \
    , NULL, STREAMING_PROTOBUFS__SPLIT_SRB__SRBTYPE__protobuf_unspecified, NULL, 0,NULL }


struct  _StreamingProtobufs__RRCTransferIEs
{
  ProtobufCMessage base;
  uint32_t id_menb_ue_x2ap_id;
  uint32_t id_sgnb_ue_x2ap_id;
  StreamingProtobufs__SplitSRB *id_splitsrb;
  StreamingProtobufs__UENRMeasurement *id_uenrmeasurement;
  Google__Protobuf__UInt32Value *id_menb_ue_x2ap_id_extension;
};
#define STREAMING_PROTOBUFS__RRCTRANSFER__IES__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__rrctransfer__ies__descriptor) \
    , 0, 0, NULL, NULL, NULL }


struct  _StreamingProtobufs__RRCTransfer
{
  ProtobufCMessage base;
  StreamingProtobufs__RRCTransferIEs *rrctransfer_ies;
};
#define STREAMING_PROTOBUFS__RRCTRANSFER__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&streaming_protobufs__rrctransfer__descriptor) \
    , NULL }


/* StreamingProtobufs__UENRMeasurementExtIEs methods */
void   streaming_protobufs__uenrmeasurement__ext_ies__init
                     (StreamingProtobufs__UENRMeasurementExtIEs         *message);
size_t streaming_protobufs__uenrmeasurement__ext_ies__get_packed_size
                     (const StreamingProtobufs__UENRMeasurementExtIEs   *message);
size_t streaming_protobufs__uenrmeasurement__ext_ies__pack
                     (const StreamingProtobufs__UENRMeasurementExtIEs   *message,
                      uint8_t             *out);
size_t streaming_protobufs__uenrmeasurement__ext_ies__pack_to_buffer
                     (const StreamingProtobufs__UENRMeasurementExtIEs   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__UENRMeasurementExtIEs *
       streaming_protobufs__uenrmeasurement__ext_ies__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__uenrmeasurement__ext_ies__free_unpacked
                     (StreamingProtobufs__UENRMeasurementExtIEs *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__UENRMeasurement methods */
void   streaming_protobufs__uenrmeasurement__init
                     (StreamingProtobufs__UENRMeasurement         *message);
size_t streaming_protobufs__uenrmeasurement__get_packed_size
                     (const StreamingProtobufs__UENRMeasurement   *message);
size_t streaming_protobufs__uenrmeasurement__pack
                     (const StreamingProtobufs__UENRMeasurement   *message,
                      uint8_t             *out);
size_t streaming_protobufs__uenrmeasurement__pack_to_buffer
                     (const StreamingProtobufs__UENRMeasurement   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__UENRMeasurement *
       streaming_protobufs__uenrmeasurement__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__uenrmeasurement__free_unpacked
                     (StreamingProtobufs__UENRMeasurement *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__SplitSRBExtIEs methods */
void   streaming_protobufs__split_srb__ext_ies__init
                     (StreamingProtobufs__SplitSRBExtIEs         *message);
size_t streaming_protobufs__split_srb__ext_ies__get_packed_size
                     (const StreamingProtobufs__SplitSRBExtIEs   *message);
size_t streaming_protobufs__split_srb__ext_ies__pack
                     (const StreamingProtobufs__SplitSRBExtIEs   *message,
                      uint8_t             *out);
size_t streaming_protobufs__split_srb__ext_ies__pack_to_buffer
                     (const StreamingProtobufs__SplitSRBExtIEs   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__SplitSRBExtIEs *
       streaming_protobufs__split_srb__ext_ies__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__split_srb__ext_ies__free_unpacked
                     (StreamingProtobufs__SplitSRBExtIEs *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__DeliveryStatusExtIEs methods */
void   streaming_protobufs__delivery_status__ext_ies__init
                     (StreamingProtobufs__DeliveryStatusExtIEs         *message);
size_t streaming_protobufs__delivery_status__ext_ies__get_packed_size
                     (const StreamingProtobufs__DeliveryStatusExtIEs   *message);
size_t streaming_protobufs__delivery_status__ext_ies__pack
                     (const StreamingProtobufs__DeliveryStatusExtIEs   *message,
                      uint8_t             *out);
size_t streaming_protobufs__delivery_status__ext_ies__pack_to_buffer
                     (const StreamingProtobufs__DeliveryStatusExtIEs   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__DeliveryStatusExtIEs *
       streaming_protobufs__delivery_status__ext_ies__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__delivery_status__ext_ies__free_unpacked
                     (StreamingProtobufs__DeliveryStatusExtIEs *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__DeliveryStatus methods */
void   streaming_protobufs__delivery_status__init
                     (StreamingProtobufs__DeliveryStatus         *message);
size_t streaming_protobufs__delivery_status__get_packed_size
                     (const StreamingProtobufs__DeliveryStatus   *message);
size_t streaming_protobufs__delivery_status__pack
                     (const StreamingProtobufs__DeliveryStatus   *message,
                      uint8_t             *out);
size_t streaming_protobufs__delivery_status__pack_to_buffer
                     (const StreamingProtobufs__DeliveryStatus   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__DeliveryStatus *
       streaming_protobufs__delivery_status__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__delivery_status__free_unpacked
                     (StreamingProtobufs__DeliveryStatus *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__SplitSRB methods */
void   streaming_protobufs__split_srb__init
                     (StreamingProtobufs__SplitSRB         *message);
size_t streaming_protobufs__split_srb__get_packed_size
                     (const StreamingProtobufs__SplitSRB   *message);
size_t streaming_protobufs__split_srb__pack
                     (const StreamingProtobufs__SplitSRB   *message,
                      uint8_t             *out);
size_t streaming_protobufs__split_srb__pack_to_buffer
                     (const StreamingProtobufs__SplitSRB   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__SplitSRB *
       streaming_protobufs__split_srb__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__split_srb__free_unpacked
                     (StreamingProtobufs__SplitSRB *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__RRCTransferIEs methods */
void   streaming_protobufs__rrctransfer__ies__init
                     (StreamingProtobufs__RRCTransferIEs         *message);
size_t streaming_protobufs__rrctransfer__ies__get_packed_size
                     (const StreamingProtobufs__RRCTransferIEs   *message);
size_t streaming_protobufs__rrctransfer__ies__pack
                     (const StreamingProtobufs__RRCTransferIEs   *message,
                      uint8_t             *out);
size_t streaming_protobufs__rrctransfer__ies__pack_to_buffer
                     (const StreamingProtobufs__RRCTransferIEs   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__RRCTransferIEs *
       streaming_protobufs__rrctransfer__ies__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__rrctransfer__ies__free_unpacked
                     (StreamingProtobufs__RRCTransferIEs *message,
                      ProtobufCAllocator *allocator);
/* StreamingProtobufs__RRCTransfer methods */
void   streaming_protobufs__rrctransfer__init
                     (StreamingProtobufs__RRCTransfer         *message);
size_t streaming_protobufs__rrctransfer__get_packed_size
                     (const StreamingProtobufs__RRCTransfer   *message);
size_t streaming_protobufs__rrctransfer__pack
                     (const StreamingProtobufs__RRCTransfer   *message,
                      uint8_t             *out);
size_t streaming_protobufs__rrctransfer__pack_to_buffer
                     (const StreamingProtobufs__RRCTransfer   *message,
                      ProtobufCBuffer     *buffer);
StreamingProtobufs__RRCTransfer *
       streaming_protobufs__rrctransfer__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   streaming_protobufs__rrctransfer__free_unpacked
                     (StreamingProtobufs__RRCTransfer *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*StreamingProtobufs__UENRMeasurementExtIEs_Closure)
                 (const StreamingProtobufs__UENRMeasurementExtIEs *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__UENRMeasurement_Closure)
                 (const StreamingProtobufs__UENRMeasurement *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__SplitSRBExtIEs_Closure)
                 (const StreamingProtobufs__SplitSRBExtIEs *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__DeliveryStatusExtIEs_Closure)
                 (const StreamingProtobufs__DeliveryStatusExtIEs *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__DeliveryStatus_Closure)
                 (const StreamingProtobufs__DeliveryStatus *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__SplitSRB_Closure)
                 (const StreamingProtobufs__SplitSRB *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__RRCTransferIEs_Closure)
                 (const StreamingProtobufs__RRCTransferIEs *message,
                  void *closure_data);
typedef void (*StreamingProtobufs__RRCTransfer_Closure)
                 (const StreamingProtobufs__RRCTransfer *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor streaming_protobufs__uenrmeasurement__ext_ies__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__uenrmeasurement__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__split_srb__ext_ies__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__delivery_status__ext_ies__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__delivery_status__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__split_srb__descriptor;
extern const ProtobufCEnumDescriptor    streaming_protobufs__split_srb__srbtype__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__rrctransfer__ies__descriptor;
extern const ProtobufCMessageDescriptor streaming_protobufs__rrctransfer__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_rrctransfer_2eproto__INCLUDED */
