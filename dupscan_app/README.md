splunk-sdk-python dupscan_app example
========================================

Streaming commands that processes search results one-by-one and tokenizes each line and looks for duplicate tokens.

This app is a modified verions of an example of Streaming Custom search commands which will returns events with a one new field 'fahrenheit'.

This is a proof of concept code to identify duplicate substrings/fields that can be collapses to decrease log line size.

### To run this example locally, follow the below steps.

### Step 1
Execute the following command from the root of this repository.
```shell
docker compose up -d
```

### Step 2
Make sure the Splunk is in `healthy` state., run:
```shell
docker ps
```
Log in into the Splunk UI.

Go to http://localhost:8000/en-US/app/dupscan_app/search page and run the following search query:
```
| makeresults count=5 | eval _raw="127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 req_id=001 ] \"GET /apache_pb.gif HTTP/1.0\" 200 2326 rid=001" | dupscan
```
Results:

_time| _raw | 001 |
:-----|:-----|:-----|
|2025-07-01 21:07:10| 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 req_id=001 ] "GET /apache_pb.gif HTTP/1.0" 200 2326 rid=001 | 2 |
|2025-07-01 21:07:10| 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 req_id=001 ] "GET /apache_pb.gif HTTP/1.0" 200 2326 rid=001 | 2 |
|2025-07-01 21:07:10| 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 req_id=001 ] "GET /apache_pb.gif HTTP/1.0" 200 2326 rid=001 | 2 |
|2025-07-01 21:07:10| 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 req_id=001 ] "GET /apache_pb.gif HTTP/1.0" 200 2326 rid=001 | 2 |
|2025-07-01 21:07:10| 127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 req_id=001 ] "GET /apache_pb.gif HTTP/1.0" 200 2326 rid=001 | 2 |


Note : In this example there are two different fields req_id and rid, which has the same value. 
