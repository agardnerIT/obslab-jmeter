--8<-- "snippets/live-code-snippets.md"
--8<-- "snippets/tenant-id.md"

## Gather Details: Create API Token

Create an API token with the following permissions:

- `ReadConfig`
- `DataExport`
- `CaptureRequestData`
- `openpipeline.events_sdlc`

The `ReadConfig`, `DataExport` and `CaptureRequestData` permissions will be used by the Monaco Configuration as Code utility to apply configuration to your Dynatrace environment.
This configuration will capture the `x-dynatrace-test` HTTP header and process the values described [here](https://docs.dynatrace.com/docs/platform-modules/automations/cloud-automation/test-automation){target=_blank}.


The `openpipeline.events_sdlc` permission is required to send the "load test finished" SDLC event to Dynatrace.

--8<-- "snippets/info-required.md"

## Start Demo

--8<-- "snippets/codespace-details-warning-box.md"

Click this button to launch the demo in a new tab.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/dynatrace/obslab-jmeter){target=_blank}

<div class="grid cards" markdown>
- [Click Here to Run the Demo :octicons-arrow-right-24:](run-demo.md)
</div>