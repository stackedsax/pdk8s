# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ..... import (
    Kind8,
    Kind9,
    Kind10,
    Kind11,
    Kind12,
    Kind13,
    Kind14,
    Kind15,
    Kind16,
    Kind17,
)
from ...apimachinery.pkg import runtime
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr
from ..core import v1 as v1_1


class RollingUpdateStatefulSetStrategy(BaseModel):
    partition: Optional[int] = Field(
        None,
        description='Partition indicates the ordinal at which the StatefulSet should be partitioned. Default value is 0.',
    )


class StatefulSetUpdateStrategy(BaseModel):
    rollingUpdate: Optional[RollingUpdateStatefulSetStrategy] = Field(
        None,
        description='RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType.',
    )
    type: Optional[str] = Field(
        None,
        description='Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.',
    )


class DaemonSetCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description='Last time the condition transitioned from one status to another.',
    )
    message: Optional[str] = Field(
        None,
        description='A human readable message indicating details about the transition.',
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description='Status of the condition, one of True, False, Unknown.'
    )
    type: str = Field(..., description='Type of DaemonSet condition.')


class DaemonSetStatus(BaseModel):
    collisionCount: Optional[int] = Field(
        None,
        description='Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.',
    )
    conditions: Optional[List[DaemonSetCondition]] = Field(
        None,
        description="Represents the latest available observations of a DaemonSet's current state.",
    )
    currentNumberScheduled: int = Field(
        ...,
        description='The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/',
    )
    desiredNumberScheduled: int = Field(
        ...,
        description='The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/',
    )
    numberAvailable: Optional[int] = Field(
        None,
        description='The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)',
    )
    numberMisscheduled: int = Field(
        ...,
        description='The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/',
    )
    numberReady: int = Field(
        ...,
        description='The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.',
    )
    numberUnavailable: Optional[int] = Field(
        None,
        description='The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)',
    )
    observedGeneration: Optional[int] = Field(
        None,
        description='The most recent generation observed by the daemon set controller.',
    )
    updatedNumberScheduled: Optional[int] = Field(
        None,
        description='The total number of nodes that are running updated daemon pod',
    )


class DeploymentCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description='Last time the condition transitioned from one status to another.',
    )
    lastUpdateTime: Optional[v1.Time] = Field(
        None, description='The last time this condition was updated.'
    )
    message: Optional[str] = Field(
        None,
        description='A human readable message indicating details about the transition.',
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description='Status of the condition, one of True, False, Unknown.'
    )
    type: str = Field(..., description='Type of deployment condition.')


class DeploymentStatus(BaseModel):
    availableReplicas: Optional[int] = Field(
        None,
        description='Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.',
    )
    collisionCount: Optional[int] = Field(
        None,
        description='Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.',
    )
    conditions: Optional[List[DeploymentCondition]] = Field(
        None,
        description="Represents the latest available observations of a deployment's current state.",
    )
    observedGeneration: Optional[int] = Field(
        None, description='The generation observed by the deployment controller.'
    )
    readyReplicas: Optional[int] = Field(
        None, description='Total number of ready pods targeted by this deployment.'
    )
    replicas: Optional[int] = Field(
        None,
        description='Total number of non-terminated pods targeted by this deployment (their labels match the selector).',
    )
    unavailableReplicas: Optional[int] = Field(
        None,
        description='Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.',
    )
    updatedReplicas: Optional[int] = Field(
        None,
        description='Total number of non-terminated pods targeted by this deployment that have the desired template spec.',
    )


class ReplicaSetCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description='The last time the condition transitioned from one status to another.',
    )
    message: Optional[str] = Field(
        None,
        description='A human readable message indicating details about the transition.',
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description='Status of the condition, one of True, False, Unknown.'
    )
    type: str = Field(..., description='Type of replica set condition.')


class ReplicaSetStatus(BaseModel):
    availableReplicas: Optional[int] = Field(
        None,
        description='The number of available replicas (ready for at least minReadySeconds) for this replica set.',
    )
    conditions: Optional[List[ReplicaSetCondition]] = Field(
        None,
        description="Represents the latest available observations of a replica set's current state.",
    )
    fullyLabeledReplicas: Optional[int] = Field(
        None,
        description='The number of pods that have labels matching the labels of the pod template of the replicaset.',
    )
    observedGeneration: Optional[int] = Field(
        None,
        description='ObservedGeneration reflects the generation of the most recently observed ReplicaSet.',
    )
    readyReplicas: Optional[int] = Field(
        None, description='The number of ready replicas for this replica set.'
    )
    replicas: int = Field(
        ...,
        description='Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller',
    )


class RollingUpdateDaemonSet(BaseModel):
    maxUnavailable: Optional[intstr.IntOrString] = Field(
        None,
        description='The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0. Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.',
    )


class RollingUpdateDeployment(BaseModel):
    maxSurge: Optional[intstr.IntOrString] = Field(
        None,
        description='The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.',
    )
    maxUnavailable: Optional[intstr.IntOrString] = Field(
        None,
        description='The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.',
    )


class StatefulSetCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description='Last time the condition transitioned from one status to another.',
    )
    message: Optional[str] = Field(
        None,
        description='A human readable message indicating details about the transition.',
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description='Status of the condition, one of True, False, Unknown.'
    )
    type: str = Field(..., description='Type of statefulset condition.')


