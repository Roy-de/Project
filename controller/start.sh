#!/usr/bin/bash


#What to do:
    #  1. start zookeeper servers and kafka servers
    #  2.  
#
cd /usr/local/kafka/bin
kill $(sudo lsof -t -i:2181)
#On start run this command
#Start zookeeper service
./zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties
