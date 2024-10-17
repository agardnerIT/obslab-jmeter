# Dynatrace Observability Lab: Apache JMeter Observability

--8<-- "snippets/disclaimer.md"
--8<-- "snippets/view-code.md"

This demo will run an [Apache JMeter](https://jmeter.apache.org){target=_blank} script and send a [Dynatrace SDLC event](https://docs.dynatrace.com/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin){target=_blank} when the load test is finished.

The HTTP requests in the JMX file are also instrumented with the recommended `x-dynatrace-test` headers.
[Monaco](https://docs.dynatrace.com/docs/manage/configuration-as-code/monaco){target=_blank} is used to apply configuration to your tenant to capture these header values.

This event can be used to trigger further automations such as Dynatrace workflows.

![Dynatrace JMeter dashboard](images/sdlc-event.png)

## Compatibility

| Deployment         | Tutorial Compatible |
|--------------------|---------------------|
| Dynatrace Managed  | ✔️                 |
| Dynatrace SaaS     | ✔️                 |

<div class="grid cards" markdown>
- [Click Here to Begin :octicons-arrow-right-24:](getting-started.md)
</div>