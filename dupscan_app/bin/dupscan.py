#!/usr/bin/env python

# This is modified code from the Splunk App Examples repository.
# The original code is available at:
#   https://github.com/splunk/splunk-app-examples/tree/master/custom_search_commands/python/streamingsearchcommands_app

# coding=utf-8
#
# Copyright © 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os, sys
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators


delimiter_patterns = r"[ ;,\"\':\n=]"
tokens_to_skip = [ 'true','false',' ', '[', ']', '', '-' ] 

@Configuration()
class DupScan(StreamingCommand):
    """
    The DupScan command scans each event and returns a record for every substring that appears more than once in the event.
    It is useful for identifying duplicate substrings in log entries, such as IP addresses, user IDs, or other identifiers.

    This command is a streaming command, meaning it processes events as they are received, rather than waiting for all events to be available.

    Example:

    ``| makeresults count=5 | eval _raw="127.0.0.1 - - [10/Oct/2000:13:55:36 -0700 rid=002 rrid=001 ] \"GET /apache_pb.gif HTTP/1.0\" 200 2326 rid=001" | dupscan``

    """

    def stream(self, records):
        # To connect with Splunk, use the instantiated service object which is created using the server-uri and
        # other meta details and can be accessed as shown below
        # Example:-
        #    service = self.service
        #    info = service.info //access the Splunk Server info

        for record in records:
            tokenDict = {}
            tokenized = re.split(delimiter_patterns,record["_raw"])
            for token in tokenized:
                if token  in tokens_to_skip:
                    continue
                if tokenDict.get(token) is not None:
                    tokenDict[token] += 1
                else:
                    tokenDict[token] = 1
            for k,v in tokenDict.items():
                if v > 1:
                    record[k] = v
            yield record


dispatch(DupScan, sys.argv, sys.stdin, sys.stdout, __name__)
