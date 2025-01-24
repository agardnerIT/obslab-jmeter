#!/bin/bash

MONACO_VERSION=v2.15.2
JMETER_VERSION=5.6.3

# Download Monaco
curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/download/${MONACO_VERSION}/monaco-linux-amd64 -o monaco-linux-amd64       
mv monaco-linux-amd64 monaco
chmod +x monaco
sudo mv monaco /usr/local/bin/

# Apply Monaco config to tenant
sed -i "s,DT_ENVIRONMENT_PLACEHOLDER,$DT_URL," dynatrace/monaco/manifest.yaml
monaco deploy dynatrace/monaco/manifest.yaml

# Download and extract JMeter
wget -O apache-jmeter.tgz https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz
tar -xf apache-jmeter.tgz
mv apache-jmeter-${JMETER_VERSION} /workspaces/$RepositoryName/apache-jmeter

# Chop off https:// and trailing slash from DT_URL
# Source: https://stackoverflow.com/a/16623897/9997385
prefix="https://"
suffix="/"
DT_URL_CLEANED=${DT_URL#"$prefix"}
DT_URL_CLEANED=${DT_URL_CLEANED%"$suffix"}

sed -i "s,DT_ENVIRONMENT_PLACEHOLDER,$DT_URL_CLEANED," /workspaces/$RepositoryName/jmeterscripts/example.jmx
sed -i "s,DT_API_TOKEN_PLACEHOLDER,$DT_JMETER_TOKEN," /workspaces/$RepositoryName/jmeterscripts/example.jmx

# Creation Ping
curl -X POST https://grzxx1q7wd.execute-api.us-east-1.amazonaws.com/default/codespace-tracker \
  -H "Content-Type: application/json" \
  -d "{
    \"tenant\": \"$DT_URL\",
    \"repo\": \"$GITHUB_REPOSITORY\",
    \"demo\": \"obslab-jmeter\",
    \"codespace.name\": \"$CODESPACE_NAME\"
  }"
