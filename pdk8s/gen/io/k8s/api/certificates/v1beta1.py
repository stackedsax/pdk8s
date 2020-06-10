# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..... import Kind63, Kind64
from ...apimachinery.pkg.apis.meta import v1


class CertificateSigningRequestSpec(BaseModel):
    extra: Optional[Dict[str, Any]] = Field(
        None,
        description='Extra information about the requesting user. See user.Info interface for details.',
    )
    groups: Optional[List[str]] = Field(
        None,
        description='Group information about the requesting user. See user.Info interface for details.',
    )
    request: str = Field(..., description='Base64-encoded PKCS#10 CSR data')
    uid: Optional[str] = Field(
        None,
        description='UID information about the requesting user. See user.Info interface for details.',
    )
    usages: Optional[List[str]] = Field(
        None,
        description='allowedUsages specifies a set of usage contexts the key will be valid for. See: https://tools.ietf.org/html/rfc5280#section-4.2.1.3\n     https://tools.ietf.org/html/rfc5280#section-4.2.1.12',
    )
    username: Optional[str] = Field(
        None,
        description='Information about the requesting user. See user.Info interface for details.',
    )


class CertificateSigningRequestCondition(BaseModel):
    lastUpdateTime: Optional[v1.Time] = Field(
        None, description='timestamp for the last update to this condition'
    )
    message: Optional[str] = Field(
        None, description='human readable message with details about the request state'
    )
    reason: Optional[str] = Field(
        None, description='brief reason for the request state'
    )
    type: str = Field(
        ..., description='request approval state, currently Approved or Denied.'
    )


class CertificateSigningRequestStatus(BaseModel):
    certificate: Optional[str] = Field(
        None,
        description='If request was approved, the controller will place the issued certificate here.',
    )
    conditions: Optional[List[CertificateSigningRequestCondition]] = Field(
        None,
        description='Conditions applied to the request, such as approval or denial.',
    )


class CertificateSigningRequest(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[Kind63] = Field(
        'CertificateSigningRequest',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: Optional[CertificateSigningRequestSpec] = Field(
        None,
        description='The certificate request itself and any additional information.',
    )
    status: Optional[CertificateSigningRequestStatus] = Field(
        None, description='Derived information about the request.'
    )


class CertificateSigningRequestList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[CertificateSigningRequest]
    kind: Optional[Kind64] = Field(
        'CertificateSigningRequestList',
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None