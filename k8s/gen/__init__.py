# generated by datamodel-codegen:
#   filename:  schema.json
#   timestamp: 2020-05-31T11:16:13+00:00

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel


class Model(BaseModel):
    __root__: Any


class Kind(Enum):
    MutatingWebhookConfiguration = 'MutatingWebhookConfiguration'


class Kind1(Enum):
    MutatingWebhookConfigurationList = 'MutatingWebhookConfigurationList'


class Kind2(Enum):
    ValidatingWebhookConfiguration = 'ValidatingWebhookConfiguration'


class Kind3(Enum):
    ValidatingWebhookConfigurationList = 'ValidatingWebhookConfigurationList'


class Kind4(Enum):
    MutatingWebhookConfiguration = 'MutatingWebhookConfiguration'


class Kind5(Enum):
    MutatingWebhookConfigurationList = 'MutatingWebhookConfigurationList'


class Kind6(Enum):
    ValidatingWebhookConfiguration = 'ValidatingWebhookConfiguration'


class Kind7(Enum):
    ValidatingWebhookConfigurationList = 'ValidatingWebhookConfigurationList'


class Kind8(Enum):
    ControllerRevision = 'ControllerRevision'


class Kind9(Enum):
    ControllerRevisionList = 'ControllerRevisionList'


class Kind10(Enum):
    DaemonSet = 'DaemonSet'


class Kind11(Enum):
    DaemonSetList = 'DaemonSetList'


class Kind12(Enum):
    Deployment = 'Deployment'


class Kind13(Enum):
    DeploymentList = 'DeploymentList'


class Kind14(Enum):
    ReplicaSet = 'ReplicaSet'


class Kind15(Enum):
    ReplicaSetList = 'ReplicaSetList'


class Kind16(Enum):
    StatefulSet = 'StatefulSet'


class Kind17(Enum):
    StatefulSetList = 'StatefulSetList'


class Kind18(Enum):
    ControllerRevision = 'ControllerRevision'


class Kind19(Enum):
    ControllerRevisionList = 'ControllerRevisionList'


class Kind20(Enum):
    Deployment = 'Deployment'


class Kind21(Enum):
    DeploymentList = 'DeploymentList'


class Kind22(Enum):
    DeploymentRollback = 'DeploymentRollback'


class Kind23(Enum):
    Scale = 'Scale'


class Kind24(Enum):
    StatefulSet = 'StatefulSet'


class Kind25(Enum):
    StatefulSetList = 'StatefulSetList'


class Kind26(Enum):
    ControllerRevision = 'ControllerRevision'


class Kind27(Enum):
    ControllerRevisionList = 'ControllerRevisionList'


class Kind28(Enum):
    DaemonSet = 'DaemonSet'


class Kind29(Enum):
    DaemonSetList = 'DaemonSetList'


class Kind30(Enum):
    Deployment = 'Deployment'


class Kind31(Enum):
    DeploymentList = 'DeploymentList'


class Kind32(Enum):
    ReplicaSet = 'ReplicaSet'


class Kind33(Enum):
    ReplicaSetList = 'ReplicaSetList'


class Kind34(Enum):
    Scale = 'Scale'


class Kind35(Enum):
    StatefulSet = 'StatefulSet'


class Kind36(Enum):
    StatefulSetList = 'StatefulSetList'


class Kind37(Enum):
    AuditSink = 'AuditSink'


class Kind38(Enum):
    AuditSinkList = 'AuditSinkList'


class Kind39(Enum):
    TokenRequest = 'TokenRequest'


class Kind40(Enum):
    TokenReview = 'TokenReview'


class Kind41(Enum):
    TokenReview = 'TokenReview'


class Kind42(Enum):
    LocalSubjectAccessReview = 'LocalSubjectAccessReview'


class Kind43(Enum):
    SelfSubjectAccessReview = 'SelfSubjectAccessReview'


class Kind44(Enum):
    SelfSubjectRulesReview = 'SelfSubjectRulesReview'


class Kind45(Enum):
    SubjectAccessReview = 'SubjectAccessReview'


class Kind46(Enum):
    LocalSubjectAccessReview = 'LocalSubjectAccessReview'


class Kind47(Enum):
    SelfSubjectAccessReview = 'SelfSubjectAccessReview'


class Kind48(Enum):
    SelfSubjectRulesReview = 'SelfSubjectRulesReview'


class Kind49(Enum):
    SubjectAccessReview = 'SubjectAccessReview'


class Kind50(Enum):
    HorizontalPodAutoscaler = 'HorizontalPodAutoscaler'


class Kind51(Enum):
    HorizontalPodAutoscalerList = 'HorizontalPodAutoscalerList'


class Kind52(Enum):
    Scale = 'Scale'


class Kind53(Enum):
    HorizontalPodAutoscaler = 'HorizontalPodAutoscaler'


class Kind54(Enum):
    HorizontalPodAutoscalerList = 'HorizontalPodAutoscalerList'


class Kind55(Enum):
    HorizontalPodAutoscaler = 'HorizontalPodAutoscaler'


class Kind56(Enum):
    HorizontalPodAutoscalerList = 'HorizontalPodAutoscalerList'


