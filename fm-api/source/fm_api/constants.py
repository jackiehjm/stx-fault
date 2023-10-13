#
# Copyright (c) 2013-2023 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

# -*- encoding: utf-8 -*-
#
#
# Author: Tao Liu
#
# This file contains CGTS alarm definitions.  The alarm ids that used by Python
# applications are defined here. For a completed alarm id list see the alarm ids
# that used by the C/C++ applications defined in
# fm-common/sources/fmAlarm.h

################################################################################
#
# Please make sure that all FM_ALARM_ID_xxx entries in this file
# have a corresponding Alarm record entry in file events.yaml
#
################################################################################

# alarm sub entity types
FM_ENTITY_TYPE_SYSTEM = 'system'
FM_ENTITY_TYPE_HOST = 'host'
FM_ENTITY_TYPE_PORT = 'port'
FM_ENTITY_TYPE_INTERFACE = 'interface'
FM_ENTITY_TYPE_SERVICE = 'service'
FM_ENTITY_TYPE_AGENT = 'agent'
FM_ENTITY_TYPE_PROVIDERNET = 'providernet'
FM_ENTITY_TYPE_INSTANCE = 'instance'
FM_ENTITY_TYPE_CLUSTER = 'cluster'
FM_ENTITY_TYPE_NTP = 'ntp'
FM_ENTITY_TYPE_ML2DRIVER = 'ml2driver'
FM_ENTITY_TYPE_K8S = 'kubernetes'
FM_ENTITY_TYPE_BGP_PEER = "bgp-peer"
FM_ENTITY_TYPE_STORAGE_BACKEND = 'storage_backend'
FM_ENTITY_TYPE_IMAGE_CONVERSION = 'fs_name'
FM_ENTITY_TYPE_SUBCLOUD = 'subcloud'
FM_ENTITY_TYPE_APPLICATION = 'k8s_application'
FM_ENTITY_TYPE_CERTIFICATE = 'certificate'
FM_ENTITY_TYPE_SYSTEM_PEER = 'system_peer'
FM_ENTITY_TYPE_SUBCLOUD_PEER_GROUP = 'subcloud_peer_group'

# alarm service sub entity values
FM_SERVICE_NETWORKING = 'networking'

#  alarm_id = <Alarm Group ID>.<Alarm Event ID>
#  <Alarm Group ID> = 000 - 999
#  <Alarm Event ID> = 000  999
ALARM_GROUP_GENERAL = "100"
ALARM_GROUP_MAINTENANCE = "200"
ALARM_GROUP_BACKUP_RESTORE = "210"
ALARM_GROUP_SYSCONFIG = "250"
ALARM_GROUP_DEPLOYMENT = "260"
ALARM_GROUP_HOST_SERVICES = "270"
ALARM_GROUP_HYPERVISOR = "275"
ALARM_GROUP_DISTRIBUTED_CLOUD = "280"
ALARM_GROUP_NETWORK = "300"
ALARM_GROUP_HA = "400"
ALARM_GROUP_SECURITY = "500"
ALARM_GROUP_LICENSING = "600"
ALARM_GROUP_VM = "700"
ALARM_GROUP_APPLICATION = "750"
ALARM_GROUP_STORAGE = "800"
ALARM_GROUP_K8S = "850"
ALARM_GROUP_SW_MGMT = "900"

# General Alarm id
FM_ALARM_ID_FS_USAGE = ALARM_GROUP_GENERAL + ".104"
FM_ALARM_ID_IMAGE_CONVERSION = ALARM_GROUP_GENERAL + ".105"
FM_ALARM_ID_CONTROLLERS_KERNEL_MISMATCH = ALARM_GROUP_GENERAL + ".120"
FM_ALARM_ID_PROVISIONED_KERNEL_MISMATCH = ALARM_GROUP_GENERAL + ".121"

# Maintenance Log id
FM_LOG_ID_HOST_DISCOVERED = ALARM_GROUP_MAINTENANCE + ".020"

# System Config Alarm id
FM_ALARM_ID_SYSCONFIG_OUT_OF_DATE = ALARM_GROUP_SYSCONFIG + ".001"

# This CONFIG_REQD alarm ID is deprecated and commented out to avoid its
# alarm id .010 from being unintentinally reused for some unrelated purpose.
# Deprecation followed the removal of the compute-config-complete command.
# FM_ALARM_ID_CONFIG_REQD = ALARM_GROUP_SYSCONFIG + ".010"

# Backup/Restore Alarm id
FM_ALARM_ID_BACKUP_IN_PROGRESS = ALARM_GROUP_BACKUP_RESTORE + ".001"
FM_ALARM_ID_RESTORE_IN_PROGRESS = ALARM_GROUP_BACKUP_RESTORE + ".002"

# Backup/Restore Log id
FM_LOG_ID_RESTORE_COMPLETE = ALARM_GROUP_BACKUP_RESTORE + ".101"

# Network alarm id
FM_ALARM_ID_NETWORK_PORT = ALARM_GROUP_NETWORK + ".001"
FM_ALARM_ID_NETWORK_INTERFACE = ALARM_GROUP_NETWORK + ".002"
FM_ALARM_ID_NETWORK_AGENT = ALARM_GROUP_NETWORK + ".003"
FM_ALARM_ID_NETWORK_PROVIDERNET = ALARM_GROUP_NETWORK + ".004"
FM_ALARM_ID_NETWORK_PROVIDERNET_CONNECTIVITY = ALARM_GROUP_NETWORK + ".005"
FM_ALARM_ID_NETWORK_ML2_DRIVER = ALARM_GROUP_NETWORK + ".010"
FM_ALARM_ID_NETWORK_OPENFLOW_CONTROLLER = ALARM_GROUP_NETWORK + ".012"
FM_ALARM_ID_NETWORK_OVSDB_MANAGER = ALARM_GROUP_NETWORK + ".014"
FM_ALARM_ID_NETWORK_BGP_PEER = ALARM_GROUP_NETWORK + ".016"

