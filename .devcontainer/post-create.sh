#!/bin/bash

JMETER_VERSION=5.6.3

# Download and extract JMeter
wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz
tar -xf apache-jmeter-${JMETER_VERSION}.tgz

# Chop off https:// and trailing slash from DT_URL
# Source: https://stackoverflow.com/a/16623897/9997385
prefix="https://"
suffix="/"
DT_URL=${DT_URL#"$prefix"}
DT_URL=${DT_URL%"$suffix"}

# Creation Ping
# curl -X POST https://grzxx1q7wd.execute-api.us-east-1.amazonaws.com/default/codespace-tracker \
#   -H "Content-Type: application/json" \
#   -d "{
#     \"tenant\": \"$DT_URL\",
#     \"repo\": \"$GITHUB_REPOSITORY\",
#     \"demo\": \"obslab-jmeter\",
#     \"codespace.name\": \"$CODESPACE_NAME\"
#   }"