class Kind57(Enum):
    Job = 'Job'


class Kind58(Enum):
    JobList = 'JobList'


class Kind59(Enum):
    CronJob = 'CronJob'


class Kind60(Enum):
    CronJobList = 'CronJobList'


class Kind61(Enum):
    CronJob = 'CronJob'


class Kind62(Enum):
    CronJobList = 'CronJobList'


class Kind63(Enum):
    CertificateSigningRequest = 'CertificateSigningRequest'


class Kind64(Enum):
    CertificateSigningRequestList = 'CertificateSigningRequestList'


class Kind65(Enum):
    Lease = 'Lease'


class Kind66(Enum):
    LeaseList = 'LeaseList'


class Kind67(Enum):
    Lease = 'Lease'


class Kind68(Enum):
    LeaseList = 'LeaseList'


class Kind69(Enum):
    Binding = 'Binding'


class Kind70(Enum):
    ComponentStatus = 'ComponentStatus'


class Kind71(Enum):
    ComponentStatusList = 'ComponentStatusList'


class Kind72(Enum):
    ConfigMap = 'ConfigMap'


class Kind73(Enum):
    ConfigMapList = 'ConfigMapList'


class Kind74(Enum):
    Endpoints = 'Endpoints'


class Kind75(Enum):
    EndpointsList = 'EndpointsList'


class Kind76(Enum):
    Event = 'Event'


class Kind77(Enum):
    EventList = 'EventList'


class Kind78(Enum):
    LimitRange = 'LimitRange'


class Kind79(Enum):
    LimitRangeList = 'LimitRangeList'


class Kind80(Enum):
    Namespace = 'Namespace'


class Kind81(Enum):
    NamespaceList = 'NamespaceList'


class Kind82(Enum):
    Node = 'Node'


class Kind83(Enum):
    NodeList = 'NodeList'


class Kind84(Enum):
    PersistentVolume = 'PersistentVolume'


class Kind85(Enum):
    PersistentVolumeClaim = 'PersistentVolumeClaim'


class Kind86(Enum):
    PersistentVolumeClaimList = 'PersistentVolumeClaimList'


class Kind87(Enum):
    PersistentVolumeList = 'PersistentVolumeList'


class Kind88(Enum):
    Pod = 'Pod'


class Kind89(Enum):
    PodList = 'PodList'


class Kind90(Enum):
    PodTemplate = 'PodTemplate'


class Kind91(Enum):
    PodTemplateList = 'PodTemplateList'


class Kind92(Enum):
    ReplicationController = 'ReplicationController'


class Kind93(Enum):
    ReplicationControllerList = 'ReplicationControllerList'


class Kind94(Enum):
    ResourceQuota = 'ResourceQuota'


class Kind95(Enum):
    ResourceQuotaList = 'ResourceQuotaList'


class Kind96(Enum):
    Secret = 'Secret'


class Kind97(Enum):
    SecretList = 'SecretList'


class Kind98(Enum):
    Service = 'Service'


class Kind99(Enum):
    ServiceAccount = 'ServiceAccount'


class Kind100(Enum):
    ServiceAccountList = 'ServiceAccountList'


class Kind101(Enum):
    ServiceList = 'ServiceList'


class Kind102(Enum):
    EndpointSlice = 'EndpointSlice'


class Kind103(Enum):
    EndpointSliceList = 'EndpointSliceList'


class Kind104(Enum):
    Event = 'Event'


class Kind105(Enum):
    EventList = 'EventList'


class Kind106(Enum):
    DaemonSet = 'DaemonSet'


class Kind107(Enum):
    DaemonSetList = 'DaemonSetList'


class Kind108(Enum):
    Deployment = 'Deployment'


class Kind109(Enum):
    DeploymentList = 'DeploymentList'


class Kind110(Enum):
    DeploymentRollback = 'DeploymentRollback'


class Kind111(Enum):
    Ingress = 'Ingress'


class Kind112(Enum):
    IngressList = 'IngressList'


class Kind113(Enum):
    NetworkPolicy = 'NetworkPolicy'


class Kind114(Enum):
    NetworkPolicyList = 'NetworkPolicyList'


class Kind115(Enum):
    PodSecurityPolicy = 'PodSecurityPolicy'


class Kind116(Enum):
    PodSecurityPolicyList = 'PodSecurityPolicyList'


class Kind117(Enum):
    ReplicaSet = 'ReplicaSet'


class Kind118(Enum):
    ReplicaSetList = 'ReplicaSetList'


class Kind119(Enum):
    Scale = 'Scale'


class Kind120(Enum):
    NetworkPolicy = 'NetworkPolicy'


class Kind121(Enum):
    NetworkPolicyList = 'NetworkPolicyList'


class Kind122(Enum):
    Ingress = 'Ingress'


class Kind123(Enum):
    IngressList = 'IngressList'


class Kind124(Enum):
    RuntimeClass = 'RuntimeClass'


class Kind125(Enum):
    RuntimeClassList = 'RuntimeClassList'


class Kind126(Enum):
    RuntimeClass = 'RuntimeClass'


