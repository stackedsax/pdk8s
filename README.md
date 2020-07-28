![CI](https://github.com/FlorianLudwig/pdk8s/workflows/CI/badge.svg)
![license](https://img.shields.io/github/license/FlorianLudwig/pdk8s.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# pdk8s

Generating Kubernetes definitions (yaml) with python, inspired by [cdk8s](https://github.com/awslabs/cdk8s).  The main use case is to use those definitions with helm.  This means cdk8s does replace all the templating that helm does - but helm still takes care of rolling out your changes to your cluster.

Know cdk8s? [See our overview of the differences between `pdk8s` and `cdk8s`.](docs/cdk8s.md)

# Getting started

<!-- add nice video here -->

## Installing pdk8s

### Prerequisites

* Python >= 3.7.


### Installation via PyPi

pdk8s is available on PyPi, you can install it with your preferred python package manage, `pip`, `pipenv`, etc:

```
pip install pdk8s
```

## Intro

The format of `pdk8s` charts is similar to helm charts, just that they are python instead of yaml.  Your “python chart" must define the following variables:

 * `name`: Name of your chart
 * `chart_version`: This is the chart version. This version number should be incremented each time you make changes to the chart and its templates, including the app version. Versions are expected to follow [Semantic Versioning](https://semver.org/).
 * `app_version`: This is the version number of the application being deployed. This version number should be incremented each time you make changes to the application. Versions are not expected to follow Semantic Versioning. They should reflect the version the application is using.
 * `chart`: Your chart. A list or `pdk8s.k8s.Chart` (or actually any iterable python object) of k8s resources.

If you had a déjà vu while reading - that is because the description for `chart_version` and `app_version` are copied straight from Helm ;)

## Getting started

```bash
$ pdk8s init
chart_name [awesome chart]: Webserver Example
slug [webserver_example]: 
chart_version [0.1.0]: 
app_version [0.1.0]: 
```

You will find a new folder and files named: `webserver_example/chart.py`.  Inside this file you will find a hello world example:

```python
chart = [
    k8s.Deployment(name='deployment',
                    spec=k8s.DeploymentSpec(
                        replicas=2,
                        selector=k8s.LabelSelector(match_labels=label),
                        template=k8s.PodTemplateSpec(
                        metadata=k8s.ObjectMeta(labels=label),
                        spec=k8s.PodSpec(containers=[
                            k8s.Container(
                            name='hello-kubernetes',
                            image='paulbouwer/hello-kubernetes:1.7',
                            ports=[k8s.ContainerPort(container_port=8080)])]))))
]
```

Which you can turn into a running helm chart with:

```bash
$ pdk8s synth
```

You will find your generated chart under `dist`:

<pre>
├── chart.py
└── <font color="#0087FF">dist</font>
    ├── Chart.yaml
    ├── <font color="#0087FF">templates</font>
    │   └── generated.yaml
    └── values.yaml
</pre>

Per default `pdk8s synth` loads the `chart.py` in the current directory.  You can also use `-i` to specify a different python file.  Also the `chart.py` generated by `pdk8s init` provides the same api as `pdk8s` except without the `-i` option:

```bash
$ ./chart.py synth
```

## Creating Ressources

Creating a service:

```python
from pdk8s import k8s

service = k8s.Service(name="service",
            spec=k8s.ServiceSpec(
                type="LoadBalancer",
                ports=[k8s.ServicePort(port=80, target_port=8080)],
                selector={"app": "hello-k8s"}))

chart = [service]
```

All `pdk8s` classes are [pydantic](https://pydantic-docs.helpmanual.io/) data classes.  Which provides - among other things - automatic conversion for parameters, so you can just as well write:

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

Note 1: Automatic casting is only available on creation.  `deployment.spec = {"replicas": 2}` would not work.

Note 2: Currently all required parameters must be provided at creation time.  You cannot create an empty `k8s.Deployment()`.  This might change.


## CamelCase names

The Kubernetes APIs use camelCase for naming attributes, while python usually uses snake_case.  `pdk8s` also follows the snake_case convention, same as `cdk8s`.

`pdk8s` provides aliases for all arguments:

```python
k8s.ServicePort(port=80, target_port=8080)
k8s.ServicePort(port=80, targetPort=8080)
```

Both work and result in the same result.  This is for compatibility when importing from other sources (and makes `pdk8s.k8s.parse` possible).

## Importing existing charts

You might already have templates you want to build upon, you can easily import them using `pdk8s.k8s.parse`. Let's assume you have the following `chart.yaml`:

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

# Why

TODO explain why this exists (NIH syndrome)

### Generate at build time

Generate everything at build time and not runtime as it makes it easier for linters and other dev tools, like IDEs.


### Versioning

# Development and building

Currently, generating the code of `pdk8s` depends on a patched version of `datamodel-code-generator`.  I am working on upstreaming changes to not depend on local patches anymore.

