package org.example;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Collections;
import java.util.Properties;
import java.util.function.Consumer;

public class MyConsumer {

    static final String BOOTSTRAP_SERVERS = "localhost:9092";
    static final String TOPIC = System.getenv("test");
    static final String AUTO_OFFSET_RESET = "auto.offset.reset";
    static final String GROUP_ID = "group.id";
    public static void main(String[] args) throws Exception {

    //Add properties
        Properties properties = new Properties();
        properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG,BOOTSTRAP_SERVERS);
        properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,StringDeserializer.class.getName());
        properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,StringDeserializer.class.getName());
        properties.put(ConsumerConfig.GROUP_ID_CONFIG,GROUP_ID);
    //Create KafkaConsumer
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);
        //Subscribe to the topics
        consumer.subscribe(Collections.singletonList(TOPIC));
        //Start consuming messages
        try {
            while (true){
                ConsumerRecords<String,String> records =  consumer.poll(100);
                for(ConsumerRecord<String, String> record : records){
                    System.out.println("Received:" +record.value());
                }
            }
        }
        finally {
                consumer.close();
        }
    }
}
