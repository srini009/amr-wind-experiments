#!/bin/bash
#Check if service is up
until [ -f $AMS_NODE_ADDR_FILE ]
do
     sleep 5
done
until [ `wc -l < $AMS_NODE_ADDR_FILE` == 60 ]
do
	sleep 5
	echo "Waiting for server to come up...."
done
sleep 20
