
# ILO - A policy engine for kubernetes

ILO let's you write policies in native python as opposed to rego, yaml or Go

https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#request


e.g. policy:


```
apiVersion: ilo.prabhatsharma.in/v1alpha1
kind: AdmissionPolicy
metadata:
  name: crappypolicy1
spec:
  rules:
  - name: rule1
    resource: deployment
    validationFailureAction: enforce
    rule: |
      def validator(input_object):
        if(input_object['name'] == "crappy"):
          return False


```
