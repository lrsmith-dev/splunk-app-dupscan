This is a modified version of the Splunk Streaming search command found in https://github.com/splunk/splunk-app-examples/tree/master. This is proof of concept code to stream splunk query results through the command to
identify duplicate fields and sub-strings in a single Splunk line.

## Setup

```
pip install -r requirements.txt -t lib --upgrade
docker compose up
```

References
* https://github.com/splunk/splunk-app-examples/tree/master
* https://dev.splunk.com/enterprise/docs/devtools/customsearchcommands/
* https://dev.splunk.com/enterprise/docs/devtools/customsearchcommands/createcustomsearchcmd/
* https://dev.splunk.com/enterprise/docs/devtools/customsearchcommands/customsearchcmdexamples/