# Storage alarm id
FM_ALARM_ID_STORAGE_CEPH_CRITICAL = ALARM_GROUP_STORAGE + ".010"
FM_ALARM_ID_STORAGE_CEPH_MAJOR = ALARM_GROUP_STORAGE + ".011"
FM_ALARM_ID_STORAGE_CEPH = ALARM_GROUP_STORAGE + ".001"
FM_ALARM_ID_STORAGE_IMAGE = ALARM_GROUP_STORAGE + ".002"
FM_ALARM_ID_STORAGE_CINDER_IO_BUILDING = ALARM_GROUP_STORAGE + ".100"
FM_ALARM_ID_STORAGE_CINDER_IO_LIMITING = ALARM_GROUP_STORAGE + ".101"
# Alarm .103 is reserved for LVM thin pool metadata alarm
FM_ALARM_ID_STORAGE_BACKEND_FAILED = ALARM_GROUP_STORAGE + ".104"

# Kubernetes Resource Alarms
FM_ALARM_ID_K8S_RESOURCE_PV = ALARM_GROUP_K8S + ".001"

# Deployment Alarm id

FM_ALARM_ID_UNRECONCILED_RESOURCE = ALARM_GROUP_DEPLOYMENT + ".001"
FM_ALARM_ID_UNSYNCHRONIZED_RESOURCE = ALARM_GROUP_DEPLOYMENT + ".002"

# Host-Services log id
FM_LOG_ID_HOST_SERVICES_FAILED = ALARM_GROUP_HOST_SERVICES + ".101"
FM_LOG_ID_HOST_SERVICES_ENABLED = ALARM_GROUP_HOST_SERVICES + ".102"
FM_LOG_ID_HOST_SERVICES_DISABLED = ALARM_GROUP_HOST_SERVICES + ".103"

# Hypervisor log id
FM_LOG_ID_HYPERVISOR_STATE_CHANGE = ALARM_GROUP_HYPERVISOR + ".001"

# Distributed Cloud alarm id
FM_ALARM_ID_DC_SUBCLOUD_OFFLINE = ALARM_GROUP_DISTRIBUTED_CLOUD + ".001"
FM_ALARM_ID_DC_SUBCLOUD_RESOURCE_OUT_OF_SYNC = ALARM_GROUP_DISTRIBUTED_CLOUD + ".002"
FM_ALARM_ID_DC_SUBCLOUD_BACKUP_FAILED = ALARM_GROUP_DISTRIBUTED_CLOUD + ".003"
FM_ALARM_ID_DC_SYSTEM_PEER_HEARTBEAT_FAILED = ALARM_GROUP_DISTRIBUTED_CLOUD + ".004"
FM_ALARM_ID_DC_SUBCLOUD_PEER_GROUP_NOT_MANAGED = ALARM_GROUP_DISTRIBUTED_CLOUD + ".005"

# HA alarm id
FM_ALARM_ID_HA_SERVICE_GROUP_STATE = ALARM_GROUP_HA + ".001"
FM_ALARM_ID_HA_SERVICE_GROUP_REDUNDANCY = ALARM_GROUP_HA + ".002"
FM_ALARM_ID_HA_NODE_LICENSE = ALARM_GROUP_HA + ".003"
FM_ALARM_ID_HA_COMMUNICATION_FAILURE = ALARM_GROUP_HA + ".005"

# VM alarm id
FM_ALARM_ID_VM_FAILED = ALARM_GROUP_VM + ".001"
FM_ALARM_ID_VM_PAUSED = ALARM_GROUP_VM + ".002"
FM_ALARM_ID_VM_SUSPENDED = ALARM_GROUP_VM + ".003"
FM_ALARM_ID_VM_STOPPED = ALARM_GROUP_VM + ".004"
FM_ALARM_ID_VM_REBOOTING = ALARM_GROUP_VM + ".005"
FM_ALARM_ID_VM_REBUILDING = ALARM_GROUP_VM + ".006"
FM_ALARM_ID_VM_EVACUATING = ALARM_GROUP_VM + ".007"
FM_ALARM_ID_VM_LIVE_MIGRATING = ALARM_GROUP_VM + ".008"
FM_ALARM_ID_VM_COLD_MIGRATING = ALARM_GROUP_VM + ".009"
FM_ALARM_ID_VM_COLD_MIGRATED = ALARM_GROUP_VM + ".010"
FM_ALARM_ID_VM_COLD_MIGRATE_REVERTING = ALARM_GROUP_VM + ".011"
FM_ALARM_ID_VM_RESIZING = ALARM_GROUP_VM + ".012"
FM_ALARM_ID_VM_RESIZED = ALARM_GROUP_VM + ".013"
FM_ALARM_ID_VM_RESIZE_REVERTING = ALARM_GROUP_VM + ".014"
FM_ALARM_ID_VM_GUEST_HEARTBEAT = ALARM_GROUP_VM + ".015"
FM_ALARM_ID_VM_MULTI_NODE_RECOVERY_MODE = ALARM_GROUP_VM + ".016"
FM_ALARM_ID_VM_GROUP_POLICY_CONFLICT = ALARM_GROUP_VM + ".017"

# Application alarm id
FM_ALARM_ID_APPLICATION_UPLOAD_FAILED = ALARM_GROUP_APPLICATION + ".001"
FM_ALARM_ID_APPLICATION_APPLY_FAILED = ALARM_GROUP_APPLICATION + ".002"
FM_ALARM_ID_APPLICATION_REMOVE_FAILED = ALARM_GROUP_APPLICATION + ".003"
FM_ALARM_ID_APPLICATION_APPLYING = ALARM_GROUP_APPLICATION + ".004"
FM_ALARM_ID_APPLICATION_UPDATING = ALARM_GROUP_APPLICATION + ".005"
FM_ALARM_ID_APPLICATION_REAPPLY_PENDING = ALARM_GROUP_APPLICATION + ".006"

