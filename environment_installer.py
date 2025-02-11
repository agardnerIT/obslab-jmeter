import os
from utils import *

CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")
REPOSITORY_NAME = os.environ.get("RepositoryName", "")

MONACO_VERSION="v2.15.2"
JMETER_VERSION="5.6.3"
RUNME_CLI_VERSION = "3.10.2"


# Build DT environment URLs
DT_TENANT_APPS, DT_TENANT_LIVE = build_dt_urls(dt_env_id=DT_ENVIRONMENT_ID, dt_env_type=DT_ENVIRONMENT_TYPE)

# Process further. Jmeter needs just abc12345.live.dynatrace. Chop off https://
DT_TENANT_LIVE_FOR_JMETER = DT_TENANT_LIVE.replace("https://", "")

# Use "main" DT_API_TOKEN to create new, temporary, properly scoped API tokens
DT_API_TOKEN_FOR_USE = create_dt_api_token(token_name="[devrel e2e testing] DT_JMETER_E2E_TEST_TOKEN", scopes=["ReadConfig", "DataExport", "CaptureRequestData", "openpipeline.events_sdlc"], dt_rw_api_token=DT_API_TOKEN, dt_tenant_live=DT_TENANT_LIVE)

# Replace placeholders
do_file_replace(pattern=f"{BASE_DIR}/dynatrace/monaco/manifest.yaml", find_string="DT_ENVIRONMENT_PLACEHOLDER", replace_string=DT_TENANT_LIVE)
do_file_replace(pattern=f"{BASE_DIR}/jmeterscripts/example.jmx", find_string="DT_TENANT_LIVE_PLACEHOLDER", replace_string=DT_TENANT_LIVE_FOR_JMETER)
do_file_replace(pattern=f"{BASE_DIR}/jmeterscripts/example.jmx", find_string="DT_API_TOKEN_PLACEHOLDER", replace_string=DT_API_TOKEN_FOR_USE)

# Download Monaco
run_command(["curl", "-L", f"https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/download/{MONACO_VERSION}/monaco-linux-amd64", "-o", "monaco-linux-amd64"])
run_command(["mv", "monaco-linux-amd64", "monaco"])
run_command(["chmod", "+x", "monaco"])
run_command(["sudo", "mv", "monaco", "/usr/local/bin/"])

# Apply Monaco config to tenant
run_command(["monaco", "deploy", f"{BASE_DIR}/dynatrace/monaco/manifest.yaml"])

# Download and extract JMeter
run_command(["wget", "-O", "apache-jmeter.tgz", f"https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-{JMETER_VERSION}.tgz"])
run_command(["tar", "-xf", "apache-jmeter.tgz"])
run_command(["mv", f"apache-jmeter-{JMETER_VERSION}", "apache-jmeter"])

# Install RunMe
run_command(["mkdir", "runme_binary"])
run_command(["wget", "-O", "runme_binary/runme_linux_x86_64.tar.gz", f"https://download.stateful.com/runme/{RUNME_CLI_VERSION}/runme_linux_x86_64.tar.gz"])
run_command(["tar", "-xvf", "runme_binary/runme_linux_x86_64.tar.gz", "--directory", "runme_binary"])
run_command(["sudo", "mv", "runme_binary/runme", "/usr/local/bin"])
run_command(["rm", "-rf", "runme_binary"])

if CODESPACE_NAME.startswith("dttest-"):
    # Set default repository for gh CLI
    # Required for the e2e test harness
    # If it needs to interact with GitHub (eg. create an issue for a failed e2e test)
    run_command(["gh", "repo", "set-default", GITHUB_REPOSITORY])

    # Now set up a label, used if / when the e2e test fails
    # This may already be set (when demos are re-executed in repos)
    # so catch error and always return true
    # Otherwise the entire post-start.sh script could fail
    # We can do this as we know we have permission to this repo
    # (because we're the owner and testing it)
    run_command(["gh", "label", "create", "e2e test failed", "--force"])
    run_command(["pip", "install", "-r", f"/workspaces/{REPOSITORY_NAME}/.devcontainer/testing/requirements.txt", "--break-system-packages"])
    run_command(["python",  f"/workspaces/{REPOSITORY_NAME}/.devcontainer/testing/testharness.py"])

    # Testing finished. Destroy the codespace
    run_command(["gh", "codespace", "delete", "--codespace", CODESPACE_NAME, "--force"])
else:
    send_startup_ping(demo_name="obslab-jmeter")
