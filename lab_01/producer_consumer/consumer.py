from kafka import KafkaConsumer
import json
import time
import logging
import os

bootstrap_servers = ['localhost:9094','localhost:9095','localhost:9096']
key_deserializer = lambda k: k.decode("utf-8") if k else None
value_deserializer = lambda v: json.loads(v.decode('utf-8'))
group_id = 'my-group'

log_path = os.path.join(os.getcwd(), 'log')

    
class Consumer:
    def __init__(self, topic):
        self.topic = topic
        self.consumer = KafkaConsumer(self.topic,
                         bootstrap_servers=bootstrap_servers,
                         key_deserializer=key_deserializer,
                         value_deserializer=value_deserializer,
                         auto_offset_reset='earliest',
                         group_id=group_id)
        self.run = True
        self.logger = self.setup_logger()
        
    def setup_logger(self):
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        """Create a separate logger for each producer instance"""
        logger = logging.getLogger(f"Consumer_{self.topic}")
        logger.setLevel(logging.INFO)

        # Create a file handler specific to this producer instance
        log_filename = os.path.join(log_path, f"consumer_{self.topic}.log")
        file_handler = logging.FileHandler(log_filename, mode="w")
        
        # Set log format
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Prevent duplicate logs
        if not logger.hasHandlers():
            logger.addHandler(file_handler)

        return logger
        
    def getValue(self):
        print('Consumer is running...')
        while self.run:
            for message in self.consumer:
                self.logger.info(f"{message.key} {message.value}")
            time.sleep(10)
    
    def close(self):
        self.run = False
        self.consumer.close()