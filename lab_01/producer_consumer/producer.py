from kafka import KafkaProducer
import json
import threading
import os
import logging
import time
import sys

cur_path = os.getcwd()
utils_path = os.path.join(cur_path, 'utils')
sys.path.append(utils_path)
from loader import multi_load

bootstrap_servers = ['localhost:9094','localhost:9095','localhost:9096']
key_serializer = str.encode
value_serializer = lambda v: json.dumps(v).encode('utf-8')

log_path = os.path.join(cur_path, 'log')


class Producer:
    lock = threading.Lock()
    
    
    def __init__(self, topic_a_file):
        self.data_set = multi_load(topic_a_file)
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers, key_serializer=key_serializer, value_serializer=value_serializer)
        self.logger = self.setup_logger()
        
    def setup_logger(self):
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        """Create a separate logger for each producer instance"""
        logger = logging.getLogger(f"Producer")
        logger.setLevel(logging.INFO)

        # Create a file handler specific to this producer instance
        log_filename = os.path.join(log_path, "producer.log")
        file_handler = logging.FileHandler(log_filename, mode="w")
        
        # Set log format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Prevent duplicate logs
        if not logger.hasHandlers():
            logger.addHandler(file_handler)

        return logger
    
    def send(self, topic):
        print(f"Sending data to topic {topic}")
        for data in self.data_set[topic]:
            with Producer.lock:
                message_key = data.station
                message_value = data.value()
                future = self.producer.send(topic, key=message_key, value=message_value)
                self.producer.flush()
                result = future.get(timeout=60)
                self.logger.info(f"Message sent to topic {result.topic} partition {result.partition} offset {result.offset}")
            time.sleep(0.5)
                
    
    def close(self):
        self.producer.close()
        