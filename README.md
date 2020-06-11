# pdk8s

Generating kubernetes defintions (yaml) with python, inspired by [cdk8s](https://github.com/awslabs/cdk8s).



# Getting started

<!-- add nice video here -->

## Creating

Creating a service:

```python
from pdk8s import k8s

k8s.Service(name="service",
            spec=k8s.ServiceSpec(
                type="LoadBalancer",
                ports=[k8s.ServicePort(port=80, target_port=8080)],
                selector={"app": "hello-k8s"}))
```

All `pdk8s` classes are [pydantic](https://pydantic-docs.helpmanual.io/) data classes.  Which provides among other things is used for automatic conversion, so you can just as well write:

```python
from pdk8s import k8s

k8s.Service(name="service",
            spec={
                "type": "LoadBalancer",
                "ports": [{"port": 80, "target_port": 8080}],
                "selector": {"app": "hello-k8s"}})
```

## Manipulating

All attributes can be manipulated after creation:

```python

deployment = k8s.Deployment(name='deployment',
                    spec=k8s.DeploymentSpec(
                        replicas=2))

deployment.spec.replicas = math.randint(0, 666)
```

Note: Automatic casting is only available on creation.  `deployment.spec = {"replicas": 2}` would not work.

## CamelCase names

The kubernetes APIs use camelCase for naming attributes, while python usually uses snake_case.  `pdk8s` also follows the snake_case convention, same as `cdk8s`.

`pdk8s` provides aliases for all arguments:

```python
k8s.ServicePort(port=80, target_port=8080)
k8s.ServicePort(port=80, targetPort=8080)
```

Both work and result in the same result.  This is for compatibility when importing from other sources.

## Importing existing charts

You might already have templates you want to build upon, you can easily import them using `pdk8s.k8s.parse`. Let's assume you have the follwoing `chart.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: service
spec:
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: hello-k8s
  type: LoadBalancer
```

With:

```python
import pdk8s
from pdk8s import k8s

my_chart = k8s.parse("example/chart.yaml")
my_chart[0].name = "service_new"
pdk8s.synth(my_chart)
```

You get:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: service_new
spec:
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: hello-k8s
  type: LoadBalancer
```

# Compatibility to cdk8s

There are a few differences that make code between the `cdk8s` and `pdk8s` incompatible.  A good overview can be archived by comparing the following to examples:

 * [cdk8s example](https://github.com/awslabs/cdk8s/blob/master/docs/getting-started/python.md#importing-constructs-for-the-kubernetes-api)
 * [pdk8s example](https://github.com/FlorianLudwig/pdk8s/blob/master/example/hello_world.py)

### Pure python

`cdk8s` is written in TypeScript and with the power of jsii usable from other languages, as python.  `pdk8s` is written in pure python with no bridge to other languages.  This means you are limited to python and cannot reuse charts written in other languages.  Therefore a `pdk8s` is focused on providing an awesome experience writing charts in python:  Readable tracebacks, happy IDE and linters, ... 

### Context / Constructs

Currently there is no equivalent of "constructs" in `pdk8s`.  In `cdk8s` highlevel objects (e.g. `Service`) are special:  They have an extra argument (the first one) which is the context in which they are defined, e.g. `k8s.Service(self, ...)` where `self` is the context.

In `pdk8s` there is no special treatment of these types.  There might be later on, but they would be added and not replaced.

This allows for more flexiblity on how to construct your chart generator.


### Names

In `cdk8s` names are automatically made unique by adding a hash to it.  `pdk8s` does not observe this behavior.  Also in `pdk8s` names must be provided as keyword argument.

```python

# cdk8s
k8s.Service(Chart("hello"), "service")
# kind: Service
# apiVersion: v1
# metadata:
#   name: hello-service-9878228b


# pdk8s
k8s.Service(name='service')
# kind: Service
# apiVersion: v1
# metadata:
#   name: service


```
<!-- TODO add reasoning -->

### IntOrString

```python
# cdk8s
k8s.ServicePort(port=80, target_port=k8s.IntOrString.from_number(8080))

# pdk8s
k8s.ServicePort(port=80, target_port=8080)
# k8s.IntOrString might be added for compatibility later on
```


# Why

TODO explain why this exists (NIH syndrom)
## Sources

 * https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec - openapi definition.
 * https://github.com/instrumenta/kubernetes-json-schema - JSON Schema of kubernetes API, generated from official openapi definitions.  Used by cdk8s.