# VM log id
FM_LOG_ID_VM_ENABLED = ALARM_GROUP_VM + ".101"
FM_LOG_ID_VM_FAILED = ALARM_GROUP_VM + ".102"
FM_LOG_ID_VM_CREATE = ALARM_GROUP_VM + ".103"
FM_LOG_ID_VM_CREATING = ALARM_GROUP_VM + ".104"
FM_LOG_ID_VM_CREATE_REJECTED = ALARM_GROUP_VM + ".105"
FM_LOG_ID_VM_CREATE_CANCELLED = ALARM_GROUP_VM + ".106"
FM_LOG_ID_VM_CREATE_FAILED = ALARM_GROUP_VM + ".107"
FM_LOG_ID_VM_CREATED = ALARM_GROUP_VM + ".108"
FM_LOG_ID_VM_DELETE = ALARM_GROUP_VM + ".109"
FM_LOG_ID_VM_DELETING = ALARM_GROUP_VM + ".110"
FM_LOG_ID_VM_DELETE_REJECTED = ALARM_GROUP_VM + ".111"
FM_LOG_ID_VM_DELETE_CANCELLED = ALARM_GROUP_VM + ".112"
FM_LOG_ID_VM_DELETE_FAILED = ALARM_GROUP_VM + ".113"
FM_LOG_ID_VM_DELETED = ALARM_GROUP_VM + ".114"
FM_LOG_ID_VM_PAUSE = ALARM_GROUP_VM + ".115"
FM_LOG_ID_VM_PAUSING = ALARM_GROUP_VM + ".116"
FM_LOG_ID_VM_PAUSE_REJECTED = ALARM_GROUP_VM + ".117"
FM_LOG_ID_VM_PAUSE_CANCELLED = ALARM_GROUP_VM + ".118"
FM_LOG_ID_VM_PAUSE_FAILED = ALARM_GROUP_VM + ".119"
FM_LOG_ID_VM_PAUSED = ALARM_GROUP_VM + ".120"
FM_LOG_ID_VM_UNPAUSE = ALARM_GROUP_VM + ".121"
FM_LOG_ID_VM_UNPAUSING = ALARM_GROUP_VM + ".122"
FM_LOG_ID_VM_UNPAUSE_REJECTED = ALARM_GROUP_VM + ".123"
FM_LOG_ID_VM_UNPAUSE_CANCELLED = ALARM_GROUP_VM + ".124"
FM_LOG_ID_VM_UNPAUSE_FAILED = ALARM_GROUP_VM + ".125"
FM_LOG_ID_VM_UNPAUSED = ALARM_GROUP_VM + ".126"
FM_LOG_ID_VM_SUSPEND = ALARM_GROUP_VM + ".127"
FM_LOG_ID_VM_SUSPENDING = ALARM_GROUP_VM + ".128"
FM_LOG_ID_VM_SUSPEND_REJECTED = ALARM_GROUP_VM + ".129"
FM_LOG_ID_VM_SUSPEND_CANCELLED = ALARM_GROUP_VM + ".130"
FM_LOG_ID_VM_SUSPEND_FAILED = ALARM_GROUP_VM + ".131"
FM_LOG_ID_VM_SUSPENDED = ALARM_GROUP_VM + ".132"
FM_LOG_ID_VM_RESUME = ALARM_GROUP_VM + ".133"
FM_LOG_ID_VM_RESUMING = ALARM_GROUP_VM + ".134"
FM_LOG_ID_VM_RESUME_REJECTED = ALARM_GROUP_VM + ".135"
FM_LOG_ID_VM_RESUME_CANCELLED = ALARM_GROUP_VM + ".136"
FM_LOG_ID_VM_RESUME_FAILED = ALARM_GROUP_VM + ".137"
FM_LOG_ID_VM_RESUMED = ALARM_GROUP_VM + ".138"
FM_LOG_ID_VM_START = ALARM_GROUP_VM + ".139"
FM_LOG_ID_VM_STARTING = ALARM_GROUP_VM + ".140"
FM_LOG_ID_VM_START_REJECTED = ALARM_GROUP_VM + ".141"
FM_LOG_ID_VM_START_CANCELLED = ALARM_GROUP_VM + ".142"
FM_LOG_ID_VM_START_FAILED = ALARM_GROUP_VM + ".143"
FM_LOG_ID_VM_STARTED = ALARM_GROUP_VM + ".144"
FM_LOG_ID_VM_STOP = ALARM_GROUP_VM + ".145"
FM_LOG_ID_VM_STOPPING = ALARM_GROUP_VM + ".146"
FM_LOG_ID_VM_STOP_REJECTED = ALARM_GROUP_VM + ".147"
FM_LOG_ID_VM_STOP_CANCELLED = ALARM_GROUP_VM + ".148"
FM_LOG_ID_VM_STOP_FAILED = ALARM_GROUP_VM + ".149"
FM_LOG_ID_VM_STOPPED = ALARM_GROUP_VM + ".150"
FM_LOG_ID_VM_LIVE_MIGRATE = ALARM_GROUP_VM + ".151"
FM_LOG_ID_VM_LIVE_MIGRATING = ALARM_GROUP_VM + ".152"
FM_LOG_ID_VM_LIVE_MIGRATE_REJECTED = ALARM_GROUP_VM + ".153"
FM_LOG_ID_VM_LIVE_MIGRATE_CANCELLED = ALARM_GROUP_VM + ".154"
FM_LOG_ID_VM_LIVE_MIGRATE_FAILED = ALARM_GROUP_VM + ".155"
FM_LOG_ID_VM_LIVE_MIGRATED = ALARM_GROUP_VM + ".156"
FM_LOG_ID_VM_COLD_MIGRATE = ALARM_GROUP_VM + ".157"
FM_LOG_ID_VM_COLD_MIGRATING = ALARM_GROUP_VM + ".158"
FM_LOG_ID_VM_COLD_MIGRATE_REJECTED = ALARM_GROUP_VM + ".159"
FM_LOG_ID_VM_COLD_MIGRATE_CANCELLED = ALARM_GROUP_VM + ".160"
FM_LOG_ID_VM_COLD_MIGRATE_FAILED = ALARM_GROUP_VM + ".161"
FM_LOG_ID_VM_COLD_MIGRATED = ALARM_GROUP_VM + ".162"
FM_LOG_ID_VM_COLD_MIGRATE_CONFIRM = ALARM_GROUP_VM + ".163"
FM_LOG_ID_VM_COLD_MIGRATE_CONFIRMING = ALARM_GROUP_VM + ".164"
FM_LOG_ID_VM_COLD_MIGRATE_CONFIRM_REJECTED = ALARM_GROUP_VM + ".165"
FM_LOG_ID_VM_COLD_MIGRATE_CONFIRM_CANCELLED = ALARM_GROUP_VM + ".166"
FM_LOG_ID_VM_COLD_MIGRATE_CONFIRM_FAILED = ALARM_GROUP_VM + ".167"
FM_LOG_ID_VM_COLD_MIGRATE_CONFIRMED = ALARM_GROUP_VM + ".168"
FM_LOG_ID_VM_COLD_MIGRATE_REVERT = ALARM_GROUP_VM + ".169"
FM_LOG_ID_VM_COLD_MIGRATE_REVERTING = ALARM_GROUP_VM + ".170"
FM_LOG_ID_VM_COLD_MIGRATE_REVERT_REJECTED = ALARM_GROUP_VM + ".171"
FM_LOG_ID_VM_COLD_MIGRATE_REVERT_CANCELLED = ALARM_GROUP_VM + ".172"
FM_LOG_ID_VM_COLD_MIGRATE_REVERT_FAILED = ALARM_GROUP_VM + ".173"
FM_LOG_ID_VM_COLD_MIGRATE_REVERTED = ALARM_GROUP_VM + ".174"
FM_LOG_ID_VM_EVACUATE = ALARM_GROUP_VM + ".175"
FM_LOG_ID_VM_EVACUATING = ALARM_GROUP_VM + ".176"
FM_LOG_ID_VM_EVACUATE_REJECTED = ALARM_GROUP_VM + ".177"
FM_LOG_ID_VM_EVACUATE_CANCELLED = ALARM_GROUP_VM + ".178"
FM_LOG_ID_VM_EVACUATE_FAILED = ALARM_GROUP_VM + ".179"
FM_LOG_ID_VM_EVACUATED = ALARM_GROUP_VM + ".180"
FM_LOG_ID_VM_REBOOT = ALARM_GROUP_VM + ".181"
FM_LOG_ID_VM_REBOOTING = ALARM_GROUP_VM + ".182"
FM_LOG_ID_VM_REBOOT_REJECTED = ALARM_GROUP_VM + ".183"
FM_LOG_ID_VM_REBOOT_CANCELLED = ALARM_GROUP_VM + ".184"
FM_LOG_ID_VM_REBOOT_FAILED = ALARM_GROUP_VM + ".185"
FM_LOG_ID_VM_REBOOTED = ALARM_GROUP_VM + ".186"
FM_LOG_ID_VM_REBUILD = ALARM_GROUP_VM + ".187"
FM_LOG_ID_VM_REBUILDING = ALARM_GROUP_VM + ".188"
FM_LOG_ID_VM_REBUILD_REJECTED = ALARM_GROUP_VM + ".189"
FM_LOG_ID_VM_REBUILD_CANCELLED = ALARM_GROUP_VM + ".190"
FM_LOG_ID_VM_REBUILD_FAILED = ALARM_GROUP_VM + ".191"
FM_LOG_ID_VM_REBUILT = ALARM_GROUP_VM + ".192"
FM_LOG_ID_VM_RESIZE = ALARM_GROUP_VM + ".193"
FM_LOG_ID_VM_RESIZING = ALARM_GROUP_VM + ".194"
FM_LOG_ID_VM_RESIZE_REJECTED = ALARM_GROUP_VM + ".195"
FM_LOG_ID_VM_RESIZE_CANCELLED = ALARM_GROUP_VM + ".196"
FM_LOG_ID_VM_RESIZE_FAILED = ALARM_GROUP_VM + ".197"
FM_LOG_ID_VM_RESIZED = ALARM_GROUP_VM + ".198"
FM_LOG_ID_VM_RESIZE_CONFIRM = ALARM_GROUP_VM + ".199"
FM_LOG_ID_VM_RESIZE_CONFIRMING = ALARM_GROUP_VM + ".200"
FM_LOG_ID_VM_RESIZE_CONFIRM_REJECTED = ALARM_GROUP_VM + ".201"
FM_LOG_ID_VM_RESIZE_CONFIRM_CANCELLED = ALARM_GROUP_VM + ".202"
FM_LOG_ID_VM_RESIZE_CONFIRM_FAILED = ALARM_GROUP_VM + ".203"
FM_LOG_ID_VM_RESIZE_CONFIRMED = ALARM_GROUP_VM + ".204"
FM_LOG_ID_VM_RESIZE_REVERT = ALARM_GROUP_VM + ".205"
FM_LOG_ID_VM_RESIZE_REVERTING = ALARM_GROUP_VM + ".206"
FM_LOG_ID_VM_RESIZE_REVERT_REJECTED = ALARM_GROUP_VM + ".207"
FM_LOG_ID_VM_RESIZE_REVERT_CANCELLED = ALARM_GROUP_VM + ".208"
FM_LOG_ID_VM_RESIZE_REVERT_FAILED = ALARM_GROUP_VM + ".209"
FM_LOG_ID_VM_RESIZE_REVERTED = ALARM_GROUP_VM + ".210"
FM_LOG_ID_VM_GUEST_HEARTBEAT_ESTABLISHED = ALARM_GROUP_VM + ".211"
FM_LOG_ID_VM_GUEST_HEARTBEAT_DISCONNECTED = ALARM_GROUP_VM + ".212"
FM_LOG_ID_VM_GUEST_HEARTBEAT_FAILED = ALARM_GROUP_VM + ".213"
FM_LOG_ID_VM_RENAMED = ALARM_GROUP_VM + ".214"
FM_LOG_ID_VM_GUEST_HEALTH_CHECK_FAILED = ALARM_GROUP_VM + ".215"
FM_LOG_ID_VM_MULTI_NODE_RECOVERY_MODE_ENTER = ALARM_GROUP_VM + ".216"
FM_LOG_ID_VM_MULTI_NODE_RECOVERY_MODE_EXIT = ALARM_GROUP_VM + ".217"


