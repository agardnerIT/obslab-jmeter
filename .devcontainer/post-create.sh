#!/bin/bash

JMETER_VERSION=5.6.3

# Download and extract JMeter
wget https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz
tar -xf apache-jmeter-${JMETER_VERSION}.tgz
mv apache-jmeter-${JMETER_VERSION} apache-jmeter

# Chop off https:// and trailing slash from DT_URL
# Source: https://stackoverflow.com/a/16623897/9997385
prefix="https://"
suffix="/"
DT_URL_CLEANED=${DT_URL#"$prefix"}
DT_URL_CLEANED=${DT_URL_CLEANED%"$suffix"}

sed -i "s,DT_ENVIRONMENT_PLACEHOLDER,$DT_URL_CLEANED," jmeterscripts/example.jmx
sed -i "s,DT_API_TOKEN_PLACEHOLDER,$DT_JMETER_TOKEN," jmeterscripts/example.jmx

# Creation Ping
# curl -X POST https://grzxx1q7wd.execute-api.us-east-1.amazonaws.com/default/codespace-tracker \
#   -H "Content-Type: application/json" \
#   -d "{
#     \"tenant\": \"$DT_URL\",
#     \"repo\": \"$GITHUB_REPOSITORY\",
#     \"demo\": \"obslab-jmeter\",
#     \"codespace.name\": \"$CODESPACE_NAME\"
#   }"