class Kind127(Enum):
    RuntimeClassList = 'RuntimeClassList'


class Kind128(Enum):
    Eviction = 'Eviction'


class Kind129(Enum):
    PodDisruptionBudget = 'PodDisruptionBudget'


class Kind130(Enum):
    PodDisruptionBudgetList = 'PodDisruptionBudgetList'


class Kind131(Enum):
    PodSecurityPolicy = 'PodSecurityPolicy'


class Kind132(Enum):
    PodSecurityPolicyList = 'PodSecurityPolicyList'


class Kind133(Enum):
    ClusterRole = 'ClusterRole'


class Kind134(Enum):
    ClusterRoleBinding = 'ClusterRoleBinding'


class Kind135(Enum):
    ClusterRoleBindingList = 'ClusterRoleBindingList'


class Kind136(Enum):
    ClusterRoleList = 'ClusterRoleList'


class Kind137(Enum):
    Role = 'Role'


class Kind138(Enum):
    RoleBinding = 'RoleBinding'


class Kind139(Enum):
    RoleBindingList = 'RoleBindingList'


class Kind140(Enum):
    RoleList = 'RoleList'


class Kind141(Enum):
    ClusterRole = 'ClusterRole'


class Kind142(Enum):
    ClusterRoleBinding = 'ClusterRoleBinding'


class Kind143(Enum):
    ClusterRoleBindingList = 'ClusterRoleBindingList'


class Kind144(Enum):
    ClusterRoleList = 'ClusterRoleList'


class Kind145(Enum):
    Role = 'Role'


class Kind146(Enum):
    RoleBinding = 'RoleBinding'


class Kind147(Enum):
    RoleBindingList = 'RoleBindingList'


class Kind148(Enum):
    RoleList = 'RoleList'


class Kind149(Enum):
    ClusterRole = 'ClusterRole'


class Kind150(Enum):
    ClusterRoleBinding = 'ClusterRoleBinding'


class Kind151(Enum):
    ClusterRoleBindingList = 'ClusterRoleBindingList'


class Kind152(Enum):
    ClusterRoleList = 'ClusterRoleList'


class Kind153(Enum):
    Role = 'Role'


class Kind154(Enum):
    RoleBinding = 'RoleBinding'


class Kind155(Enum):
    RoleBindingList = 'RoleBindingList'


class Kind156(Enum):
    RoleList = 'RoleList'


class Kind157(Enum):
    PriorityClass = 'PriorityClass'


class Kind158(Enum):
    PriorityClassList = 'PriorityClassList'


class Kind159(Enum):
    PriorityClass = 'PriorityClass'


class Kind160(Enum):
    PriorityClassList = 'PriorityClassList'


class Kind161(Enum):
    PriorityClass = 'PriorityClass'


class Kind162(Enum):
    PriorityClassList = 'PriorityClassList'


class Kind163(Enum):
    PodPreset = 'PodPreset'


class Kind164(Enum):
    PodPresetList = 'PodPresetList'


class Kind165(Enum):
    StorageClass = 'StorageClass'


class Kind166(Enum):
    StorageClassList = 'StorageClassList'


class Kind167(Enum):
    VolumeAttachment = 'VolumeAttachment'


class Kind168(Enum):
    VolumeAttachmentList = 'VolumeAttachmentList'


class Kind169(Enum):
    VolumeAttachment = 'VolumeAttachment'


class Kind170(Enum):
    VolumeAttachmentList = 'VolumeAttachmentList'


class Kind171(Enum):
    CSIDriver = 'CSIDriver'


class Kind172(Enum):
    CSIDriverList = 'CSIDriverList'


class Kind173(Enum):
    CSINode = 'CSINode'


class Kind174(Enum):
    CSINodeList = 'CSINodeList'


class Kind175(Enum):
    StorageClass = 'StorageClass'


class Kind176(Enum):
    StorageClassList = 'StorageClassList'


class Kind177(Enum):
    VolumeAttachment = 'VolumeAttachment'


class Kind178(Enum):
    VolumeAttachmentList = 'VolumeAttachmentList'


class Kind179(Enum):
    CustomResourceDefinition = 'CustomResourceDefinition'


class Kind180(Enum):
    CustomResourceDefinitionList = 'CustomResourceDefinitionList'


class Kind181(Enum):
    CustomResourceDefinition = 'CustomResourceDefinition'


class Kind182(Enum):
    CustomResourceDefinitionList = 'CustomResourceDefinitionList'


class Kind183(Enum):
    APIGroup = 'APIGroup'


class Kind184(Enum):
    APIGroupList = 'APIGroupList'


class Kind185(Enum):
    APIResourceList = 'APIResourceList'


class Kind186(Enum):
    APIVersions = 'APIVersions'


class Kind187(Enum):
    DeleteOptions = 'DeleteOptions'


class Kind188(Enum):
    Status = 'Status'


class Kind189(Enum):
    APIService = 'APIService'


class Kind190(Enum):
    APIServiceList = 'APIServiceList'


class Kind191(Enum):
    APIService = 'APIService'


class Kind192(Enum):
    APIServiceList = 'APIServiceList'