# Patching alarm id
FM_ALARM_ID_PATCH_IN_PROGRESS = ALARM_GROUP_SW_MGMT + ".001"
FM_ALARM_ID_PATCH_HOST_INSTALL_FAILED = ALARM_GROUP_SW_MGMT + ".002"
FM_ALARM_ID_PATCH_OBS_IN_SYSTEM = ALARM_GROUP_SW_MGMT + ".003"

# Upgrades alarm id
FM_ALARM_ID_HOST_VERSION_MISMATCH = ALARM_GROUP_SW_MGMT + ".004"
FM_ALARM_ID_UPGRADE_IN_PROGRESS = ALARM_GROUP_SW_MGMT + ".005"

# Device image alarm id
FM_ALARM_ID_DEVICE_IMAGE_UPDATE_IN_PROGRESS = ALARM_GROUP_SW_MGMT + ".006"

# Kubernetes Upgrade alarm id
FM_ALARM_ID_KUBE_UPGRADE_IN_PROGRESS = ALARM_GROUP_SW_MGMT + ".007"

# Kubernetes RootCA Update alarm id
FM_ALARM_ID_KUBE_ROOTCA_UPDATE_IN_PROGRESS = ALARM_GROUP_SW_MGMT + ".008"

# Kubernetes RootCA Update abort alarm id
FM_ALARM_ID_KUBE_ROOTCA_UPDATE_ABORTED = ALARM_GROUP_SW_MGMT + ".009"