class StatefulSetStatus(BaseModel):
    collisionCount: Optional[int] = Field(
        None,
        description='collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.',
    )
    conditions: Optional[List[StatefulSetCondition]] = Field(
        None,
        description="Represents the latest available observations of a statefulset's current state.",
    )
    currentReplicas: Optional[int] = Field(
        None,
        description='currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.',
    )
    currentRevision: Optional[str] = Field(
        None,
        description='currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).',
    )
    observedGeneration: Optional[int] = Field(
        None,
        description="observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.",
    )
    readyReplicas: Optional[int] = Field(
        None,
        description='readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready Condition.',
    )
    replicas: int = Field(
        ...,
        description='replicas is the number of Pods created by the StatefulSet controller.',
    )
    updateRevision: Optional[str] = Field(
        None,
        description='updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)',
    )
    updatedReplicas: Optional[int] = Field(
        None,
        description='updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.',
    )


class ControllerRevision(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    data: Optional[runtime.RawExtension] = Field(
        None, description='Data is the serialized representation of the state.'
    )
    kind: Optional[Kind8] = Field(
        'ControllerRevision',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    revision: int = Field(
        ...,
        description='Revision indicates the revision of the state represented by Data.',
    )


class ControllerRevisionList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ControllerRevision] = Field(
        ..., description='Items is the list of ControllerRevisions'
    )
    kind: Optional[Kind9] = Field(
        'ControllerRevisionList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata',
    )


class DaemonSetUpdateStrategy(BaseModel):
    rollingUpdate: Optional[RollingUpdateDaemonSet] = Field(
        None,
        description='Rolling update config params. Present only if type = "RollingUpdate".',
    )
    type: Optional[str] = Field(
        None,
        description='Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.',
    )


class DeploymentStrategy(BaseModel):
    rollingUpdate: Optional[RollingUpdateDeployment] = Field(
        None,
        description='Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.',
    )
    type: Optional[str] = Field(
        None,
        description='Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.',
    )


class DaemonSetSpec(BaseModel):
    minReadySeconds: Optional[int] = Field(
        None,
        description='The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).',
    )
    revisionHistoryLimit: Optional[int] = Field(
        None,
        description='The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.',
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: v1_1.PodTemplateSpec = Field(
        ...,
        description="An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template",
    )
    updateStrategy: Optional[DaemonSetUpdateStrategy] = Field(
        None,
        description='An update strategy to replace existing DaemonSet pods with new pods.',
    )


class DeploymentSpec(BaseModel):
    minReadySeconds: Optional[int] = Field(
        None,
        description='Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)',
    )
    paused: Optional[bool] = Field(
        None, description='Indicates that the deployment is paused.'
    )
    progressDeadlineSeconds: Optional[int] = Field(
        None,
        description='The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.',
    )
    replicas: Optional[int] = Field(
        None,
        description='Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.',
    )
    revisionHistoryLimit: Optional[int] = Field(
        None,
        description='The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.',
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.",
    )
    strategy: Optional[DeploymentStrategy] = Field(
        None,
        description='The deployment strategy to use to replace existing pods with new ones.',
    )
    template: v1_1.PodTemplateSpec = Field(
        ..., description='Template describes the pods that will be created.'
    )


class ReplicaSetSpec(BaseModel):
    minReadySeconds: Optional[int] = Field(
        None,
        description='Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)',
    )
    replicas: Optional[int] = Field(
        None,
        description='Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller',
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    template: Optional[v1_1.PodTemplateSpec] = Field(
        None,
        description='Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template',
    )


class StatefulSetSpec(BaseModel):
    podManagementPolicy: Optional[str] = Field(
        None,
        description='podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.',
    )
    replicas: Optional[int] = Field(
        None,
        description='replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.',
    )
    revisionHistoryLimit: Optional[int] = Field(
        None,
        description="revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.",
    )
    selector: v1.LabelSelector = Field(
        ...,
        description="selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors",
    )
    serviceName: str = Field(
        ...,
        description='serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.',
    )
    template: v1_1.PodTemplateSpec = Field(
        ...,
        description='template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.',
    )
    updateStrategy: Optional[StatefulSetUpdateStrategy] = Field(
        None,
        description='updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.',
    )
    volumeClaimTemplates: Optional[List[v1_1.PersistentVolumeClaim]] = Field(
        None,
        description='volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.',
    )


class DaemonSet(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind10] = Field(
        'DaemonSet',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[DaemonSetSpec] = Field(
        None,
        description='The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )
    status: Optional[DaemonSetStatus] = Field(
        None,
        description='The current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )


class DaemonSetList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[DaemonSet] = Field(..., description='A list of daemon sets.')
    kind: Optional[Kind11] = Field(
        'DaemonSetList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata',
    )


class Deployment(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind12] = Field(
        'Deployment',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description='Standard object metadata.'
    )
    spec: Optional[DeploymentSpec] = Field(
        None, description='Specification of the desired behavior of the Deployment.'
    )
    status: Optional[DeploymentStatus] = Field(
        None, description='Most recently observed status of the Deployment.'
    )


class DeploymentList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Deployment] = Field(
        ..., description='Items is the list of Deployments.'
    )
    kind: Optional[Kind13] = Field(
        'DeploymentList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(None, description='Standard list metadata.')


class ReplicaSet(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind14] = Field(
        'ReplicaSet',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[ReplicaSetSpec] = Field(
        None,
        description='Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )
    status: Optional[ReplicaSetStatus] = Field(
        None,
        description='Status is the most recently observed status of the ReplicaSet. This data may be out of date by some window of time. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )


class ReplicaSetList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ReplicaSet] = Field(
        ...,
        description='List of ReplicaSets. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller',
    )
    kind: Optional[Kind15] = Field(
        'ReplicaSetList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class StatefulSet(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind16] = Field(
        'StatefulSet',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[StatefulSetSpec] = Field(
        None, description='Spec defines the desired identities of pods in this set.'
    )
    status: Optional[StatefulSetStatus] = Field(
        None,
        description='Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time.',
    )


class StatefulSetList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[StatefulSet]
    kind: Optional[Kind17] = Field(
        'StatefulSetList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None