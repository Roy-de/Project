#!/usr/bin/zsh
cd /usr/local/kafka
bin/kafka-topics.sh --create --bootstrap-server localhost:9902 --replication-factor 1 --partitions 1 --topic minuteData