# The SYSTEM_CONFIG_UPDATE alarms are originated by vim strategy which is the
# same as the other sw-mgmt alarms, put them in the same group
# System Config Update alarm id
FM_ALARM_ID_SYSTEM_CONFIG_UPDATE_IN_PROGRESS = ALARM_GROUP_SW_MGMT + ".010"

# System Config Update abort alarm id
FM_ALARM_ID_SYSTEM_CONFIG_UPDATE_ABORTED = ALARM_GROUP_SW_MGMT + ".011"

# Security log id
FM_LOG_ID_INVALID_PASSWORD = ALARM_GROUP_SECURITY + ".001"
FM_LOG_ID_USER_LOCKOUT = ALARM_GROUP_SECURITY + ".002"

# Security alarm id
FM_ALARM_ID_TPM_INIT = ALARM_GROUP_SECURITY + ".100"

# Security nonstandard certificate in use for patching alarm id
FM_ALARM_ID_NONSTANDARD_CERT_PATCH = ALARM_GROUP_SECURITY + ".101"

# Security ExpiringSoon & Expired Certificates
FM_ALARM_ID_CERT_EXPIRING_SOON = ALARM_GROUP_SECURITY + ".200"
FM_ALARM_ID_CERT_EXPIRED = ALARM_GROUP_SECURITY + ".210"

# Software Update Orchestration
FM_ALARM_ID_SW_PATCH_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".101"
FM_ALARM_ID_SW_PATCH_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".102"
FM_ALARM_ID_SW_PATCH_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".103"

FM_LOG_ID_SW_PATCH_AUTO_APPLY_START = ALARM_GROUP_SW_MGMT + ".111"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".112"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_REJECTED = ALARM_GROUP_SW_MGMT + ".113"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_CANCELLED = ALARM_GROUP_SW_MGMT + ".114"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".115"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_COMPLETED = ALARM_GROUP_SW_MGMT + ".116"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_ABORT = ALARM_GROUP_SW_MGMT + ".117"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".118"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_ABORT_REJECTED = ALARM_GROUP_SW_MGMT + ".119"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_ABORT_FAILED = ALARM_GROUP_SW_MGMT + ".120"
FM_LOG_ID_SW_PATCH_AUTO_APPLY_ABORTED = ALARM_GROUP_SW_MGMT + ".121"

FM_ALARM_ID_SW_UPGRADE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".201"
FM_ALARM_ID_SW_UPGRADE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".202"
FM_ALARM_ID_SW_UPGRADE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".203"

FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_START = ALARM_GROUP_SW_MGMT + ".211"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".212"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_REJECTED = ALARM_GROUP_SW_MGMT + ".213"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_CANCELLED = ALARM_GROUP_SW_MGMT + ".214"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".215"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_COMPLETED = ALARM_GROUP_SW_MGMT + ".216"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_ABORT = ALARM_GROUP_SW_MGMT + ".217"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".218"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_ABORT_REJECTED = ALARM_GROUP_SW_MGMT + ".219"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_ABORT_FAILED = ALARM_GROUP_SW_MGMT + ".220"
FM_LOG_ID_SW_UPGRADE_AUTO_APPLY_ABORTED = ALARM_GROUP_SW_MGMT + ".221"

FM_ALARM_ID_FW_UPDATE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".301"
FM_ALARM_ID_FW_UPDATE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".302"
FM_ALARM_ID_FW_UPDATE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".303"

FM_LOG_ID_FW_UPDATE_AUTO_APPLY_START = ALARM_GROUP_SW_MGMT + ".311"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".312"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_REJECTED = ALARM_GROUP_SW_MGMT + ".313"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_CANCELLED = ALARM_GROUP_SW_MGMT + ".314"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".315"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_COMPLETED = ALARM_GROUP_SW_MGMT + ".316"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_ABORT = ALARM_GROUP_SW_MGMT + ".317"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".318"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_ABORT_REJECTED = ALARM_GROUP_SW_MGMT + ".319"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_ABORT_FAILED = ALARM_GROUP_SW_MGMT + ".320"
FM_LOG_ID_FW_UPDATE_AUTO_APPLY_ABORTED = ALARM_GROUP_SW_MGMT + ".321"

FM_ALARM_ID_KUBE_UPGRADE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".401"
FM_ALARM_ID_KUBE_UPGRADE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".402"
FM_ALARM_ID_KUBE_UPGRADE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".403"

FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_START = ALARM_GROUP_SW_MGMT + ".411"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".412"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_REJECTED = ALARM_GROUP_SW_MGMT + ".413"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_CANCELLED = ALARM_GROUP_SW_MGMT + ".414"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".415"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_COMPLETED = ALARM_GROUP_SW_MGMT + ".416"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_ABORT = ALARM_GROUP_SW_MGMT + ".417"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".418"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_ABORT_REJECTED = ALARM_GROUP_SW_MGMT + ".419"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_ABORT_FAILED = ALARM_GROUP_SW_MGMT + ".420"
FM_LOG_ID_KUBE_UPGRADE_AUTO_APPLY_ABORTED = ALARM_GROUP_SW_MGMT + ".421"

FM_ALARM_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".501"
FM_ALARM_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".502"
FM_ALARM_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".503"

FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_START = ALARM_GROUP_SW_MGMT + ".511"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".512"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_REJECTED = ALARM_GROUP_SW_MGMT + ".513"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_CANCELLED = ALARM_GROUP_SW_MGMT + ".514"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".515"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_COMPLETED = ALARM_GROUP_SW_MGMT + ".516"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_ABORT = ALARM_GROUP_SW_MGMT + ".517"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".518"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_ABORT_REJECTED = ALARM_GROUP_SW_MGMT + ".519"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_ABORT_FAILED = ALARM_GROUP_SW_MGMT + ".520"
FM_LOG_ID_KUBE_ROOTCA_UPDATE_AUTO_APPLY_ABORTED = ALARM_GROUP_SW_MGMT + ".521"

FM_ALARM_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".601"
FM_ALARM_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".602"
FM_ALARM_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".603"

FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_START = ALARM_GROUP_SW_MGMT + ".611"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_INPROGRESS = ALARM_GROUP_SW_MGMT + ".612"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_REJECTED = ALARM_GROUP_SW_MGMT + ".613"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_CANCELLED = ALARM_GROUP_SW_MGMT + ".614"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_FAILED = ALARM_GROUP_SW_MGMT + ".615"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_COMPLETED = ALARM_GROUP_SW_MGMT + ".616"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_ABORT = ALARM_GROUP_SW_MGMT + ".617"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_ABORTING = ALARM_GROUP_SW_MGMT + ".618"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_ABORT_REJECTED = ALARM_GROUP_SW_MGMT + ".619"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_ABORT_FAILED = ALARM_GROUP_SW_MGMT + ".620"
FM_LOG_ID_SYSTEM_CONFIG_UPDATE_AUTO_APPLY_ABORTED = ALARM_GROUP_SW_MGMT + ".621"

FM_ALARM_STATE_SET = 'set'
FM_ALARM_STATE_CLEAR = 'clear'
FM_ALARM_STATE_MSG = 'msg'
FM_ALARM_STATE_LOG = 'log'

FM_ALARM_CONTEXT_STARLINGX = 'starlingx'
FM_ALARM_CONTEXT_OPENSTACK = 'openstack'
FM_ALARM_CONTEXT_NONE = 'none'

FM_ALARM_TYPE_0 = 'other'
FM_ALARM_TYPE_1 = 'communication'
FM_ALARM_TYPE_2 = 'qos'
FM_ALARM_TYPE_3 = 'processing-error'
FM_ALARM_TYPE_4 = 'equipment'
FM_ALARM_TYPE_5 = 'environmental'
FM_ALARM_TYPE_6 = 'integrity-violation'
FM_ALARM_TYPE_7 = 'operational-violation'
FM_ALARM_TYPE_8 = 'physical-violation'
FM_ALARM_TYPE_9 = 'security-service-or-mechanism-violation'
FM_ALARM_TYPE_10 = 'time-domain-violation'

FM_ALARM_SEVERITY_CLEAR = 'clear'
FM_ALARM_SEVERITY_WARNING = 'warning'
FM_ALARM_SEVERITY_MINOR = 'minor'
FM_ALARM_SEVERITY_MAJOR = 'major'
FM_ALARM_SEVERITY_CRITICAL = 'critical'

FM_ALARM_OK_STATUS = "OK"
FM_ALARM_DEGRADED_STATUS = "degraded"
FM_ALARM_CRITICAL_STATUS = "critical"

ALARM_CRITICAL_REPLICATION = 'Potential data loss. No available OSDs in storage replication group '
ALARM_MAJOR_REPLICATION = 'Loss of replication in replication group '

ALARM_PROBABLE_CAUSE_1 = 'adaptor-error'
ALARM_PROBABLE_CAUSE_2 = 'application-subsystem-failure'
ALARM_PROBABLE_CAUSE_3 = 'bandwidth-reduced'
ALARM_PROBABLE_CAUSE_4 = 'call-establishment-error'
ALARM_PROBABLE_CAUSE_5 = 'communication-protocol-error'
ALARM_PROBABLE_CAUSE_6 = 'communication-subsystem-failure'
ALARM_PROBABLE_CAUSE_7 = 'configuration-or-customization-error'
ALARM_PROBABLE_CAUSE_8 = 'congestion'
ALARM_PROBABLE_CAUSE_9 = 'corrupt-data'
ALARM_PROBABLE_CAUSE_10 = 'cpu-cycles-limit-exceeded'
ALARM_PROBABLE_CAUSE_11 = 'dataset-or-modem-error'
ALARM_PROBABLE_CAUSE_12 = 'degraded-signal'
ALARM_PROBABLE_CAUSE_13 = 'dte-dce-interface-error'
ALARM_PROBABLE_CAUSE_14 = 'enclosure-door-open'
ALARM_PROBABLE_CAUSE_15 = 'equipment-malfunction'
ALARM_PROBABLE_CAUSE_16 = 'excessive-vibration'
ALARM_PROBABLE_CAUSE_17 = 'file-error'
ALARM_PROBABLE_CAUSE_18 = 'fire-detected'
ALARM_PROBABLE_CAUSE_19 = 'flood-detected'
ALARM_PROBABLE_CAUSE_20 = 'framing-error'
ALARM_PROBABLE_CAUSE_21 = 'heating-ventilation-cooling-system-problem'
ALARM_PROBABLE_CAUSE_22 = 'humidity-unacceptable'
ALARM_PROBABLE_CAUSE_23 = 'io-device-error'
ALARM_PROBABLE_CAUSE_24 = 'input-device-error'
ALARM_PROBABLE_CAUSE_25 = 'lan-error'
ALARM_PROBABLE_CAUSE_26 = 'leak-detected'
ALARM_PROBABLE_CAUSE_27 = 'local-node-transmission-error'
ALARM_PROBABLE_CAUSE_28 = 'loss-of-frame'
ALARM_PROBABLE_CAUSE_29 = 'loss-of-signal'
ALARM_PROBABLE_CAUSE_30 = 'material-supply-exhausted'
ALARM_PROBABLE_CAUSE_31 = 'multiplexer-problem'
ALARM_PROBABLE_CAUSE_32 = 'out-of-memory'
ALARM_PROBABLE_CAUSE_33 = 'output-device-error'
ALARM_PROBABLE_CAUSE_34 = 'performance-degraded'
ALARM_PROBABLE_CAUSE_35 = 'power-problem'
ALARM_PROBABLE_CAUSE_36 = 'processor-problem'
ALARM_PROBABLE_CAUSE_37 = 'pump-failure'
ALARM_PROBABLE_CAUSE_38 = 'queue-size-exceeded'
ALARM_PROBABLE_CAUSE_39 = 'receive-failure'
ALARM_PROBABLE_CAUSE_40 = 'receiver-failure'
ALARM_PROBABLE_CAUSE_41 = 'remote-node-transmission-error'
ALARM_PROBABLE_CAUSE_42 = 'resource-at-or-nearing-capacity'
ALARM_PROBABLE_CAUSE_43 = 'response-time-excessive'
ALARM_PROBABLE_CAUSE_44 = 'retransmission-rate-excessive'
ALARM_PROBABLE_CAUSE_45 = 'software-error'
ALARM_PROBABLE_CAUSE_46 = 'software-program-abnormally-terminated'
ALARM_PROBABLE_CAUSE_47 = 'software-program-error'
ALARM_PROBABLE_CAUSE_48 = 'storage-capacity-problem'
ALARM_PROBABLE_CAUSE_49 = 'temperature-unacceptable'
ALARM_PROBABLE_CAUSE_50 = 'threshold-crossed'
ALARM_PROBABLE_CAUSE_51 = 'timing-problem'
ALARM_PROBABLE_CAUSE_52 = 'toxic-leak-detected'
ALARM_PROBABLE_CAUSE_53 = 'transmit-failure'
ALARM_PROBABLE_CAUSE_54 = 'transmitter-failure'
ALARM_PROBABLE_CAUSE_55 = 'underlying-resource-unavailable'
ALARM_PROBABLE_CAUSE_56 = 'version-mismatch'
ALARM_PROBABLE_CAUSE_57 = 'duplicate-information'
ALARM_PROBABLE_CAUSE_58 = 'information-missing'
ALARM_PROBABLE_CAUSE_59 = 'information-modification-detected'
ALARM_PROBABLE_CAUSE_60 = 'information-out-of-sequence'
ALARM_PROBABLE_CAUSE_61 = 'unexpected-information'
ALARM_PROBABLE_CAUSE_62 = 'denial-of-service'
ALARM_PROBABLE_CAUSE_63 = 'out-of-service'
ALARM_PROBABLE_CAUSE_64 = 'procedural-error'
ALARM_PROBABLE_CAUSE_65 = 'unspecified-reason'
ALARM_PROBABLE_CAUSE_66 = 'cable-tamper'
ALARM_PROBABLE_CAUSE_67 = 'intrusion-detection'
ALARM_PROBABLE_CAUSE_68 = 'authentication-failure'
ALARM_PROBABLE_CAUSE_69 = 'breach-of-confidentiality'
ALARM_PROBABLE_CAUSE_70 = 'non-repudiation-failure'
ALARM_PROBABLE_CAUSE_71 = 'unauthorized-access-attempt'
ALARM_PROBABLE_CAUSE_72 = 'delayed-information'
ALARM_PROBABLE_CAUSE_73 = 'key-expired'
ALARM_PROBABLE_CAUSE_74 = 'out-of-hours-activity'
ALARM_PROBABLE_CAUSE_75 = 'configuration-out-of-date'
ALARM_PROBABLE_CAUSE_76 = 'configuration-provisioning-required'
ALARM_PROBABLE_CAUSE_77 = 'certificate-expiration'
ALARM_PROBABLE_CAUSE_UNKNOWN = 'unknown'

ALARM_STATE = [FM_ALARM_STATE_SET, FM_ALARM_STATE_CLEAR,
               FM_ALARM_STATE_MSG, FM_ALARM_STATE_LOG]

ALARM_TYPE = [FM_ALARM_TYPE_0, FM_ALARM_TYPE_1, FM_ALARM_TYPE_2,
              FM_ALARM_TYPE_3, FM_ALARM_TYPE_4, FM_ALARM_TYPE_5,
              FM_ALARM_TYPE_6, FM_ALARM_TYPE_7, FM_ALARM_TYPE_8,
              FM_ALARM_TYPE_9, FM_ALARM_TYPE_10]

ALARM_SEVERITY = [FM_ALARM_SEVERITY_CLEAR, FM_ALARM_SEVERITY_WARNING,
                  FM_ALARM_SEVERITY_MINOR, FM_ALARM_SEVERITY_MAJOR,
                  FM_ALARM_SEVERITY_CRITICAL]

ALARM_STATUS = [FM_ALARM_OK_STATUS, FM_ALARM_DEGRADED_STATUS,
                FM_ALARM_CRITICAL_STATUS]

ALARM_CONTEXT = [FM_ALARM_CONTEXT_STARLINGX, FM_ALARM_CONTEXT_OPENSTACK,
                 FM_ALARM_CONTEXT_NONE]

ALARM_PROBABLE_CAUSE = [ALARM_PROBABLE_CAUSE_1, ALARM_PROBABLE_CAUSE_2,
                        ALARM_PROBABLE_CAUSE_3, ALARM_PROBABLE_CAUSE_4,
                        ALARM_PROBABLE_CAUSE_5, ALARM_PROBABLE_CAUSE_6,
                        ALARM_PROBABLE_CAUSE_7, ALARM_PROBABLE_CAUSE_8,
                        ALARM_PROBABLE_CAUSE_9, ALARM_PROBABLE_CAUSE_10,
                        ALARM_PROBABLE_CAUSE_11, ALARM_PROBABLE_CAUSE_12,
                        ALARM_PROBABLE_CAUSE_13, ALARM_PROBABLE_CAUSE_14,
                        ALARM_PROBABLE_CAUSE_15, ALARM_PROBABLE_CAUSE_16,
                        ALARM_PROBABLE_CAUSE_17, ALARM_PROBABLE_CAUSE_18,
                        ALARM_PROBABLE_CAUSE_19, ALARM_PROBABLE_CAUSE_20,
                        ALARM_PROBABLE_CAUSE_21, ALARM_PROBABLE_CAUSE_22,
                        ALARM_PROBABLE_CAUSE_23, ALARM_PROBABLE_CAUSE_24,
                        ALARM_PROBABLE_CAUSE_25, ALARM_PROBABLE_CAUSE_26,
                        ALARM_PROBABLE_CAUSE_27, ALARM_PROBABLE_CAUSE_28,
                        ALARM_PROBABLE_CAUSE_29, ALARM_PROBABLE_CAUSE_30,
                        ALARM_PROBABLE_CAUSE_31, ALARM_PROBABLE_CAUSE_32,
                        ALARM_PROBABLE_CAUSE_33, ALARM_PROBABLE_CAUSE_34,
                        ALARM_PROBABLE_CAUSE_35, ALARM_PROBABLE_CAUSE_36,
                        ALARM_PROBABLE_CAUSE_37, ALARM_PROBABLE_CAUSE_38,
                        ALARM_PROBABLE_CAUSE_39, ALARM_PROBABLE_CAUSE_40,
                        ALARM_PROBABLE_CAUSE_41, ALARM_PROBABLE_CAUSE_42,
                        ALARM_PROBABLE_CAUSE_43, ALARM_PROBABLE_CAUSE_44,
                        ALARM_PROBABLE_CAUSE_45, ALARM_PROBABLE_CAUSE_46,
                        ALARM_PROBABLE_CAUSE_47, ALARM_PROBABLE_CAUSE_48,
                        ALARM_PROBABLE_CAUSE_49, ALARM_PROBABLE_CAUSE_50,
                        ALARM_PROBABLE_CAUSE_51, ALARM_PROBABLE_CAUSE_52,
                        ALARM_PROBABLE_CAUSE_53, ALARM_PROBABLE_CAUSE_54,
                        ALARM_PROBABLE_CAUSE_55, ALARM_PROBABLE_CAUSE_56,
                        ALARM_PROBABLE_CAUSE_57, ALARM_PROBABLE_CAUSE_58,
                        ALARM_PROBABLE_CAUSE_59, ALARM_PROBABLE_CAUSE_60,
                        ALARM_PROBABLE_CAUSE_61, ALARM_PROBABLE_CAUSE_62,
                        ALARM_PROBABLE_CAUSE_63, ALARM_PROBABLE_CAUSE_64,
                        ALARM_PROBABLE_CAUSE_65, ALARM_PROBABLE_CAUSE_66,
                        ALARM_PROBABLE_CAUSE_67, ALARM_PROBABLE_CAUSE_68,
                        ALARM_PROBABLE_CAUSE_69, ALARM_PROBABLE_CAUSE_70,
                        ALARM_PROBABLE_CAUSE_71, ALARM_PROBABLE_CAUSE_72,
                        ALARM_PROBABLE_CAUSE_73, ALARM_PROBABLE_CAUSE_74,
                        ALARM_PROBABLE_CAUSE_75, ALARM_PROBABLE_CAUSE_76,
                        ALARM_PROBABLE_CAUSE_77,
                        ALARM_PROBABLE_CAUSE_UNKNOWN]


FM_CLIENT_SET_FAULT = "/usr/local/bin/fmClientCli -c "
FM_CLIENT_CLEAR_FAULT = "/usr/local/bin/fmClientCli -d "
FM_CLIENT_GET_FAULT = "/usr/local/bin/fmClientCli -g "
FM_CLIENT_GET_FAULTS = "/usr/local/bin/fmClientCli -G "
FM_CLIENT_GET_FAULTS_BY_ID = "/usr/local/bin/fmClientCli -A "
FM_CLIENT_CLEAR_ALL = "/usr/local/bin/fmClientCli -D "
FM_CLIENT_STR_SEP = "###"

FM_UUID_INDEX = 0
FM_ALARM_ID_INDEX = 1
FM_ALARM_STATE_INDEX = 2
FM_ENT_TYPE_ID_INDEX = 3
FM_ENT_INST_ID_INDEX = 4
FM_TIMESTAMP_INDEX = 5
FM_SEVERITY_INDEX = 6
FM_REASON_TEXT_INDEX = 7
FM_ALARM_TYPE_INDEX = 8
FM_CAUSE_INDEX = 9
FM_REPAIR_ACTION_INDEX = 10
FM_SERVICE_AFFECTING_INDEX = 11
FM_SUPPRESSION_INDEX = 12
FM_INHIBIT_ALARMS_INDEX = 13
MAX_ALARM_ATTRIBUTES = 14

# Proposed Repair actions
FM_PRA_CONTROLLERS_KERNEL_MISMATCH = ("Modify controllers using "
                                      "'system host-kernel-modify' "
                                      "so that both are running the "
                                      "desired 'standard' or "
                                      "'lowlatency' kernel.")
FM_PRA_PROVISIONED_KERNEL_MISMATCH = ("Retry 'system host-kernel-modify' "
                                      "and if condition persists, "
                                      "contact next level of support.")
